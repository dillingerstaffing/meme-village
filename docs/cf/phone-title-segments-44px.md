# Phone Title Segments Meet the 44px Thumb Target

On screens 560px and under, the title screen season and posting
segments meet the 44px thumb target the game's in-play buttons already
meet.

The segments are the first controls a phone player touches: the season
row (Standard, Hard Winter, Dry Year) and the posting row (Open Books,
Shared Hearth, Quiet Order) sit above Begin, and a mis-tap here starts
the village under the wrong difficulty or posting rule. They measured
43px tall from the title overlay's padding, one pixel below the target,
so the phone rule gives them a 44px minimum height. The global
border-box rule makes that minimum land exactly 44px, and the one pixel
changes no row layout.

The rule is phone-only CSS, display only: no state, no dispatch, no sim
touch, and no second DOM writer. Tapping a segment still moves the gold
.on state and rewrites the choice line naming that choice's consequence,
exactly as before, and the desktop title keeps its compact segments.
