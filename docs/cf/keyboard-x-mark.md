# Keyboard X mark

X is the keyboard twin of the pin button: it runs exactly the
button's verb, the shared __saveCamMark call, so the key and the
button can never disagree. One press appends the live camera pose
(target x/z, yaw, distance) through the ui/cammark dispatch into
the four-slot G.camMarks ring, toasts the slot just saved (View N
saved), and on a fifth save names the drop (View 4 saved, oldest
view replaced), then refreshes the tray. The return chips recall a
slot's pose exactly; the key itself only saves, never recalls.

X marks the spot, and X is a free letter. A, S, D, and W pan
the camera, Q and E rotate it, R resets it, F follows the selected
resident, Y returns to the last alert, and every other letter is a
tray verb (B proclaim, C claim, G spotlight, H road, I idle, J
story, K speak, L lens, M mute, N found, O model, P pause, T
thoughts, U build, V visit) or a speed key. No bare letter in Save
or View is free (S pans, V is Visit, A pans, E rotates), so the
save takes the free letter that names pinning a place, in the same
first-free-letter grammar as G for Spotlight and K for Speak For.

X is a camera verb, not a resident verb: it needs no selection and
never changes one, like the reset button, and it clears no arm,
because saving a view is camera only and never sim state. A mark
saved while an arm stands leaves the arm standing, exactly as the
button does, so the key path cannot silently cancel a pending verb.

X is guarded like every other camera key: it fires only once the
game has started, never while the game is over, never while an
incident panel stands, never with Ctrl, Meta, or Alt held, and
never while typing in a text field. A save behind a modal decision
would move nothing the player can see, and a save while typing
would steal the letter, so both guards are intentional, not
omissions. The pin button's title names it ("Save this view (X
key)"), so a desktop player can learn X exists from the button
itself, in the StarCraft II command-hotkey grammar: the hotkey
shown on the button, not only in a tooltip.

The SC2 grammar is adapted, not copied, because this game runs in
a browser page: Blizzard's guide names Ctrl+F5-F8 to save a
location and F5-F8 to recall it, but F5 reloads a page, so the
browser adaptation is X to save and the return chips to recall.
Do not add an F5 handler without re-arguing the reload conflict:
a save key that reloads the page on a missed preventDefault loses
the village it was meant to mark.

Shared guard (2026-11-03): while a Story panel stands open, the shared keydown guard returns before this verb, so it never acts behind the chronicle; Escape, the pause keys, the speed keys, and M stay live. See story-panel-key-guard.md.
