# Rivalry Drift: Feuds Leave a Residue, and the Record Is Auditable

A feud eruption is not a reset. It ignites a drift record on the pair,
and the record outlives the incident that caused it.

Ignition. When addTension pushes a pair past 70 and the feud erupts,
the eruption writes three things in the same branch: the pair's
tension settles to MIM.driftResidue (45), not a clean reset; G.drifts
gains the pair key with the starting floor and the season stamps;
G.driftLog appends the ignition ledger entry (the two ids and names,
the season stamps, the station they were converging on or null, the
shared model or null), capped at MIM.driftLogCap entries. The
chronicle names the cause in the same line ("X and Y fell into a feud
over the Clinic.", station named when known). A re-eruption refreshes
the record: floor back to the residue, a new ledger entry, a new
chronicle line.

Drift. While a drift is active the pair's tension decays at
MIM.driftDecay (0.12) per second instead of 0.5, except on the green,
which always cools at 2.4 (the household-partner discount still
applies). Separation still works: only co-stationed pairs reheat. When both members of a drifted pair are acting at the
same station other than green or home, their tension reheats at
MIM.driftReheat (0.35) per second through addTension, so the feud
warning at 50 and the eruption at 70 fire normally. The triggering
want is forgotten; proximity alone sustains the conflict. All drift
numbers live in the MIM table; never scatter new constants through
statDrift or the feud branch.

Cooling and clearing. Each season boundary lowers every drift floor by
MIM.driftFloorDecay (6), floored at MIM.driftFloorMin (10). When a
floor is at or below MIM.driftClearFloor (15) and the pair's tension
is at or below MIM.driftClearTension (20), the drift clears and the
chronicle records the quiet ("The feud between X and Y has gone
quiet."). Ordering either member relieves all their pair tension by
22, which can end a drift. Removing an agent deletes their drift
keys, the same discipline as the tension ledger.

Visibility. The tension lens draws an active drift pair as a dashed
edge, even below the 40 heat threshold, with a "--- feud drift"
legend line: shape, never color alone. The character sheet carries the
per-resident leg of the auditable record (v4 view step 4): the selected
resident's sheet lists every active drift pair with the partner's name,
the station they converged on, the shared model, the ignition season
stamps, and the live tension number, plus the current convergences
(residents wanting the same station right now). Cleared drifts leave
the sheet; their ledger entries stay in the chronicle. The sheet
section omits itself when there are no records, and it never explains
or moralizes: facts and numbers only. The feud warning names its lever (separate them or cool them on the
green), and the eruption toast now carries the same lever sentence,
because ordering either member and the green still cool the pair
after eruption. The drift is never a verb or a button;
scapegoating stays emergent and nonconscious.

Mimetic cause. The drift record is written at the moment converging
desires (along a.model edges, counted in G.mimic.converged) push
G.pairs past the feud point; the residue is the graph's own tension
ledger, never a fresh modifier. Reheat reads live station membership,
not hidden state. Old snapshots predate G.drifts and G.driftLog, so
every read is defensive; the save version is unchanged.
