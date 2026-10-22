# Overlay Markers Stay Inside the Anchor Budget

Keep every resident overlay within LIFT_MAX (56px up) and DX_MAX (110px
sideways) of its resident's projected head anchor. Screen clamps and the
HUD nudge spend from the same budget. Resolve collisions in priority
order (selected resident, event bubbles, want bubbles, ambient markers),
sidestep first, then lift, and past the budget hide the marker for that
frame. While the camera is moving (150ms hysteresis via _ovlMoveAt), the
collision pass and the HUD nudge stand down entirely so markers track
their anchors exactly; both resume at rest.

Why: position is identity. A marker pushed past its budget lands over a
different resident and reads as that resident's state. The tempting fix
for crowding, stacking markers as high as needed, is exactly what made
bubbles float and attach to the wrong people in playtests. Hiding for
one frame is cheaper than lying about who a marker belongs to.
