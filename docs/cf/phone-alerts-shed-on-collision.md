# The Phone Alerts Stack Sheds on Collision With the Objective Card

On screens 560px and under, the #alerts stack is bottom-pinned above the
tray, so a full stack grows upward into the objective card when the card
is tall (a decision pick row open, a resident selected on a short phone).
A stack over the card is not just a visual overlap: its chips are
tappable, so they capture taps meant for the card's pick buttons.

hudTick therefore gives the stack its own collision rule, measured, not
guessed, on the same pattern as the stats panel collision rule. Every
tick, on phones only, it first restores every stack child, then sheds
lowest priority first until the stack's top clears the card's bottom
edge: the save receipt (a status span, not a verb), camera bookmark
chips, the last-alert chip, the group row, and idle chips last, since
idle chips are the time-sensitive verb. A shed chip is hidden with
display only: no state, no dispatch, no alert is deleted, and the chip
returns on its own the next tick the card shortens or the tray closes,
because the rule re-evaluates every tick. The stats pin in the same tick
reads the shed stack height, so the stats panel does not rise on a
hidden chip.

A sliver of 12px or less is border and padding, not a chip, so it does
not shed, on the same rule as the stats collision: shedding for a few
pixels of alert-height wobble would flicker chips away at the decision
moment. On wider screens the rule does not run: the column has room,
and the stack never reaches the card.
