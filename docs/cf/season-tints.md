# Season Tints: Every Season Reads on the Map Itself

The season is visible on the map itself, never only in a toast or a
card kicker. The Stardew standard: each season carries a distinctive
visual style, so the player reads the time of year by looking at the
world, not by opening a panel. Winter is the season that needs the
read most: it carries the scarcity bill and the death roll, and it
used to look exactly like spring. Summer and autumn used to read as
spring too, so half the year was indistinguishable on the map.

- applySeasonTint() runs in stepSim beside applySoilTint(), diffs
  G.seasonTintApplied against the season key ("spring", "summer",
  "autumn", or "winter"), and on change only: recolors the stored
  ground material, the tree foliage, and the hill meshes, recolors
  the fog and the hemisphere ground color, and repaints the sky
  gradient canvas. On any other frame it does nothing. The palettes
  live in one table, SEASON_PALETTES, keyed by season number, so a
  new season read is a new row, never a new branch.
- The tints: spring ground 0xffffff, foliage 0x557f42, hills
  0x6d9153, fog 0xcfe9f2, hemisphere ground 0x5d7a45, sky stops
  #6fb6e6, #a8d8f0, #e8f6ee. Summer deepens and warms it: ground
  0xfbfbe8, foliage 0x4e7d33, hills 0x688a4a, fog 0xd6e9e6,
  hemisphere ground 0x6b8a48, sky #5fb0e8, #a2d6f2, #eef8f0
  (Stardew's summer grass reads yellowish against spring's vivid
  green, with thicker green leaves). Autumn turns umber: ground
  0xf3e6c8, foliage 0xc07f2e, hills 0xa8895a, fog 0xe6dcc4,
  hemisphere ground 0x8a7a4a, sky #d8a86a, #e8c890, #f4ead8
  (Stardew's fall covers the town in orange and reddish tones with
  browner grass). Winter ground 0xe6edf2 against the spring
  0xffffff (the color multiplies the ground canvas texture, so the
  fields pale toward snow without losing the paths), winter foliage
  0x8ba08f, winter hills 0x9aa892, winter fog 0xdde8f0, winter
  hemisphere ground 0x8b9aa0, winter sky stops #a8c4d8, #c8dcea,
  #e8f0f4. A new season re-tints every value, so no season ever
  inherits the last one's palette.
- The materials are stored at build time (seasonTintRefs, filled in
  buildWorld) instead of re-found: buildWorld is the only place that
  names them, and the tint never searches the scene graph or reads
  DOM. The crop cones are deliberately not tinted here: their color
  is the soil system's readout, owned by applySoilTint. A save made
  under the old winter-or-other key re-tints on the first stepSim
  frame, because the new key is a season name and never equals the
  old "other".
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
