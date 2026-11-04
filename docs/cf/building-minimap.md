# Building Minimap: Founded Sites Read on the Strategic Channel

A plot square alone cannot say whether its ground is empty, rising,
or built, so a founded site draws over its own plot at a larger size
on the minimap: a finished site as a bordered cream square (7px, the
station cream with a dark outline, larger than the 6px station square
and bordered where stations are plain), an unfinished site as a dashed
gold outline (7px, dashed where the empty plot outline is solid 4px).
Shape plus fill plus size, never color alone, so the three states
(empty plot, rising site, finished building) stay apart at phone
minimap scale too.

- drawMinimap draws every plot site in G.sites at its mapped position,
  after the plot squares and the claim ring, so the building mark
  replaces the empty plot read at that spot.
- Project sites are skipped: their plot is -1 and they sit at station
  marks already drawn, so drawing them again would double mark a
  station.
- Display only: the block reads G.sites and writes the minimap canvas.
  It never writes state, never calls wk(), never touches the
  driven-work ledgers, and never changes a site, a plot, or a road.
  The 3D staged meshes and tap targets are untouched; this layer is
  the same building on the second channel.

Why: the minimap already showed stations, roads, surveyed plots, and
claims, but a finished cottage read exactly like the empty plot it
stood on, and a rising site read like no site at all. A player
returning to the strategic channel could not find a building they
had paid labor for without flying the camera there. The building
layer closes that gap at the same grammar as the claim layer, with
no new verb, no new panel, and no sim change.
