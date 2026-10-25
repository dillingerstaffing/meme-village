# Proclaim Minimap: The Season Focus Reads on the Strategic Channel

Proclaim names a station (or a building site) as the village focus for
the season, but after its commit toast expired nothing on the map said
which one, so a player returning mid-season could not check the choice
they made. The Civ standard: a standing strategic decision reads on the
map itself, not only in the message that announced it, so the player can
read what they decided without re-committing it.

- drawMinimap draws the focus for exactly the week it holds
  (G.proclaim present and G.proclaim.week === G.week): the tray's own
  megaphone glyph above the focus, ringed dashed in the objective gold.
  The mark carries by icon and by shape, never by color alone.
- A station focus marks that station's square; a site focus marks the
  site's plot, while the site is unfinished (a finished site is no
  longer a focus target, so its mark drops). The abstract home station
  never draws: it has no station square to mark.
- Scale-aware like the event pings: ring radius, line width, glyph size,
  and glyph offset divide by the displayed-width ratio (118/192 on
  phones, 1 on desktop), so the mark reads at the same CSS size on both.
- Display only: the block reads G.proclaim, STATION3, PLOTS, and
  siteById, and writes the minimap canvas. It never writes state, never
  calls wk(), never touches the driven-work ledgers, and never changes
  what the focus does. The commit toast, the arm grammar, and the
  focus effects are untouched; this layer is the same decision on the
  second channel. The mark paints last in drawMinimap, above the lens
  layers and the ping rings, so it is never hidden by them, and it
  restores the canvas text alignment it borrows, so the lens captions
  keep their left alignment.

Why: the objective station already reads gold on the minimap, and the
claim layer already puts surveyed ground on the strategic channel, but
the one player decision that lasts a whole season had no persistent
mark at all. A focus the player cannot re-read is a focus they cannot
steer around, and a re-proclaim to recover it costs cohesion when done
early.
