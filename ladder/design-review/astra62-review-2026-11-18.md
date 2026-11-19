## The one thing

Give the planner a way to change a disputed contract while the wave is still open.
Show it the failed observation, the agreement both sides used, and who can change each side. Let it revise the agreement within the approved scope.
Prove the change on ShelfLife u01. The API and page owners must deliver one agreed interpretation of “today” and pass the same user-path check.

## Contradictions and gaps, ranked

Source references are under `src/seldon/` at `a02ecb30e776731cba40011b80b8faaf08f4c23b`. The binding documents there are Charter v1.8 and Blueprint v1.12. Run labels below refer to the retained ShelfLife stores under `C:/seldon/tests/m1/`. An `r` number identifies a store record.

1. **A worker can discover that the agreement is wrong. It cannot get that agreement changed.** C16 and Blueprint §3.2 give the planner this move. COACH can give guidance or ask a question. Its guidance reopens the same unit. Even a FLOW gap that explicitly names a contract becomes a fix for its provider unit. The unowned-check branch can reach ARCHITECT, but a disputed contract with two known owners misses that branch. (`schema.py:75–85`, `decisions.py:64–88`, `judgment.py:143–152`, `run.py:201–209`.)
   In `a02ecb3-u01`, r374 tells the page owner to use server-local dates. At r421 the backend gets the request for an `X-Pantry-Today` header. At r510 the judge acknowledges passing checks and objects that the header is undocumented. At r513 the page owner gets the job again. The canonical API text still specifies server-local “today” and omits the header. At r516 the user gets Pause, Try again, or Leave this out. The missing decision is how the two components share a fact. The user already chose the date semantics.

2. **Area review can inspect the wrong team's work.** Charter §4 and R2 promise each area its own facts. SQLite serialization sorts node keys. The architecture keeps the planner's list order. REVIEW zips the two orders. Final commitment validation builds the same positional mapping. Equal lengths satisfy both zips. (`store.py:16–17`, `plan_review.py:15–25`, `judgment.py:15–22`.)
   In u01 the outline orders backend, interface, import. Stored area nodes order backend, import, interface. Question r40 gives the import reviewer the interface unit. Answer r52 reports the interface has no implementation owner. The same swap is visible in `deaad8d-r01` r38, `15682aa-s01` r36 and `b72a733-t01` r38. Join on the area handle already present on both sides. Reordering the saved outline must leave each named reviewer's units and each commitment's evidence unchanged. The REVIEW error was observed. The final-validation consequence follows from source.

3. **A repair can quietly retire a passing check.** C9/C15 and Blueprint §3.2 require every accumulated check to run on the integrated revision. Each WORK report replaces the unit's entire check list. Code numbers it afresh and links every listed check to every requirement the unit has ever held. Final eligibility compares the observations to this new list. (`plan.py:56–70`, `wave_verify.py:8–24`, `run.py:38–42`.)
   In u01 r149, check 1 runs `interface.cjs` and check 2 runs `import.cjs`. At r177, check 1 means `import.cjs` alone. At r302, it means `interface.cjs` alone. Judges r288 and r324 send the worker back for the alternating missing evidence. Both commands return at r346. Retain a check's identity and obligation across reports. Retire or replace it explicitly when the plan changes. A repair to import must keep exercising the original interface path.

4. **Changing accepted scope after B has no ordinary way back to B.** C8/C10 promise re-approval and continued delivery. ARCHITECT can send a scope change through ALIGN and A while the old B remains set. REVIEW uses the presence of B to select EXECUTE. EXECUTE then compares that old approval to the new vision and refuses it. The guard protects consent. The missing move is routing a changed vision to a fresh B. (`run.py:135–136,159–167,181–185`, `plan_review.py:38–39`, `plan.py:343–347`.)
   This is a source finding. The scope journey stops at the new A before any worker starts (`tests/seldon/test_journey.py:285–320`). The decisive case starts with wave 1 integrated. Approve a new commitment at A, inspect the revised plan at B, and observe the next worker use that approval while wave 1's commit survives.

5. **C answers two different questions about completeness.** C15 and R5 require every accepted commitment to be validated. R9 permits a small unproven requirement as a note. The prompt calls it a nit. Nits can yield “satisfied,” and `verification_complete` depends on the absence of “not judged.” Explicit uncertainty is visible, but a nit about missing evidence can coexist with complete verification. The front door also projects SCRIPTED_C as ACCEPTED while the outcome records `accepted=false`. (`questions.py:31–39`, `judgment.py:155–169`, `decisions.py:309–319`, `frontdoor.py:67–79`.)
   Let the user accept with a named evidence gap. Derive verification from which accepted obligations have evidence. Show the recorded acceptance origin. DV6 acknowledges the validation gap, but its M2 expiry and the C request's unconditional DV6 label give no usable exit test for M3. (Charter §8, `run.py:110–119`.)

