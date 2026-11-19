Reviewed HEAD `6b2ba9a` read-only; no edits, tests or product runs. These are source-established design paths, not runtime reproductions. File references below are under `src/codex_harness/core`.

1. **D1 — Verification capability is still delivery authority.** A verifier error becomes failed integration, withholds the product, and prevents C.
   **Evidence:** `planner_candidate.py:_semantic_validation,deliver,delivered_candidate`; `dispatch.py:_integrate_bead`; `acceptance.py:require_c_evidence` — `integrated validation failed`, `acceptance-delivery-invalid`.
   **Blast radius / siblings:** Every semantic product; missing browser tools, observation-size limits, verifier deadlines and absent visual judgment can veto otherwise working code.
   **ONE rule:** Only an observed product failure refuses delivery; unavailable verification lowers candidate-bound evidence. **Delete:** PASS-only delivery admission and repeated validation predicates at integration, delivery and C; retain actual failed assertions.

2. **D2 — The semantic plan is a tiny product factory.** Product intent must fit the controller’s executable vocabulary and fixed topology before workers can implement it.
   **Evidence:** `spine.py:semantic_spec,compile_manifest`; `semantic_schema.py:validate,web_journey`; `planner_execution.py:execution_scope` — `plan-semantic-scenarios-invalid`, “Multiple/parallel Build unsupported.”
   **Blast radius / siblings:** HTTP services, mixed frontend/backend, libraries, mobile, pipelines, ordinary web forms; targets must be Python or static `index.html`, with exactly two serial beads and no semantic wave scope.
   **ONE rule:** Planner semantics describe required behavior; workers own executable verification and implementation topology. **Delete:** product-surface admission whitelist, exactly-two-bead rules, mandatory viewport/motion matrix and unsupported-action vetoes; unsupported observers remain labelled.

3. **D3 — Deadlines stop work but do not release ownership.** An interrupted owner leaves a durable claim that subsequent callers can only observe.
   **Evidence:** `planner_acceptance.py:AcceptanceOwner.start,drain,close`; `plan_store.py:admit_audit`; `planner_review.py:status,ReviewOwner.start` — `unknown-interrupted`, `audit-busy`, `acceptance-execution-pending`.
   **Blast radius / siblings:** All products after disconnect, server restart or acceptance timeout; worker recovery’s bounded abandonment does not govern audit, acceptance and review ownership.
   **ONE rule:** Every admitted attempt has a bounded terminal disposition that retires its claim without inventing success or forgetting spent calls. **Delete:** indefinite UNKNOWN admission locks and each owner’s separate “poll forever/no replay” policy; reuse existing stop/quarantine behavior.

4. **D4 — Reviewer availability is a compulsory product dependency.** Review transport, packet eligibility and missing assessment machinery can veto publication or acceptance without identifying broken behavior.
   **Evidence:** `plan_store.py:_check_evidence,acceptance_review_guard`; `planner_review.py:acceptance_reviewers`; `roundtable.py:packet_shards`; `planner_views.py:plan_review_policy_next` — `plan-publication-evidence-required`, `acceptance-review-required`, `plan-review-policy-unmet`.
   **Blast radius / siblings:** Every product with unavailable reviewers, malformed returns or oversized packets; optional adopted policy explicitly holds on unavailable closure producers.
   **ONE rule:** Review availability determines assurance; a blocking review finding must identify a concrete violated obligation. **Delete:** successful-review/quorum prerequisites and unavailable-producer closure vetoes. Optional-policy exposure is conditional, not universal.

5. **D5 — A display projection has become a second admission owner.** Publication permits advisory findings while dispatch consumes a projection that reclassifies all open findings as blockers.
   **Evidence:** `plan_store.py:_check_publish` excludes `advisory_finding_ids`; `planner_views.py:review_resolution_state` collects every open non-readiness finding; `planner_execution.py:execution_scope` requires that list empty — `worker-execution-canonical-prerequisite`.
   **Blast radius / siblings:** Any plan retaining minor, note or beyond-brief findings; `plan_quality.py:_roundtable` adds another interpretation of the same review truth.
   **ONE rule:** The finding owner decides blocking disposition once; publication, dispatch and views consume it. **Delete:** projection-derived admission and duplicate blocker queries. This removes responsibility from existing oversized owners: PlanStore 3,497 lines, views 1,647.

