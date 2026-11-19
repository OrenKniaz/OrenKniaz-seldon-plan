# Cohort m2c walls (c03, c04, c05) + T-144 (c01 oracle) — Fable design review, 2026-11-14

Read on main f5d23aa (+5546f7a). Read-only; nothing here is built. Evidence = store records in
`C:/seldon/tests/m1/shelflife-f5d23aa-c0N/product/.seldon/state.sqlite3` (record ids given as rNNN).

## 0. Verdict in five lines
- c03 and the FIRST half of c05 are one cause (Rule 1). The suspicion "a cross-area contract nobody owns" is
  close but not exact: the contracts exist; one planning sentence makes the wrong area write the check.
- The SECOND half of c05 (the wall itself) is a T-134 sibling in the REVIEW brief (Rule 2, bug-sized).
- c04 is a separate cause: three plan/proof rules that cannot all hold (Rule 3). It is latent in c03 and c05 too.
- T-144: the premise is wrong. c01 DID prove the real-browser path. Six of the nine oracle failures come from
  the oracle's own control discovery, three are shared with native. Rig fix, no Seldon rule (section 4).
- None of the walls needs a user question once the rules land; all three are planner-side.

## 1. c03 — u001 ASKED (judgment gap <-> worker `blocked` on a discovery it owns)
**TRIAGE: DESIGN.** Family: *Judge asked beyond its view* (also *Blame lands on wrong owner*).
**Root cause.** DETAIL is told "use one wave check per contract, owned by the provider area, for integrated
behaviour" (questions.py DETAIL prompt). `data` provides item-record/store-interface and consumes nothing
(u001 `consumes: []`), so its five `checks/data/wave.py` checks must drive the integrated product through the
server's HTTP surface (http-api, server-command), contracts u001 does not hold. The unit JUDGE then correctly
rejects "exact 409 without agreed text visible to this unit" (r241, r274) and the worker correctly reports the
launch/API agreement missing (r252). Neither can fix it: the text exists, in another area's contract.
**Siblings (same sentence):** c03 r62 and c05 r62 architecture gaps ("wave checks must be owned by each
contract's provider... authorize delivery-owned end-to-end checks") — this burned the one ARCHITECT re-ask in
both runs; c04 u001 first failure r161 ("wave sources require exact HTTP 200 without visible agreed text");
duplicate proof (c03 n009-n011 by data repeat n020 by server). 4 of 5 runs show it; c01/c02 got through by luck.
Also: a WORK discovery can only name a unit as owner (schema.py:119), so a missing agreement has no address
until STEER (M3). After Rule 1 the need disappears; leave the M3 route to M3.

## 2. c05 — DETAIL asked ("Remains after one ARCHITECT re-ask ... supply the handle of delivery's check")
**TRIAGE: BUG (incomplete T-134 fix) on top of the section-1 DESIGN cause.** Family: *Two rules disagree*.
**Root cause.** Revision 3 was already right: `quality:004 -> [n031, n032, n036]`, n036 being delivery's wave
check. `plan_review.briefs` (plan_review.py:36-38) deletes other areas' checks from each criterion before
showing it, so the importer reviewer saw quality:004 without n036 and asked for it (r137). The correction went
to importer, which cannot see or name a delivery handle, so it answered `contract_gap` (r157). `detail.gap`
(detail.py:15-19) allows one ARCHITECT re-ask per vision, already spent on r62 (section 1) -> user question.
**Siblings:** T-134 (same function, check requirements); any per-area view that filters a cross-area link
instead of showing where it lives (trace rows for `quality:*` at plan_review.py:39-41 do the same).
The re-ask guard is a count standing in for "no progress": a second, unrelated gap is refused a planner answer.

## 3. c04 — u004 ASKED three times ("this check does not detect the missing requirement ... n037")
**TRIAGE: DESIGN.** Family: *Two rules disagree* (touches *Proof observes impure state*, T-104).
**Root cause.** Three rules cannot hold together for a unit whose product is a README plus check machinery:
(a) "every owned requirement needs a local check" (questions.py "How the plan executes"); (b) an `establishes`
check must fail at T; (c) T keeps all check machinery (`checkPaths`), removing product only (T-104). n037
`checks/workflow/mechanics.cjs` tests the workflow helpers, which live in checkPaths, so it passes at T and at
wave start by construction (r169, r245, r293). The failure text tells the worker to "declare it preserves",
which only the planner can do (`mode` is plan schema). Unwinnable, like T-134.
**Siblings (will hit next):** c03 n035 `checks/integration/check_harness.py`, c05 n035
`checks/delivery/verify.py --probe-runtime` — same shape in the delivery unit of every walled run. c01 escaped
only because its local delivery check happened to read the README (exit 1 at T).

## 4. T-144 — c01 SCRIPTED_C, oracle 30/40 vs native 36
**TRIAGE: BUG in the rig (oracle), family *Rig gives false signals*. Not a Seldon proof gap.**
- The "uncaught error at `set`, line 5" is the oracle's injected helper (oracle_ui.py:132,
  `throw Error('semantic control not found')`, script url empty), not product code.
