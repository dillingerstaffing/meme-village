# Camera key pan

The camera moved on drag, edge scroll, minimap jump, rotate, and zoom,
but no key ever moved it, so a desktop player with hands on the
keyboard had to reach for the mouse to look around, while The Sims 4
moves its camera with WASD and arrows in Sims 3 camera mode and
StarCraft II pans with arrow keys.

Arrow keys and WASD pan the view: one press steps cam.dist * 0.12 along
the yaw-relative axes, forward and back along the view direction, left
and right across it, clamped to the camera bounds (x within 62, z
within 48). A key pan is an explicit camera move like a drag, so it
clears a camera follow instead of fighting it, unlike edge scroll,
which stands aside while a follow holds, and unlike rotate and zoom,
which orbit the followed resident.

The pan is guarded like the other keyboard verbs: it fires only once
the game has started, never while the game is over or an incident panel
is open, never with Ctrl, Meta, or Alt held, and never while typing in
a text field.
