# Model-Prestige Flip: Admired Past a Point, Envied Past the Flip

A model's prestige is their a.vis, the same 0 to 100 stat that already
gates name display, charisma watching, inspiration strength, and want
spread (spec section 4). Past the documented flip point the imitation
graph treats the model as an obstacle instead of an example: this is
the Girard model/rival flip from the v4 brief (5.2), "flattered by
adoption, threatened when the imitator becomes too much like me."

The flip point lives in data, not code: MODEL_PRESTIGE.prestigeFlip
{sourceStat: "a.vis", threshold: 85, flipBehavior: "rivalry"}, spec
sections 4/24, checked by the spec drift gate (spec-tables-drift-gate.md).
The heat a flipped copy lays is the one MIM tunable of the system:
MIM.prestigeFlipTension (12, provisional).

The flip engages at Village tier and above (prestigeFlipUnlocked:
villageLevel().count >= 2). Hamlet stays a learning tier where models
are always admired. The sheet names the visible stat: follower count,
and at Village tier and above the standing, "admired" or
"envied (past 85)". prestigeStanding() builds that line; renderSheet
writes it and keys it into the sheet diff so it re-renders on change.

Behavior. On a watch-completion copy, when the model is not
spotlighted: below the flip the event lays the admiration pattern
(+6 tension watcher to model, +9 watcher to one co-admirer at the
same station, desires-travel-the-graph.md). Past the flip it lays
rivalry heat instead (+MIM.prestigeFlipTension watcher to model) and
the sideways +9 is skipped: the desire has redirected from the object
to the model as the obstacle. Spotlight suppression still wins (no
tension at all while the model is spotlighted). The heat feeds the
existing feud machinery (warning at 50, eruption at 70), so an envied
model can feud with their own followers; the tension lens shows it
like any pair edge.

Announcements. prestigeScan runs on a 1-second tick in stepSim and
recomputes G.prestigeFlip from live a.vis and the tier gate; nothing
else writes the flags. Crossing upward fires a camera-focus toast
naming the model plus a chronicle line; crossing back down fires a
plain toast plus a chronicle line. The flip is never silent, and it
is never a surprise either: a forecast fires before it. At Village
tier and above, a model with at least one follower whose a.vis is
within 10 of the threshold (75 to 84) gets one latched warning per
approach, on the blame/departure forecast grammar: a bubble, a
camera-focus toast naming the threshold and the consequence, a
minimap ping, and the warn sound, with no chronicle line (the
crossing itself chronicles). The latch lives in G.prestigeWarn, set
in newSlice and guarded in restoreState like G.prestigeFlip; it
clears when a.vis drops below the band or the model flips, so it
re-arms on the next approach and never goes stale. Below Village
tier, or with no followers, it stays silent: a flip with no
followers changes no copy event. The counter-move the toast names
is the Model verb: re-pointing followers elsewhere shrinks the
flip's blast radius, since a flipped copy lays its heat only on
followers who still copy.

Persistence. G.prestigeFlip rides the wholesale G serialization;
restoreState guards it for older saves. Derived state is never trusted
across a load: the next prestigeScan recomputes it.

Guards: prestigeFlipUnlocked and prestigeScan are probe-facing through
SLICE.prestige (unlocked, threshold, heat, per-id flipped, vis, and
follower counts). Do not add a second flip stat, do not move the
threshold into code, and never let the flip fire below the tier gate.
