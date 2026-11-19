Reviewed D1–D9 first, then current source, README, North Stars and capability audit. **Read-only; no edits, tests or provider runs.** HEAD moved during review from `6b2ba9a` to `3a11b68`, committing the changes already present when I started.
**Conclusion:** Seldon has most structural machinery, but two competing execution models prevent the core from composing. Semantic mode restricts products; legacy mode carries the richer graph/wave machinery. Neither supplies the complete semantic-judgment-and-replanning loop.
Paths below are under [src/codex_harness/core](~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core). Counts are physical lines, including comments/blanks: **36,470 top-level Python lines**, excluding browser assets, adapters below subdirectories and tests.

| Owner’s core | Current implementation, approximate lines | Verdict |
|---|---|---|
| Everything runs in a loop | `mcp_planner` 2,901; `plan_store` 3,495; `dispatch` 2,781 | **RESHAPE / MISSING:** worker scheduling loops exist; planning, judging, repair and wave progression still require caller choreography. |
| Deterministic structure | `spine` 728; `graph` 358; `plan_store` 3,495; `provider_call_budget` 332; attempt/receipt owners | **KEEP:** canonical revisions, links, DAGs, ownership, budgets and observed execution belong here. Consolidate duplicate consumers. |
| Tools replace mechanical LLM work | `plan_cli` 1,406; `mcp_planner` 2,901; `planner_views` 1,647; refusal modules 329 | **RESHAPE:** many tools expose internal transitions and recovery interpretation instead of completing deterministic work. |
| LLM creates/judges semantics | `roundtable` 2,095; `review_instructions` 111; `planner_candidate.record_judgment` 37 | **KEEP review; MISSING general routing.** The judgment writer accepts only two web checks and records caller-mediated human observations. |
| Improve dream, decompose, obtain acceptance | `planner_vision` 181; `intake` 586; `approvals` 296; `planner_confirmations` 269 | **RESHAPE:** durable intent/consent is useful; fixed expansion counts and affirmative vocabulary substitute ceremony for meaning. |
| Dream → features → stories → requirements → tests; preserve WHY | `spine` 728; render/diagrams 413; `worker_packet` 896; `waves` 919 | **KEEP / RESHAPE:** graph exists. Semantic mode forbids test nodes; scenarios are vision payloads with requirement aliases, not a complete worker-test-to-result spine. |
| More LLM reviewers | `roundtable` 2,095; `planner_review` 390; review-budget owner 332 | **KEEP / RESHAPE:** retain bounded independent judgments and disagreements. Two reviewer names—even duplicated model tuples—do not establish independent reasoning or deterministic correctness. |
| Concurrent beads; expensive planning, fast execution | `graph` 358; `dispatch` 2,781; `worker_packet` 896; `planner_execution` 162 | **KEEP scheduler; DELETE semantic restrictions:** exactly two beads, shared entry ownership and `max_parallel=1` defeat the promised concurrency. |
| Validate actual dream, including omissions/stubs | `acceptance` 1,918; `semantic_runner` 506; `planner_candidate` 393; review packet | **RESHAPE / MISSING live completeness:** full-vision review exists, but is packet-only; finite scenario PASS and web-only qualitative judgments cannot establish every product’s dream. |
| Planner reviews progress and steers | `steering` 396; `supervision` 622; dispatch notifications | **RESHAPE:** current steering is retrospective, advisory and Python-heuristic-driven; no complete event → semantic judgment → repair/replan loop. |
| Wave 1 → vision resync → wave 2 | `waves` 919; `wave_refine` 734; roughly 560 wave-related store lines | **RESHAPE, not absent:** substantial lock/refinement/accounting exists, but semantic compilation rejects wave scope and refinement depends on legacy protected tests/static interfaces. |

**Minimal core:** retain existing owners, unify their contracts, and make MCP/CLI/views thin consumers. These are design budgets—not measured achievable patches. Group memberships follow the modules above; shared modules are counted only once below.

