# Phone Close Buttons Meet the 44px Thumb Target

On screens 560px and under, the two close buttons a phone player
actually reaches meet the 44px thumb target the game's pick-row chips,
alerts-stack chips, speeds-row buttons, and toast skip button already
meet.

The tray deselect X is the only reliable deselect and arm-cancel on a
phone: a ground tap keeps the selection and keeps an armed verb armed
(measured in the 2026-10-31 loop run that shipped this rule), so the X
cannot be a 30px corner button the thumb must hunt for. The phone tray
rule gives it a 44px square, and the info block's right padding grows
with it, 38px to 52px, so the larger button still clears the name text
instead of covering it. The button's verb is unchanged: it deselects
and ends the map-targeted arms, exactly as before.

The sheet header close is sticky at the top of the sheet and is the
sheet's immediate dismissal path, while the foot Close sits below the
whole journal: a player who opens the sheet to check a thought and
closes at once must land on the header button, not scroll the journal
to reach the foot. The phone rule gives the header close a 44px
square; the desktop sheet keeps its compact 34px close, and the header
is a flex row beside a 46px chip, so the larger button changes no
layout. The foot Close is untouched and still closes the same way.

Both rules are phone-only CSS, display only: no state, no dispatch,
no sim touch, and no second DOM writer.
