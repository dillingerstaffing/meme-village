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

One deliberate exemption: the selected resident's card may sidestep past
DX_MAX when the west-edge nudge clears the left HUD column (the card
lands at hud.right + 6 + its half-width, however far that is from the
anchor). Hiding the selected card for the frame would flicker the
selection readout while the resident walks behind the column, and
identity stays unambiguous: the resident carries the visible selection
ring and the card names them. Non-selected overlays have no exemption;
past the budget they hide for the frame.

The station aggregate bubble (#pressure, "N all want the <station>") follows
the same rule against opaque chrome: it clears the minimap and the offer
card within the same 110px sideways budget measured from its clamped
station anchor, or hides for the frame, never rendering clipped under
either panel.

Resident overlays follow the same rule against the minimap specifically:
the minimap is opaque (z-index 11 over the overlays at 9), so a marker
under it is invisible, not merely overlapping. Placement shifts a
minimap-overlapping box left of the minimap within the same 110px
sideways budget (selected resident exempt, as with the west-edge
nudge); a de-overlap sidestep candidate that would land under the
minimap is skipped; and a final guard after lifting and clamping
re-shifts or hides for the frame. Like the HUD nudge, minimap
clearance stands down while the camera moves.
