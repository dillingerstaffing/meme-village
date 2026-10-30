# Recall: An In-Flight Claim, Road, or Founded Site Can Be Called Off

A claim or road, once staked or laid, locked the village's only claim
slot or road slot until the work finished, with no way back: the
refusals named the crew still out, but the player could neither
recall them nor start anything else. The Age of Empires rule governs
the refund: only the unused parts of a build come back, and a claim
has built nothing until it stakes, so every carried store is still
unused and comes home in full. A founded site had the same trap in
a different shape: "Not yet" cancelled only the pick, so a misclicked
kind locked its plot until the site finished, with no way back.

- Tapping the Claim tray verb while a claim is in flight opens a
  recall row instead of the bearing and ring picks: it names the
  stores that come back (delivered stores plus any crate in a party
  member's hands, computed by the pure claimRefundStores()), offers
  Recall the claim, and offers Let them finish, which only closes the
  row. Tapping Road while a road is in flight opens the same shape
  of row, with no refund number, because planks are carry labor,
  not stock.
- cancelClaim() returns each in-hand crate to the village stockpile
  (G.stores, with the stored-crate mesh restored per unit) and the
  delivered stores with it, clears every claim fetch and claimParty
  flag, releases claim-stationed members to idle, removes the stake
  banner mesh, nulls G.claim, and frees the claim slot, so a new
  claim can be staked at once. The release also cancels the social
  intent it replaces, on the same rule as the other walk-replacing
  doors: visitId, pendingWatch, and a stale watchOf clear beside the
  idle, or arrive() fires the stale leg at the released resident's
  next station instead of the work there. cancelRoad() clears every road fetch
  and roadCrew flag, releases road-stationed crew to idle, removes
  the surveyed line, drops the road record from G.roads, and nulls
  G.roadBuild, freeing the road slot. Its release cancels the social
  intent on the same rule as the claim release.
- Both recalls toast and chronicle as the player's own call ("called
  off", never "scattered" or "abandoned", which are the season
  boundary's words for a crew that died or departed). Both add no
  graph edge and write no wk() ledger: the recall withdraws the party
  or crew the imitation graph recruited (spec section 23), and
  returns only material already carried, never ground, since no plot
  or road exists until staking or building completes.
- A founded site recalls through the same shape of row, with a
  different refund, because the site has already built: arming Found
  while a non-project site is under way opens a recall row in the
  foundPick row (a pick in progress keeps its kind chips; "Not yet"
  returns to the recall row), naming the kind, its current stage and
  labor, and the materials on site, then the stores that come back,
  then Recall the build and Let them finish. Project sites are never
  offered here: they belong to the project system, which has no
  cancel verb. cancelFoundSite() returns only the current stage's
  delivered stores plus any crate in a builder's hands; stores
  consumed by finished stages stay consumed, stage labor stays sunk,
  and planks are carry labor, not stock. It clears every buildSite
  and fetchSite pointer to the site, releases builders stationed at
  the site to idle, removes the site mesh, restores the plot ring,
  drops the site from G.sites, clears buildPref when it pointed at
  the site, clears the season focus when the site held it (G.proclaim
  nulls when its site matches, so a fresh proclaim in the same week
  pays no early-shift cost for a focus that is already gone), and
  clears Build orders when no site remains open, so a
  new founding can start on the freed plot at once. The release
  cancels the social intent on the same rule as the claim and road
  releases: visitId, pendingWatch, and a stale watchOf clear beside
  the idle, or arrive() fires the stale leg at the released
  builder's next station instead of the work there. It toasts and
  chronicles as the player's own call, adds no graph edge, and writes
  no wk() ledger, the same as the claim and road recalls.
- The recall row is a pick row, so on phones it compacts the stats
  panel like every other pick row; arming another verb clears the
  recall row without recalling, the same as any draft cancel.

Why: a commit with no way back is a trap, not a decision. The
recall keeps the commit honest by pricing the reversal exactly: what
was carried comes home, what was never built costs nothing, and the
player can change their mind about ground they have not yet bought.
For a founded site the ground itself comes back too: the building
never finished, so the plot is freed and only the materials already
consumed by finished stages are lost.
