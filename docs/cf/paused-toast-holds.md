# A Paused Sim Holds Its Toast

A toast's life is wall-clock: it shows until Date.now() reaches its
until, and the animation loop promotes the head of the queue the moment
the current toast expires. Pause breaks that clock on purpose. While
speed is 0 the sim itself is frozen (stepSim never runs, so initiative
telegraphs, which run on sim time, also freeze), and a player pauses
exactly to read and think. A toast that expired during the pause would
punish the pause: the message the player stopped to read would be gone,
and the queue behind it would drain unseen.

So the animation loop holds the live toast while paused: every frame
with speed 0 dispatches ui/toastHold with the real elapsed time since
the last holding frame, and the action advances the live toast's until
by that delta. The hold measures wall time, not the sim step delta:
the step delta is capped at 50ms, so on slow frames it would undercount
elapsed time and the toast would still expire during a long pause. On resume the
toast keeps the remaining life it had at pause, and the queue, which
promotes only on expiry, holds with it. Only a live toast moves: a
toast the player skipped (until 0) is never revived, and a toast that
arrives during the pause queues behind the held one under the usual
ui/toast rule instead of overwriting it.

The hold is a loop dispatch, never a renderer write: renderers only
read until to decide whether the pill shows. The speed buttons and the
Space key are the only ways to enter pause, and both go through
setSpeed, so the hold condition (speed 0) covers every pause entry.