- c01 proved the real path: `checks/web/assets.wave.cjs` (n030) and `checks/delivery/fresh_folder.cjs` (n041)
  launch the real `server.py` and Edge, then add, filter, consume, delete; both exit 0 on the final commit
  80a208d2 (observations r475, r478, 10 and 4 evidence files). PRODUCT/flow verdicts had that evidence.
- 3 failures (375/1440/healthy console) are the favicon.ico 404; native and c02 fail the same three. Not a delta.
- 4 failures (inline validation, add, consume, delete) are one oracle bug: `field(/name/)` returns the first
  visible input whose description contains "name"; c01's search box has placeholder "Search by name", so the
  oracle drives the filter form, finds no quantity there and throws. The last two only cascade.
- 2 failures (search, expiry filter): c01 filters on an explicit "Apply filters" submit; the oracle sets the
  value and waits for a live update. The brief says "search and an expiry filter", not "live".
**Fix (rig, contender-neutral, `work/fight-1/oracle_ui.py`):** resolve the add form first (the form that holds
a quantity field) and look for name/unit/expiry inside it; after setting a search or filter value, if the
list has not changed, submit the enclosing form (Enter), as a person would. Re-score c01, c02 and native with
the same oracle. Expected, not verified: c01 lands at parity. Product-side only the favicon is real, and it
is common to all contenders: one ticket, no rule.
**One rule for "every user-facing criterion proven in a real browser"?** It already exists (C26 + wave checks
on the integrated product) and held here. Do not add one from a rig artefact. The one honest residue: a UI
check is written by the UI's author and knows its choreography. That is what the blind oracle and Oren's own
run are for (P5); if a second run shows a UI its own checks pass and a stranger cannot operate, open a ticket.

