# Desires Travel the Graph: Wants Carry an Origin

Every want carries an origin: a.want.from is the id of the resident
the want was copied from, or null when the want is the resident's
own. Set it only through the want/set dispatch, which stores
p.from, and thread it through every wantPend: a pending want keeps
its from, and the wantPend processing passes wp.from into
giveWant as fromId.

Spread follows the imitation graph first. In giveWant, a follower
(b.model === the wanter) adopts with MIM.spreadFollower. Proximity
spread is allowed only from a public model (visEff at or above
MIM.spreadVisMin, within the wanter's want range): a spotlighted
wanter spreads at the follower rate, anyone else at
MIM.spreadNeighbor. Never restore raw proximity contagion for
everyone, and never spread to a resident who is sick, a child, or
already holding a want or a pending want. Count each adoption in
G.mimic.spread, and name the spread in a toast only when two or
more residents adopt.

Convergence breeds heat. When a resident takes a want and another
resident (not the origin the want was copied from) already wants
the same station, add MIM.rivalTension to that pair, once per
giveWant call, and count it in G.mimic.converged.

Fulfillment and misses write back into the graph. Capture
a.want.from before clearing the want in either branch. A copied
want fulfilled lowers the pair tension with its origin by
MIM.gratitudeTension, records the origin in watchHist, adds
MIM.fulfillCohesion to cohesion, and counts in
G.mimic.doneCopied. An own want fulfilled adds
MIM.fulfillPurposeSelf to the purpose need and counts in
G.mimic.doneSelf. A copied want that expires adds
MIM.resentTension to the pair with its origin and counts in
G.mimic.missedCopied. Keep the existing morale effects and the
player-order bonus exactly as they are.

Every tuning number for this system lives in the MIM table.
Change behavior by editing that table, never by scattering new
constants through giveWant or the want lifecycle.
