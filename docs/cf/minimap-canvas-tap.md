# Minimap Jump Is Detected at Canvas Level, Never on the Element

#minimap stays pointer-events:none so drags starting on it pan the
camera. Tap-to-jump therefore lives in endPointer: a pointerup that was
not a drag, whose down point falls inside minimapRect(), calls
minimapJump and skips tapAt. Never bind a click or tap listener to the
minimap element itself. A right-button release is not a tap at all:
endPointer clears it and returns, leaving the contextmenu handler as
the sole right-click path, so a right-click never first selects,
orders, or deselects through the left-tap path before the smart tap
runs.

Why: an element with pointer-events:none never fires its own listener,
so the binding looks correct and silently does nothing. Taps then fall
through to the canvas and deselect instead of jumping. This shipped
once as a regression after a scroll fix and was caught only by a tap
probe, not by reading the code.

A successful jump answers with the tap blip, in the camera-return
grammar: every other camera jump answers aloud, so a silent minimap
tap read like a tap that missed. A drag that starts on the minimap
pans instead of jumping and stays silent, because a continuous pan
is not a discrete tap.

A hidden minimap takes no jumps. When hudTick hides the minimap
(visibility hidden) because the selected tray leaves no slot for it,
whether with no toast live (the tray pin) or with a toast live (the
toast pin stands down and the tray overlaps the minimap's home rect),
the element keeps its rect, so a tap on the tray area over it would
otherwise jump the camera to a map point the player cannot see.
minimapJump refuses the jump when the element's inline visibility is
hidden, and the tap falls through to tapAt instead. The inline style
is the signal: hudTick sets visibility hidden inline, nothing else
hides the minimap.
