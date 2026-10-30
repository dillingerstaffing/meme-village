# Pick Rows Scroll Inside the Objective Card on Phones

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
from day one rather than re-discovering the fold failure. On wider
screens the rule does not apply and rows lay out uncapped as before.

Guarded by pwtest_pickrows.py at 390px and 375px: every chip's right
edge inside the row, the row's bottom inside the viewport, the first
chip visible at scroll top, a real wheel gesture moving the row, the
last chip fully visible at scroll bottom, and the Claim Stake and
Road Lay chips landing their commits from real clicks. The probe
failed pre-fix on exactly the below-fold commit chips and the found
chip's sideways overflow, and passes post-fix at both sizes.
