# Claim Minimap: Surveyed Ground Reads on the Strategic Channel

Claimed and grown ground must read on the minimap, not only as gold
rings in the 3D view. The Civ standard: claimed land is marked on the
map for all to see, so the player can read what they own without
flying the camera there. A claim staked far out, or a growth ring
beyond the village edge, is otherwise invisible on the strategic
channel, and the player cannot find new ground they paid for.

- drawMinimap draws every PLOTS entry at its mapped position:
  original surveyed plots as gold outline squares, plots CLAIM or
  GROW appended (a cluster or ring key on the row) filled solid.
  New ground reads solid, old ground reads as an outline: shape
  plus fill, never color alone.
- An in-flight claim (G.claim present and not staked) draws a dashed
  gold ring at its center, the road grammar for work not yet built:
  dotted while under construction, solid when built.
- Display only: the block reads PLOTS and G.claim and writes the
  minimap canvas. It never writes state, never calls wk(), never
  touches the driven-work ledgers, and never changes a claim, a
  road, or a plot. The 3D rings and tap targets are untouched; this
  layer is the same ground on the second channel.

Why: the sim already built roads onto the minimap (solid when
built, dotted while surveyed) but left plots off it entirely, so
the strategic channel showed the transport network and hid the
territory it serves. The claim layer closes that gap at the same
grammar, with no new verb, no new panel, and no sim change.
