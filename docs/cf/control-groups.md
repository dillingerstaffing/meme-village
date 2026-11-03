# Control Groups: Resident Recall Slots

Three numbered slots, one resident each. Assign: select a resident,
arm Groups in the tray, tap a group chip. Recall: tap the chip, or
press its digit key (1, 2, or 3); recall selects the resident and
centers the camera on them. Keyboard assign is Shift plus the digit.

Invariants:

- A slot holds at most one resident, and a resident holds at most
  one slot. Assigning a resident who already holds a slot moves
  them; assigning to an occupied slot overwrites it, and the toast
  names the new occupant, so an overwrite is never silent.
- Groups is an armed verb in the one-highlight vocabulary: arming
  it disarms every other armed verb, arming any other verb disarms
  it, re-tapping the gold button disarms it, and a selection change
  ends a pending arm, because the arm's subject is the selection.
  At most one gold border ever stands; the chips themselves never
  carry a lit treatment.
- A chip is a route to its resident. The three chips always render
  as one horizontal row in the alerts stack, including empty slots,
  because an empty slot needs a tappable target for its first
  assignment; a column of three would push the stack up into the
  objective card on phones. A chip for a resident who left
  the village never renders: removeAgent clears any slot holding
  the removed resident, and a recall of a gone resident clears the
  slot and answers, changing nothing else.
- Recall never follows: it centers once and clears any camera
  follow. Recall of an empty slot answers how to fill it and
  changes nothing. Both recall answers jump the toast queue, on
  the direct-reply rule: a recall that changes nothing has no
  other visible effect, so a queued answer reads as a dead chip
  tap, and the displaced toast waits at the head of the queue.
  Groups mutate selection and camera only, never
  sim state: no order, model edge, want, meter, or store changes.
- The keyboard assign bypasses the tray button, so Shift plus a
  digit with nothing selected answers that no resident is selected,
  and that answer jumps the toast queue on the same direct-reply
  rule: the keypress changes nothing visible, so a queued answer
  reads as a dead key. The successful assign is untouched: its
  toast names the occupant and the chip row visibly changes.
- The digit keys carry the same guard as every other keyboard
  verb: only once started, never while over or an incident panel
  is open, never with a Ctrl, Meta, or Alt modifier, never while
  typing. An incident panel is a modal decision, so a digit behind
  it moves no selection, rewrites no slot, and jumps no camera
  behind the panel.
- State is G.groups, an array of three resident ids or null, read
  through Store.dispatch actions (ui/group/set, ui/group/clear).
  A legacy save without the field reads as three empty slots, and
  the first assignment writes the array, after which saves persist
  it like any other state field.
- Titles name the keys, in the game's established naming grammar for
  keyboard verbs: the Groups button names the digit recall and the
  Shift plus digit assign, an occupied chip names its own digit
  recall and its Shift plus digit assign, and an empty chip names
  its Shift plus digit assign. Titles only, no visible text change,
  so the chip row's layout and the one-highlight vocabulary are
  untouched; guarded by pwtest_keygroupname.py.

Shared guard (2026-11-03): while a Story panel stands open, the shared keydown guard returns before this verb, so it never acts behind the chronicle; Escape, the pause keys, the speed keys, and M stay live. See story-panel-key-guard.md.
