# The Desktop Stats Panel Compacts Against the Alerts Stack

On screens wider than 560px, hudTick anchors the stats panel below
the objective card's real bottom (card bottom plus 8, 146px floor)
and now measures it against the alerts stack the same tick: the
stack is bottom-pinned above the tray (group row, idle chips,
last-alert chip, camera bookmark chips, save receipt), so with a
tall card (an arrival pending with its Welcome and Turn away row)
over a full stack the panel's bottom rows used to slide under the
stack's chips and read as clipped meters.

The rule is the phone STATSCLEAR grammar, against the stack instead
of the card: whenever the panel would overlap the stack it compacts
first (the meter strip keeps every meter glanceable), and when even
the strip cannot fit between card and stack it hides the panel with
visibility, so its rect stays measurable and it returns on its own
when the card shortens or the stack sheds. A panel is therefore
never partly under the stack: it is fully clear, compact and clear,
or fully hidden. A sliver of 12px or less is border and padding, not
a meter row, so it does not hide the panel.

The compact class is measured against the full panel: it lifts for
one layout read per tick, so a cleared collision restores the full
rows instead of sticking on the strip. The four compact rules live
outside the phone media query so the class works at every width;
the phone copy inside the query stays as that article's protected
block, identical declarations, harmless duplicate.

The five text rows (tier, growth, claim, home, population) wrap
instead of overflowing the panel: they carry sentences, and the
156px content width cannot hold their longest states on one line
(Growth unlocks at Town, 0/4 rings; Claims and roads unlock at
Town), so they painted past the panel border. Wrapping keeps the
spec'd text whole; the anchor and collision rules re-measure the
panel every tick, so a taller panel stays clear. Meter rows keep
nowrap.

Display only: no state, no dispatch, no meter value changes.
Guarded by pwtest_statsoverlap.py in the goal's hidden_files (tall
arrival card over a full stack at 1440x900 and 1440x800, with the
return leg), FAIL pre-fix on exactly the tall leg at both sizes.
