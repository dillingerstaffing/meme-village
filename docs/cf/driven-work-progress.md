# Progress Counts Only Driven Work, Through the wk() Gate

Objective metrics read weekWorkP, never weekWork. wk() adds to
weekWorkP only when a.driveObj is true, together with the synergy and
crew-rhythm multipliers and the project part credit. Construction
labor enters wk() under the build key and returns before the driven
branch: it fills the site labor ledger in G.sites, never weekWorkP,
and build work is never credited as driven work. Adjacency is the
one multiplier inside that ledger: a workshop site within 20 units
of the mill accrues site labor at 1.25x (spec section 24), applied
after weekWork and earnPay have taken the unmultiplied amount, so
the bonus speeds the build without touching any driven total. A new way of
working enters the driven ledger only by setting driveObj through the
paths that already do (a player order in setOrder3 and decide(), a
copied model or a want that decide() resolves), and initiatives always
run with driveObj false: fireInitiative clears it on the actor and on
any resident it sweeps along. A resident in their Established arc counts one extra
synergy partner in `wk()`'s multiplier; the gate itself does not
move. Station tier progress is not `wk()`'s business at all: it
accrues in `stepAgents` under its own ledger (`G.tierProg`).
Income (Stage 6) also observes `wk()` from inside it: `earnPay`
pays the resident on every `wk()` call, driven or not, on the same
amount `wk()` counted; it reads neither weekWork nor weekWorkP and
writes only the resident's cash. A wallet is never progress.

Why: if self-started or ambient work filled objectives, the player
could win by watching and ordering people around would stop mattering.
Crediting the plain weekWork totals looks harmless and silently deletes
the distinction the whole objective system is built on.
