# Keyboard Escape close

The character sheet closed only through its own X and Close buttons
and the Story panel only through its X or, for a manual open, a
backdrop tap, while every other camera verb had already gained a
keyboard twin, so a desktop player with hands on the keyboard had to
reach for the mouse to dismiss either panel. The Sims 4 cheat sheet
lists Esc as bringing up the main menu or cancelling the current
operation, and StarCraft lists Esc as Cancel: Escape dismisses the
panel in front of the player.

Escape closes the topmost closable panel first: an open Story overlay
closes through the existing close function, else an open sheet closes
through the ui/sheet dispatch, exactly the sheet close button's verb,
so the selection survives and Escape never deselects. An incident
panel is never closed this way: it needs a choice, so Escape does
nothing while one stands. The verb is guarded like the other keyboard
verbs: it fires only once the game has started, never while the game
is over, never with Ctrl, Meta, or Alt held, and never while typing
in a text field.

The close buttons name the key, so a desktop player can discover it
without a guide: the sheet header X and foot Close carry titles
naming Escape, following the naming grammar the other keyboard verbs
already use (Follow names F, the camera button names R/Home and
WASD/arrows, the pause button names Space, P, and 0). The Story X
names Escape only on a live panel; on the final panel, where Escape
is blocked because the game is over, its title is plain Close, so
no button ever promises a key that does nothing.
