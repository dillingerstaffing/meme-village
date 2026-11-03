# Keyboard Shift+O call out

Shift+O is the keyboard twin of the tray Call Out button: it runs
exactly the button's verb, calling out the selected resident and
refreshing the tray, so the key and the button can never disagree.
For a sick resident with no tier it spends the spot fee from cash
first, then the bank, and dispatches Jonah at once when he is free
or queues the patient at the front when he is busy; a patient
already queued hears they are already waiting and pays no new fee;
with no medic it answers that there is no medic and charges
nothing; a resident who cannot cover the fee hears so and pays
nothing. Those answers are the button's own answers, because the
key runs callOut itself, not a copy of it.

Shift+O is the second modifier chord in the tray grammar, after
Shift+C, and it exists for two reasons, not one. Every letter in
Call Out is already taken: C claims Claim, A pans, L is Lens, O is
Model, U is Build, T is Thoughts. And a chord is deliberate beyond
alphabet exhaustion: the verb spends the spot fee, so it must never
fire on a stray single keypress. O is the Out half of the button's
name, and Shift names the second verb on O, in the game's own
control-group grammar (Shift plus a digit assigns, the digit alone
recalls) and in StarCraft II, where Shift plus a number adds to a
group while Ctrl plus a number creates it. Before this chord,
Shift+O misfired into Model, because the Model handler accepted
capital O with Shift held, so a player reaching for Call Out armed
a model pick instead and paid nothing, queued nobody, and dispatched
nobody. The plain O handler therefore stands aside while Shift is
held; see keyboard-o-model.md.

Shift+O clears no arm, unlike the arm keys: Call Out commits at
once, it is not an arm waiting for a target tap, and the button
clears nothing either, so the key mirrors the button instead of
inventing a wider clear. It needs a selection, like the button,
which renders only for the selected resident; for a healthy,
tiered, or child selection callOut itself refuses silently, exactly
as an absent button does, in the Shift+C unbanked precedent.

Shift+O is guarded like a panel key, not like the display-only pause
and mute keys: it fires only once the game has started, never while
the game is over, never while an incident panel stands, never with
Ctrl, Meta, or Alt held, and never while typing in a text field. A
spend behind a modal decision would hide the decision it needs, so
the incident guard is intentional, not an omission. Do not add an
incident exception here without re-arguing that panel rule: the
guard is intentionally identical to the camera, group, idle, lens,
story, thoughts, claim, proclaim, found, road, visit, model,
spotlight, build, speak, and cover keys, not to Space, P, 0, or M.
The Call Out button's title names it ("Call Out (Shift+O key)"), so
a desktop player can learn Shift+O exists from the button itself,
in the StarCraft II command-hotkey grammar: the hotkey shown on the
button, not only in a tooltip.

Shared guard (2026-11-03): while a Story panel stands open, the shared keydown guard returns before this verb, so it never acts behind the chronicle; Escape, the pause keys, the speed keys, and M stay live. See story-panel-key-guard.md.
