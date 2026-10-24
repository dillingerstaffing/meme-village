# The chronicle and the saved village

Invariants for the village memory (Stage 8): the chronicle, the two
true endings, and the localStorage snapshot.

- The chronicle lives in Store state (G.chronicle). Only the single
  writer chronicle(text) appends to it, and only systems call it,
  inside their existing transact/dispatch flow, never a renderer.
  Entries are one factual line each, stamped with the week, year, and
  season they fired in. Selection is for graph significance (project
  and site completions, feuds, blame turns, Speak For successes,
  initiatives of note, households, arrivals, departures, births,
  maturations, deaths, contested successions, tier ups). Routine
  work, wants, and per-tick noise are never written. The list is
  capped at CHRONICLE_CAP entries; past the cap the oldest drop.
- The game ends only through endGame(kind): "collapse" when
  checkEnd() finds zero residents after a removal path (dieAgent,
  or a departure inside arrivalCheck), or "closed" when the player confirms
  Close the Chronicle on a manual Story open: the first tap arms (gold, the
  button and an arm toast both name the permanent end and the cleared save)
  and only the second tap commits. The arm clears when the panel closes and
  on save restore, so a reopened or restored panel never inherits a stale
  arm. The winter death
  floor (LIFE.minPopulation) guards the winter death roll only; it
  does not guard departures, so collapse stays reachable without
  weakening the floor. After an ending the sim stays gated by G.over,
  the final panel is the section 19 verdict over the final state
  with the full chronicle, and a manual Story open re-renders that
  final summary rather than the lens. The final panel also carries a
  Remembered epitaph block naming the first to fall (and, on a
  collapse, the last), plus the eldest living resident on a closed
  chronicle; the lines are display only, drawn from G.deaths and the
  agents' ages, and never invent names.
- The snapshot is one localStorage key (mv_save) holding
  {v: 1, state}. State serializes minus transient render objects
  (stripped by key in SAVE_STRIP) and minus deck references:
  objectives, offer, and the incident fields are stored as indices
  into OBJECTIVES and INCIDENTS and rehydrated by restoreState.
  An unknown version or a corrupt payload is discarded and the game
  starts fresh; reading a snapshot never throws.
- Restore happens only through the title screen Continue button
  (continueGame, gated on the boot-time pendingSave). #play and #ff
  auto-begins start fresh and never read or clear the snapshot.
  Begin from the title button starts a new village and clears the
  snapshot; an ending clears it too.
- Saves happen at each season boundary (end of endWeek) and on
  pagehide or visibilitychange hidden, only while G.started and not
  G.over. Figures, overlays, site meshes, tier silhouettes, and grave
  markers are rebuilt on restore through the ordinary construction
  paths (makeFigure, buildSiteMesh, applyTierMesh, rebuildGraves from
  the G.deaths entries that carry x/z); nothing render-side is ever
  serialized.
