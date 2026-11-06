# Minimap Feud Heat: Warned Pairs Read on the Strategic Channel

A pair at or past the feud-warning threshold (tension 50) must read on
the minimap without the tension lens. The SC2 standard: the minimap is
the alarm, flashing where the trouble is while it lasts, so a player
who misses the toast still finds the fight. Meme Village's feud ping
lasts 4 sim-seconds and the warning toast expires, while the heat
itself persists for minutes at the drift (0.12 per second) and base
(0.5 per second) cooling rates, so a warned pair was invisible on the
strategic channel after the flash, unless the player opened the lens.

- drawMinimap draws every G.pairs entry at or past 50 as an edge
  between the two residents' dots, gold below 60 and red at or above
  60, with a gold ring on each member, in the tension lens's own
  grammar. Pairs below 50 draw nothing in this layer.
- The layer is skipped while the tension lens stands open, because
  the lens already draws every pair at or past 40 with the same
  geometry; the lens adds the sub-50 pairs, the drift dashes, and
  the legend, and nothing is double-drawn.
- Display only: the block reads G.pairs and writes the minimap
  canvas. It never writes state, never calls wk(), never touches
  the driven-work ledgers, and never changes a pair, a drift, or
  a warning. The 3D markers, the ping, and the toast are untouched;
  this layer is the same heat on the second channel.

Why: the sick ring already proves the grammar, a persistent state
that needs the player's attention reads on the minimap without a
lens. A feud at warning heat needs the player at least as much as
a sick resident does, and the warning names two residents the
player must find and separate or cool on the green. The lens stays
the fuller audit read; this layer is the alarm.

