# One Store Owns State; Only the Four Renderers Write DOM

All game state lives in Store.state, and G is only an alias for it.
Discrete UI events go through Store.dispatch; simulation code changes
state inside Store.transact, which commits once per frame. The only DOM
writers are the four subscribed renderers: renderOverlay, renderHud,
the tray refresh, and renderSheet. New state gets a field on the state
object and, for UI events, a dispatch action. New display extends a
renderer or its selector. Thought text renders only in the character
sheet, never in the tray.

Why: anything that writes DOM from the sim, or keeps a second copy of
state, desyncs within a frame and the next commit rewrites it anyway.
The single door is what makes every visible change traceable to one
state transition.
