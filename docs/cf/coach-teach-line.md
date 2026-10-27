# Coach teach line

Before the first order, the world teaches with no text: one gold cone
over the longest-loafing resident and one over the objective station.
Two separate markers do not say they belong together, so a first
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
