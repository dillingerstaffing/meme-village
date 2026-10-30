# Claim Adjacency: Founded Kinds Gain From Standing Next to a Station

Two one-way rows, and three readers that must never disagree about a
bonus. A workshop within 20 world units of the mill accrues its own
construction labor 25 percent faster; a completed hall within 20 of
the green drains blame through green mediation 25 percent faster.
The mill and the green gain nothing back: the bonus belongs to the
founded kind, never to the source.

- The rows live in one ADJACENCY table (kindA, kindB, maxDistance,
  bonusStat, bonusAmount), read by adjacencyRowFor() and
  adjacencyApplies(), which measure world units between a site or
  pending plot and the source station center. No reader hardcodes a
  distance, a percent, or a pair: a new row is one new table row
  plus its reader branch, never a second copy of the numbers.
- The bonus is a rate multiplier, judged from live positions every
  time it applies and never stored on the site or the hall. A
  workshop site accrues at 1.25x in wk()'s build key on every accrual
  while it stands in range; the mediation drain multiplies by 1.25
  on every tick while a completed hall stands in range. A bonus
  lives only while the pair stands, because nothing about the pair
  is cached.
- The site labor ledger keeps the driven-work rule intact: wk()
  multiplies only the amount written to the site (sb.labor and
  sb.stageLabor), after weekWork and earnPay have already taken the
  unmultiplied amount, and the build branch still returns before
  the driven branch, so adjacency labor never becomes driven
  progress.
- The claim pick row previews the same rows before the Stake chip
  commits: when a bearing and ring are picked, each row whose source
  lies within range of any of the claim's three cluster plots is
  named in the row with its kind, percent, stat, and source. A
  preview of a bonus that does not exist would be a lie on the map,
  so the row and the ledgers share the one table and the one
  distance test; the preview reads claimClusterPlots(), the same
  rows staking appends.

Why: placement is a decision the player makes once and lives with
for the building's life, so the yield of the ground must read
before the commit (the Civilization placement-lens grammar), and
the bonus itself must stay a live property of standing next to
something, not a discount stamped at founding that survives the
pair breaking apart.
