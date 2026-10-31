# CF-DOC Trigger Index

## Rendering and Overlays
overlay, marker, bubble, name tag, hud, camera move, collision, anchor, hide, desire lens, lens mode, toast, pause

| Article | Summary |
|---------|---------|
| overlay-anchor-budget.md | Markers stay within 56px up and 110px sideways of their resident, or hide; the selected resident's card may sidestep past the sideways cap when the west-edge nudge clears the HUD column |
| desire-lens.md | The desire lens draws model-to-follower edges from live a.model edges, thickness by follower count, one lens active at a time, view only; the Lens button names its active mode persistently |
| soil-tints.md | The field soil boxes and crop cones render the soil clock stage on the map itself: recolor plus stunted height per stage, display only |
| claim-minimap.md | Surveyed plots read on the minimap: original plots as gold outline squares, CLAIM/GROW plots filled solid, an in-flight claim as a dashed gold ring, display only |
| proclaim-minimap.md | The season focus reads on the minimap for exactly the week it holds: the tray megaphone glyph above the focus station or site plot, ringed dashed in gold, display only |
| claim-preview.md | The pending claim reads on the map before staking: a gold ring at the picked center plus three dots at the pending cluster, no pole or flag; a blocked center breaks the ring, hollows the dots, and crosses the center, display only |
| camera-rotate-buttons.md | The speeds-row rotate buttons step cam.yaw by the Q/E step (left +0.35, right -0.35), never clear a camera follow, and ride the thumb-zone move into the tray on phones |
| camera-zoom-buttons.md | The speeds-row zoom buttons step cam.dist by the wheel factor (in 0.9, out 1.1, clamped 15 to 62), never clear a camera follow, and ride the thumb-zone move into the tray on phones, whose buttons narrow by side padding only to fit the pair |
| camera-key-pan.md | Arrow keys and WASD pan the view one dist step per press along the yaw-relative axes, clamped to the camera bounds, clearing a camera follow like a drag |
| camera-key-zoom.md | Plus and equals zoom in, minus and underscore zoom out, stepping cam.dist by the wheel factor (in 0.9, out 1.1, clamped 15 to 62), never clearing a camera follow |
| camera-key-follow.md | F toggles cam.follow on the selected resident, exactly the Follow button's verb, doing nothing with no selection and never changing the selection |
| follow-edge-scroll.md | Mouse edge scroll stands aside while a camera follow holds: it neither moves the camera nor drops the mode; drag, minimap jump, and selection stay the explicit follow releases |
| coach-teach-line.md | A gold line joins the loafer coach cone to the destination station coach cone while the first-order teach window holds, and vanishes with the cones at the first order, display only |
| paused-toast-holds.md | While speed is 0 the live toast's deadline advances with the frame clock, so a pause never loses the message or drains the queue behind it; a skipped toast is never revived |

## Game Rules and Scoring
objective, progress, project, parts, work credit, score, driven, order bonus, household, arrival, newcomer, cottage, capacity, speak for, blame, want, desire, model, spread, contagion, origin, coverage, tier, premium, medic, queue, call out, founding, growth, expansion, autonomous, plot

| Article | Summary |
|---------|---------|
| driven-work-progress.md | Progress reads weekWorkP only, credited through the driveObj gate in wk() |
| household-capacity-ledger.md | Housing is one ledger: households plus solo newcomers never exceed G.houseCapacity |
| departure-forecast.md | The departure rule renders before it can fire: contentment under 30 with blame at 60 or more forecasts the lowest-morale household once per approach, display only |
| desires-travel-the-graph.md | Wants carry an origin; spread follows model edges first, convergence adds tension, fulfillment and misses write back into the graph |
| membership-never-gates-the-medic.md | The medic serves everyone through the manual path; tiers move only queue order and the death roll; premiums debit bank only, floor zero, lapse never debt |
| autonomous-founding-gates.md | The village founds at most one building a season, at the boundary, only when every GROWTH gate holds, through foundSite |
| rivalry-drift.md | A feud eruption leaves a tension residue with an auditable ignition record; proximity reheats the drift, time and the green cool it, the lens shows it dashed |
| model-prestige-flip.md | Past a documented vis threshold a model attracts rivalry instead of admiration; the flip is announced and shown as a sheet line, never silent, and a latched forecast warns a followed model within 10 of the threshold before it flips |
| village-growth-gates.md | Growth extends the boundary one plot-ring per qualifying season at Town tier, earned never labored, the price named on the receipt |
| road-building.md | Roads are built segments between stations at Town tier, priced by distance, laid by a crew from the imitation graph, and they shorten walks only on the segment |
| recall-in-flight.md | An in-flight claim, road, or founded site can be called off from its tray verb; carried stores come home, the party, crew, or builders walk home, and the slot or plot frees |
| claim-adjacency.md | A workshop within 20 units of the mill builds 25 percent faster and a completed hall within 20 of the green mediates 25 percent faster, judged live, previewed in the claim pick row before Stake |

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
| idle-finder.md | The Idle button cycles one loafer at a time, orders nothing, and never carries a lit treatment |
| control-groups.md | Three recall slots, one resident each: Groups arm plus chip tap assigns, chip tap or digit recalls and centers, a gone resident clears the slot |
| keyboard-escape-close.md | Escape closes the topmost closable panel first (Story overlay, then sheet), never an incident panel, never a deselect |
| minimap-canvas-tap.md | Minimap jump is detected in endPointer at canvas level, never on the element |
| pointercancel-never-a-tap.md | pointercancel only resets pointer state; only pointerup can become a tap |

## Character Sheet and Phone Layout
sheet, character panel, objective card, project pick, mobile, phone, layout, overlap, stats, stats panel, meter strip, pick row, compact

| Article | Summary |
|---------|---------|
| sheet-below-objective-card.md | On small screens hudTick pins the open sheet below the objective card |
| phone-stats-compact-during-picks.md | On phones an open decision pick row compacts the stats panel to a meter strip; a panel that would sit behind the objective card compacts on collision, or hides until it fits |
| pick-rows-scroll-on-phones.md | On phones every objective-card pick row caps below the card content and scrolls internally, with wrapping chips, so the commit chip is always reachable |
| phone-alerts-shed-on-collision.md | On phones the alerts stack sheds lowest priority first when it would cover the objective card, and the shed chips return when space returns |

## Thoughts and Temperament
thought, monologue, axis, label, persona, generation, inference, llm, template

| Article | Summary |
|---------|---------|
| axis-label-selected-surfaces.md | The axis chip renders only in the tray role line and the sheet header |
| thoughts-local-inference-only.md | Thought generation is on-device only; never an API key or cloud call |
