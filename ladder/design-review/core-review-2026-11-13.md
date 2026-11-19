# Seldon core simplicity review, 2026-11-13

Main `60bef4f`. `src/seldon`: **4,277 lines, 24 files**. `tests/seldon`: 3,896 lines of Python, 8 test functions.
Binding: CHARTER v1.7, BLUEPRINT v1.6. Read-only review; every `src` file read in full, tests read by structure.
**[LANE]** = already the intent of check-owner / owner-repair (Rule 1). Note: `check-owner.patch` also edits
`architecture.py` and `plan_review.py`, which are not in the "changing now" list.

## 1. Cross-cutting findings, by value

**F1. Reads grow with the square of the product (will not hold at 50-500 units).**
- `store.py:210` `plan()` decodes the whole plan JSON on every call; it is called in almost every function and inside
  loops (`flow_review.py:138` calls `evidence()` once per requirement). Revisions are immutable: cache by id.
- `cursor.finalObservations` is scanned with one `store.read` per ref, per subject: `judgment.py:32,47,170,218`,
  `flow_review.py:23`, `run.py:37`. At 1,500 checks that is millions of JSON decodes of stdout-bearing records.
  One `{check: ref}` / `{unit: tree}` index built once per final commit removes all six scans.
- `plan.py:382` `prerequisites` rebuilds the unit dict per call; `scheduler.py:21` calls it per unit per pass,
  `units.py:33` per unit per closure round. `scheduler.py:16` also decodes and type-checks every unit row per pass.
- `store.records(kind)` full scans per unit: `fixups.py:39,54`, `units.py:48` (every provider reply with its raw
  answer, to find one attempt), `detail.py:10,58,138`, `plan_review.py:58,132`.
- B stores the plan three times and compares whole documents instead of the revision id: `run.py:137`,
  `decisions.py:41`, `run.py:168-170`, `judgment.py:156-159` (repeated on every FLOW and PRODUCT step).
- No worktree is ever removed: `gitwork.py:38-41` adds one per unit start, per REWORK without worktree and per
  observer thread (`proof.py:27-30`); nothing calls `worktree remove`.
- FLOW and PRODUCT questions are asked serially (`flow_review.py:191`, `judgment.py:214`); planning is parallel.
  100 features at a 300 s timeout is hours. Integration holds one lock while checks run (`units.py:125`, T-32).

**F2. "Uncertain, re-ask once, else not judged" is implemented four times in four shapes.**
`inference.py:73-81` (JUDGE, inline), `plan_review.py:69-93` (REVIEW, inline), `flow_review.py:96-103,170-189`
and `judgment.py:195-212,228-234` (durable, through run states). The durable form costs two run states
(`states.py:23,26`), `pendingJudge`, the `judge_uncertain` record, `max_bytes` and a twice-built brief, to protect one
LLM call against a crash. One rule in `inference.call` (a `more_facts` callback, one inline re-ask, then "not judged")
deletes the states and about 70 lines. Requested-facts text is duplicated verbatim: `flow_review.py:74-79`,
`judgment.py:96-102`.

**F3. Two parallel final-judgment stacks.** `flow_review.step` (55 lines) and `judgment.step` (62 lines) are the same
loop: prune stale verdicts, resolve pending, ask per subject, gap to fixup, save, combine. Blueprint 3.2 says flow
review is the only cross-unit judge and replaces the PRODUCT stand-in; PRODUCT-JUDGE is still a second one (DV6).
A quality criterion is a subject with traced checks exactly like a feature. One subject loop removes
`PRODUCT-JUDGE`, `PRODUCT-FACTS`, `qualityVerdicts`, `productVerdict`, and the half-generic `kind` plumbing in
`judgment.py:11-27,134-150,188` (`kind` is always "PRODUCT", `field` always "qualityVerdicts"). Lead decision.

**F4. The guide is a pseudo-unit with about 14 special cases.** `ref == "guide"` / `tryItGuide` branches:
`obligations.py:7`, `plan_review.py:12`, `plan.py:340,386-397`, `wave_verify.py:18-30`, `units.py:172-177`,
`proof.py:99`, `judgment.py:14-16,20,25-26,69,88-91,164`, `questions.py:291-297`, `run.py:38`. Root gap: the guide has
no requirement, criterion or planned check, so every consumer invents one. Fix once in `plan.add_guide`: code adds one
requirement and one criterion node for it; subjects, owners and trace then need no branch. `wave_verify.py:24-30`
fabricates an observation with `exitCode None` to carry a format refusal; `guide.py:16-17,24-25` refuse a guide
without links or with a non-argv fence. Normalise: no links means no path probe; other fences are prose.

