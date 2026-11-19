CHARTER: serves C1–C4 — violates no I1–I9; read-only audit.

Snapshot: `dcfaedf999ed9ad89a4c19da2daa4f967f724a46`. Semantic-v1 first, including reachable legacy boundaries. Counts use **decision families**, deduplicating shared helpers and splitting structural versus semantic questions inside mixed functions.
TRIAGE: DESIGN — semantic authority is mixed into validators, evidence gates and projections; sibling cases span consent, proof, review, amendments and acceptance.
R1 = [astra-reset-1](C:/Users/oren/codex-harness/work/ladder/design-review/astra-reset-1.md); R2 = [astra-reset-2](C:/Users/oren/codex-harness/work/ladder/design-review/astra-reset-2.md). NEW means the concrete boundary repair is not explicitly covered.

**A. Misallocated points**

| file:function | Decides what | Currently | Should be | Rule broken | Reset |
|---|---|---|---|---|---|
| `intake.py:propose` | Minimum planning recipe from ambiguity labels, producer count and ownership-area count | CODE | HYBRID | C3, I1/I2 | R1 1b |
| `planner_vision.py:expansion_status` | Expansion adequate only with 3–7 upgrades | CODE | HYBRID | C3, I1 | R1 1b |
| `approvals.py:record_approval`; `planner_confirmations.py:_chat_evidence` | Meaning of user consent through affirmative/negative word lists | CODE | HYBRID¹ | C3, I1 | R1 1b |
| `plan_store.py:accept` | Any nonblank supplied statement can become recorded C consent; no interpreted decision record | CODE | HYBRID¹ | C3/C4, I6 | R1 2e |
| `approvals.py:intent`; `PlanStore._classify_vision_edit` | Whether an amendment changes intent through a fixed field subset and literal equality | CODE | HYBRID | C3, I1/I3 | R2 C10: 1a/2a/3b |
| `spine.py:Spine.__init__,compile_manifest`; `graph.py:load_plan` | Admissible plan/proof shape: no semantic test nodes, exactly Contracts→Build, restricted surfaces | CODE | HYBRID | C3, I1/I3 | R1 1a/3a/3b |
| `semantic_schema.py:validate,web_journey` | Proof admissibility through closed operations, mandatory positive visibility and fixed viewport/motion combinations; unknown scenarios eventually refused at execution | CODE | HYBRID | I1–I4/I8 | R1 1a/1c |
| `semantic_runner.py:run` | Executable product representation limited by source-extension whitelist and fixed source limits | CODE | HYBRID | I2/I3 | R1 1c; R2 C26 |
| `semantic_runner.py:execute`; `planner_candidate.py:_semantic_validation` | “Correct RED” and absence of stubs from `SELDON-STUB`, exit 3 and marker coverage | CODE | HYBRID | C3, I1/I4 | R1 1c |
| `semantic_runner.py:execute` | Missing qualitative judgment becomes `passed=False`, then scenario FAIL | CODE | HYBRID | I2/I4 | R1 1c/2e |
| `planner_candidate.py:record_judgment` | Only web `textContrastAA`/`visualQuality` may receive candidate judgments | CODE | HYBRID | C3/C4, I3 | R1 4a; R2 C6/C26 |
| `plan_quality.py:first_moment_proof` | First-use adequacy from text containment and declared flags | CODE | HYBRID | C3, I1 | R1 2a |
| `plan_quality.py:_evaluate,_cross_bead_contract,quality_report` | Semantic quality labels from edge-case keywords, graph width, import presence and weighted checklist scores | CODE | HYBRID | C3, I1/I6 | R1 2a |
| `steering.py:_python_findings` | Stub/mock meaning and severity from AST shapes, TODO markers and identifier prefixes; currently advisory reporting, not an integration veto | CODE | HYBRID | C3, I1 | R1 2a/3b |
| `wave_refine.py:proposal` | Contract compatibility and locked contradictions from inferred return shapes; unknown extraction prevents completion | CODE | HYBRID | C3, I1/I2 | R1 3b; R2 C10 |
| `plan_store.py:cluster_findings,resolve_findings` | Findings are equivalent at Jaccard ≥0.6; resolving one closes every cluster member | CODE | HYBRID | C3, I1/I6 | NEW — 2a owner |
| `PlanStore._review_repairs_match,successful_reviews` | Changes within previously flagged nodes/scenarios qualify for carried-forward review without fresh semantic assessment | CODE | HYBRID | C3/C4, I1/I6 | NEW — 2a owner |
| `roundtable.py:_merge_finding` | Conflicting scope classifications become `defect-in-plan` automatically | CODE | HYBRID | C3, I2 | R1 2a |
| `roundtable.py:_execution_context`; `acceptance.py:prepare_execution_assessment` | Relevant evidence requires protected Python test lines/direct `ownedCalls`; other evidence cannot reach the judge | CODE | HYBRID | C3, I1–I3 | NEW — 1c/2a owners |
| `PlanStore._check_evidence,acceptance_review_guard`; `review_instructions.py:finding_response` | Successful finding-array reviews—including `[]`—supply approval credit without an explicit positive verdict and rationale | CODE | HYBRID | C3/C4 | R1 2a/2e |
| `acceptance.py:require_c_evidence` | C readiness from scenario PASS, delivery, review and web judgment, without mandatory explicit completeness/no-stubs/full-bar verdicts | CODE | HYBRID | C3/C4, I6 | R1 2e/4a; R2 C6/C26 |
| `roundtable.py:_review_shard,_review_dossier` | Malformed judgment ends as invalid review; no two exact-fix retries followed by judge/steer | CODE | HYBRID | C4, I2/I8 | R1 2a/2c |
| `PlanStore._closure_declaration,plan_review_policy_state` | Optional closure policy remains ineligible because assessment producers are unavailable, without a pending-judgment route | CODE | HYBRID | I2/I8 | R1 2a/2c |
| `dispatch.py:_observe_attempt` | Worker blocking from an untyped report marker or blocker-file presence, without requiring a typed concrete-gap verdict | CODE | HYBRID | C4, I4 | R1 2c/3c |
| `review_instructions.py:focus` | Reviewer repeats structural link-completeness checking alongside semantic coverage assessment | LLM | CODE² | C1/C2, I6 | R1 2a |
| `acceptance.py:_prepare_acceptance_review` | Reviewer instructed to reconstruct command strings and verify SHA-256 bindings | LLM | CODE | C2, I1 | NEW — 2e owner |
| `planner_guidance.py:planning_turn`; `planner_consent_views.py:status_next,semantic_consent_next`; `planner_recovery.py:resolve` | Planner orchestrates compile/advance/publish/start and routine recovery instead of deterministic continuation | LLM | CODE² | C1/C2, I6 | R1 2c/2d/3b; R2 C23 |

