# Departure Forecast: The Household at Risk Is Named Before the Season Turns

A departure is the one permanent, game-ending loss with no forecast:
at a season boundary, with contentment under 30 and blame at 60 or
more, a 50 percent roll walks the lowest-morale household out with
its children, and repeated departures can empty the village, yet
nothing on screen names the threatened household before the boundary.
The only departure text is the after-the-fact toast. The Into the
Breach standard, and the blame forecast already shipped in this same
tick, is the opposite: the threat, its target, and its counter-move
are on screen before the irreversible step.

- statDrift, the per-frame stat tick, checks the same condition
  arrivalCheck will check at the boundary: contentment() under
  HH.departContentment (30) with G.blame at or above HH.departBlame
  (60). When it holds and the G.departWarn latch is clear, the
  forecast fires once per approach.
- It names the household arrivalCheck would take:
  lowestMoraleHousehold(), two or more members, lowest average of
  the first two members' morale. The selection is factored into one
  helper shared by the forecast and arrivalCheck, so the forecast
  and the departure can never name different households.
- The forecast is display only: a walking bubble on both members,
  a tappable toast naming both first names with "may leave" (the
  boundary roll is 50 percent, never a certainty) and the two blame
  interventions (Speak For, or send them to the green), a warn ping
  at the household midpoint, and the warn sound. It removes nobody,
  departs nobody, writes no chronicle line, and never forces or
  blocks a departure.
- The latch clears when contentment rises to 30 or blame falls below
  60, so a second approach forecasts again; while the latch holds,
  no repeat toast fires.
- After the departure itself, the announcement toast carries the
  same return grammar as a death notice: departHousehold captures
  the vacated dwelling before any removal (the household's claimed
  site, else the first member's home) and passes it as a coordinate
  focus with a loss ping, so the toast renders a view chip while
  live and a last-alert chip after it expires, and the minimap
  flashes at the site. A focus on the departing ids would resolve
  to nothing, since the subjects are removed before the toast.

Why: the blame forecast already proved this grammar in the same
tick (name the target and the two real interventions before the
irreversible expulsion at 100), and the departure is the same shape
one step further out. The counter-moves are ones the player already
owns: Speak For multiplies blame by the speakBlameKeep factor once
blame reaches the speak minimum, and green mediation drains blame
while the blamed resident stands on the green, and draining blame
also lifts contentment, since the contentment formula includes 100
minus blame. The forecast adds no mechanic and no graph cause: it
renders the already-spec'd departure rule (spec section 12) before
it fires, exactly as the blame forecast renders the expulsion rule.
