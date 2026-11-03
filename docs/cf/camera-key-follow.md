# Camera key follow

The camera followed only through the tray Follow button, a double-tap,
or the Follow toggle, while every other camera verb had already gained
a keyboard twin, so a desktop player with hands on the keyboard had to
reach for the mouse to follow the selected resident. The Sims 4 enables
its Follow Camera by right-clicking a Sim portrait, and StarCraft II's
follow camera maintains smooth, constant movement over its target:
follow is an anchor verb, and an anchor verb needs a reachable twin on
every input the game already serves.

F toggles cam.follow on the selected resident, exactly the Follow
button's verb: follow becomes the selection when it was not following,
and clears when it was, and the tray refresh flips the button face
from Follow to Following with it, so the key and the button cannot
disagree. With no selection F does nothing, like the disabled button,
and F never changes the selection: following is a camera move, not a
reselection.

The key is guarded like key pan and key zoom: it fires only once the
game has started, never while the game is over or an incident panel is
open, never with Ctrl, Meta, or Alt held, and never while typing in a
text field. The Follow button title names the key it mirrors.

The double-tap owns the double-click: a fast double-tap in tapAt
toggles follow and stamps the pair in G.lastDblTap, and the canvas
dblclick handler defers when it names the same resident within 600ms,
because tapAt already toggled follow and already selected. A slower
double-click past the 380ms tap window leaves no fresh stamp, so the
dblclick handler still owns that case, and a double-click ending on a
different resident is unaffected, since the stamp id must match. The
handler never changes the selection beyond what tapAt already selected.

Shared guard (2026-11-03): while a Story panel stands open, the shared keydown guard returns before this verb, so it never acts behind the chronicle; Escape, the pause keys, the speed keys, and M stay live. See story-panel-key-guard.md.
