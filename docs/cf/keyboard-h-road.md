# Keyboard H road arm

H is the keyboard twin of the tray Road button: it runs exactly
the button's verb, toggling roadArm and refreshing the tray, so
the key and the button can never disagree. The Road button is
never disabled, so H needs no selection: arming the road verb
is not a resident verb. R is taken (camera reset, with Home as
its twin), so H stands for Highway: the road network between
stations. The Road button's title names it ("Road (H key)"), so a
desktop player can learn H exists from the button itself.

H carries the button's whole verb, not just its toggle: below
Town it explains the Town unlock instead of arming, exactly like
the button; at Town it clears the two station picks and the
button's own armed-verb clear list (the generic arm flag, Model,
Visit, Proclaim, Speak, Cover, Found, Claim, Groups) and toasts
on arming, with the crew-out wording when a road is under way,
else the tap-two-stations wording ("Tap one station, then
another: the crew lays a road between them"). It deliberately
does not clear the other state the button leaves alone: the lens
arm keeps the button's own grammar, so the key mirrors the
button instead of inventing a wider clear.

H is guarded like a panel key, not like the display-only pause and
mute keys: it fires only once the game has started, never while
the game is over, never while an incident panel stands, never with
Ctrl, Meta, or Alt held, and never while typing in a text field.
An armed verb over a modal decision would hide the decision it
needs, so the incident guard is intentional, not an omission. Do not
add an incident exception here without re-arguing that panel rule:
the guard is intentionally identical to the camera, group, idle,
lens, story, thoughts, claim, proclaim, and found keys, not to Space, P, 0, or M.

Below Town, the unlock explanation jumps the toast queue, on the
direct-reply rule the group answers already follow: the press arms
nothing and opens no pick row, so a queued answer would read as a
dead key, and the displaced toast waits at the head of the queue
instead of being erased. The tray Road button's locked answer jumps
on the same rule. Guarded by pwtest_claimroadlock.py in this goal's
hidden_files.

Shared guard (2026-11-03): while a Story panel stands open, the shared keydown guard returns before this verb, so it never acts behind the chronicle; Escape, the pause keys, the speed keys, and M stay live. See story-panel-key-guard.md.
