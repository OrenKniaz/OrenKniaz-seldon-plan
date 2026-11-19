CHARTER: serves C6/C9/C10/C12/C19/C22–C26 — uses existing DV1–DV9 during restoration; proposes no additional I1–I9 exception.

Read ratified v1.1 and [ASTRA-RESET-1](~/codex-harness/work/ladder/design-review/astra-reset-1.md). The following is the minimal amendment; no files changed, tests run or providers launched.

Keep the existing stages. Only 1b/1c remain parallel, on their existing disjoint files. One integration owner serializes `plan_store.py`, `roundtable.py`, `dispatch.py` and `test_golden_path.py`; shared-file amendments below occur in their listed stage order. File stems mean `src/codex_harness/core/*.py`.

- **C6 → 1b, 2e, 4a.** Replace “UX quality bar” with the full relevant Vision Lock bar: UX/visual, performance, maintainability, architecture, observability and failure behavior. Owners remain `intake`, `planner_vision`, `acceptance`, `planner_candidate`, `steering`. Harvest accepted quality criteria and candidate-bound judgments; delete UX-only completeness predicates. Ladder: L0 records the applicable bar; L3 exposes and repairs a nonfunctional quality gap despite functional GREEN.
- **C10 → 1a, 2a, 3b.** Define typed upward amendments in 1a: source discovery/evidence, affected upstream IDs/revisions, proposed change, rationale and decision linkage. `steering` judges meaning; `waves`/`wave_refine`/`run_loop` consume approved changes through the serial `plan_store` owner. Harvest impact traversal and decision provenance; delete silent downstream-only patching. Ladder: L2 discovery produces an amendment, scope change waits for the user, and only affected descendants become stale.
- **C12 → 3a.** Extend `dispatch`, `graph`, `planner_jobs`, `worker_packet` scheduling to elastic machine/provider capacity, file conflicts and visible waiting reasons. Harvest readiness, ownership and provider-limit observations; delete arbitrary ceilings without deleting actual capacity controls. Ladder: L2 shows available independent beads overlap, capacity/conflicts explain waits, and released capacity admits waiting work.
- **C19 → 3c.** Existing `project_memory`, `memory_promotion`, `mail`, `worker_packet`, `intake` owners retain source citations in every memory-influenced decision. Harvest provenance/retrieval; delete any memory-derived authority overriding canonical decisions. Ladder: L3 applies a cited lesson, while conflicting advice leaves the accepted trace authoritative.
- **C22 → 1a/1b, 3b, 4a.** Define metric, measurement provenance, iteration history and stop-condition links in 1a; `planner_vision` records user-agreed metric and stopping conditions at Vision Lock. `run_loop`/`waves` retain measured iterations through `plan_store`; `acceptance` evaluates the agreed outcome. Harvest research measurements and wave results; delete any success predicate equating “iteration finished” with “dream achieved.” Ladder: an L3 metric-search variant records real measurements and stops for an agreed, stated reason; stopping alone grants no acceptance.
- **C23 → 2c, 2d.** `run_loop` and serial `plan_store` persist a revision-bound baton every loop: decisions, assumptions, open questions, current state, next safe action and rationale. `planner_resume`/recovery consume that canonical state. Harvest phase history and recovery receipts; delete competing resume/next-action truth. Ladder: L1 kill/restart plus context/agent replacement resumes the same direction without repeating completed effects or inventing consent.
- **C24 → 1a, 1b, 1c, 2e.** Use ordinary feature/test/code/result nodes with existing-baseline provenance, rather than a second graph. `intake`/`planner_vision` map existing behavior, rationale and verification before change planning; existing runner and acceptance owners preserve GREEN. Harvest baseline references and requirement/test links; delete new-project-only admission assumptions. Ladder: L1 shows existing features and observed evidence before proposed changes, then preserves their GREEN while proving the changed behavior.
- **C25 → 2c/2d, 3a/3b, 4b.** `mcp_planner`/`plan_cli` expose provider-chat pause/resume/stop/reprioritize; `run_loop`/`plan_store` own durable intent, `attempt_control` owns worker cancellation, and `dispatch` honors it. `planner_views`/`status_api`/cockpit expose each worker’s activity, rationale and evidence read-only. Harvest cancellation and job inspection; delete automatic continuation that disregards user control. Ladder: L2 exercises all four commands mid-wave, bounded worker quiescence, restart persistence and priority changes respecting dependencies; scope changes use C10 approval.
- **C26 → 1a, 1c, 2e, 4a/4b.** Define evidence states once in 1a; runners produce observations, canonical persistence records them, acceptance consumes them, views display them. Harvest execution receipts and candidate binding; delete scenario-tier/completion shortcuts that imply live validation. Ladder: L2 browser and HTTP proof; L3 persistence readback and an authorized simulator/HIL/signal-measurement case for the relevant HW/DSP/audio surface. Missing observations remain awaiting judgment, never fabricated failure or success.

