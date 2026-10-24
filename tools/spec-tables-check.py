#!/usr/bin/env python3
"""spec-tables-check: the v4 drift gate (world-expansion-research-brief.md 5.4).

Fails the build when:
  1. docs/data/spec-tables.json is stale against the SPEC-TABLE markers in
     game-spec.md (section 25). One file to update, zero drift by
     construction: edit the marker, re-run tools/spec-tables-extract.py.
  2. A registered live key is never named as a quoted literal outside its own
     table block (a dead row rots into a lie).
  3. Code references a key a table does not define, via the table's accessor
     patterns or cross-table references (a resident's aff must name a
     STATION3 station, a project's station must name one, GROWTH.kindOrder
     must name BUILD_KINDS kinds, PROJ_SITE_POS must name PROJECTS ids,
     PART_STATION values must name STATION3 stations, an incident's patient
     must name a RES3 resident).

Keyless tables (PLOTS, OBJECTIVES, NEWCOMERS) check their row counts.
Queued tables (ADJACENCY, CLAIM_COST, DEPLETION, MODEL_PRESTIGE) report
QUEUED; their code checks engage when their rows ship (v4 step 3).

Usage: python3 tools/spec-tables-check.py
  Exit 0 with one OK line, or exit 1 listing every finding.
"""

import json
import re
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
GAME = REPO / "index.html"
JSON = REPO / "docs/data/spec-tables.json"

findings = []


def fail(msg):
    findings.append("FAIL " + msg)


def quoted(src, key):
    return len(re.findall(r"""["']""" + re.escape(key) + r"""["']""", src))


def table_block(src, name):
    """Return the source text of `var NAME = ...;` (brace matched)."""
    m = re.search(r"var %s = " % re.escape(name), src)
    if not m:
        return ""
    i = m.end()
    depth = 0
    in_str = None
    j = i
    while j < len(src):
        c = src[j]
        if in_str:
            if c == "\\":
                j += 1
            elif c == in_str:
                in_str = None
        elif c in "\"'":
            in_str = c
        elif c in "{[":
            depth += 1
        elif c in "}]":
            depth -= 1
            if depth == 0:
                return src[m.start():j + 2]
        j += 1
    return ""


