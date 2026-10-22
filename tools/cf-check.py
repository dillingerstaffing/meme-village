#!/usr/bin/env python3
"""cf-check: consistency checker for this project's CF-DOC articles.

Invariants live as short articles in docs/cf/. Code points at the
article that governs it with a CF-REF comment:

    // CF-REF: some-article.md [12]

The bracketed number is the protected block: the N lines immediately
following the ref comment. This checker verifies the wiring between
articles, the trigger index (docs/cf/_index.md), the refs, and the
recorded block hashes, and reports drift when a protected block no
longer matches its hash.

Findings:
  BROKEN REF    a CF-REF names an article that does not exist
  SYNTAX        a line mentions CF-REF but is not a well formed ref,
                or the article name is not a bare file in docs/cf/
  ORPHANED      an article in docs/cf/ has no row in the index
  DUPLICATE     an article has more than one row in the index
  STALE INDEX   an index row names an article that does not exist
  STALE         a protected block changed since its hash was recorded,
                or the manifest disagrees with the refs now in the code
  MISSING HASH  a ref has no manifest entry yet
  EXTRA HASH    a manifest entry pairs with no ref in the code

Usage:
  python3 tools/cf-check.py
      Run every check. Exit 1 and print findings, or exit 0 with a
      one line OK.
  python3 tools/cf-check.py --write-hashes
      Record fresh hashes for every well formed ref (do this only
      after reviewing any drift the plain run reported), then run the
      structural checks. Exit 1 if structural findings remain.

Hash manifest (docs/cf/_hashes.json): a JSON object keyed by repo
relative file path. Each value is a list with one entry per CF-REF in
that file, in file order, so a file may carry many refs:

  {"article": "store-single-source.md", "ref_line": 248,
   "lines": 71, "hash": "0123abcd"}

ref_line is the 1 based line of the ref comment when the hash was
recorded; it is kept for humans only. Matching is positional: refs
found in a file pair with that file's manifest entries in order, a
pair must agree on article and line count, and the hash is always
recomputed from the block following the ref's current position, so
insertions above a ref never cause false drift. A hash is the first
8 hex digits of the SHA-256 of the block's exact text.

Scan scope: source files (.html .js .ts .css .py .sh) outside .git,
outside docs/, and excluding this checker itself. Articles retired to
docs/cf/archived/ are exempt from the index checks.
"""

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CF_DIR = ROOT / "docs" / "cf"
INDEX_PATH = CF_DIR / "_index.md"
MANIFEST_PATH = CF_DIR / "_hashes.json"
SELF = Path(__file__).resolve()

SCAN_EXTS = {".html", ".htm", ".js", ".mjs", ".ts", ".tsx", ".css", ".py", ".sh"}
REF_RE = re.compile(r"CF-REF:\s*([A-Za-z0-9._\-]+\.md)\s*\[\s*(\d+)\s*\]")
ROW_RE = re.compile(r"\|\s*([A-Za-z0-9._\-]+\.md)\s*\|")


def block_hash(lines, start, count):
    """Hash the count lines (0 based slice starting at start)."""
    block = lines[start:start + count]
    text = "".join(line + "\n" for line in block)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:8]


def scan_refs():
    """Return (refs, findings). A ref is a dict with path (repo relative),
    line (1 based), article, lines (the protected block size)."""
    refs = []
    findings = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.suffix not in SCAN_EXTS:
            continue
        rel = path.relative_to(ROOT)
        if rel.parts[0] in (".git", "docs") or path.resolve() == SELF:
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except (UnicodeDecodeError, OSError):
            continue
        for i, line in enumerate(lines):
            if "CF-REF" not in line:
                continue
            m = REF_RE.search(line)
            if not m:
                findings.append(
                    "SYNTAX:      %s:%d (malformed CF-REF)" % (rel, i + 1))
                continue
            article, count = m.group(1), int(m.group(2))
            if ".." in article or count < 1:
                findings.append(
                    "SYNTAX:      %s:%d (invalid article name or line count)"
                    % (rel, i + 1))
                continue
            refs.append({"path": str(rel), "line": i + 1,
                         "article": article, "lines": count})
    return refs, findings


def load_articles():
    if not CF_DIR.is_dir():
        return None
    return sorted(p.name for p in CF_DIR.glob("*.md") if p.name != "_index.md")


