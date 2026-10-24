# Soil Tints: The Field Reads Its Own Depletion

The soil clock's stage is visible on the map itself, never only in a
toast or a meter. The Minecraft farmland standard: hydrated soil reads
dark brown and dry soil light tan on the tile itself, and crops grow
taller and darker per growth stage, so the farmer reads the field by
looking at it, not by opening a panel.

- G.soilStage (0 rich, 1 tired, 2 exhausted) is the view's tint index,
  from DEPLETION tintStages. soilTick still owns every stage
  transition, its toast, and its chronicle line; the tint only renders
  the stage soilTick already computed.
- applySoilTint() runs in stepSim just before the crops rewrite, diffs
  G.soilTintApplied against G.soilStage, and on change only: recolors
  the two stored field soil boxes, recolors the crop cone material,
  and forces the crops matrix rewrite (G.growthApplied = -1) so the
  stage's crop scale lands on the next rewrite. On any other frame it
  does nothing.
- The tints, shape plus color, never color alone: rich soil
  0x7a5c38/0x84643c with crops 0x86b95e at full height (1.0); tired
  soil 0x8f7a52/0x9a8258 with crops 0xa8b85e at 0.8 height; exhausted
  soil 0x9a8a72/0xa3967e with crops 0xc9b458 straw at 0.55 height.
  A tired or exhausted field reads as stunted and straw-colored even
  to a player who cannot tell the soil browns apart.
- The soil boxes are stored at build time (soilMeshes) instead of
  re-found: buildWorld is the only place that names them, and the tint
  never searches the scene graph or reads DOM.
- Display only: the tint writes no sim state except the view
  bookkeeping G.soilTintApplied and G.growthApplied, never calls wk(),
  never touches the driven-work ledgers, and never changes a yield,
  a threshold, or a stage boundary. A stage restored from a save
  re-tints on the first stepSim frame, because the diff runs every
  frame, not only at the season boundary.

Why: the depletion system shipped with a clock, a throttle, toasts,
and a chronicle, but the field itself never changed: a player who
missed the toast could work an exhausted field for a whole season
without seeing it. The tint closes that gap at the Minecraft standard:
the state of the ground is legible from the ground.
