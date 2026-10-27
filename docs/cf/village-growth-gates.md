# Growth Is Earned at the Boundary, Never Labored, Never Silent

growSeasonCheck() runs once, at the start of endWeek, right after
claimSeasonCheck() and before the ledgers reset, so it reads the
just-finished season. It extends the buildable boundary only when
every gate holds at that moment: the game is started and not over,
the village stands at Town tier (villageLevel().count >= 9, the same
gate as CLAIM), contentment() is at or above GROWTH.growMin, and
fewer than GROWTH.growMaxRings growth rings exist. If any gate
fails, the check returns and tries nothing else that season.

The extension is one plot-ring: GROWTH.growRingPlots surveyed plots
appended to the PLOTS data list by data extension, never hardcoded.
Each slot sits at the current boundary edge plus GROWTH.growRingStep
on a ring-rotated bearing set (the bearings rotate 135 degrees per
ring so growth does not stack on one side), validated
GROWTH.growPlotClear clear of every plot and GROWTH.growStationClear
clear of every station, with the river band excluded. A ring ships
with whatever slots validate; a fully blocked edge stalls with a
named toast and a chronicle line instead of a partial write.

Growth is earned, never labor: no wk() calls, no costs, no party, no
tray verb, so growth can never leak into the driven-work ledgers.
The trigger names its cause: the toast and the chronicle read the
contentment value that earned the ring, with a camera-focus chip on
the new ground. Growth rings persist in the save (G.growPlots is
re-extended onto PLOTS on Continue, G.growRings counts the rings),
and the new plots accept Founding exactly like the original six
through the ordinary foundSite path.

The gate also reads ahead: the stats panel carries a growth row
(growLbl, rendered by renderHud after the tier row) that names the
Town gate below Town, the contentment against the 78 line at Town,
and the ring count throughout, and promises no further ring once
all four rings are grown. The read names the gate, it never moves
it: no gate, ledger, or labor rule in this article changes because
the row exists.

Why: earned ground must read as earned. A boundary that grows only
at the season boundary, only past a named contentment price, with
the price printed on the receipt, teaches the player that good
mimesis expands the village; silent or labored growth would be
indistinguishable from a bug. The ring caps (max rings, clearances,
the stall instead of a partial write) keep one high-contentment
season from paving the map.