def check_index(articles):
    """Cross check the article files against the trigger index rows."""
    findings = []
    if not INDEX_PATH.is_file():
        return ["STALE INDEX: docs/cf/_index.md does not exist"], {}
    rows = ROW_RE.findall(INDEX_PATH.read_text(encoding="utf-8"))
    counts = {}
    for name in rows:
        counts[name] = counts.get(name, 0) + 1
    for name in sorted(counts):
        if name not in articles:
            findings.append(
                "STALE INDEX: docs/cf/_index.md -> %s (article does not exist)"
                % name)
        if counts[name] > 1:
            findings.append(
                "DUPLICATE:   docs/cf/%s (listed %d times in the index)"
                % (name, counts[name]))
    for name in articles:
        if name not in counts:
            findings.append(
                "ORPHANED:    docs/cf/%s (no index entry)" % name)
    return findings, counts


def file_lines(rel):
    return (ROOT / rel).read_text(encoding="utf-8").splitlines()


def check_drift(refs, manifest):
    findings = []
    by_file = {}
    for ref in refs:
        by_file.setdefault(ref["path"], []).append(ref)
    for rel in sorted(set(list(by_file) + list(manifest))):
        found = by_file.get(rel, [])
        entries = manifest.get(rel, [])
        lines = file_lines(rel) if found else []
        paired = min(len(found), len(entries))
        for i in range(paired):
            ref, entry = found[i], entries[i]
            if entry.get("article") != ref["article"] or \
                    entry.get("lines") != ref["lines"]:
                findings.append(
                    "STALE:       %s:%d (manifest records %s [%s], code has "
                    "%s [%d]; re-run with --write-hashes after review)"
                    % (rel, ref["line"], entry.get("article"),
                       entry.get("lines"), ref["article"], ref["lines"]))
                continue
            if ref["line"] + ref["lines"] > len(lines):
                findings.append(
                    "STALE:       %s:%d (protected block of %d lines overruns "
                    "end of file)" % (rel, ref["line"], ref["lines"]))
                continue
            digest = block_hash(lines, ref["line"], ref["lines"])
            if digest != entry.get("hash"):
                findings.append(
                    "STALE:       docs/cf/%s (code block at %s:%d changed)"
                    % (ref["article"], rel, ref["line"]))
        for ref in found[paired:]:
            findings.append(
                "MISSING HASH: %s:%d -> %s (run with --write-hashes)"
                % (rel, ref["line"], ref["article"]))
        for entry in entries[paired:]:
            findings.append(
                "EXTRA HASH:  %s (manifest entry for %s [%s] has no ref)"
                % (rel, entry.get("article"), entry.get("lines")))
    return findings


def write_manifest(refs):
    manifest = {}
    skipped = []
    by_file = {}
    for ref in refs:
        by_file.setdefault(ref["path"], []).append(ref)
    for rel in sorted(by_file):
        lines = file_lines(rel)
        entries = []
        for ref in by_file[rel]:
            if ref["line"] + ref["lines"] > len(lines):
                skipped.append(ref)
                continue
            entries.append({
                "article": ref["article"],
                "ref_line": ref["line"],
                "lines": ref["lines"],
                "hash": block_hash(lines, ref["line"], ref["lines"]),
            })
        manifest[rel] = entries
    MANIFEST_PATH.write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest, skipped


def main(argv):
    write_mode = "--write-hashes" in argv
    articles = load_articles()
    if articles is None:
        print("cf-check: docs/cf/ does not exist")
        return 1
    refs, findings = scan_refs()
    for ref in refs:
        if ref["article"] not in articles:
            findings.append(
                "BROKEN REF:  %s:%d -> %s (article does not exist)"
                % (ref["path"], ref["line"], ref["article"]))
    index_findings, _ = check_index(articles)
    findings += index_findings

    if write_mode:
        valid = [r for r in refs if r["article"] in articles]
        _, skipped = write_manifest(valid)
        for ref in skipped:
            findings.append(
                "STALE:       %s:%d (protected block overruns end of file; "
                "no hash recorded)" % (ref["path"], ref["line"]))
    else:
        manifest = {}
        if MANIFEST_PATH.is_file():
            try:
                manifest = json.loads(
                    MANIFEST_PATH.read_text(encoding="utf-8"))
            except ValueError:
                findings.append(
                    "STALE:       docs/cf/_hashes.json is not valid JSON")
        findings += check_drift(refs, manifest)

    if findings:
        for finding in findings:
            print(finding)
        print("cf-check: %d finding(s)" % len(findings))
        return 1
    print("cf-check: OK (%d refs, %d articles, all hashes current)"
          % (len(refs), len(articles)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
