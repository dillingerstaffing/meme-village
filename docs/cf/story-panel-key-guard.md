# Story-panel key guard

While a Story panel stands open, the chronicle is a modal reading
surface: the overlay sits above the tray and above the toast pill,
so nothing behind it can be seen, and the tap path already blocks
the tray behind it. The keyboard path must match, or a key would
silently arm a verb, open a sheet under the panel, re-render the
chronicle and lose the body's scroll place, or move the camera
behind the panel, with no visible effect until the panel closes.

The shared keydown guard therefore returns before every other verb
while the story overlay stands open (manual or auto Winter Count),
except the exit and the thinking tools: Escape closes the panel,
Space, P, and 0 pause, comma and period change speed, and M mutes.
The final panel is not covered: the game is over there, and every
verb already requires a live game. Typing in a text field is never
blocked: the panel carries no field, and a field elsewhere keeps
its keys.

The character sheet is deliberately not covered by this guard: on
desktop it is a side panel that leaves the tray verbs visible, so
arming behind it is visible there, and on phones the keyboard is
not a meant control surface. The incident panel keeps its own
per-verb guard, which is stricter: even the pause keys' incident
exception does not extend to any other verb.

Do not weaken this guard without re-arguing the modal rule: a key
that acts behind a modal is a misfire, not a shortcut, because its
feedback (the tray treatment, the pick row, the toast) is hidden
under the overlay at the moment it fires. Guarded by
pwtest_storykeys.py in the loop's hidden_files, at 390 and 1440,
mutation checked both ways (it fails on exactly the L, J, T, and
Q legs on the pre-fix tree).
