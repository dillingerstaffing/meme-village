# Keyboard G spotlight arm

G is the keyboard twin of the tray Spotlight button: it runs exactly
the button's verb, toggling the generic armed flag and refreshing
the tray, so the key and the button can never disagree. The Spotlight
button is disabled with no selection, so G needs a selection too:
arming a resident-targeted verb with no subject would leave the gold
armed treatment standing over nobody, and the next resident tap would
eat the spotlight pick instead of selecting. The button is also
disabled while its 45s cooldown runs, so G arms nothing on cooldown:
a key that bypassed the cooldown would let the player spotlight
again before the paid wait ends, which the button itself forbids.
Spotlight's initial S pans the camera down in WASD, P is the pause
key, O is the Model key, T is the Thoughts key, L is the Lens key,
and I is the Idle key, so G, the first free letter of Spotlight,
stands for it; G is claimed by no other key, so no mnemonic
compromise beyond that letter is needed. It is the third
resident-targeted armed verb to gain a key, after Visit and Model.

G carries the button's whole verb, not just its toggle: it clears
the button's own armed-verb clear list (Model, Visit, Proclaim,
Speak, Cover, Groups) and toasts on arming with the tap-a-resident
wording ("Tap a resident to spotlight them: a 20s shield, then a
45s cooldown"). It deliberately does not clear the state the button
leaves alone: Found, Claim, and Road keep the button's own grammar,
so the key mirrors the button instead of inventing a wider clear.
The Spotlight button's title names it ("Spotlight (G key)"), so a
desktop player can learn G exists from the button itself.

G is guarded like a panel key, not like the display-only pause and
mute keys: it fires only once the game has started, never while
the game is over, never while an incident panel stands, never with
Ctrl, Meta, or Alt held, never while typing in a text field, and
never with no selection, and never while the spotlight cooldown
runs. An armed verb over a modal decision would hide the decision
it needs, so the incident guard is intentional, not an omission.
Do not add an incident exception here without re-arguing that panel
rule: the guard is intentionally identical to the camera, group,
idle, lens, story, thoughts, claim, proclaim, found, road, visit,
and model keys, not to Space, P, 0, or M.

Shared guard (2026-11-03): while a Story panel stands open, the shared keydown guard returns before this verb, so it never acts behind the chronicle; Escape, the pause keys, the speed keys, and M stay live. See story-panel-key-guard.md.

Arm toast answers at once (2026-11-03): the arming toast jumps the toast queue, like the still-armed reminder and the other direct replies, because the toast is the only text naming the next tap and a queued instruction would let the next resident tap commit the spotlight instead of selecting; the displaced ambient toast waits at the head of the queue instead of being erased.
