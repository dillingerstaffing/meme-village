# The Idle Finder Cycles One Loafer at a Time, and Orders Nothing

The Village cluster carries an Idle button beside Follow. One tap
selects the next resident whose loafT has passed 15, the same
threshold that fires the idle alert chips, moves the camera to that
resident, and stops there. It never issues an order, never selects
more than one resident, and never becomes a control group: the
player still directs the found resident with the ordinary Send to
buttons, or taps Idle again for the next loafer. Tapping with no
loafer answers "Everyone is busy right now" instead of going silent
or greying out, and the button face names the loafer count while
any exist, so the player reads whether there is anyone to find
before tapping.

The button carries no lit treatment in any state: never .on,
.armed, or .cam. It is navigation, like Follow, not an order, not
an armed verb, and not a follow state, and it sets no order when
tapped. A tap that finds a loafer does end a pending map-targeted
armed verb (Spotlight, Model, Visit, Proclaim, Found), because the
verb belonged to the selection the tap replaces; a tap with no
loafer changes no selection, so it changes no arm. Tapping an idle
alert chip ends a pending map-targeted armed verb for the same
reason: the chip changes the selection the verb belonged to, while
still selecting the alerted resident and moving the camera. Any
selection change, by any route, also ends a pending Speak For arm:
Speak commits on its own button, but its preview is read from the
current selection (speakPlan picks its target from the selection),
so a preview read for one selection cannot commit for another, and
the gold clearing beside the new selection is the signal. The loafer list is computed fresh on
every tap from the live loafT values, never cached, so a resident
who starts working between taps is never selected as idle.

Why: the idle alert chips fire once per loaf episode and expire
after 9 seconds, and they show at most two loafers, so a resident
still loafing a minute later, or a third loafer, had no route back
to the player at all. A chip for a resident who leaves the village
ends at once rather than standing out its 9 seconds: a chip is a
route to its resident, and a route to someone gone selects nobody
and moves no camera. A chip for a resident who starts working ends
at once too, on the same rule: the chip is a live claim that the
resident is idle, and loafT resets the moment work starts, so the
render filter keeps only alerts whose resident still loafs past 15. The finder is the persistent route for the
same definition, not a second definition.
