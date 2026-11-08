# Sheet Swipe-Down Close

On phones the character sheet is a bottom sheet, and a bottom sheet
closes by dragging it down: a downward touch drag of at least 60px,
mostly vertical, starting off any button while the sheet is scrolled
to the top, closes through the ui/sheet dispatch, the same verb as the
header X, so the selection survives. The drag never writes DOM
mid-gesture and never blocks scrolling: a drag that starts scrolled
down scrolls content instead, a short or sideways drag leaves the
sheet open, and a second finger disarms the gesture. The gate is the
same 720px breakpoint the sheet CSS uses, so the desktop side panel
never drags. A thin grabber bar at the top of the phone sheet names
the gesture the way Material and iOS sheets do: the handle is always
draggable, and the content below it dismisses only from the top.

Why: every phone player knows the bottom-sheet gesture, and the
sheet's other dismissals all sit far from the thumb after reading:
the header X at the top of the screen, the foot Close below the whole
journal, the Escape key on no phone keyboard. A sheet that ignores
the swipe reads as stuck, and the player reaches for the tray
deselect underneath instead, which leaves the sheet open.

Guarded by pwtest_sheetsipe.py in the loop's hidden_files at 390 and
375 (plus a 1440 control proving the desktop side panel never
drags): the probe fails pre-fix on exactly the swipe-close and
grabber legs with the short, sideways, button-start, and scrolled
controls passing.
