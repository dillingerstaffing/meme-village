# Camera key zoom

The camera zoomed on the mouse wheel, pinch, and two speeds-row
buttons, but no key ever zoomed, so a desktop player with hands on
the keyboard could pan with arrows and WASD and rotate with Q and E
without the mouse, yet had to reach for it to zoom, while The Sims 4
zooms with the plus and minus keys as well as the wheel.

Plus and equals zoom in, minus and underscore zoom out, stepping
cam.dist by exactly the wheel factor: in 0.9, out 1.1, clamped 15 to
62. The keys, the buttons, and the wheel step the same factors from
the same camera, so they cannot disagree, and no zoom verb clears a
camera follow: zooming orbits the followed resident at the new
distance instead of dropping them, like the buttons and unlike key
pan, which is an explicit move and clears the follow.

The zoom keys are guarded like key pan: they fire only once the game
has started, never while the game is over or an incident panel is
open, never with Ctrl, Meta, or Alt held, and never while typing in
a text field. The zoom button titles name the keys they mirror.
