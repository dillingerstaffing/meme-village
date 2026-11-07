# Coach teach line

Before the first order, the world teaches with no text: one gold cone
over the teach loafer and one over the objective station. The teach
loafer is the resident nearest the destination station among those
within 2 sim-seconds of the longest loaf whose cone projects inside the
viewport (32px margin), so both ends of the loop stay in the opening frame
with the station cone instead of the cone pointing at a loafer idling
off-screen; the band keeps the pick among the genuinely idlest, and with no
destination station the longest loafer stands. When no band loafer is on
screen the nearest pick stands, so the teach never goes empty for a camera
the player dragged away. The screen test reads the camera the overlay
already projects with, one frame stale like the overlays. Two separate markers do not say they belong together, so a first
player can see both ends of the loop without seeing the loop: the
loafer, and the station, but not that the loafer is meant to go
there. A gold line joins the two cones while the teach window holds,
in the same gold as the order pulses, so the loop reads as one path
from the resident to the station.

The line is display only. It is a single scene line whose endpoints
are the two cone positions each frame, so it follows the loafer if
the longest-loafing resident changes and follows the station cone
through its bob. It shares the cones' own teach condition exactly:
visible only while the game has started, is not over, and no order
has been committed, and it vanishes with the cones at the first
order. It is never a tap target: tap picking intersects only the
agent, plot, and station hit meshes, never the scene, so the line
cannot capture or block a tap. No state is added and no dispatch
runs for it.

When the band itself is empty (no one has loafed past 5) the
fallback marks a resident who can take the order anyway, so the
teach never goes dark while the first order still stands. With a
destination station the fallback takes the nearest resident who can
take the order, preferring one whose cone is on screen; with no
station it takes the idlest resident whose cone is on screen, else
the idlest overall. Membership is exactly setOrder3's refusal set:
no sick, no sick-walking, no children. Ordering a busy resident
commits a real first order and drops their current activity.
Measured 2026-11-07 at 390, the band was empty for 24.9 of the
first 52 sim-seconds, including a 15.8s stretch with all 9 adults
busy, so before this fallback the cones and the line vanished for
nearly half the opening minute.
