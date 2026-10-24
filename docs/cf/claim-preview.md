# Claim Preview: The Pending Claim Reads on the Map Before It Costs Anything

A claim is the one BUILD verb whose commit buys ground the player has
never seen: the bearing and ring chips name the price, but nothing on
the map shows the center being bought or the three plots it will
become, so the player stakes blind and learns the 10-unit spacing
refusal only from the post-commit error. The Emperor standard: when
you are placing a building, the footprint image shows where it will
land, and a red footprint means it cannot go there. Meme Village
applies the same grammar to a claim, without validity tinting (that
follow-up still needs a vocabulary decision, since red already means
envied models and tension): the pending claim itself is drawn, in
gold, before the Stake chip commits anything.

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

Why: the road route preview already proved this grammar in the same
pick-row family (a gold ghost strip between two picked stations,
cleared on lay, cancel, or re-pick), and the claim pick row was the
one BUILD decision left without it. The ghost adds no mechanic and
no graph cause: it renders the already-spec'd claim (spec section
23: the founding household's imitation edges recruit the party)
before it commits, so the decision the player makes is the ground
they actually see.
