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
the same rule against opaque chrome: it clears the minimap, the offer card,
the alerts stack, and a live toast. Sidestep first within the same 110px
sideways budget measured from its clamped station anchor (minimap-left,
offer-card-right, stack-right, toast-left then toast-right), accepting only
a shift that clears every panel; then lift so its bottom sits on the top
edge of a panel it hits when the lift stays inside the 56px budget and the
lifted bubble clears every panel; past both it hides for the frame, never
rendering clipped under any panel. The stack (z 29) and a live toast (z 12)
both paint over the bubble (z 11), so a bubble under either reads as no
convergence at all. Measured 2026-11-07: at 390px the bubble sat under the
standing stack by 2668 px^2 and under a live toast by 5400 px^2, its center
covered by an alert chip and a toast chip; at 1440px by 2603 px^2 under the
stack and 3266 px^2 under the toast. Guarded by pwtest_pressure.py in the
loop's hidden_files (pre-fix FAIL on exactly the stack and toast invariant
legs at 390 and 1440, ALL PASS post-fix).

Resident overlays follow the same rule against the minimap specifically:
the minimap is opaque (z-index 11 over the overlays at 9), so a marker
under it is invisible, not merely overlapping. Placement shifts a
minimap-overlapping box left of the minimap within the same 110px
sideways budget (selected resident exempt, as with the west-edge
nudge); a de-overlap sidestep candidate that would land under the
minimap is skipped; and a final guard after lifting and clamping
re-shifts or hides for the frame. Like the HUD nudge, minimap
clearance stands down while the camera moves.

Resident overlays follow the same rule against the alerts stack: the
stack is opaque chrome (z-index 29 over the overlays at 9), so a marker
under it is invisible, not merely overlapping. Placement sidesteps a
stack-overlapping box right of the stack within the same 110px sideways
budget (selected resident exempt, as with the west-edge nudge and the
minimap shift), then lifts it so its bottom sits on the stack's top
edge when the lift stays inside the 56px budget and the lifted box
clears the HUD column and a live toast; past both it hides for the
frame. A sidestep that would land under the HUD column, the minimap, or
a live toast is no clearance at all, so it is refused. A de-overlap
sidestep candidate that would land under the stack is skipped, and a
final guard after lifting and clamping re-shifts or hides for the frame.
Like the minimap clearance, stack clearance stands down while the camera
moves, and the stack rect is measured live every frame, so the rule
follows the stack as it sheds rows against the objective card and grows
again when space returns.

Resident overlays follow the same rule against a live toast: the toast
is opaque chrome (z-index 12 over the overlays at 9), so a marker under
it is invisible, not merely overlapping. Placement sidesteps a
toast-overlapping box left of the toast first, then right, within the
same 110px sideways budget (selected resident exempt), then lifts it so
its bottom sits on the toast's top edge when the lift stays inside the
56px budget and the lifted box clears the HUD column, the minimap, and
the alerts stack; past both it hides for the frame. A sidestep that
would land under the HUD column, the minimap, or the alerts stack is no
clearance at all, so it is refused. A de-overlap sidestep candidate that
would land under a live toast is skipped, and a final guard after lifting
and clamping re-shifts or hides for the frame. The toast is transient, so
a hide lasts only its remaining life and the marker returns on its own
when the toast dies. Like the other clearances, toast clearance stands
down while the camera moves, and the toast rect is measured live every
frame, only while a toast is actually showing.

Resident overlays follow the same rule against the tray: the tray is
opaque chrome (z-index 10 over the overlays at 9), so a marker under
it is invisible, not merely overlapping, and the tray spans the full
width, so no sideways shift can clear it. Placement lifts a
tray-overlapping box so its bottom sits on the tray's top edge when
the lift stays inside the 56px budget; past the budget the box hides
for the frame. A final guard after de-overlap re-lifts or hides, and
a lift that would collide with an already placed box hides instead.
There is no exemption for the selected resident on the lift: the 56px
cap is absolute, and the tray header already names the selected
resident, so hiding their card costs no identity. Like the minimap
clearance, tray clearance stands down while the camera moves, and the
tray rect is measured live every frame, so the rule follows the tray
as it grows from its slim height to its full selected height.