**F5. The same plan rule is written two or three times.** `architecture.local_plan` (per area), `plan.merge`
(cross-area), `plan.validate*` and `architecture.validate` (canonical) each restate it; every area answer is validated
in `detail.py:76`, again in `plan.py:151`, again in `plan.py:126`.
- one file owner / reads need an edge: `architecture.py:82-91`, `architecture.py:204-220`, `plan.py:248-282`
- concrete-file test (`"*" in path or "?" in path`, misses `[`, T-73): `architecture.py:84,172,208`
- contract binds one provider and all consumers: `architecture.py:63-74,174-180`, `plan.py:210-224`
- scope overlap: `architecture.py:123-125`, `plan.py:259-264,342-346,370-374`
- obligation owner: `obligations.py:11-14`, `architecture.py:151-155`
- ancestor-to-area contract projection, identical code: `detail.py:48-54`, `plan.py:144-150`; the same participant
  filter again at `questions.py:226-228`, `plan_review.py:31-33`
- evidence on the final commit: `flow_review.py:23-27`, `judgment.py:47-50`, `run.py:37-43`
- unit verdict still current: `flow_review.py:33-38`, `judgment.py:54-59,163-169`
- B is for this exact plan: `run.py:167-171`, `judgment.py:156-159`
- negative assessment means gap: `questions.py:389-394`, `inference.py:64-66`, `flow_review.py:105-110`
- reset-field lists: `units.py:21-23`, `fixups.py:74-77,111-112,119-120`, `store.py:200-207`

**F6. Leftover of the single-call PLAN (T-105 fixed, shape kept).** `plan.merge` builds an LLM-shaped answer with
1-based positions, then `plan.create` (`plan.py:89-127`) translates it to handles and validates against
`schema.PLAN` / `PLAN_BODIES` (`schema.py:44-56`); `questions.example_plan` (`questions.py:177-193`) exists to feed
`example_detail` and tests. No LLM writes this shape any more. `merge` should write nodes directly.

**F7. Refusals that should be normalisations or steering.**
- `plan_review.py:150-151`: three repairs exhausted ends the run. C11 says about three rounds, then Seldon decides:
  go to B with the open gaps shown.
- `detail.py:14-19` stops planning after one re-ask; `Run.resume_planning` (`run.py:198-210`), the
  `INCOMPLETE -> DETAIL/ARCHITECT` moves (`states.py:29`), `planning_stop`, `planning_resume` and `resume_id`
  exist only to restart it by hand. Only tests call it. A terminal state that is not terminal.
- `questions.py:102-107`: the 64 KB limit that Blueprint section 5 lists under Drop. `judge_brief` sends whole product
  files at P and the diff (`questions.py:344-346`), so a real unit hits it (T-56). [LANE makes it retryable; the
  limit and the double payload stay.]
- `inference.py:82-83`: an uncertain ALIGN, ARCHITECT, DETAIL or WORK ends the run; ALIGN's needed facts are a
  question for the user (C8). `decisions.py:35-39`: "unclear" ends the run instead of asking again.
- `providers.py:208-213`: "denied" by substring ("login", "log in", "forbidden") over stderr and events makes a
  failure permanent; any worker output containing those words turns a transient loss into FAILED.
- `fixups.py:17-21`: key-set validation of dicts that only code builds. [LANE]

**F8. Prompts and semantic constants outside `questions.py`.** `flow_review.py:67-72` (T-103; FLOW borrows
`answer_schema("DEMO")`, while `PROMPTS["DEMO"]`, its example and its "Judge coverage" line at `questions.py:84-87,
138-139,157` are dead), `plan_review.py:51-52,78-81,87`, `plan.py:11-16`, `providers.py:75-78` (browser how-to;
Playwright and Edge discovery in the provider module breaks I7), `providers.py:128-131`, `units.py:108`,
`fixups.py:113`, `judgment.py:15,68-73`, `schema.py:59-61,94-99,154`. `questions.py:115-141` is a 20-line paragraph
that is a history of patches (R12).

**F9. Dead or test-only code in the core.**
- `store.py:188,192-207` stale-marks consumers on a new revision, but revisions are only written before B, when no
  unit exists; with it `architecture.py:94-97` and `run.py:46-47`. It is C10 work for M3, placed in the store, which
  therefore imports `judgment` and `architecture`.
- `judgment.py:170-180` re-judges a unit whose scope tree changed after integration; scopes are disjoint and enforced
  from the diff, so only a test that injects it reaches this. With it the `commit, observations` parameters of
  `questions.judge_brief`.
- `store.py:95-96` compatibility default for old runs (I9: never kept for compatibility).
- `inference.py:11` `retries` never passed; `inference.py:25,41,47` two provider protocols via `hasattr`;
  `providers.py:176-177`; `providers.py:28,111` unused `context`; `providers.py:16` role "worker" unused.
