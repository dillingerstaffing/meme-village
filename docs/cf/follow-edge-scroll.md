# Edge Scroll Stands Aside While Following

Mouse edge scroll is a passive camera move: it fires whenever the mouse
rests within 30px of a screen edge, with no click, drag, or button press.
While a camera follow holds, that passivity is the problem. The follow
lerp pulls the camera target toward the followed resident every frame,
and edge scroll pushes the same target away every frame, so the camera
flies off the resident for the 1.5 second edge window and then slides
back. Moving the mouse to the bottom tray buttons while following a
resident triggered it on every trip, since the tray lives at the edge.

The rule: the edge scroll condition carries `!cam.follow`. While follow
holds, edge scroll does nothing at all: it neither moves the camera nor
drops the follow mode. That matches the rotate and zoom grammar, which
orbit the followed resident instead of dropping them, and it leaves the
explicit follow releases untouched: drag pan, minimap jump, selection,
alert focus, camera reset, and bookmark return all still clear follow
on purpose, because the player asked for a different view with a gesture
or a tap. A passive mouse position never counts as asking.

Removing the `!cam.follow` term reintroduces the fight, and replacing it
with a follow clear would silently drop an armed mode on a passive
position, so neither edit is a fix for anything else.
