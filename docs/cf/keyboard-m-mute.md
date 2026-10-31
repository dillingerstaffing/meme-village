# Keyboard M mute

M is the keyboard twin of the tray Sound button: it runs exactly the
button's verb (dispatch ui/mute, persist mv_muted in localStorage,
play the toggle blip, refresh the tray), so the key, the button, and
the saved preference can never disagree. M is the most common mute
toggle across programs, and the button already exists, but M did
nothing at all, so a desktop player reaching for the canonical mute
key got silence.

M is guarded like the pause keys, including the same deliberate
exception: it fires only once the game has started, never while the
game is over, never with Ctrl, Meta, or Alt held, and never while
typing in a text field, but it STAYS live while an incident panel
stands. Muting is display only and disturbs no sim state, unlike a
camera or selection key; the panel still needs its choice. Do not add
an incident guard here without re-arguing that exception: the guard
is intentionally not identical to the camera keys, exactly as Space,
P, and 0 are.

The Sound button's title names the key ("Sound (M key)"), in the
naming grammar of the other keyboard verbs, so a desktop player can
learn M exists from the button itself.
