# The Desire Lens: One Information Layer at a Time

The minimap carries data-map lenses, and at most one lens is active at
a time (the Civ VI lens grammar: a lens drapes one information layer
over the map, each with its own visual code, and the player picks which
question the map answers):

- G.ui.lens is a mode, never a boolean: null (off), "tension", or
  "desire". The tray Lens button cycles off to tension to desire to
  off. Legacy boolean lens state restores to "tension".
- The button is a view switch with an icon swap plus a persistent mode
  label (the mute button precedent, extended): map plus "Lens" with no
  lens, crossed swords plus "Tension", eye plus "Desire". The label names
  the active layer after the switch toast expires, so the player never
  has to guess which question the minimap is answering. It is never a
  lit verb: no .on, .armed, or .cam class.
- The desire lens draws model-to-follower edges from the live
  imitation graph: a.model inbound edges, read at draw time, never a
  cached graph. Edge thickness is the copy number (0.75 plus 0.35 per
  follower, capped at 3.5): a thick line is a fashion many followers
  share.
- The fashion's object is labeled, never guessed: the dominant want
  station among the model's followers (the model triple's object, from
  the want's origin data) renders as its station icon at the model's
  dot. No label appears when no follower carries a want.
- An envied model (prestigeFlipped, the model-prestige flip point)
  gets a red ring, so the admiration-to-rivalry flip stays legible on
  the lens. Shape plus line, never color alone.
- The canvas carries a "DESIRE LENS" caption plus a legend line naming
  the read, so the layer is identified on the map itself.
- The lens is display only: it never writes sim state, never commits,
  and never reads DOM to decide anything.

Why: the mimetic layer was the game's central system and its least
visible one. The tension lens showed where converging desire had
already turned hot; nothing showed who the village was copying, what
was being copied, or how many followers a fashion had, so the player
could only react to feuds instead of watching the imitation graph that
causes them. The desire lens is the graph made visible, computed from
the same edges the spread system reads.