## 5. The rules (three causes, three rules; all planner-side, none asks the user)
**Rule 1 (c03, c05 first half). A check reaches only through what its owner holds: its own product and the
contracts its unit consumes. So a contract's integrated check belongs to a consumer, which holds both sides;
a provider proves its side locally.** Delivery-like areas consume everything, so the end-to-end check is theirs
without asking ARCHITECT. A leaf provider has unit checks only. Failures still route to the provider through
the requirement links code already adds (`plan.merge` deferred checks -> `proof.gaps` -> fixups).
**Rule 2 (c05 wall). A per-area view never deletes a cross-area link; it shows where the link lives** (T-134's
rule, finished). And: **a contract gap always gets a planner answer; the user is asked only at a fixed point**
(the same outline produced the gap again), never at a count.
**Rule 3 (c04). RED is an observation, not a declaration.** Code records whether each check failed without the
unit's product and never refuses on it; whether a check that passes without the product is enough for its
requirement is the unit JUDGE's question (it already answers `baselineDemonstrated` and `meaningful`, with the
T / wave-start exit codes as code facts). `mode` is derivable, so it leaves the schema (normalise, not refuse).
**Needs Oren before the lane starts:** this rewords BLUEPRINT 3.1 (Check "declares establishes or preserves"),
the PROVING row of 3.2 and the 8.1 reading of C14 ("code proves the tests fail without the work" becomes "code
observes, the judge decides the reason"). C14's "RED for the right reason (observed)" stays true; a vacuous
check now ends as a judge gap with the exact fact instead of a code refusal. If Oren declines, the fallback is
plan-side only: delete sentence (a) for requirements whose checks are all wave level, and keep the refusal.

## 6. Lane briefs (no unit tests; journeys assert outcomes only; no caps; net src lines fall)
**Lane 0 — oracle (rig, not src). Now, in parallel.** `work/fight-1/oracle_ui.py` as in section 4; re-score
c01, c02, native; close or re-triage T-144 on the numbers.
**Lane A — Rule 1. First; lands alone.** Files: `questions.py` (DETAIL prompt: REPLACE "use one wave check per
contract, owned by the provider area" with the rule; no added sentence elsewhere), `architecture.py`
`local_plan` (check -> contract reference requires `endpoint(...) == "consumer"`, was any endpoint; a provider
naming its own contract gets the ordinary DETAIL correction). Delete first: the provider-owned sentence, the
"one per contract" count, the recorded fixtures that assert it (tests/seldon/test_architect.py:546, 563).
Journeys: (1) replay c03's recorded ARCHITECT + DETAIL: no `architecture_gap` record, data area has no wave
check, run reaches B; (2) scripted 4-area twin where the leaf provider's JUDGE stub rejects any exact value
not in its facts: all units DONE; (3) twin where the consumer's wave check fails on a provider defect: the
fixup lands on the provider unit, the consumer spends no recovery. Expected src: about -3.
**Lane B — Rule 2. Parallel with A (disjoint files).** `plan_review.py` `briefs`: keep each criterion's
foreign checks as `{area, purpose}` under `provenElsewhere` (same for `quality:*` trace rows), about +4.
`detail.py` `gap`: store the outline with the `architecture_gap` record; raise only when a prior gap of this
vision was raised against an equal outline; delete the `resume` key from the guard, about -2. Journeys:
(1) replay c05 revision 3 through REVIEW with a stub reviewer that flags any criterion lacking an API/UI
check: importer answers adequate, run reaches B; (2) two different gaps in a row both reach ARCHITECT and the
run reaches B; (3) ARCHITECT returns the same outline twice: WAITING at DETAIL with the gap text shown.
**Lane C — Rule 3. After A (shares questions.py) and after Oren's word.** `proof.py` `prove`: one pass at T
for every unit check, wave-start pass for those that passed at T, P must pass; delete the
establishes/preserves split, `undetected` and its message (about -12). `schema.py`: drop `mode`.
`questions.py`: the two establishes/preserves sentences in "How the plan executes" and the JUDGE prompt
collapse to one ("a requirement new in this unit needs a check that failed without the product; a check that
passed there proves preservation only"); the example loses `mode`. Journeys: (1) replay c04 u004 from its
recorded patch: PROVING passes, unit reaches JUDGING with the T exit code 0 in the facts, no recovery spent;
(2) twin with a vacuous check (passes at T, product requirement): JUDGE stub answers gap, the worker's next
brief carries the judge's words, then DONE; (3) the 50-unit journey unchanged. Open risk, stated: whether the
real JUDGE accepts a machinery self-test beside a wave-only requirement is LLM behaviour; one real ShelfLife
run after landing settles it (P4).
**Order:** Lane 0 and A and B now (0 is rig; A and B touch disjoint files) -> cohort m2d on the result ->
Lane C once Oren has answered. A before C because A removes most T-passing machinery checks at the source.

## 7. Tickets to open (P9)
c03 wall -> DESIGN, Rule 1. c05 wall -> BUG (T-134 reopened or sibling) + the gap-guard count -> family
*Hard stops end runs*. c04 wall -> DESIGN, Rule 3, blocked on Oren's reading of C14. T-144 -> retitle
"oracle drives the wrong form on c01", type rig; plus one small product ticket: favicon 404 in every contender.

## 8. Cohort m2d on fa04237 (Rules 1 + 2 landed): 0/5 C — review of the five walls
**Rule 1: keep and amend, do not revert.** Its mechanics held: no provider-side "unagreed 409/200" judge loop
in any run; d02 and d05 each got four units DONE and reached final verify; seven contract gaps (d02, d03, d05)
all got a planner answer through the new fixed-point guard. 0/5 is one environment fault (2 runs), the Rule 3
wall still waiting (1 run, hit twice more), and two holes Rule 1 exposed (2 runs).

**8.1 d01 u002, d03 u001 (T-136) — BUG, environment (Codex Windows sandbox). Not Rule 1 or 2.**
Family: *Blame lands on wrong owner*. Proven from ACLs and `~/.codex/.sandbox/sandbox.2026-11-14.log`:
- The worker wrote files freely from 06:00, then every write failed from about 06:10, inside ONE session.
- Codex keeps a per-workspace capability SID in one shared file, `~/.codex/cap_sid`. The log shows "granting
  write ACE ... for sandbox group and capability SID" on the d01 worktree four times (06:00:02, 06:02:44,
  06:10:16, 06:10:27); the worktree dir carries four explicit SIDs.
- The two SIDs now stored for that worktree are on the worktree DIR and on none of `static/`, `app.js`,
  `styles.css`, `index.html`; those carry the two earlier SIDs. So the SID was re-minted mid-session and the
  new grant was not propagated to existing children: old files and subfolders deny the new token.
- Not the cause: read-only attributes (Archive only), git locks, worktree location, writable_roots (cwd is
  granted each time), a prior attempt's leftovers (first call, empty checkout).
Inferred, not proven: the store entry is lost when concurrent Codex processes rewrite `cap_sid` (five streams,
plus parallel units inside one run: d03 u001 and u003 refreshed within the same second and both hit it). That
matches "once in g05, 2 of 5 since the 5-stream cohort" and why the T-139 git lock did nothing.
**Smallest fix (Lane D, `providers.py`, one line):** workers on Windows run without the Codex Windows sandbox
(the mode in which the log prints "Windows sandbox selection: disabled"). Scope stays enforced by Seldon from
the observed diff (R6) and proof runs in disposable checkouts. This widens what a worker process may touch, so
tell Oren at the next check-in; it fits his 10-11 "basic security" and 10-12 "confinement optional" rulings.
No Seldon-side heal is reliable (files are owned by the sandbox user). Also: report upstream; a no-LLM repro
(two parallel sandboxed command loops in two folders, watch `cap_sid`) would settle the inferred half.

**8.2 d02 u005 — the Rule 3 wall, confirmed, nothing new.** n042 `checks/delivery/helper_behavior.py` passes at
T and wave start; the worker ends by asking Seldon to change the registered mode (r455). d05 u004 hit the same
wall (r396, r413) and got through on its second recovery. Evidence is now c04, d02, d05: Lane C is the top
planner-side blocker and waits only on Oren.

**8.3 d04 DETAIL — DESIGN, family *Two rules disagree*. Exposed by Rule 1; one part is my Lane B omission.**
Three refusals stacked on the `handoff` area:
(a) its unit check cited consumed contract handles (Rule 1's wording invites that); `plan.merge` links provider
requirements to ANY check naming a contract and `normalize_checks` then promotes it to wave, so
`validate_owned_work` said "needs a local semantic check" (r67);
(b) ARCHITECT named handoff a consumer of `inventory-query`, the area does not need it, and merge refuses
"bind every named consumer" (same refusal recovered in d02 r263 and d05 r256);
(c) `detail.py` still allows one `detail_correction` per revision (a count); (a) spent it, (b) went to the user.
I fixed that guard for contract gaps and missed its twin.

**8.4 d05 u002 — DESIGN, a hole in Rule 1 (not a regression of its mechanics).** n020 is correctly `wave` and ran
on the integrated commit at final verify. It failed because it expects `SELDON_BASE_URL`: the interface area
consumes the HTTP contracts but not `server-command`, so under "a check reaches only through contracts its unit
consumes" its planner forbade launching the server and assumed Seldon supplies a running product. Seldon runs
checks as plain commands; nothing is running. Same hole, planner-recovered: d03 r66, d05 r62 ("supply a consumed
contract handle covering server startup"). The fixup then went to u002, whose plan text forbids the only fix.

**8.5 Amendments (one lane, E) — two rules, both normalise instead of refuse**
**Rule 1a. Nothing is running: a wave check is an ordinary command on the integrated checkout that starts what
it needs and stops it.** One fact in "How the plan executes" (it is a code fact that was missing).
**Rule 1b. Consumers are derived from binding, never refused.** ARCHITECT names each contract, its text and its
provider; an area that binds a contract is its consumer, a named consumer that does not bind it is not one.
Changes: DETAIL briefs list every contract (today only the area's endpoints, `detail.py` `relevant`); delete
the consumer half of merge's "bind exactly one provider and every named consumer" and the consumer-side
refusal in `architecture.local_plan`; the compiled contract's consumers are the units that bound it. With 1b
the interface area simply binds `server-command` and launches the server; no ARCHITECT round trip.
**Declared level decides (8.3a):** merge links provider requirements only for checks declared `wave`; a unit
check may cite consumed contract text and stays unit. **Fixed point for corrections (8.3c):** the
`detail_correction` guard raises only when the same corrections come back, as the gap guard now does.
Files: `plan.py`, `architecture.py`, `detail.py`, `questions.py`. Delete first: the two consumer refusals,
the per-revision correction count. Journeys (outcome only): replay d04's recorded DETAIL -> reaches B with no
user question; replay d05's plan with a stub worker whose wave check launches `server.py` -> final verify
green; twin where an area binds a contract ARCHITECT did not assign to it -> compiled consumer list includes
it and its WORK brief carries the text; two different corrections in a row both return to the area. Stated
cost: every DETAIL brief grows by the contract list; measure it (P11), never cap it.

**8.6 Lane order.** D (T-136, `providers.py`) and E (amendments) now, in parallel, disjoint files -> cohort m2e.
C (Rule 3) the moment Oren answers; it shares `questions.py` with E, so after E. Small separate ticket seen in
d05: the guide format check read a URL as a path ("docs/http:/127.0.0.1:8000", fixup r490).

## 9. Cohort m2f on 260584f (3/5 C, oracle 36/37/39 vs native 36): the two walls and the oracle residue
**9.1 f01 u003 (UI) — DESIGN: a missing route, not a bug.** Family: *Blame lands on wrong owner*.
Contract `expiry-and-search` says "today means the server machine's local calendar date" and "Expired means
expires < today"; `items-http` gives a consumer no way to learn that date. The UI either uses the browser date
(judge gap r211) or invents `X-ShelfLife-Today` (judge gap r244). Both verdicts are right. The fault is in
agreed text, and a WORK discovery can only name a unit (schema.py WORK `owner`), so the unit pays three times.
**Rule: a fault in agreed text goes to the planner as one bounded contract question; the unit that found it
spends nothing, and only a change to an accepted commitment goes to the user.**
**Route — yes, the smallest correct one is discovery -> contract correction, not full M3 steering and not a
re-run of ARCHITECT + DETAIL** (that re-merges areas and renumbers handles under DONE units). Shape:
- WORK discovery `owner` may also be a contract handle the unit consumes.
- Code asks ONE question (planner tier): the need in the worker's words, the contracts that unit consumes, each
  provider's responsibility. Answer: `[{contract, text}]` plus a decision, or `user` when the fix would change
  an accepted commitment (C16).
- Code stores a revision with those texts replaced in place (handles stable) and the decision recorded; shown
  at the next check-in (blueprint 3.2 already lets Seldon change contracts).
- Stale-marking reuses what exists: a DONE provider gets the present `blocked` handoff fixup
  (`fixups.handoff`) with the new text as its correction; a provider not yet started just reads the new text;
  the discoverer returns to WORK with recoveries untouched.
This is the "corrects a contract" branch of unit steering, built where STEER will sit, so M3 extends it.
**Lane G.** Files: `schema.py`, `units.py` (`work`), `questions.py` (one brief), `fixups.py` (reuse handoff),
`plan.py` (replace contract text). Delete first: the path where a self-owned `blocked` discovery spends a
recovery (it never changes on retry; it goes straight to the unit question). Journeys: (1) twin, consumer
worker reports a contract discovery, the provider is DONE -> provider fixed once, discoverer DONE with zero
recoveries, run reaches C, check-in lists the contract change; (2) provider not started -> no fixup, its brief
carries the new text; (3) answer `user` -> WAITING with that one question; (4) replay f01 to r211 with a
stubbed contract answer. Net src will NOT fall here (about +30): it is a new capability; say so at landing.
Known loose end: requirement bodies copy contract text (n021 "Provide static-entry: ..."), so a corrected
contract leaves stale copies in prose. Ticket under *Questions copy everything*; briefs must show the contract
node as the authority.

**9.2 f04 u004 (delivery) — DESIGN, the Rule 3 risk I named.** Family: *Judge asked beyond its view*.
n026 ("server, UI and importer work together from a fresh folder") is provable only by wave check n028; the
unit's local check n027 tests helpers and passes at T. The JUDGE is asked `baselineDemonstrated` for n026 with
no RED-capable observation in its facts and answers False three times (r214, r293). It is right on its facts.
**Rule: a check's RED is observed by its owner's PROVING at the level it can be observed: a unit check at T,
a wave check at wave start. GREEN for a wave check stays at WAVE-VERIFY.** C14 holds ("observed"); the JUDGE
prompt already reads "RED output at T or wave start", so no prompt sentence is added.
**Lane F.** `proof.py` `prove`: add the unit's own wave checks to the existing wave-start observation
(`gitwork.check_commit` is already there); never run them at T or P. `units.py`/`questions.judge_brief`: the
unit JUDGE's `Checks` fact includes those wave declarations so the rows are readable. Replace, not add, the
UNIT_EVIDENCE sentence "Wave checks are written here and first run by Seldon on the integrated product".
Journeys: (1) replay f04 u004 from its recorded patch: n028 fails at wave start (product absent), JUDGE stub
that requires one RED per requirement answers satisfied, unit DONE with no recovery; (2) later-wave twin where
the wave check passes at wave start -> recorded as preserving, no refusal; (3) 50-unit journey unchanged.
Net src about +5. Cost to measure (P11): one extra run per owned wave check per proof; a check that waits for
a server that is not there should fail on its own readiness bound, never on a Seldon number.

**9.3 Oracle residue (rig, `work/fight-1/oracle_ui.py`) — both delete failures are oracle BUGs.**
- f02: delete is a two-step in-page confirmation ("Yes, delete"); the oracle only auto-accepts
  `window.confirm`, clicks once and waits.
- f03: the oracle clicks Delete while the row is still pending from the consume it just proved (its own
  evidence shows the button text "Using..."); `mutateItem` ignores clicks on a pending item.
Fix, contender-neutral: wait until the control is enabled before clicking; after the click, if a confirm
control appears in that row, click it. Re-score f02, f03, f05 and native.
- Focus ring on the date input (f02, f03): undetermined. f05 also uses `type="date"` and passes, but the oracle
  tabs only eight times and may never reach it there. One manual Tab in Edge on f02 settles product vs oracle.
- f02 "UI search" (list not restored after clearing): one run, not triaged.

**9.4 Lane order.** Oracle fix now (rig). F first: small, one file group, unblocks every delivery-style unit.
G second: larger, shares `units.py` and `questions.py` with F, so after F lands. Then cohort m2g.

**9.5 g02 u004 on 9a5d6c0 — DESIGN, one field. Family: *Judge asked beyond its view*.**
RED now works (baselineDemonstrated True). The JUDGE answers `exercisedAtP: False` for n029 because its
substance is proven by wave check n031, which by design has not run at P (r237, r297), and its correction asks
for what WAVE-VERIFY does anyway. The judge is honest; the question is wrong. `exercisedAtP` is a judge boolean
about whether something ran, which R12 already forbids ("whether something ran is a code fact, never a judge
boolean"): code knows every unit check exited 0 at P (PROVING fails otherwise), and "skipped, empty, asserting
nothing" is what `meaningful` asks.
**Rule: the unit JUDGE is not asked whether a check ran. Code states what ran; the judge says whether it means
anything.** Delete the field; do not derive "wave-only targets", do not mark them, do not filter gaps by their
wording (each of those is a special case standing in for one wrong question).
**Exact change (about 6 lines, net -1; small enough for the lead directly):**
- `schema.py:110`: drop `exercisedAtP=flag` from the JUDGE requirement assessment.
- `questions.py:172` (`assessments` example): drop `"exercisedAtP": True`.
- `questions.py:430` (`satisfied`): require `a["baselineDemonstrated"] is True` only.
- `questions.py` JUDGE prompt, same length: "are its checks meaningful; did they actually exercise the
  requirement at P (not skipped, not empty, not asserting nothing)" becomes "are its checks meaningful: they
  exercise the requirement, not skipped, not empty, not asserting nothing".
- `questions.py` `judge_brief`, the existing "Checkout coverage" fact: add that an owned wave check shows its
  RED here and its passing run at wave verify (a fact edit, no new prompt sentence).
- Test fixtures and recorded JUDGE answers that carry `exercisedAtP` lose the field (test-only).
Journey: replay g02 u004's recorded JUDGE answer r237 with the field removed -> `satisfied` is still False
only because the recorded answer says verdict "gap"; a stub JUDGE given the new brief answers satisfied and the
unit reaches DONE with no recovery. Not verified: that the real JUDGE stops writing the "run n031 at wave
verify" gap once the boolean is gone. If it still does in the next cohort, the next move is the fact wording
in "Checkout coverage", not a gap filter.
