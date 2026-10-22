# Chrome Over the Canvas Passes Taps; Only Its Buttons Capture

Containers that float over the game canvas (#tray, #alerts) are
pointer-events:none, and only their buttons are pointer-events:auto.
Give any new overlay strip, stack, or panel the same split: container
none, interactive children auto.

Why: a container that captures taps swallows every camera drag that
starts inside its rectangle, and the player experiences that as
scrolling that randomly sticks in certain screen regions. Only the
buttons need the tap; the rest of the container is backdrop.
