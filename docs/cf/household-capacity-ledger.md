# Housing Is One Ledger: Households Plus Housed Newcomers Never Exceed Capacity

G.houseCapacity is the count of dwellings (10 starting homes, +1 per
finished cottage from the site table). Two claims draw on it:
G.households (one unit per household) and G.soloHoused (one unit per
welcomed newcomer not yet in a household). housingFree() is capacity
minus both claims, and it is the only gate at both doors: households
form and arrivals are welcomed only while the ledger leaves room, and
population never exceeds POP_CAP (16). A member who was solo frees
their solo claim in the same step their household takes its claim, so
a household formed out of a housed newcomer is capacity neutral. A
household claims a finished cottage site by setting site.claimedBy;
freeing the household clears it. A solo newcomer's dwellingSite is
only a home position, never a claim. Departures free every claim they
held before the members are removed.

Why: separate counters per system drift apart within a season, and
the village either grows past its roofs or refuses people while
cottages stand empty. One ledger, consulted at both doors, keeps the
accounting exact.
