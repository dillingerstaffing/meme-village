# Claim Preview: The Pending Claim Reads on the Map Before It Costs Anything

A claim is the one BUILD verb whose commit buys ground the player has
never seen: the bearing and ring chips name the price, but nothing on
the map shows the center being bought or the three plots it will
become, so the player stakes blind and learns the 10-unit spacing
refusal only from the post-commit error. The Emperor standard: when
you are placing a building, the footprint image shows where it will
land, and a red footprint means it cannot go there. Meme Village
applies the same grammar to a claim, with one deliberate change of
vocabulary: red already means envied models and tension on the
lenses, so the refused footprint is carried by shape, not by a new
color, and the ghost stays gold in both states.

- syncClaimPreview() is called from hudTick's claim-pick row, the
  per-frame HUD render, so every pick change re-syncs it. The ghost
  is null until claimArm AND a bearing AND a ring are all picked;
  picking a different bearing or ring moves it to the new
  claimCenter(), cancelling, staking, or arming another verb clears
  it, because claimArm falls and the key empties.
- The ghost is scene-graph only: one gold ring (RingGeometry 3.1 to
  3.5, 0xe8b34b) at claimCenter() plus three gold dots
  (CircleGeometry, same gold) at claimClusterPlots(), the pending
  cluster itself. No pole, no flag, so it can never be mistaken for
  a staked claim banner (pole plus flag plus ring) or a surveyed
  plot (gold ring alone, already on the ground).
- Display only: the block reads G.claimBearing and G.claimRing and
  writes the scene. It never enters G.claim, G.claimPlots, or PLOTS,
  never calls wk(), never touches the driven-work ledgers, never
  recruits the founding party, and never survives a save, because
  it is rebuilt from the picks on every hudTick and dies with them.
- Validity reads from the ghost itself, before any tap: when the
  picked center sits within 10 units of a surveyed plot, the ring
  breaks into four arcs, the three plot dots hollow out into rings,
  and a cross marks the center, and the pick row's Stake chip is
  renamed "Ground already claimed" (tapping it still runs the stake
  path, which toasts the same named refusal). The ghost and the
  refusal share one pure test, claimCenterBlocked(), so the preview
  and the refusal can never disagree; the ghost's key carries the
  blocked flag, so a change to PLOTS re-syncs it.

Why: the road route preview already proved this grammar in the same
pick-row family (a gold ghost strip between two picked stations,
cleared on lay, cancel, or re-pick), and the claim pick row was the
one BUILD decision left without it. The ghost adds no mechanic and
no graph cause: it renders the already-spec'd claim (spec section
23: the founding household's imitation edges recruit the party)
before it commits, so the decision the player makes is the ground
they actually see.

The Town gate itself reads before any tap, in the stats panel claim
row (claimLbl, rendered by renderHud after the growth row): below
Town it names the gate for both Town verbs, "Claims and roads unlock
at Town"; at Town and above it names the unlocked state and the live
road count against the cap. The row is display only and changes no
gate, so a refusal toast after a tap can never be the first time the
player hears about the gate.

The same pick row carries the adjacency read (spec section 24,
claim-adjacency.md): once a bearing and ring are picked, each
ADJACENCY row whose source station lies within range of any of the
claim's three cluster plots is named in the row with its kind,
percent, stat, and source, before the Stake chip commits. It is
display only and shares the table and the distance test with the
ledgers, so the preview and the bonus can never disagree; a bonus
with no plot in range names nothing.
