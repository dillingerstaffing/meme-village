# Roads Are Built Segments That Shorten Walks, Never Drawn Overlays

layRoad() builds one road at a time between two different STATION3
stations (never "home"), at Town tier (villageLevel().count >= 9, the
same gate as CLAIM), and only when no other road is under construction.
The price is named before anything commits: the Road pick row previews
CONNECT_ROAD basePlanks plus one plank per planksPerDist world units of
station-to-station distance on every To chip and repeats it on the Lay
confirm. The route is shown before anything commits too: once both
ends are picked, syncRoadPreview() (called from hudTick's road-pick
row, the per-frame HUD render, so every pick change re-syncs it)
draws a gold ghost strip between the two stations, in the Factorio
ghost grammar: a semi-transparent marker for the thing to be built,
doing none of the thing's work. Picking a different end, cancelling,
arming another verb, or laying the road clears it; it never enters
G.roads, never boosts a walker, and never survives a save. The ghost
is gold where surveyed lines are brown and built roads are packed
earth, and it carries no flags, so a ghost can never be mistaken for
a road. A pair already joined by a road refuses with the reason
named, and the refusal names the way back: re-arm Road and pick
two stations not yet joined, because the failed lay disarms the
verb and the pick row closes with it. Before the commit, the Lay chip names the joined state
for such a pair (no priced Lay chip offered), in the blocked-Claim
grammar, so the player sees the refusal before committing; the chip
stays tappable, so tapping it still refuses loudly rather than
going silent. The village keeps at most
CONNECT_ROAD.maxRoads roads, and the cap reads before any lay: the
stats panel claim row (claimLbl, rendered by renderHud after the
growth row) names the live road count against the cap once Town is
reached, and names the Town gate for both verbs below Town. The row
is display only and changes no gate.

The road crew is recruited from the imitation graph: the earliest-formed
household's members plus up to 2 admirers (followersOf counts, spec
section 4), children, the sick, the departed, and existing crew excluded.
Crew members stay committed through the decide() roadCrew hook, fetch
planks from the lumber pile to the road midpoint, and deposit them into
the road's matsIn. Road carries make no wk() calls, so road labor never
leaks into the driven-work ledgers (the same rule as claim carries).
A crew member walked out walks out clean: goRoad() settles any
unrelated carry before the walk, in the recall's own terms, so a
season-boundary re-recruit cannot deposit a crate into a site from
the road midpoint or fire a pickup leg there: a site or claim crate
carry returns one store, every other carry drops with nothing owed,
and fetch and carrying clear. It cancels the social intent on the
same rule as the other walk-replacing doors: visitId, pendingWatch,
and a stale watchOf clear before the walk, or arrive() fires the
stale leg at the road midpoint instead of the road work. The initial lay walks the crew out
through decide() when idle, after any haul has completed on arrival,
so the settle changes nothing there; it bites on the re-recruit
walk-out, which walks a resident out at once whatever they were doing.
When the carried planks meet the cost, the road is built: the surveyed
line becomes a solid packed-earth strip with a Settlers flag at each
end, the crew is released, and a camera-focus toast plus a chronicle
line name the finished road.

The walk boost is physical, not a tooltip number: roadBoostFor() runs in
the walk branch and returns CONNECT_ROAD.walkMult only when the
walker's position sits inside the road's corridor
(CONNECT_ROAD.corridorHalf) and the walk direction runs within
CONNECT_ROAD.alignDeg of the road's bearing, either way. Walkers
crossing the road gain nothing. The multiplier applies to carrying and
unloaded walkers alike, so roads shorten both walk times and material
carries. Roads are drawn on the minimap too: solid lines for built
roads, dotted surveyed lines while under construction.

Roads persist in the save (G.roads); on Continue their meshes rebuild,
an in-flight road keeps its carried planks, the crew's roadCrew flags
survive on the agents, and G.roadBuild re-points at the restored road
record. The season boundary re-recruits a scattered crew or abandons
the half-laid road (mesh removed, record dropped) rather than leaving a
permanent surveyed line.

Why: the transport ladder must be visible on the map itself. A road
that only changed a number would be superstition; a road the player
watches the crew lay, plank by plank, and then watches walkers move
visibly faster along, teaches the Factorio tier rule at village scale:
walking < roads < (later) carts.
