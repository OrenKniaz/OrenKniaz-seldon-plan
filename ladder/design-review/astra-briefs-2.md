CHARTER: serves C1–C26 — uses existing DV4/DV5/DV7/DV8/DV9 during restoration; proposes no additional I1–I9 exception.

Verified HEAD `5f7dbc6c604ad480f7e5ccda211d988a4465d467`; read the charter, all requested reviews/addendum, Stage 1 report and retained capability audit. No files changed, tests run or providers launched.
Stage 1’s retained result is 19 scripted-provider cases GREEN with real subprocess RED/GREEN; autonomous real-provider L0 remains unproven.

**Binding terms carried by every brief below**
File stems mean `src/codex_harness/core/<stem>.py`; **G** means `tests/python/core/{test_golden_path,test_approval_v2_journey}.py`.
Each lane must be **NET-NEGATIVE in production lines**, counting new files and deletions together; report `PROD +/−/net; TEST +/−/net; cases versus base; runtime`. No cosmetic deletions or moving code outside the count.
Use only existing **1j prepare/submit/read**, its canonical bindings, pending state and two exact-fix retries; no second judge store, retry counter or inferred semantic approval.
Golden is the first gate; every behavior change extends it in the same patch through canonical producers/consumers. Script provider replies only; observe execution, persistence and cleanup. Name the regression and existing coverage gap.
Retain the ≤19-case ceiling, mark/measure the ≤10-minute fast gate, reuse unaffected evidence, and record discoveries in `docs/legacy-capability-audit.md`. Ladder claims require actual authorized runs.
One serial integration owner controls `plan_store`, `roundtable`, `dispatch` and G throughout Stage 2. Other owned files below transfer only after the preceding lane lands GREEN.

**2p — Land shared prerequisites first**
CHARTER: serves C3/C4/C13/C14 — uses DV4/DV9; preserves I1–I9.
Own: `worker_packet` + G; production deletion is the obsolete Contracts stub/exit-3/DOM-marker and Build “unit tests” instructions.
Prerequisites: retain existing 1j/schema/pending contracts; extend the shared scripted-provider harness for explicit review verdicts, equivalence/reuse judgments and later loop/acceptance replies. Keep real process observations and ordinary executable tests.
Close the worker-packet C14 instruction defect **here, before 2a**, including web instructions; DV4 remains partial. Contracts asks workers for meaningful semantic tests and observed behavioral RED, never manufactured marker RED.
Golden: generated packet → worker-authored test → ordinary failing execution → 1j assessment → Build → GREEN; prove the shared harness works before downstream lanes depend on it.
Ladder: L0 must use this actual packet/worker path. TRIAGE: DESIGN — producer still requests deleted stub semantics — siblings: web markers, exit 3, unit-test instructions.

**2a — Separate plan review from semantic judgment**
CHARTER: serves C2–C4/C10/C11/C14/C16 — targets DV7 and the review portion of DV4.
Own: `plan_store`, `roundtable`, `planner_review`, `review_instructions`, `reviewer_evidence`, `steering`, `plan_quality`, `acceptance`, `dispatch`, `mcp_planner`, `planner_schema` + G.
Replace Jaccard authority and automatic cluster-wide closure with bound 1j equivalence/member-disposition judgments; carried-forward review requires an explicit judgment of the actual revision delta.
Replace empty-array/minor-only approval inference with explicit verdict+rationale; conflicting `_merge_finding` classifications stay pending for judgment. Malformed reviews use 1j’s two fixes then steer; unavailable closure assessments remain pending and release ownership.
Remove semantic regex/AST/checklist grades and Python/direct-call relevance admission, including upstream dispatch finding witnesses; code checks links/provenance, judges assess relevance and meaning. Independent plan reviewers retain separate verdicts, truthful provider/model labels and consequence-scaled depth; convergence is judged around the default three rounds.
Move SHA/command reconstruction into deterministic evidence preparation **now, advancing that row from 2e**; delete reviewer hashing instructions. Do not revive Stage 1’s already-closed consent/intent rules.
NET-NEGATIVE deletions: clustering/reuse heuristics, semantic graders, duplicate review-credit rules and reconstruction prompts. Golden extends review→repair→B with conflicting, empty, malformed, stale/reused and non-Python evidence; retain complete flow coverage.
Ladder: L0 checks genuine plan review, meaningfulness judgments and same-model labeling; close DV7 only with that evidence. TRIAGE: DESIGN — review structure grants semantic authority — siblings: clustering, reuse, closure and approval.