def main():
    data = json.loads(JSON.read_text(encoding="utf-8"))
    tables = data["tables"]

    # 1. JSON must match a fresh extraction from the spec.
    fresh = subprocess.run(
        [sys.executable, str(REPO / "tools/spec-tables-extract.py"), "--stdout"],
        capture_output=True, text=True)
    if fresh.returncode != 0:
        fail("extractor error: " + fresh.stderr.strip()[:200])
        report()
        return
    if json.loads(fresh.stdout) != data:
        fail("spec-tables.json is stale against game-spec.md markers; "
             "run tools/spec-tables-extract.py")

    src = GAME.read_text(encoding="utf-8")
    blocks = {name: table_block(src, name) for name in tables
              if tables[name].get("status") == "live" and not tables[name].get("keyless")}

    def keys(name):
        return tables[name]["keys"]

    # Consumption model per table. Key-lookup tables are read by naming a key
    # (STATION3["mill"], inc.key === "feudwell"): a row never named outside its
    # own definition is a dead row. Iteration tables are read by a generic path
    # that walks every row (RES3.map in makeAgents; Object.keys(BUILD_KINDS) in
    # foundableKinds): no row can be dead that way, so the gate asserts the
    # iteration path exists instead of demanding per-row literals.
    CONSUME = {
        "STATION3": ("key", []),
        "NEED_DEFS": ("key", []),
        "INCIDENTS": ("key", []),
        "PROJECTS": ("key", []),
        "RES3": ("iteration", [r"RES3\.map\s*\("]),
        "BUILD_KINDS": ("iteration", [r"Object\.keys\(BUILD_KINDS\)"]),
    }

    # 2. Dead rows: every key of a key-lookup table named outside its own block.
    for name, (mode, _) in CONSUME.items():
        if mode != "key":
            continue
        own = blocks.get(name, "")
        rest = src.replace(own, "", 1)
        for k in keys(name):
            if quoted(rest, k) == 0:
                fail("dead row: %s key %r never named outside its table" % (name, k))

    # Iteration tables: the generic read path must exist.
    for name, (mode, patterns) in CONSUME.items():
        if mode != "iteration":
            continue
        for pat in patterns:
            if not re.search(pat, src):
                fail("iteration path missing: %s is not read by %s" % (name, pat))

    # 3a. Accessor patterns: literals that must name a defined key.
    def check_refs(table, pattern, label):
        for m in re.finditer(pattern, src):
            for g in m.groups():
                if g and g not in keys(table):
                    fail("undefined %s reference %r (%s)" % (table, g, label))

    check_refs("INCIDENTS", r'inc\.key\s*===\s*"([a-z]+)"', "inc.key ===")
    check_refs("NEED_DEFS", r'needVal\(\s*[a-zA-Z_]+\s*,\s*"([a-z]+)"\s*\)', "needVal")
    check_refs("RES3", r'\bagent\(\s*"([a-z]+)"\s*\)', "agent()")
    check_refs("RES3", r'\borderAgent\(\s*"([a-z]+)"\s*,', "orderAgent id")
    check_refs("RES3", r'\b(?:sendMedic|blameAgent|restPatient|recoverPatient)\(\s*"([a-z]+)"', "resident-id call")

    # orderAgent's second argument names a station.
    for m in re.finditer(r'\borderAgent\(\s*"[a-z]+"\s*,\s*"([a-z]+)"\s*\)', src):
        if m.group(1) not in keys("STATION3"):
            fail("undefined STATION3 reference %r (orderAgent station)" % m.group(1))

    # 3b. Cross-table references.
    def cross(table, block_name, pattern, label):
        blk = table_block(src, block_name) or src
        for m in re.finditer(pattern, blk):
            g = m.group(1)
            if g not in keys(table):
                fail("undefined %s reference %r (%s in %s)" % (table, g, label, block_name))

    cross("STATION3", "RES3", r'aff:"([a-z]+)"', "resident aff")
    cross("RES3", "RES3", r'admires:"([a-z]+)"', "resident admires")
    cross("STATION3", "NEWCOMERS", r'aff:"([a-z]+)"', "newcomer aff")
    cross("STATION3", "PROJECTS", r'station:"([a-z]+)"', "project station")
    cross("STATION3", "OBJECTIVES", r'station:"([a-z]+)"', "objective station")

    # PROJECTS part keys name PART_STATION keys; PART_STATION values name stations.
    part_blk = table_block(src, "PROJECTS")
    part_keys = set(re.findall(r"var PART_STATION = \{([^}]+)\}", src))
    part_names = set()
    if part_keys:
        part_names = set(re.findall(r"([a-z]+):", next(iter(part_keys))))
    for m in re.finditer(r"parts:\{([^}]+)\}", part_blk):
        for pk in re.findall(r"([a-z]+):", m.group(1)):
            if pk not in part_names:
                fail("undefined PART_STATION part %r (project parts)" % pk)
    for m in re.finditer(r'var PART_STATION = \{([^}]+)\}', src):
        for v in re.findall(r':"([a-z]+)"', m.group(1)):
            if v not in keys("STATION3"):
                fail("undefined STATION3 reference %r (PART_STATION value)" % v)

    # PROJ_SITE_POS keys name PROJECTS ids.
    for m in re.finditer(r"var PROJ_SITE_POS = \{([^}]+)\}", src):
        for k in re.findall(r"([a-z]+):", m.group(1)):
            if k not in keys("PROJECTS"):
                fail("undefined PROJECTS reference %r (PROJ_SITE_POS)" % k)

    # GROWTH.kindOrder names BUILD_KINDS kinds.
    for m in re.finditer(r"kindOrder:\s*\[([^\]]+)\]", src):
        for k in re.findall(r'"([a-z]+)"', m.group(1)):
            if k not in keys("BUILD_KINDS"):
                fail("undefined BUILD_KINDS reference %r (GROWTH.kindOrder)" % k)

    # INCIDENTS patient names a RES3 resident.
    cross("RES3", "INCIDENTS", r'patient:"([a-z]+)"', "incident patient")

    # 4. Keyless tables: row counts.
    def count_entries(block_name, pattern):
        blk = table_block(src, block_name)
        return len(re.findall(pattern, blk))

    keyless = {"PLOTS": (r"\{x:", "plot"), "OBJECTIVES": (r"\{station:", "objective"),
               "NEWCOMERS": (r"\{name:", "newcomer")}
    for name, (pat, what) in keyless.items():
        want = tables[name]["rows"]
        got = count_entries(name, pat)
        if got != want:
            fail("row count: %s has %d %s rows, spec registers %d" % (name, got, what, want))

    # 5. Queued tables: schema present, code checks not yet engaged.
    queued = [n for n, t in tables.items() if t.get("status") == "queued"]
    report(queued)


def report(queued=()):
    n_live = 0
    if findings:
        print("\n".join(findings))
        sys.exit(1)
    print("SPEC-TABLES OK (queued: %s)" % ", ".join(sorted(queued)))


if __name__ == "__main__":
    main()
