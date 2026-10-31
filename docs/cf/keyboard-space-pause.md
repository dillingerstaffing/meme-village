# Keyboard Space pause

Space is the keyboard twin of the speed buttons, toggling speed 0 and
1 (from 2x it pauses). It was the one key in the keydown handler with
no guard at all: it toggled unconditionally and preventDefaulted every
press, so Space on the title screen flipped speed to 0 and beginGame
never resets speed, so the village started paused with no explanation;
Space after game over flipped the speed lights on the end screen;
Ctrl+Space was hijacked from the browser; and Space while typing in a
field was swallowed while still toggling speed.

Space is guarded like every other key, with one deliberate exception:
it fires only once the game has started, never while the game is over,
never with Ctrl, Meta, or Alt held, and never while typing in a text
field, but it STAYS live while an incident panel stands. Pausing is
the thinking tool (while speed is 0 the live toast holds, never
drains), and freezing the sim behind a decision disturbs nothing,
unlike a camera or selection key; the panel still needs its choice,
and the sim already runs at 0.3x behind an incident, so a full freeze
is a smaller step, not a bypass. Do not add an incident guard here
without re-arguing that exception: the guard is intentionally not
identical to the camera keys.
