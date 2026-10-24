#!/usr/bin/env python3
"""spec-tables-extract: parse the SPEC-TABLE markers in game-spec.md (section 25)
into docs/data/spec-tables.json.

The spec is the definition of record. This script is the data stage of the
v4 drift gate (world-expansion-research-brief.md 5.4): one extraction, zero
drift by construction. Run it after editing a marker, then commit the JSON
with the spec.

Marker format (one per line, inside game-spec.md):

  <!-- SPEC-TABLE name=STATION3 status=live keys=clinic,fields,store -->
  <!-- SPEC-TABLE name=PLOTS status=live keyless=true rows=6 -->
  <!-- SPEC-TABLE name=ADJACENCY status=queued columns=kindA,kindB fixed=a:b -->

Usage:
  python3 tools/spec-tables-extract.py            # write docs/data/spec-tables.json
  python3 tools/spec-tables-extract.py --stdout   # print canonical JSON
"""

import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SPEC = Path.home() / "workspace/goals/meme-village-full-3d-rebuild/hidden_files/game-spec.md"
OUT = REPO / "docs/data/spec-tables.json"

MARKER = re.compile(r"<!--\s*SPEC-TABLE\s+(.*?)\s*-->")


def parse_marker(body):
    table = {}
    for m in re.finditer(r"(\w+)=([^\s]+)", body):
        k, v = m.group(1), m.group(2)
        table[k] = v
    if "name" not in table or "status" not in table:
        raise ValueError("SPEC-TABLE marker missing name/status: %r" % body)
    if "keys" in table:
        table["keys"] = [k for k in table["keys"].split(",") if k]
    if table.get("keyless") == "true":
        table["keyless"] = True
        table["rows"] = int(table.get("rows", "0"))
    if "columns" in table:
        table["columns"] = [c for c in table["columns"].split(",") if c]
    if "fixed" in table:
        table["fixed"] = [r for r in table["fixed"].split(",") if r]
    return table


def extract(spec_path=SPEC):
    text = spec_path.read_text(encoding="utf-8")
    tables = {}
    for m in MARKER.finditer(text):
        t = parse_marker(m.group(1))
        name = t.pop("name")
        if name in tables:
            raise ValueError("duplicate SPEC-TABLE marker for %s" % name)
        tables[name] = t
    if not tables:
        raise ValueError("no SPEC-TABLE markers found in %s" % spec_path)
    return {"tables": tables}


def canonical(data):
    return json.dumps(data, indent=2, sort_keys=True) + "\n"


def main():
    data = extract()
    if "--stdout" in sys.argv:
        sys.stdout.write(canonical(data))
        return
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(canonical(data), encoding="utf-8")
    print("wrote %s (%d tables)" % (OUT, len(data["tables"])))


if __name__ == "__main__":
    main()