| Retained responsibility/modules | Today | Proposed budget |
|---|---:|---:|
| Canonical truth: `plan_store`, `spine`, `graph`, `waves`, `wave_refine` | 6.23k | 4.5–5.0k |
| Intent/consent: `intake`, `planner_vision`, `approvals`, migration/confirmation/card/consent modules | 1.79k | 1.4–1.5k |
| Judges: `roundtable`, `review_instructions`, reviewer access/evidence, `provider_call_budget` | 2.62k | 2.0–2.3k |
| Execution: `dispatch`, planner execution/jobs/candidate/recovery/acceptance/review/audits, `acceptance_recovery`, attempt/process/launch owners | 7.10k | 6.0–6.5k |
| Observation/acceptance: `acceptance`, runners/schema, `test_audit`, `proof_imports`, steering/supervision/readiness/quality | 6.68k | 4.5–5.0k |
| Interfaces: MCP/CLIs, views/schema/guidance/refusals/resume/connection/stdio/audit views, render/diagrams/status | 8.52k | 5.5–6.0k |
| Retain supporting packet, mail, memory, initialization, provenance, storage and admission modules | 3.53k | 3.4–3.5k |
| **Total** | **36.47k** | **27.3–29.8k** |

**Deletable responsibilities and size:**

- **380 lines directly inventoried:** steering stub/mock classifiers 88; cross-bead import-based quality classifier 106; prospective interface classifiers/audit classification 186. Replace their semantic conclusions with recorded judgments; retain structural links and observations.
- **Conditional migration candidates:** 733 lines of specialized interpreter/unittest observer machinery and 130 lines of acceptance command projection/reconstruction. Some observation/provenance behavior must survive; these are gross candidate ranges, **not 863 safely removable lines**.
- **Estimated further reductions:** product-specific admission/RED protocol ~0.3–0.6k; duplicate phase/Next/admission/projection logic ~1.5–2.5k; dual legacy/semantic proof and wave plumbing ~2–3k. These estimates need dependency-level inventories and exclude wholesale deletion of their owning modules.
- The old `SEMANTIC-DELETION-LEDGER.md` is stale: it cites `test_audit.py` through line 1,616; today that module is 463 lines. Do not reuse its 1,918-line total. The 27–30k target remains an estimate.

**Concrete boundary violations and routing gaps:**

- `steering.py:_stub,_python_findings`: `pass`, `NotImplementedError`, TODO markers and `fake_` names become semantic stub/mock findings. Dispatch labels these advisory; they are **not presently an automatic delivery veto**, but still violate the requested semantic boundary.
- `plan_quality.py:_evaluate,_cross_bead_contract`; `test_audit.py:_interface_assertion,audit_prospective_tests`: regex edge-case grading and import/assertion recognition stand in for meaningful coverage. The current audit makes unknown interfaces informational; it still does not route them to a judge.
- `semantic_schema.py:web_journey,validate`; `spine.py:semantic_spec,compile_manifest`: fixed actions, Python/static-web targets, homogeneous surfaces, mandatory viewport/motion matrices and two-bead topology. `3a11b68` softens planning admission; execution still demands a supported replacement.
- `semantic_runner.py:execute`; `planner_candidate.py:_semantic_validation`: exit 3 plus `SELDON-STUB`, every action stubbed and every scenario failing define RED. Preserve observed failures; let judges assess whether they demonstrate the missing requirement.
- `wave_refine.py:extract_interfaces,proposal`: only Python/JSON interfaces are extracted; unknown static return shapes leave refinement unapplied. An extractor limitation needs semantic review, not an obligatory annotation/representation change.
- `planner_candidate.py:record_judgment`; `planner_vision.py:expansion_status`; `approvals.py:record_approval`: two allowed web judgments, 3–7 upgrades, and a short affirmative vocabulary constrain meaning. Interpret free text through recorded judgment; preserve actual user authority and unresolved ambiguity.
- `planner_views.py:review_resolution_state` → `planner_execution.py:execution_scope`: advisory findings become blocking through a projection. `plan_store.py:_check_evidence,_closure_declaration` leaves missing review/closure producers as holds rather than scheduling the missing semantic work.

