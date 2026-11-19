# Is Seldon going the wrong way? Honest review (Fable, 2026-11-15, main b95331c)

Read-only. Basis: CHARTER v1.8, BLUEPRINT v1.10, `src/seldon` (4,943 lines), tickets T-124..T-178, all 652 recorded calls of the ten
Terra runs `shelflife-b7b613a-t01..t05, u01..u05`, speed-data 11-14 (Sol runs), my own five design reports. No provider calls, no tests.
Yardstick (Oren): a head coach puts the QB in the best position to succeed; he does not referee every throw.

## Short answer
**Correct course, do not restart.** The core idea is right and about half the code is good. But since 11-13 Seldon has drifted from
coach to referee, and I pushed it there. "Determinism owns structure" quietly grew to mean "code and judges police a plan grammar that
Seldon invented". The models now spend most of their calls satisfying Seldon, not building the dream. That is the old-core pattern
starting again, one layer up: then we patched mechanics, now we patch rules about plans, checks and judges.

## 1. Guiding or handcuffing? Evidence
Ten Terra runs, 652 calls, none reached C:

| What | Count | Meaning |
|---|---|---|
| DETAIL + REVIEW (planning) | 409 calls (63%) | 3.7 planning calls for every WORK call, on a 4-unit app |
| DETAIL re-asked after code rejected the answer | 66 of 208 | the model is told "no" by the plan grammar |
| REVIEW answers with a gap | 89 of 201 (44%) | a model refereeing another model's plan before any code exists |
| WORK calls that are reworks | 60 of 111 (54%) | more than half of building is redoing |
| WORK answers `blocked` | 51 of 111 | the worker's main message to Seldon is "I cannot satisfy you here" |
| JUDGE answers negative | 38 of 57 (67%) | two throws out of three are flagged |

What the questions look like:
- **DETAIL** (planning one area): a 1,965-character prompt of about 29 rule clauses, 15 KB of facts, a 6.7 KB schema, and one
  hello-world example. Sample: *"Wave check: one real path per contract crossed, asserting agreement only; repeat no unit state or
  edge case."* It also carries a 1.3 KB fact "How the plan executes", which is Seldon's internals explained to the model so it can
  plan around them. Behind it sit about 60 distinct code refusals (`plan.py`, `architecture.py`), e.g. *"Local requirements must name
  this area's requirement handles"*. Blueprint R12 says a fix never becomes a new prompt sentence. This prompt is a history of fixes.
- **JUDGE**: 31-55 KB per call, and the question is open-ended: *"is anything a stub, mock or missing?"* "Missing" has no boundary, so
  the judge always finds something. Real example (u01): the contract says "quantity (integer >= 0)"; the judge failed the unit because
  values above SQLite's 64-bit range were not stored. The worker then **added support for quantities beyond int64 to a pantry app**.
  Next round the judge found "out-of-range id must be 404". The product got more complicated and no better. The oracle sees none of it.
- **REVIEW**: asks whether the plan's *proof design* is enough, before a line of product exists. Typical gap: *"Extend the interface
  check ... keyboard-only navigation at 375px and desktop widths"*. Each such gap makes the planned check heavier, and the worker
  inherits a test specification written by someone who has not seen the code.
- **WORK** is the one well-coached question: 922-character prompt, about 9 KB of facts, the contracts, a browser kit. But it runs in a
  worktree with no peers, is handed planned checks it cannot fully run there, and is offered `blocked` as an answer. So it says blocked.

**Weak model or bad questions?** Both, but mostly the questions. Terra's int64 reading is a model limit (4 of 5 runs). But only an
unbounded question lets that limit stop a run. Sol shows the same shape with less noise: before S2 its runs spent 5-9 min planning;
after my "proven once" rules, 15-28 min and 37-70 calls. Tickets T-130..T-178: about 25 of 49 are Seldon's own plan/proof/judge
rules colliding with each other, about 15 are rig or provider, **2 are about the built app being wrong** (T-148, T-151). We are
debugging Seldon's rulebook, not dreams.

## 2. Is the code growth a wrong core idea?
The core idea is sound. The growth comes from one wrong extension of it. Since 11-09: 8,004 lines added and 4,841 deleted to stand at
4,943, and the churn sits in `questions.py`, `plan.py`, `judgment.py`: exactly the referee layer.

| Bucket | Files | Lines | Coach or referee |
|---|---|---|---|
| The field: store, states, processes, providers, claude, inference, gitwork, scheduler, run, frontdoor | 10 | ~2,030 | neither; essential, stable, keep |
| The scoreboard: proof, wave_verify, units, recovery, decisions, guide, obligations | 7 | ~660 | essential: code observes RED/GREEN on commits. A score is not a referee |
| Plan grammar and its policing: plan, architecture, detail, plan_review, schema, questions | 6 | ~1,710 | about one third coaching (building briefs), two thirds refereeing |
| Judges and gap routing: judgment, flow_review, fixups | 3 | ~540 | flow review on the integrated product is essential; unit re-judging and gap routing are refereeing |

So about 2,700 lines are the charter's real guarantees (durable state, contracts, parallel worktrees, proof by code, never fails,
resume). About 1,000-1,300 lines exist only because the planner must write *checks, levels, proof maps and quality coverage* into a
strict grammar, and then two layers of models argue about it. That layer is the patch magnet.

