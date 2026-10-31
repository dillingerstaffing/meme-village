# Camera zoom buttons

The camera zooms on the mouse wheel and two-finger pinch, and no
on-screen element ever named either, so a player without a wheel or a
pinch gesture had no zoom at all except the reset button's fixed 38,
while every other camera control in the speeds row already had a
button. The speeds row carries two zoom buttons beside rotate, so they
ride the thumb-zone move into the tray on phones exactly like the
reset, rotate, and save-view buttons.

Each tap steps cam.dist by exactly the wheel factor: zoom in 0.9,
zoom out 1.1, clamped 15 to 62. The buttons and the wheel step the
same factors from the same camera, so they cannot disagree, and
neither button clears a camera follow: zooming orbits the followed
resident at the new distance instead of dropping them. The button
titles name the wheel directions they mirror.

On phones the tray speeds row carries nine buttons once zoom joins
it, and nine 44px buttons cannot fit one tray row (396px plus gaps
against 374px inner width at 390, 359px at 375), so the row is a
five-column grid in two rows (five plus four), each button at least
44px tall and a full grid cell wide, and the collapsed tray cap rises
to 110px so the second row is never clipped. The whole row still fits
the tray at 390 and 375 with no button overlapping another, and the
stats panel and alerts stack re-pin from the tray's measured height,
so the taller tray covers nothing.