6. **The largest recovery question arrives when the planner most needs a small one.** R2 promises that a question grows with its subject. Step-level COACH receives the entire execution plan, the vision, earlier directions and every user answer. Every WORK correction-owner menu grows with the run. In r01 the recorded COACH question was 38,376 bytes after just one closed wave. (`decisions.py:48–62`, `questions.py:306–322`, `m3d/r01.log`.) Start with the contested obligation, its endpoints and the last observation. The stored plan already supplies the rest if the planner needs a named fact.

7. **A milestone can pass without testing a class of dream the Charter explicitly promises.** C22 requires an agreed metric, iteration history and stop condition. Blueprint §6 leaves this as a later attachment. None of M1–M4 requires a run that improves a metric and then knowingly stops. Quiet Bench's deterministic measurements can test the generated app while Seldon's own planner never makes that decision. A cheap eventual exit is an unreachable target with an agreed plateau condition. The planner should show the best observed result and the reason to stop. (C22, Blueprint §6, `m3-lanes-fable-2026-11-16.md` §4.)

## The M3 bug pattern and its root idea

The shared assumption is that a valid record gives the next actor enough to act. The decisive test comes one step later. Can this receiver use that record, against this repository and plan revision, to change the outcome? Five failures expose different missing parts of that test.

| Run | What the next step actually received |
|---|---|
| m3a / n01 | The provider rejected Seldon's STEER schema before model execution. Its 400 names missing required property `areas` (r356). The simulated user kept picking Try again. T-201 reports 6,688 calls. Better model answers could not affect that request. |
| m3d / r01 | Call `cdf3f991` received two previous waves and one remaining wave. It returned one remaining wave. DETAIL indexed that answer as the whole history and failed before asking a wave-2 question (r378, r389). Current `architecture.py:91–111` retains the completed prefix. |
| m3e / s01 | A repair legitimately had no worktree. The Git lookup then used Seldon's working directory with a product commit. See r439/r450 and T-206. Current `questions.py:330` uses the product root. Neither the model nor its schema owned the directory choice. |
| m3f / t01 | The guide identified an absent importer. r198 assigns it to backend as the nearest available owner. r226 explicitly tells backend to leave that file alone. r253 assigns it back. The earlier design assumed a worker naming an owner settled who could make the repair. |
| m3g / u01 | The failed handoff survives even after Seldon can replan genuinely unowned work (r192). Here both owners exist. The header changes what they may rely on. The deferred unit judge sends that gap back to the unit under review (`units.py:213–222`). |

The convenient stub explains part of this. The 50-unit, five-wave journey supplies an ordered outline, independent value files and **zero contracts**. It exercises scheduling and restart while leaving cross-contract steering untouched. The recorded Git-state regression in `tests/seldon/test_journey.py:199` is closer to the failure boundary. Use the live record at the point of disagreement and inspect what the next owner actually receives. Keep the scale journey for its concurrency claim.

The five product incidents span several commits. The rig also logged a slot collision in m3b and an interrupted attempt in m3c. Only u01 ran on the reviewed commit.

## Core bets

| Bet | Decision | What earns its place and what should change |
|---|---|---|
| Schema-bound questions | **Keep.** | Typed choices let code own transitions and preserve exactly what was asked. Limit exact-fix requests to answers the model can correct. Today an arbitrary exception inside the consumer transaction can buy another model answer (`inference.py:94–110`). A store or controller fault needs a Seldon repair. |
| Contracts first | **Change.** | Parallel writers need an agreement before they start. Let either side challenge it with a concrete input on which two plausible implementations disagree. Give ARCHITECT authority to settle that case inside accepted scope and return the revised text to both owners. |
| Waves | **Keep.** | An integrated checkpoint gives the next planner a product it can inspect. Give STEER the unfinished horizon to edit. Code attaches completed history. A worker should be able to raise a contract decision before the wave can pass. |
| Code-observed RED/GREEN | **Keep.** | Exact commits, exit status and cleanup make a worker's claim independently observable. A missing peer can also turn a test red. Preserve what failed, on which base, and which user action became possible on green. Let the judge interpret that difference. |
| Separate judges | **Change.** | A fresh reader caught a clipped phone form in z09. Independence alone supplies no new facts. The tune set found 0/3 named defects and 0/15 false alarms on answered negatives. All three positives were unit JUDGE cases. For uncertain cases, spend the next call or check obtaining the missing observation. (`effic-astra-2026-11-16.md`, `judge-eval/report.md`, T-204.) |
| Planner before user | **Keep.** | u01's date convention was already settled. Route implementation choices to a planner with an actual plan-edit action. Ask the user when two feasible answers would change their accepted experience. Let unrelated units continue. |
| Never fail, only pause | **Change.** | Saved work should survive an outage or an engine defect. Record that the operation failed, what has to change, and who owns the next move. Resume automatically when the missing condition changes. A saved run and a useful next action are two separate claims. |

## New ideas and cheap tests

