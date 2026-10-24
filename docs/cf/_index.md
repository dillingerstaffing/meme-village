# CF-DOC Trigger Index

## Rendering and Overlays
overlay, marker, bubble, name tag, hud, camera move, collision, anchor, hide

| Article | Summary |
|---------|---------|
| overlay-anchor-budget.md | Markers stay within 56px up and 110px sideways of their resident, or hide; the selected resident's card may sidestep past the sideways cap when the west-edge nudge clears the HUD column |

## Game Rules and Scoring
objective, progress, project, parts, work credit, score, driven, order bonus, household, arrival, newcomer, cottage, capacity, speak for, blame, want, desire, model, spread, contagion, origin, coverage, tier, premium, medic, queue, call out, founding, growth, expansion, autonomous, plot

| Article | Summary |
|---------|---------|
| driven-work-progress.md | Progress reads weekWorkP only, credited through the driveObj gate in wk() |
| household-capacity-ledger.md | Housing is one ledger: households plus solo newcomers never exceed G.houseCapacity |
| desires-travel-the-graph.md | Wants carry an origin; spread follows model edges first, convergence adds tension, fulfillment and misses write back into the graph |
| membership-never-gates-the-medic.md | The medic serves everyone through the manual path; tiers move only queue order and the death roll; premiums debit bank only, floor zero, lapse never debt |
| autonomous-founding-gates.md | The village founds at most one building a season, at the boundary, only when every GROWTH gate holds, through foundSite |

## State and Architecture
state, store, dispatch, transact, render, dom, panel, new field, new event, chronicle, save, snapshot, ending, persistence, continue, grave

| Article | Summary |
|---------|---------|
| store-single-source.md | Store.state is the only state; only the four subscribed renderers write DOM |
| chronicle-and-saves.md | The chronicle is written by systems only; saves are versioned, index based, and restored only via Continue |
| spec-tables-drift-gate.md | Content lives in spec-registered data tables; the drift gate fails on dead rows, undefined references, or stale JSON |

## Input and Touch
tap, drag, scroll, touch, pointer, gesture, tray, alerts, minimap, button, click, highlight, armed, selection panel

| Article | Summary |
|---------|---------|
| tray-passes-taps.md | Overlay containers are pointer-events none; only their buttons capture |
| highlight-vocabulary.md | Each tray treatment means one thing: teal is the current order, gold is the one armed verb, status is chips never lit buttons |
| minimap-canvas-tap.md | Minimap jump is detected in endPointer at canvas level, never on the element |
| pointercancel-never-a-tap.md | pointercancel only resets pointer state; only pointerup can become a tap |

## Character Sheet and Phone Layout
sheet, character panel, objective card, project pick, mobile, phone, layout, overlap, stats, stats panel, meter strip, pick row, compact

| Article | Summary |
|---------|---------|
| sheet-below-objective-card.md | On small screens hudTick pins the open sheet below the objective card |
| phone-stats-compact-during-picks.md | On phones an open decision pick row compacts the stats panel to a meter strip |

## Thoughts and Temperament
thought, monologue, axis, label, persona, generation, inference, llm, template

| Article | Summary |
|---------|---------|
| axis-label-selected-surfaces.md | The axis chip renders only in the tray role line and the sheet header |
| thoughts-local-inference-only.md | Thought generation is on-device only; never an API key or cloud call |
