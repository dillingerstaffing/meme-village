# Tap Grace: A Name Tapped a Moment Ago Still Selects Its Owner

A canvas tap selects through pickAt in this order: a fresh jumped
box, then the resident's currently placed overlay box, then any box
held within the last 800ms, then the 3D body raycast, then the 40px
torso-projection fallback, then a plot, then a station. The 800ms
recent-box ring is kept by renderOverlay beside _ovlBox: every placed
box snapshots into its agent's ring each frame, and entries older
than 800ms, or stamped ahead of the current clock, never answer.

Why: a de-overlap sidestep teleports a box up to ~77px in a single
frame, and a bubble expiring hides a box outright, so a tap aimed at a
name that was visible when the player aimed can land on ground, a
plot, or a station instead. A tap on a name that was there a moment
ago is a tap on its owner, not a miss. The ring is pick only, never
display: placement, the anchor budget, and hiding are untouched.
Fresh means under 300ms old, inside the aim-to-tap window; jumped
means the entry's owner has no placed box or its current box center
sits over 30px from the point, a sidestep teleport rather than a
walk. A fresh entry whose owner is still near never steals, so a
resident who moved onto the point is never stolen by a stale box.
The case that forced the refinement: a tap aimed at Jonah's box
selected Mara instead, because a sidestep teleported Jonah's box
away between aim and tap and Mara's current box covered the point,
and current-first picked Mara even though Jonah's box had been on
the point during the aim window.
