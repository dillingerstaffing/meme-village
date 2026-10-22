# The Village Founds at Most One Building a Season, at the Boundary, Through the Player Path

foundingCheck() runs once, at the end of endWeek, after arrivals and
departures have resolved. It founds nothing unless every gate in the
GROWTH table holds at that moment: the game is started and not over,
no founding has happened yet this season (G.lastFoundSeason against
G.week), at least one household exists, contentment() is at or above
GROWTH.contentmentMin, housingFree() is exactly 0, G.builtWealth is
at or above GROWTH.wealthMin, and at least one surveyed plot is free.
If any gate fails, the check returns without founding and tries
nothing else that season.

The founding itself is not a second path: it calls foundSite() with
the first free plot and the kind the GROWTH.kindOrder preference
resolves to (a later kind in the order must also clear its level gate
and double the wealth minimum), founded by the earliest-formed
household. Materials, site records, meshes, the founding toast, and
the chronicle line are exactly the ones a player founding produces.
Construction then proceeds through the ordinary build labour system.
If foundSite() refuses (its own gates: unknown kind, level lock,
occupied plot), the check treats that as a closed gate and stops.

Why: growth the player never chose must never outrun the player. One
founding per season, at the boundary, behind strict surplus gates,
means the village visibly thrives without silently spending plots
the player was saving, and a single founding path means autonomous
and player buildings can never diverge in cost or behaviour.
