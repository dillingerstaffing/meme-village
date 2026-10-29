# The Phone Stats Panel Compacts While a Decision Pick Is Open

On screens 560px and under, when any objective-card decision pick row is
visible (offer, project, found, claim, arrival), hudTick adds the `compact` class
to #stats. Compact hides the eight meter rows and the header and shows
#statsStrip instead: one wrapping strip with every meter's icon and value
(contentment included always, blame included only while the blame row itself is showing). When the pick
closes, the class comes off and the full rows return; on wider screens the
class is always removed.

Why: on phones the stats panel is bottom-pinned above the tray, so its top
extends upward into the objective card when a pick row opens the card. The
offer row plus a tall selection sheet left 34px of the panel (the header
and the first meter rows) covered, with genuinely no room for card, full
panel, and tray at 390px. The strip keeps every meter glanceable at the
decision moment (the Reigns-at-choice-time standard) in ~36px, so the card
never covers a meter row and no meter ever hides behind a decision.

Collision extension (2026-10-29): the pick-row rule alone did not
cover the tray-open state. With a resident selected the tray rises,
and the tray-pinned panel rises with it behind the objective card
(the card paints above it), so at 375px the panel hid almost
entirely and at 390px its top rows hid after the offer was accepted,
even with no pick row open. hudTick now also compacts by
measurement: whenever the pinned panel would overlap the card it
compacts first, and when even the strip cannot fit between card and
tray it hides the panel with visibility, so its rect stays
measurable and it returns on its own when the tray closes or the
card shortens. A panel is therefore never partly behind the card:
it is fully clear, compact and clear, or fully hidden.
A sliver of 12px or less is border and padding, not a meter row, so
it does not hide the panel: hiding for a 3px alert-height wobble
would flicker the panel away at the decision moment.