- `gitwork.py:78` `named`, `gitwork.py:81` `if entry`, `gitwork.py:167` `scratch` unused.
- `decisions.py:23-28` a dict reply path beside the LLM path; `providers.py:82` hard-codes `scriptedUser: True`.
- `architecture.py:43-44` `area_decisions` has no caller.

**F10. Functions over about 40 dense lines.** `processes._run_process` 219 (292-510), `plan.merge` 168 (136-303),
`detail.step` 127 (T-110), `architecture.local_plan` 86, `processes._run_portable_process` 82, `run.Run.step` 76,
`inference.call` 74 with three closures, `judgment.step` 62, `judgment.brief` 61, `providers.Codex.prepare` 60,
`questions.build` 58, `proof.prove` 57, `units.run_unit` 57, `flow_review.step` 55, `proof.observe` 51,
`scheduler.execute` 46, `decisions.decide` 43.

**F11. Tests.** `test_journey.py` is 1,995 lines: 360 lines of base64 fixtures (1450-1810, T-101), a 200-line Python
program in a string (125-323), a 205-line scripted provider (324-528) and a 216-line `simple_journey` switching on 61
mode predicates. `test_architect.py`, `test_review.py` and `test_proof.py` hold no test function; their journeys run
only inside `test_clean_core_golden`, so one failure hides about 70 journeys and nothing can be selected or run alone.
Seven places write the cursor directly instead of driving the run.

## 2. Modules

| Module | Lines | One responsibility | Findings |
|---|---|---|---|
| processes.py | 537 | Bounded process lifetime | Bootstrap interpreter, gate pipe and status protocol (17-46, 311-427) exist to place the child in the Job before it runs; each check pays a second Python start. A suspended start, assign, resume does the same. Blueprint section 5 says Keep: lead decision. T-99 lives here. |
| plan.py | 397 | Plan records, scopes, merge | F5, F6; `merge` 168 lines; owner by argv pattern `75-80` and first-superset `57-65` [LANE]; F1 `382`. |
| questions.py | 394 | Briefs and prompts | F7 64 KB, F8, dead DEMO; `build` mixes prompt, facts, examples for nine kinds. |
| architecture.py | 260 | Area and contract rules | F5 (35 raises, three validators); `area_decisions` dead; `stale_consumers` unreachable. |
| judgment.py | 244 | PRODUCT subject judgment | F2, F3, F4; `170-180` unreachable; six observation scans. |
| store.py | 240 | Typed durable state | F1 `plan()`; F9 `187-208`, `95-96`; cursor carries four growing ref lists. |
| run.py | 224 | Run loop and C eligibility | `step` if-chain 76 lines; `eligible` restates F5 checks; `137` plan inside B subject; `141` "DV6" literal in a user subject. |
| providers.py | 221 | Codex calls | Command built twice `139-149`; F7 denied; F8, I7 `59-82`; dead role and params. |
| gitwork.py | 211 | Git snapshots, worktrees | No worktree removal; three caches for scope trees (99-128): a unit's last integration commit is the same identity, cheaper; unused params. |
| flow_review.py | 209 | Flow judgment | F2, F3, F8; `138` per-requirement `evidence()`; `105-110` duplicates `satisfied`. Flow gap owners [LANE]. |
| units.py | 205 | Unit lifecycle | `run_unit` 57 lines; `48` reply scan; `43-64` two recovery sources for one report; guide branch `172-177`. [LANE edits] |
| plan_review.py | 164 | Plan review | F2; F7 `150-151`; prompts inline; `132-133` re-finds the architecture review by rebuilding its brief. |
| schema.py | 164 | Answer schemas, validator | F6 `44-56`; `bounded` applied twice (89-90, 126); prompt text in `59-61`; DEMO and PRODUCT schemas identical. |
| proof.py | 162 | RED/GREEN by code | `prove` 57 lines, reads the same record up to five times (127-147); import inside function `107`. |
| detail.py | 160 | Per-area DETAIL | T-110; five record kinds of re-ask bookkeeping (`area_detail`, `detail_correction`, `review_repair`, `architecture_gap`, `planning_stop`); F7. |
| fixups.py | 121 | Local rework admission | `checks_for` mode flip, handoff path lookup, gap dict validation: all [LANE]. Lazy import of `units` `97`. |
| inference.py | 84 | One recorded call | F2; `validate` holds per-kind verdict rules that belong with the kinds; `hasattr` protocols. |
| states.py | 62 | Transition tables | Loses 4-6 states with F2, F3, F7. |
| decisions.py | 58 | Gates | Writes the C outcome and imports `run` and `judgment` lazily (46-56); that is the run's job. |
| scheduler.py | 55 | Waits and dispatch | F1; `47-50` busy-continue when a unit was blocked this pass. [LANE edits] |
| wave_verify.py | 39 | Final observation | F4 `18-30`; a pool per call. |
| guide.py | 35 | Guide to checks | F7 refusals. |
| obligations.py | 30 | Skeleton obligations | Fine; guide filter `7`. |

