# The Alerts Stack Sheds on Collision With the Objective Card

The #alerts stack is bottom-pinned above the tray, so a full stack grows
upward into the objective card when the card is tall (a decision pick row
open, a resident selected on a short phone). A stack over the card is not
just a visual overlap: its chips are tappable, so they capture taps meant
for the card's pick buttons.

hudTick therefore gives the stack its own collision rule, measured, not
guessed, on the same pattern as the stats panel collision rule. Every
tick, at every width, it first restores every stack child, then sheds
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
moment. The rule used to run on phones only, on the assumption the
desktop column had room; measured 2026-11-07 it does not: at 1440x900
a full stack with the Found pick row open met the card by 65376 px^2
(card bottom 687, stack top 342), every chip in the stack under the
card, the stack painting at z 29 over the card at z 10, so the rule now
runs at every width.

A live toast is a second clearance target on the same rule, phones only.
The pill is top-anchored at 114px on phones and a long toast reaches past
the stack's top when a selected tray pins the stack high, so the stack's
chips covered the toast's left strip (measured 2026-11-06: 2256 px^2 at
375px, the message's start, for the toast's whole 3.6s life). The shed
loop therefore also breaks only once the stack top clears the live
pill's bottom edge, on the same 12px sliver and the same priority order,
so the idle chips hide while the toast is live and return on their own
when it dies. With no toast live the toast target is absent and the rule
reduces to the card rule alone. On desktop the pill is bottom-anchored
at 118px, below the stack's bottom band, and would need to be over 152px
tall to reach the stack, so the toast target stands down there and the
rule reduces to the card rule alone.

Phone chip height: on screens 560px and under the stack's chips carry
min-height 44px, the thumb target the game's pick-row chips already
meet. The stack chips were 33px tall from the shared .alert-chip
padding, below that standard. The height is phone-only, so the desktop
stack is unchanged, and it interacts with the shed rule only through
measurement: a taller stack reaches the card's bottom edge sooner, so
it sheds sooner in crowded states, never later.
