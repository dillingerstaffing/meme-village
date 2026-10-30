# Membership Never Gates the Medic

The medic serves everyone through the manual path: sendMedic() is
unchanged by coverage, and any resident, member or not, can be sent
for exactly as before. A tier changes only three things: position
in the medic queue (auto-dispatch works the queue by tier rank,
then by time waiting), and the winter death roll (a divisor from
the tier row, plus the Platinum row's stabilisation saves). It
never changes whether care exists.

Premiums debit the bank account only, at the season boundary in
premiumSweep(), right after bankSweep(). They never touch cash on
hand, never take a balance below zero, and never create debt: an
account that cannot pay in full lapses to no tier, with no partial
debit. Premiums and Call Out fees are a sink only; no coverage code
may write to weekWork, weekWorkP, or any driven ledger (see
driven-work-progress.md).

Why: the moment membership decides who gets a medic at all, the
village stops being a community the player oversees and becomes a
gate the player rations. Queue order and odds are legible benefits
the player can watch working; access is not a benefit, it is the
baseline.

Existence is not coverage: when Jonah himself is gone (dead or
departed), there is no medic to send, and no new medic appears.
The paid Call Out button and the incident Send Jonah action then
disable with a plain note that there is no medic, callOut refuses
before any fee check, and no patient is enqueued into a line that
can never move. A disabled action without its reason would read as
a broken button; the note is part of the control, not decoration.
