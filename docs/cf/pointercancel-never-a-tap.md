# pointercancel Only Cleans Up; It Never Becomes a Tap

The pointercancel handler in bindInput deletes the pointer and resets
downAt and dragged, and does nothing else. Only pointerup runs
endPointer, the single path that can reach minimapJump and tapAt. The
window-level pointercancel likewise only clears ptrDown.

Why: pointercancel fires when the browser takes a gesture over (scroll
intervention, system gesture, touch leaving the surface). Routing it
through the tap path turns cancelled gestures into phantom taps that
select residents, issue orders, or jump the camera to places the
player never touched.