**Stage 1a re-check:** the original brief lacks explicit C26 states, C24 baseline representation and C10 amendment records. Add all three now, plus the C22 metric/result links and C23 baton references, within the existing typed trace. Later stages implement their behavior without replacing the graph contract.

**Exact Stage 1a lane brief — 17 lines**
```text
CHARTER: serves C4/C9/C10/C22–C24/C26 — uses DV1/DV4/DV9; proposes no additional I1–I9 exception.
Outcome: one complete, domain-open trace contract consumed through the canonical producer/store/compiler path.
Own: src/codex_harness/core/{spine,graph,semantic_schema,planner_schema}.py.
Serial integration owner alone edits plan_store.py, necessary mcp_planner.py bindings, and tests/python/core/test_golden_path.py.
Do not edit roundtable.py or dispatch.py; their later stages retain serial ownership.
Trace: dream→features→stories→requirements→architecture/design→contracts→tests→beads→code→results; decision/research side links.
Evidence states: awaiting, failed, stale, integrated, validated live; bind evidence to item revision, candidate, source and observation.
Integrated does not imply validated live; missing proof stays awaiting; historical/fake-provider evidence cannot establish real-provider acceptance.
Brownfield: ordinary existing-feature nodes link baseline code, behavior, rationale, tests and observed evidence before change planning.
Amendments: typed discovery/source, upstream target revisions, proposed change, rationale and decision links; preserve exact impact.
Include metric definition/stop-condition/iteration-result links and canonical baton references; add no separate stores or execution engines.
Harvest legacy test nodes, traversal, impact calculation, baseline provenance and canonical revision/evidence binding.
Delete replaced mode-specific topology, closed product vocabulary and unit-test assumptions; preserve historical provenance.
Golden extension: public producer→store→reload→compiler consumes full/brownfield trace and amendment; exact affected evidence becomes stale.
Protect against lost existing features, dropped evidence links and broad invalidation; current scenario journeys do not prove this full contract.
Ladder: L0 collapsed and L1 full/brownfield trace preserve IDs, baseline evidence and exact impact; contract proof alone earns no promotion.
TRIAGE: BUG|DESIGN — name cause and sibling cases; repair shared-rule DESIGN at its owner, never bypass admission or invent proof.
```

Existing deletion estimates and dates remain estimates; this amendment adds no deviation expiry extension. Last retained evidence is fixture-level behavior, not complete actual-provider acceptance. Next unproven step: Stage 1a’s canonical end-to-end contract, followed by the existing L0→L3 gates.
## CC addendum 11-04: JUDGE-BOUNDARY-1 (judge-boundary-1.md) folds into the reset
The audit found 27 misallocated decision families: 24 have code judging meaning, 3 have the LLM doing a function's job. 51 are correctly allocated.
Every later brief carries the 5 shared repairs, each at one owner:
- the typed judgment record in plan_store (2a);
- one pending-judgment state, with 2 exact fixes then steer (1c/2a);
- spine and runners own structure and observations only (1a/1c);
- run_loop owns continuation (2c);
- review/intent owners judge equivalence and impact (2a).

The NEW rows have these owners:
- Jaccard finding clustering and carried-forward review reuse → 2a;
- the evidence-relevance filter (protected Python lines) → 1c+2a;
- the LLM verifying SHA-256/command strings → moved to code in 2e.

Stage 1a removes rows 16/17 (closed plan/proof shape). The gate will confirm it.