## 3. Top 10 changes, by lines deleted plus risk removed

| # | Change | Where | Lines | Risk removed |
|---|---|---|---|---|
| 1 | Cache `plan()`; one observation index per final commit; precompute prerequisites; B by revision id | `store.py:210`, `judgment.py:32,47,170,218`, `flow_review.py:23`, `run.py:37,137,168-170`, `plan.py:382`, `scheduler.py:21` | -25 | Quadratic reads at 50-500 units |
| 2 | One uncertain rule in `inference.call` | `inference.py:73-83`, `plan_review.py:69-93`, `flow_review.py:96-103,170-189`, `judgment.py:195-212,228-234`, `states.py:21-26` | -70 | Four divergent protocols, two states |
| 3 | Quality criteria as flow-review subjects; delete the PRODUCT stack | `judgment.py:134-150,184-244`, `flow_review.py:155-209`, `states.py:20-26`, `store.py:41-44` | -120 | Second cross-unit judge (Blueprint 3.2) |
| 4 | Guide gets a code-made requirement and criterion; delete its branches; normalise format | F4 list; `guide.py:16-25`, `wave_verify.py:18-30` | -45 | The T-83/T-96/T-112 class |
| 5 | Each plan rule once; `local_plan` and `merge` call the canonical validators; one contract projection | F5 list; `architecture.py:136-221`, `plan.py:136-303` | -80 | Rules drifting apart; `merge` 168 lines |
| 6 | `merge` writes nodes; delete `create`, `PLAN`, `PLAN_BODIES`, `example_plan` | `plan.py:89-127,298-301`, `schema.py:44-56`, `questions.py:177-207` | -55 | A dead intermediate format |
| 7 | Suspended start in place of the bootstrap protocol | `processes.py:17-46,292-510` | -200 | T-99; an interpreter start per check |
| 8 | DETAIL: no manual resume; exhausted corrections go to B labelled; split `step` into ask / collect / merge | `detail.py:9-33,35-160`, `run.py:72-78,198-210`, `states.py:29`, `plan_review.py:150-151` | -60 | T-110; a run that ends on a plan gap |
| 9 | Delete dead and test-only code | F9 list | -45 | Store importing judgment; two provider protocols |
| 10 | All prompts in `questions.py`; FLOW a real kind; drop 64 KB and the double source payload; remove worktrees at DONE | F8 list; `questions.py:84-87,102-107,115-141,344-346`, `gitwork.py:38-41` | -20 | T-103, T-56, disk growth |

Not counted above: `test_journey.py` fixtures to JSON files, the native stub to its own file, one pytest case per
journey (T-101): about -560 lines from that file and local failures.

## 4. Lane batches

Parallel batches have disjoint file sets. A, B, C can start now; D to G wait for check-owner and owner-repair to land.

| Batch | Files | Changes | When |
|---|---|---|---|
| A scale reads | `store.py`, `gitwork.py`, `proof.py`, `wave_verify.py` | 1 (store side: plan cache, observation index), F9 store items, worktree removal, `prove` re-reads | now |
| B process | `processes.py` | 7 | now, after the lead's decision |
| C provider call | `providers.py`, `inference.py` | F9 provider items, one protocol, command built once, denied rule, the single uncertain rule (callee side of 2) | now |
| T tests | `tests/seldon/*` | T-101, per-journey cases | now; rebase after the lanes |
| D planning | `detail.py`, `plan_review.py`, `architecture.py`, `plan.py`, `schema.py` | 5, 6, 8 (planning side), T-110 | after lanes |
| E final judgment | `judgment.py`, `flow_review.py`, `run.py`, `states.py`, `decisions.py`, `obligations.py` | 2 (callers), 3, B by revision, C outcome into run, `eligible` reading the index | after lanes and A, C |
| F briefs | `questions.py`, `guide.py`, `scheduler.py`, `units.py`, `fixups.py` | 10, scheduler precompute, reply scan | after lanes |
| G guide | crosses D, E, F | 4 | last, alone |

## 5. Target

Current 4,277. The lanes add about 160. Changes 1-10 remove about 720 (520 without the process change).
**Target about 3,700 lines of `src/seldon`** (about 3,900 if `processes.py` stays), no file over 400, no function over
60. R14: the total is reported, not targeted; the count is the result of deleting the duplicates above.

## 6. Not verified

Nothing was run. F9's two "unreachable" claims (`store.py:192-207`, `judgment.py:170-180`) come from reading the
transition table and scope rules; confirm with one journey before deleting. Line savings are estimates.
