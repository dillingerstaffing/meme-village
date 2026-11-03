# On Small Screens the Sheet Starts Below the Objective Card

On screens 720px and under, hudTick pins the open character sheet's
top to the objective card's height plus 20px and sets the sheet height
to auto; on wider screens it clears both values. Keep project pick
buttons at min-height 44px and full width on phones. If the sheet's
layout or the card changes, re-check the pin against the card.

Why: in CSS the sheet is z-above the card and 86% tall, so unpinned it
covers the project pick buttons completely. The choice then reads as
flaky, and the sheet eats every camera drag across most of the screen.
A reading surface never gets to cover a decision control.

Minimap floor (2026-11-03): at 560px and under the minimap sits
top-anchored at 202px, so the same pin also floors the sheet top at
the minimap's bottom edge plus 8px. Without the floor a sheet top
inside the minimap's strip covered its bottom edge and swallowed taps
there, leaving the minimap's south strip dead while the sheet stood.
Above 560px the minimap is bottom-anchored and the sheet covers that
corner by design, so the floor applies only at 560px and under.