**Against my own designs:**
- *speed-design S2 ("proven once", four check levels)*: right observation (3x more check code than product), wrong lever. I cured
  worker waste by adding planner law. Planning cost doubled and Terra copied my vocabulary into worker instructions.
- *plan-converge*: careful routing for a review loop that should not be that hot in the first place. Symptom work.
- *terra-u002 Rule 2*: +16 lines to tame a judge whose question is unbounded. Bound the question instead.
- *m3-steering* (change records, adoption, comparison table): machinery to protect expensive plans. If plans are cheap, replanning is
  cheap and most of it is unnecessary. It also builds M3 on an M2 that does not pass.
- *ui-split*: a design for a problem no run has shown. Park it.
- The blueprint's own header, "every rule exists because a real run failed without it", is the rule-per-misbehaviour engine, written
  down as a virtue. P9 (every failure a ticket, every ticket a fix) drives it at 15+ rules a day.

One more: ShelfLife is a 10-minute single-session app. Seldon splits it into 4 areas with contracts, then pays for every cross-area
problem that split creates. Blueprint section 2 says Seldon's value begins where one session fails. We are tuning the big machine on a
dream where it can only lose, and R1 already allows the fix: small = 1 area, 1 unit, same machine.

## 3. What a coaching Seldon looks like
| Coach does | In Seldon |
|---|---|
| Picks plays the QB can run | ARCHITECT defaults to the **fewest units**; it splits only where one session cannot hold the work or parallel work clearly pays. ShelfLife becomes 1-2 units |
| Short playbook | The plan is commitments -> (areas, contracts only when there are 2+ units) -> units with requirements. **The planner plans no checks**: no levels, proof map, peer checks or quality-by-position |
| Clear read | The worker gets requirements, contract text, and a real example of a good check for its surface, as skill files in the worktree, not as prompt prohibitions |
| Lets him throw | The worker writes its checks and says which requirement each proves. Code records them as trace nodes and observes RED/GREEN, as today. No `blocked` answer |
| Fixes footwork between drives | One unit judge, **closed question**: per requirement, delivered? exercised by a check that failed before and passes now? any stub? A gap must quote the requirement sentence it breaks. Anything else is a note. One rework, then integrate with any open gap shown |
| Watches the game, not each throw | The strict judging happens once, on the **integrated product**: WAVE-VERIFY, flow review per user flow, VALIDATE per commitment. This already exists and stays |
| One plan review | One review of the small plan: are all commitments covered? One repair. Leftovers shown to the user at B |

**Guarantees kept:** C1 (loop calls the LLM), C3/C4, C8 gates, C12/C13 units in worktrees, C14 observed RED then GREEN, C15/C26 proof
on the integrated product, C18 never stuck, C23 resume, the full trace walk. **Needs your words (I will not assume):** C9 says tests
are "planned semantically". My reading: the requirement's acceptance sentence is the semantic plan of its test; the worker writes the
check and code links it. And the unit judge stops being a gate after one rework; the gate is the integrated product.

**Delete:** check planning in DETAIL and its ~25 validation refusals; the per-area REVIEW loop; "How the plan executes", "Peer checks",
"Judge coverage", "Proof map" facts; open re-judgment; the `blocked` outcome and its routing; unit-stage contract correction;
source targets 3 and 4. Estimate: minus 1,000 to 1,300 lines, and the DETAIL prompt drops from 29 clauses to about 6.

**For weaker models:** do not tune the core to Terra. Terra-as-judge and Terra-as-reviewer generate most of the "no" above, and each
fix lands on every model. Terra writes code for simple units, with examples. Judges and the planner stay on the strong model (the
11-14 judge replay already said this).

## 4. Verdict and first moves
**Correct course.** Not a restart: the field and the scoreboard (~2,700 lines) are hard-won and right, and the old core died from
patching mechanics, which is not what is wrong here. What is wrong is one layer, and the fix is to delete it, not redesign it.

1. **The in-flight lane.** Lane A (Rule 1) **lands as written**: it is a deletion and it is coaching (a worker's "blocked" stops
   being a failure; only code proof counts). Lane B (Rule 2) **stops**: it is another patch on the referee. In its place I need one
   sentence from you: *"the unit judge runs once; one rework; an open gap integrates labelled and shows at check-in."*
2. **One experiment before any new rule (about a day, one lane): the thin plan.** DETAIL writes units and requirements only; the
   worker writes and maps its checks; one plan review; ARCHITECT prefers the fewest units. Run 5 Sol ShelfLife on it against today's
   main, same oracle. If the score holds at 36 or above and time falls toward 15-20 min, delete the check-planning layer. If quality
   drops, the layer earns its place and I am wrong. Either way a measurement decides, not an argument.
3. **Freeze the rulebook until that reads out.** No new prompt sentence, schema field or validation rule from a ticket. Pause the
   m3-steering and ui-split builds and Terra cohorts as a design driver. Change the P9 habit: a ticket's first question is "which
   rule can we delete so this cannot happen", and "what would a coach have told the model beforehand".

## Not verified
I ran nothing. I did not run the oracle on the ten Terra products, so I cannot say how good the apps were while Seldon was stuck;
workers reported unit checks passing in most. Line buckets are by file, so the coach/referee split inside a file is my estimate.
The ticket classification (25 / 15 / 2) is my reading of titles. The Sol planning figures come from T-172 and speed-data, not from
a recount. That the thin plan keeps oracle quality is a prediction; move 2 exists to test it.
