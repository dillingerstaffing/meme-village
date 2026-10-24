# Recall: An In-Flight Claim or Road Can Be Called Off

A claim or road, once staked or laid, locked the village's only claim
slot or road slot until the work finished, with no way back: the
refusals named the crew still out, but the player could neither
recall them nor start anything else. The Age of Empires rule governs
the refund: only the unused parts of a build come back, and a claim
has built nothing until it stakes, so every carried store is still
unused and comes home in full.

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
  claim can be staked at once. cancelRoad() clears every road fetch
  and roadCrew flag, releases road-stationed crew to idle, removes
  the surveyed line, drops the road record from G.roads, and nulls
  G.roadBuild, freeing the road slot.
- Both recalls toast and chronicle as the player's own call ("called
  off", never "scattered" or "abandoned", which are the season
  boundary's words for a crew that died or departed). Both add no
  graph edge and write no wk() ledger: the recall withdraws the party
  or crew the imitation graph recruited (spec section 23), and
  returns only material already carried, never ground, since no plot
  or road exists until staking or building completes.
- The recall row is a pick row, so on phones it compacts the stats
  panel like every other pick row; arming another verb clears the
  recall row without recalling, the same as any draft cancel.

Why: a commit with no way back is a trap, not a decision. The
recall keeps the commit honest by pricing the reversal exactly: what
was carried comes home, what was never built costs nothing, and the
player can change their mind about ground they have not yet bought.