Typed receipt schemas, reference integrity, authorization, spending limits and exact assertion comparisons remain deterministic. “Never refuses semantics” does **not** mean invalid structure proceeds or missing evidence becomes success.

**D1–D9 and lanes:** D2/D5/D6/D7/D8/D9 still fit, with D2’s planning refusal partially softened. D3 remains for audit/acceptance owners; review already exposes explicit abandonment, so “all owners lock forever” was too broad.
**Revise D1/D4:** verifier/reviewer unavailability is not product failure, but removing PASS/quorum gates cannot establish dream completion. Retain the candidate, route unresolved judgments, recover within authorization, and keep completion pending.
Keep A/B/C as ownership themes, but change boundaries: **A = observations/delivery**, **B = intent/trace/judging**, **C = deterministic lifecycle**. B cannot own `semantic_runner` while A changes RED/validation. Serialize changes to `plan_store`, `roundtable` and dispatch owners.

**Sequenced reset:** negative figures below are proposed net-production budgets, including replacement code. Parallel rows have disjoint files; later stages deliberately reuse owners.

| Stage / lane | Owned files | Deletion target and decisive ladder behavior |
|---|---|---|
| 1 / B — semantic judge | `test_audit`, `steering`, `plan_quality`, `roundtable`, `review_instructions` | −0.15–0.3k. **L0 hello-CLI:** a meaningful opaque test receives a recorded judgment; a tautology fails semantic review despite GREEN execution. |
| 1 / C — terminal lifecycle, parallel with B | `planner_acceptance`, `planner_review`, `planner_audits`, `planner_recovery`, `acceptance_recovery`, `plan_store` | −0.3–0.6k. **L0:** interrupt acceptance/review; retire ownership without success or lost spend; no overlapping retry. |
| 2 / B — one product-neutral plan | `spine`, `graph`, `semantic_schema`, `worker_packet`, `planner_schema` | −0.3–0.6k. **L1 small CLI:** preserve existing GREEN behavior, trace new requirements to worker-authored tests, admit independent Build beads. |
| 2 / A — observation and delivery, parallel with B | `semantic_runner`, `semantic_web.cjs`, `planner_candidate`, `planner_execution`, `dispatch`, `acceptance`, `runners`, `proof_imports` | −0.8–1.2k. **L1→L2:** ordinary RED→GREEN without magic stubs; real HTTP proof; unavailable observer requests judgment, observed assertion failure remains RED. |
| 3 / C — deterministic continuation | `plan_store`, `mcp_planner`, `plan_cli`, `planner_views`, `planner_consent_views`, `planner_refusals`, `planner_refusal_events`, `planner_resume` | −2–2.5k. **L2:** one semantic submission progresses to the next judgment/user decision; restart resumes; advisory findings never become blockers in a view. |
| 4 / B — resync and next wave | `waves`, `wave_refine`, `spine`, `graph`, `plan_store`, `worker_packet`, `supervision` | −1–1.5k. **L3 full-stack:** integrate wave 1, judge it against locked intent, refine wave 2 from observed interfaces, then run parallel UI/backend beads and cumulative proof. |
| 5 / A — full-dream closure and retirement | `acceptance`, `planner_candidate`, `roundtable`, `review_instructions`, `approvals`, `planner_confirmations`, `test_audit`, `runners` | −1–1.5k. **L3:** omit one accepted feature while tests stay GREEN; judge must identify the gap, trigger repair, and require actual user acceptance before completion. Retire remaining duplicate proof paths. |

One serial integration owner extends `tests/python/core/test_golden_path.py` after each stage; parallel lanes must not share that file. Prove each behavior there once and remove superseded tests without weakening coverage.
**Unproven:** these deletion budgets, composed multi-wave behavior and actual-provider/full-dream acceptance. Retained fixture journeys do not settle them. The next step is the bounded L0 judge/lifecycle pair, not a wholesale rewrite.