1. **Ask both ends of a disputed interface to predict the same observation.** Use one awkward input. For u01, set server and browser to different dates and put an item at the seven-day boundary. Ask each side what the user will see and which response field makes that possible. A disagreement gives the architect one concrete decision before another patch. On three archived contract incidents, give a reviewer only the pre-failure briefs and the paired predictions. Keep this if two causes can be located before coding at under one third of their recorded repair-call cost. Drop it if both sides keep agreeing on the same wrong answer.

2. **Measure whether the evidence contains the answer before tuning the judge.** For one known-good product and one deliberately broken copy, perform the same user action. Hide which is which. Ask a reviewer to distinguish the two using only the evidence Seldon would have sent. If the packets look identical, repair the observation first. Start with three reversible product edits in different surfaces and three unchanged controls outside the sealed holdout. Compare paired and single-case evidence on these same six cases. Keep the paired format if it distinguishes all three edits, preserves all three controls and finds a defect the single-case review missed. Drop it if both formats do equally well.

3. **Let a difficult boundary change the division of labor.** Compare two repairs of u01 from the saved pre-header candidate. In one, keep separate API and UI sessions. In the other, have one planner-authorized worker own both endpoints for one repair, after both prior writers yield. Keep the accepted behaviors and the independent integrated check identical. This challenges the whole-run path-owner rule and would need ratification. Try it only as a development experiment. Keep it if the same date-boundary check passes at one third of the worker time with no unrelated diff. Reject it if the gain depends on weakening the check or duplicating ownership.

4. **Make equivalent plans compete against the harness itself.** Permute u01's area order in a copy of its saved plan. Project the original and permuted records into REVIEW and VALIDATE. Compare the actual units, commitments and checks each named subject receives. No provider is needed. This catches the positional join even when every individual answer is valid. Keep this as one regression at the persistence boundary if it catches both consumers. Drop variants that cannot change a recipient's evidence.

## Kill list

- Delete the positional joins in REVIEW and final validation. Both collections already carry the same area handle.
- Delete renumbering as check identity. Keep the worker's freedom to add checks. A shortened repair report must leave previously accepted coverage intact.
- Delete the second full-plan answer format for STEER once code owns the finished prefix. Preserve old answers in their original run records. The model needs one way to describe future work.
- Delete the unconditional page, form and screenshot directions from `plan.py:10–15`. C26 already specifies the real path for a browser, API or signal processor. Keep the try-it guide and its observed walkthrough on the product's own surface.
- Delete R16's requirement that **every** improvement lane remove a shackle. The cited thin cohort supports specific deletions. It supplies no failure caused by a lane making one necessary fix.
- Replace “every incident adds a row” in `DEV-VERIFICATION.md` §5 with a test of the failed handoff when reproducible. `LANDING-CHECKLIST.md` rows 1 and 5 address real incidents. Another reminder cannot expose an area swap in a structurally valid plan.

## Your design vs ours

I wrote these eight lines from the Charter before opening the Blueprint or source.

- Start with one user journey and the observation that would convince the user it works.
- At A, save the accepted ambition, quality bar and decisions the user still owns.
- Plan the architecture once, let areas propose work in parallel, and take the joined plan to B.
- Give each promise a witness on its real surface and each shared boundary a producer and consumer.
- Have isolated workers build the smallest runnable slice across those boundaries.
- Let code integrate, run witnesses and retain their inputs, results and revision.
- Give the planner the unresolved difference and the changes it may make. Ask the user about changes to accepted scope.
- At C, let the user try the integrated result and decide.

I would take Seldon's publication design. It records intent before changing the checkout and verifies the preimage on reopen (`units.py:106–110`, `gitwork.py:215–229`). My sketch left that crash window open. I would also replace “plan the architecture once” with progressive DETAIL against the built product.

I would keep my starting point for proof. Name the observation that distinguishes delivery from a plausible miss while the user can still correct the interpretation. Then each check has a reason to survive a repair, and the planner has a concrete disagreement to resolve.

## What you are least sure about

- The strongest alternative explanation for u01 is a poor local implementation. The saved verdict says the checks passed, including a date-mismatch check. I did not establish that a new header was necessary. A solution using the existing API that passes the same cross-time-zone case would weaken the case for changing this particular contract.
- T-204 says the tune positives concern a correlated SQLite-closure defect family. The locking handle was unconfirmed. One PRODUCT call timed out. The eval measures agreement on these labels. It cannot estimate general judge recall or compare FLOW with PRODUCT.
- The brief reports 20 scored M2 apps at 36–39 versus plain Codex at 34–36. The named `m2twenty3` score file contains 19 rows at 36–39. Its 20 original stores contain 19 SCRIPTED_C and one EXECUTE (z11). Product score, autonomous closure and human acceptance have different denominators. I did not establish the twentieth score from that cohort file.
- The next unproven transition is a real contract amendment followed by both owners' integrated behavior passing in the same multi-wave run. The sealed second dream remains the M3 exit. This review inspected source, saved prompts, replies, logs and state. It ran neither Seldon nor a provider.