¹ The human retains A/B/C authority; an LLM interprets their words, and code binds/enforces the recorded decision.
² Only the deterministic portion moves to code; semantic coverage, replanning and recovery strategy remain LLM work.

**B. Correctly allocated families:** CODE **42**; LLM **7**; HYBRID **2**. Advisory prospective interface recognition is not a blocking meaningfulness judgment. Structural checks and ordinary execution observations remain code responsibilities.

**C. Shared repairs**

- **`plan_store` owns one typed judgment record:** subject IDs/revisions, candidate/evidence binding, verdict, rationale and concrete gaps. Review, steering and acceptance consume it; they do not infer semantic success.
- **One pending-judgment state:** absent, inconclusive or unsupported semantic evidence neither passes nor fails the product. Code routes judgment; malformed output gets two exact fixes, then steering.
- **`spine`/runners own structure and observations:** open executable-test contracts, canonical links, hashes, actual RED/GREEN and receipts. Heuristics may nominate evidence; judges decide meaningfulness.
- **`run_loop` owns continuation:** phase transitions, scheduling, bounded retries and resumption come from canonical state. Planner calls produce semantic records.
- **Review/intent owners judge equivalence and impact:** finding clusters, repaired-review reuse and scope amendments require explicit bound assessments; similarity and field-location rules cannot grant authority.

**D.** No unresolved judge-kind question requires Oren’s decision. Runtime/provider behavior was not exercised. No files changed; no tests or providers launched.