# Season Tints: Winter Reads on the Map Itself

The season is visible on the map itself, never only in a toast or a
card kicker. The Stardew standard: each season carries a distinctive
visual style, so the player reads the time of year by looking at the
world, not by opening a panel. Winter is the season that needs the
read most: it carries the scarcity bill and the death roll, and it
used to look exactly like spring.

- applySeasonTint() runs in stepSim beside applySoilTint(), diffs
  G.seasonTintApplied against the season key ("winter" or "other"),
  and on change only: recolors the stored ground material, the tree
  foliage, and the hill meshes, recolors the fog and the hemisphere
  ground color, and repaints the sky gradient canvas. On any other
  frame it does nothing.
- The tints: winter ground 0xe6edf2 against the summer 0xffffff (the
  color multiplies the ground canvas texture, so the fields pale
  toward snow without losing the paths), winter foliage 0x8ba08f
  against 0x557f42, winter hills 0x9aa892 against 0x6d9153, winter
  fog 0xdde8f0 against 0xcfe9f2, winter hemisphere ground 0x8b9aa0
  against 0x5d7a45, winter sky stops #a8c4d8, #c8dcea, #e8f0f4
  against #6fb6e6, #a8d8f0, #e8f6ee. A non-winter season restores
  every value, so spring after winter is the same green the game
  opened with.
- The materials are stored at build time (seasonTintRefs, filled in
  buildWorld) instead of re-found: buildWorld is the only place that
  names them, and the tint never searches the scene graph or reads
  DOM. The crop cones are deliberately not tinted here: their color
  is the soil system's readout, owned by applySoilTint.
- Display only: the tint writes no sim state except the view
  bookkeeping G.seasonTintApplied, never calls wk(), never touches
  the driven-work ledgers, and never changes a yield, a threshold,
  or a season boundary. A season restored from a save re-tints on
  the first stepSim frame, because the diff runs every frame, not
  only at the season boundary.

Why: winter arrived with a forecast toast, an arrival toast, and a
card kicker, but the world never changed: a player who missed the
toasts could play the whole hardest season without seeing it. The
tint closes that gap at the Stardew standard: the state of the year
is legible from the ground.
