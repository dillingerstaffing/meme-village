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