**2b — Delete product budgets, preserve launch authority**
CHARTER: serves C8/C18/C20 — targets DV8; preserves I4–I6.
Own: `provider_call_budget`, `approvals`, `approval_migration`, `planner_confirmations`, `planner_jobs`, `planner_execution`, `planner_review`, `planner_candidate`, `planner_refusals`, `acceptance_recovery`, `plan_store`, `roundtable`, `dispatch`, `mcp_planner`, `plan_cli` + G.
Before deleting the budget module, retain its job/run/attempt verification in the existing job/provenance owners (`attempt_provenance` included); consumers must use those owners directly.
Delete spending/call/review quotas, reservations, renewals and budget-bearing B subjects; preserve historical records without reauthorizing them. Keep attempt deadlines, provider context capacity and development-only usage metrics.
NET-NEGATIVE: remove the module and its product plumbing. Golden: approved launch→review→delivery without renewal; stale/unapproved subjects still refuse with one remedy. This protects authority accidentally removed with quota code.
Ladder: L0 needs no budget decision and respects current B; DV8 closes after proof. TRIAGE: DESIGN — quota and authorization share an owner — siblings: worker starts, review starts, acceptance assessment.

**2d — Finish bounded owner lifetimes before the loop consumes them**
CHARTER: serves C4/C18/C23/C25 — preserves I2/I4/I5/I6; no standalone DV closure.
Own: `planner_acceptance`, `planner_audits`, `planner_review`, `planner_recovery`, `acceptance_recovery`, `planner_resume`, `attempt_control`, `planner_jobs`, `plan_store`, `roundtable`, `dispatch` + G.
Give every attempt/claim/hold a bounded terminal disposition through existing owners; expose durable completion/recovery observations for 2c. Two automatic bead recoveries, then recorded steering; remove competing counters and indefinite holds.
Transport loss grants neither success nor consent. Uncertain cleanup ends in truthful abandonment/quarantine, excludes abandoned evidence and releases logical ownership without claiming process quiescence. Awaiting the user owns no running attempt.
NET-NEGATIVE: delete duplicate retry/hold/resume rules. Golden fault journeys use real crash/stall/transport-loss observations, supported cleanup and canonical recovery; reach C or an explicit released pending/steering state.
Ladder: L1 fault twins prove bounded recovery and preserved direction; 2c adds autonomous consumption. TRIAGE: DESIGN — terminal ownership lacks one rule — siblings: review, audit, acceptance, worker and confirmation waits.

**2c-T — Adopt SDK transport before changing continuation**
CHARTER: serves C2/C4/C20/C23/C25 — preserves I5/I6/I9; no standalone DV closure.
Own: `mcp_planner`, `planner_stdio`, `planner_connection`, `seldon_cli`, `seldon_mcp`, `pyproject.toml` + G.
Adopt the approved official MCP Python SDK in **Stage 2c**, replacing handwritten protocol/session/stdio machinery while retaining thin Seldon domain adapters, tool contracts, confirmation provenance and canonical state.
NET-NEGATIVE includes the dependency adapter: delete replaced transport, not domain checks. Preserve durable decision identity across reconnect; stale wire replies cannot grant consent.
Golden: real SDK stdio initialize→tool calls→pending decision→disconnect/reconnect→completion, with provider replies scripted; retain golden coverage through the public transport.
Ladder: L0 uses this transport; Stage 4b retains all-provider experience verification. TRIAGE: DESIGN — custom protocol machinery competes with domain ownership — siblings: cancellation, reconnect, deferred replies.

