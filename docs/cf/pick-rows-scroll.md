# Pick Rows Scroll Inside the Objective Card

On screens 560px and under, every decision pick row inside the
objective card (project, offer, found, claim, road, lens, arrival)
caps at the viewport height minus 360px and scrolls internally:
max-height calc(100vh - 360px) with a calc(100dvh - 360px) override,
overflow-y auto. The row itself carries pointer-events auto, so the
scroll gesture lands on the row; the card stays pass-through
everywhere else, and only the row's own buttons captured taps before
this rule. The row's chips wrap (flex-wrap plus min-width 0) so no
chip exceeds the row's width.

Why: the card has no height cap and the page cannot scroll (html,body
overflow hidden), so a long pick row grew past the viewport and its
commit chip sat below the fold with no gesture to reach it. At 390px
the Claim row's Stake chip and cancel chip, and the Road row's Lay
chip and cancel chip, were all below the fold; the verb could only be
escaped by re-tapping its tray button, never committed. The same
family had a sideways failure: a found kind chip's blurb pushed its
button about 57px past the 172px card edge (Workshop measured at
228px against a 172px card), painting over the card's neighbor. The
stats compaction in phone-stats-compact-during-picks.md covers the
stats panel during picks; it never capped the pick rows themselves,
so it could not fix either failure.

The cap is on the row, not the card, so the objective text above the
row stays visible as context while the choices scroll beneath it.
The rule covers all seven rows because they share one CSS pattern;
a future long row (a many-option offer, a new pick family) is capped
from day one rather than re-discovering the fold failure. On phones
the cap is the viewport height minus 360px, tightened by measurement
against the collapsed tray top while a long row stands; the rows need
overflow-y auto at every width for the cap to scroll instead of clip,
and it is a no-op while uncapped.

Desktop cap (2026-11-07): the desktop tray never collapses for a pick
row, so a tall card grew past the tray top instead (measured at
1440x900: card bottom 687 against a tray top of 642, 11250 px^2, the
tray's opaque gradient painting over the card's bottom pick rows, the
Not yet exit chip half under it). The same grammar, measured the same
way: hudTick caps the open long row (project, found, claim, road) so
the card bottom clears the tray's measured top by 8px, and the row
scrolls internally. The cap reads the tray's measured top, not an
analytic bound: the tray does not collapse on desktop, so the measured
top is stable on the arming dispatch itself, and the cap changes the
card bottom, never the tray top, so no latch is needed. The offer row
takes no cap: it is a single decision, and it sits above every long
row, so when the long row clears the tray the offer clears too.
Guarded by pwtest_cardtray.py in the loop's hidden_files at 1440 and
390 (plus 1440x700 in the battery): the probe fails pre-fix on
exactly the clearance and scroll legs at 1440, and passes post-fix at
all three sizes.

Guarded by pwtest_pickrows.py at 390px and 375px: every chip's right
edge inside the row, the row's bottom inside the viewport, the first
chip visible at scroll top, a real wheel gesture moving the row, the
last chip fully visible at scroll bottom, and the Claim Stake and
Road Lay chips landing their commits from real clicks. The probe
failed pre-fix on exactly the below-fold commit chips and the found
chip's sideways overflow, and passes post-fix at both sizes.

Long-pick tray collapse (2026-11-03): the cap above assumed the
unselected tray, but a selected resident's tray rises to 56 percent
of the viewport height or more, so a long pick row (project, found,
claim, road) grew the objective card down the left column until the
card, which paints above the tray, covered the tray's whole left
command column, including the arming button itself and the speeds
row, while the pick stood open (measured at 390x844: card bottom 791
against a tray top of 332). Short rows (arrival chips, lens modes)
never reach the tray and keep it as-is; the offer row is the
exception, covered in the paragraph below. While a long row is open,
hudTick collapses the tray to its speeds-only
height through a pickopen class (the row itself carries the commit
and the cancel chip, so no exit is lost), and tightens that row's cap
by measurement so the card bottom, site line included, clears the
collapsed tray top by 8px; the cap is computed from the collapsed
tray's analytic top (viewport height minus the 110px collapsed cap),
not a measured top, because the tray's height animates over 300ms
and hudTick runs on dispatch rather than every frame, so a measured
top on the arming dispatch would still read the expanded tray. The
row still scrolls internally for the chips below the tightened cap.
Guarded by pwtest_pickrowtray.py in the goal's hidden_files at 390
and 375 (plus a 1440 control proving the class never applies on
desktop): the probe fails pre-fix on exactly the collapse, clearance,
and speeds-clear legs, and passes post-fix at both phone sizes.

Offer-row tray collapse (2026-11-07): the paragraph above says short
rows never reach the tray, and that held for arrival chips and lens
modes, but not for the offer row. At 375px a long offer's hint wraps
the card tall enough to reach the selected tray (measured: card bottom
302 against a tray top of 270 at 375x844, the Ignore button covered by
3576 px2 and the role line by 1232 px2; card bottom 318 against a tray
top of 202 at 375x720, the whole offer row and the first command row
covered; clean at 390x844, card bottom 318 against a tray top of 332).
So the offer row collapses the tray as well, but only when measured:
while the offer stands open and the offer row's bottom would pass
the tray's top content row (the selInfo role line when a resident is
selected, else the tray top), hudTick collapses the tray to its
speeds-only height through the same pickopen class, and the offer row
carries Accept and Ignore, so no exit is lost. The measurement is the
offer row's bottom, not the card's: the card bottom includes any long
pick row standing open, so measuring the card latched the marker off
another verb's row (arming Claim with the week-1 offer up set the
marker at 390, where the offer never reaches the tray, and the tray
stayed collapsed after the cancel; caught by pickrowtray L4). The
offer row sits above every long row in the card, so when it clears
the tray, everything above it clears too. The collapse latches on its
own marker class, pickopen-offer, while the offer stands, because the
collapsed tray top no longer measures the overlap, so a per-tick
re-measure would un-collapse on the next dispatch and flicker the
tray; the tray restores the moment the offer is answered. The marker
is the latch, not pickopen itself: latching on pickopen held the
collapse for ANY offer standing open, including at 390 where the
offer never overlaps, so a long pick cancelled with the week-1 offer
still up left the tray collapsed (caught by pickrowtray L4 in the
battery). A tray collapsed for a long pick never sets the marker: the
measurement then reads the collapsed tray top, which the capped row
always clears, so the offer cannot latch off another verb's collapse;
the next tick after the long pick closes re-measures the expanded
tray and latches then if the offer genuinely overlaps. The offer row
itself takes no max-height cap: it is a single
decision, not a list, and with the tray collapsed the card bottom
clears the collapsed tray top by hundreds of pixels. Guarded by
pwtest_offertray.py in the goal's hidden_files at 375, 390, and
375x720: the probe fails pre-fix on exactly the collapse, clearance,
and no-covered-text legs at 375, passes post-fix at all three sizes,
and proves the measured rule at 390, where the tray never collapses
because there is no overlap.
