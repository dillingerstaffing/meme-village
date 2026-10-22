# CF-DOC Trigger Index

## Rendering and Overlays
overlay, marker, bubble, name tag, hud, camera move, collision, anchor, hide

| Article | Summary |
|---------|---------|
| overlay-anchor-budget.md | Markers stay within 56px up and 110px sideways of their resident, or hide |

## Game Rules and Scoring
objective, progress, project, parts, work credit, score, driven, order bonus, household, arrival, newcomer, cottage, capacity, speak for, blame, coverage, tier, premium, medic, queue, call out

| Article | Summary |
|---------|---------|
| driven-work-progress.md | Progress reads weekWorkP only, credited through the driveObj gate in wk() |
| household-capacity-ledger.md | Housing is one ledger: households plus solo newcomers never exceed G.houseCapacity |
| membership-never-gates-the-medic.md | The medic serves everyone through the manual path; tiers move only queue order and the death roll; premiums debit bank only, floor zero, lapse never debt |

## State and Architecture
state, store, dispatch, transact, render, dom, panel, new field, new event, chronicle, save, snapshot, ending, persistence, continue

| Article | Summary |
|---------|---------|
| store-single-source.md | Store.state is the only state; only the four subscribed renderers write DOM |
| chronicle-and-saves.md | The chronicle is written by systems only; saves are versioned, index based, and restored only via Continue |

## Input and Touch
tap, drag, scroll, touch, pointer, gesture, tray, alerts, minimap, button, click

| Article | Summary |
|---------|---------|
| tray-passes-taps.md | Overlay containers are pointer-events none; only their buttons capture |
| minimap-canvas-tap.md | Minimap jump is detected in endPointer at canvas level, never on the element |
| pointercancel-never-a-tap.md | pointercancel only resets pointer state; only pointerup can become a tap |

## Character Sheet and Phone Layout
sheet, character panel, objective card, project pick, mobile, phone, layout, overlap

| Article | Summary |
|---------|---------|
| sheet-below-objective-card.md | On small screens hudTick pins the open sheet below the objective card |

## Thoughts and Temperament
thought, monologue, axis, label, persona, generation, inference, llm, template

| Article | Summary |
|---------|---------|
| axis-label-selected-surfaces.md | The axis chip renders only in the tray role line and the sheet header |
| thoughts-local-inference-only.md | Thought generation is on-device only; never an API key or cloud call |