**2c — Make run_loop own continuation, baton and chat control**
CHARTER: serves C1–C4/C8/C16/C23/C25 — restores DV5’s continuation portion; wave steering remains Stage 3b.
Own: new `run_loop`; `plan_store`, `mcp_planner`, `plan_cli`, `planner_guidance`, `planner_consent_views`, `planner_resume`, `planner_recovery`, `planner_jobs`, `planner_execution`, `planner_views`, `attempt_control`, `dispatch` + G.
Consume canonical semantic submissions and terminal events; code owns compile/advance/publish/start/observe/continue. Planners provide semantics, never scheduling instructions; untyped worker markers cannot establish a concrete semantic blocker.
Persist the C23 revision-bound baton each loop: decisions, assumptions, questions, state, next safe action and why. Resume from canonical state, reconcile recorded effects and never repeat completed launches or invent consent.
Implement durable chat pause/resume/stop/reprioritize; use 2d cancellation/terminal behavior, honor dependencies and approved scope, and expose worker activity/rationale/evidence read-only. Cockpit mutation remains excluded.
NET-NEGATIVE: delete planner choreography and competing next-action/resume inference. Golden reaches the existing acceptance boundary after worker exit without planner transition calls; interruption/restart and all four controls exercise the same loop.
Ladder: L0 proves autonomous continuation; L1 proves restart/agent replacement; L2 proves controls during concurrent waves. TRIAGE: DESIGN — continuation has multiple owners — siblings: post-exit work, recovery, restart and user control.

**2e — Deliver the first complete dream through C**
CHARTER: serves C6/C8/C9/C14/C15/C21/C24/C26 — establishes DV6 foundations; full closure remains Stage 4a.
Own: `acceptance`, `planner_candidate`, `planner_acceptance`, `planner_views`, `planner_refusals`, `planner_refusal_events`, `plan_store`, `roundtable`, `planner_review`, `run_loop` + G.
Require current integrated evidence for every accepted feature, explicit 1j completeness/no-stubs-mocks-missing/full-relevant-Vision-Lock-bar judgments, live demo and try-it guide before interpreted user C. Reuse Stage 1’s C-consent owner.
Delete post-build multi-model review and duplicate completion predicates; retain semantic acceptance judgments. Concrete gaps return to repair and renewed integrated proof; unavailable evidence remains pending. Preserve L1 baseline GREEN and truthful evidence states.
NET-NEGATIVE includes all replacements. Golden extends the autonomous journey through demo/guide/C and a concrete acceptance-gap repair; a GREEN test run alone cannot reach C.
Ladder: L0 hello-world through actual user C, then L1 brownfield; Stage 4a supplies L3 adversarial completeness/full-quality proof. TRIAGE: DESIGN — test success substitutes for dream acceptance — siblings: missing features, stubs, quality and stale evidence.

**Order and first real proof**
Land **2p → 2a → 2b → 2d → 2c-T → 2c → 2e**, each GREEN on its own resulting tree. This puts the shared judge harness, provenance replacement, bounded terminal observations and SDK transport before their consumers.
No parallel implementation lanes in this wave: shared production owners and both golden files prevent disjoint, independently GREEN patches. Read-only review may overlap; no lane waits for an unlanded sibling fix.
**Run L0 immediately after 2e’s integrated golden/fast gate passes, before L1, Stage 3 or any other new real-run experiment.** Obtain task-specific provider-launch authorization; bind the run to that exact candidate and use real planner/judge/worker providers on the hello-world tier through actual user C.
L0 is Stage 2’s first real-run proof, not an earlier isolated provider smoke test. Any blocker stops promotion: record `TRIAGE: BUG|DESIGN — why — sibling cases`, repair its owner, rerun affected evidence, then retry L0 under authorization. No DV expiry is extended by this plan.
## CC addendum 11-05, after MACRO-DRIFT-1 (verdict MINOR-DRIFT)
Wrong idea named by MACRO-DRIFT-1: "finish the internal reset before learning from real product work." Corrections adopted:
1. **Earlier real signal.** Right after 2a lands: ONE bounded real-provider replay of the failed ShelfLife importer→SQLite→HTTP path (real planner/judge/workers, work/fight-1 harness). Diagnostic only: record failures with TRIAGE, no ladder promotion. Full L0 after 2e is unchanged.
2. **Merge 2c-T into 2c**, one owned deliverable. New order: 2a → [ShelfLife replay] → 2b → 2d → 2c(+SDK) → 2e → L0.
3. **Real deletion targets, not token net-negative.** Each remaining lane states a numeric src/ target. 2a+2e: the proof/review family (~7k: runners, semantic_runner, semantic_schema, test_audit, proof_imports, roundtable, acceptance, readiness) heads to ≤3.5k, scenario-DSL machinery retired now that ordinary tests exist. 2b: −685 (budgets). 2c: the planner choreography/next-action/resume duplicates plus hand-written MCP transport (~3k). Track the nonblank core count per publish (35,014 at efc4a25).
4. Worst remaining offenders beyond Stage 2 stay assigned: wave_refine inferred-shape authority (3b), memory "follow" command (3c).
