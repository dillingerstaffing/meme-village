# Tap Grace: A Name Tapped a Moment Ago Still Selects Its Owner

A canvas tap selects through pickAt in this order: the resident's
currently placed overlay box, then a box that box occupied within the
last 800ms, then the 3D body raycast, then the 40px torso-projection
fallback, then a plot, then a station. The 800ms recent-box ring is
kept by renderOverlay beside _ovlBox: every placed box snapshots into
its agent's ring each frame, and entries older than 800ms, or stamped
ahead of the current clock, never answer.

Why: a de-overlap sidestep teleports a box up to ~77px in a single
frame, and a bubble expiring hides a box outright, so a tap aimed at a
name that was visible when the player aimed can land on ground, a
plot, or a station instead. A tap on a name that was there a moment
ago is a tap on its owner, not a miss. The ring is pick only, never
display: placement, the anchor budget, and hiding are untouched, and
current boxes always win over recent ones, so a resident who moved
onto the point is never stolen by a stale box.
