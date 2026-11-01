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