6. **D6 — RED means “obeys our stub protocol,” not “demonstrates the missing behavior.”** Every scenario/action must exhibit artificial stub failure before Build is admitted.
   **Evidence:** `semantic_runner.py:execute` requires exit 3 plus `SELDON-STUB <operation>` before parsing/import/I/O; `planner_candidate.py:_semantic_validation` requires every scenario FAIL and every action stubbed.
   **Blast radius / siblings:** Existing applications, partially implemented requirements and workflows mixing working setup with missing behavior; legitimate existing GREEN scenarios cannot satisfy universal RED.
   **ONE rule:** RED proves the behavior being changed; unaffected working behavior remains GREEN. **Delete:** universal stub-marker admission and all-actions/all-scenarios-must-fail checks; workers write meaningful behavioral proofs.

7. **D7 — B budgets logical reviews while execution spends physical starts.** Sharding and resharding can exhaust an approved review allowance before the promised review completes.
   **Evidence:** `approvals.py:subject` calculates reviewers × rounds; `roundtable.py:_review_dossier,_review_shard` launches per shard; `provider_call_budget.py:_reserve` charges starts — `plan-b-consent-required`, `review-call-cap-exhausted`.
   **Blast radius / siblings:** Larger plans, acceptance packets containing source/results, context-overflow retries; exact failure threshold depends on packet size.
   **ONE rule:** B authorizes the bounded launch schedule actually prepared, and exhaustion downgrades unfinished review assurance. **Delete:** competing round/start allowance arithmetic and mandatory renewal loops; never exceed authorized spending.

8. **D8 — Evidence labels participate in artifact identity instead of travelling as evidence.** Changing verification strength can make an unchanged published product appear unpublished, while exports recognize only selected labels.
   **Evidence:** `plan_store.py:publish,publication_current,_export,_status`; `planner_views.py:review_resolution_state`; `approvals.py:executable_candidate` — `plan-proof-level-required`, `plan-publication-required`, “Unknown recorded audit mode.”
   **Blast radius / siblings:** Legacy prospective plans gaining oracle evidence, future lower tiers, status/export consumers; semantic results and reviewer tiers follow separate paths.
   **ONE rule:** Candidate identity describes product/plan bytes; evidence is a separately bound record projected unchanged everywhere. **Delete:** proof-dependent publication hashing, its executable-preimage reversal, tier-specific freshness tests and renderer whitelists.

9. **D9 — The planner is the workflow scheduler and refusal interpreter.** Chat must coordinate deterministic stage transitions and recover meaning from generic status redirects.
   **Evidence:** `mcp_planner.py:PlannerServer._dispatch,_next`; `plan_store.py:advance`; `planner_refusals.py:refusal_text` — separate compile/advance/publish/start calls, `plan-phase-order`, generic `harness_plan_status` recovery.
   **Blast radius / siblings:** Every run; failures add inspect/schema/retry calls, and polls increase with duration. `test_golden_path.py:call` excludes polls/probes from its ≤25 “happy” ceiling, so it does not bound total calls.
   **ONE rule:** Each semantic submission advances deterministic work to the next required input, decision or bounded job event, returning the owning refusal’s single concrete remedy. **Delete:** caller-managed transition choreography and competing Next/refusal inference tables; existing batching is useful but insufficient.

**First three DESIGN lanes**

- **Lane A — Delivery verdict:** Own `planner_candidate.py`, `dispatch.py`, `acceptance.py`. Define observed failure versus unavailable verification through integration → delivered files → C; remove PASS-only vetoes. Acceptance example: missing verifier yields labelled delivery, failed product assertion still refuses.
- **Lane B — Product-neutral semantics:** Own `spine.py`, `semantic_schema.py`, `semantic_runner.py`, `graph.py`, `worker_packet.py`. Remove controller vocabulary/topology from product eligibility; keep semantic intent and worker-authored code distinct. Acceptance examples: HTTP+UI and an existing partly GREEN application remain expressible.
- **Lane C — Terminal ownership:** Own `plan_store.py`’s attempt persistence, `planner_acceptance.py`, `planner_audits.py`, `planner_review.py`, `planner_recovery.py`. Specify one bounded retirement rule across owners, retaining costs and quarantined evidence. Acceptance example: owner loss cannot permanently monopolize the workspace.

These scopes share no files; keep them net-deleting and avoid introducing another coordinator or oversized owner.