# Spec tables drift gate

Game content lives in data tables, not in code branches. The row-key tables
(STATION3, RES3, NEED_DEFS, INCIDENTS, PROJECTS, BUILD_KINDS) and the keyless
tables (PLOTS, OBJECTIVES, NEWCOMERS) are the single source for kinds, tiers,
stations, and content rows; the v4 tables (ADJACENCY, CLAIM_COST, DEPLETION,
MODEL_PRESTIGE) join them when their rows ship.

The tables are registered in game-spec.md section 25 with machine-readable
SPEC-TABLE markers. tools/spec-tables-extract.py parses those markers into
docs/data/spec-tables.json (the build's data stage). tools/spec-tables-check.py
is the drift gate and FAILS when:

- the JSON is stale against the spec markers (edit the marker, re-run the
  extractor, commit both; one file to update, zero drift by construction);
- a registered key of a key-lookup table is never named outside its own table
  block (a dead row rots into a lie);
- code references a key a table does not define, through the table's accessor
  patterns or cross-table references (a resident's aff names a STATION3
  station, their admires names a RES3 resident, a project's station names a
  STATION3 station, its part keys name PART_STATION keys, PART_STATION values
  name STATION3 stations, PROJ_SITE_POS names PROJECTS ids, GROWTH.kindOrder
  names BUILD_KINDS kinds, an incident's patient names a RES3 resident);
- a keyless table's row count drifts from its registered count.

Iteration-consumed tables (RES3 read by makeAgents, BUILD_KINDS read by
foundableKinds) cannot have dead rows by construction; for them the gate
asserts the iteration path exists and still checks everything their rows
point at. Queued tables report QUEUED and their code checks engage when
their rows ship (v4 step 3).

Adding a row means: update the marker in game-spec.md section 25,
re-run the extractor, keep the gate green. A row the gate does not know is
not done. Scalar tunables (LIFE, ECON, KIDS, MIM, TTI, INCIDENT_PACE) stay
prose definitions of record until a later gate covers them. The CF-REFs on
the table blocks in index.html mark the definitions the gate protects;
changing a block's rows without updating the marker fails the gate.
