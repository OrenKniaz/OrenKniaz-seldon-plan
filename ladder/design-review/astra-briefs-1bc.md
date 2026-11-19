CHARTER: serves C2–C10/C13–C15/C21/C22/C24/C26 — uses existing DV4/DV8/DV9 during restoration; proposes no additional I1–I9 exception.

**Decision:** land Stage 1j before 1b/1c because both lanes must consume one durable judgment contract and pending state; assigning its creation to either parallel lane introduces a dependency and competing authority.
Paths below are relative to `src/codex_harness/core/`, except the golden path. Audit rows are identified by function, since JUDGE-BOUNDARY-1’s table is unnumbered.
Start from the published Stage 1a candidate; this checkout still contains its uncommitted changes.

**Stage 1j — shared judgment prerequisite**
```text
CHARTER: serves C2/C3/C4 — violates no I1–I9.
Outcome: one canonical typed judgment contract and durable pending-judgment state, available to both lanes.
Own: plan_store.py, mcp_planner.py, planner_schema.py; sole serial owner of tests/python/core/test_golden_path.py during 1j.
Record: judgment ID, subject IDs/revisions, candidate when applicable, evidence/source bindings, verdict, rationale and concrete gaps.
Code gathers facts/flags and checks structure/bindings; the LLM supplies meaning; no positive credit without a current, bound verdict.
Shared repairs 1–2: absent/inconclusive/unsupported meaning → pending-judgment; malformed output → two exact-fix attempts, then steer.
Persist retry/steering disposition; release attempt ownership; pending never becomes product failure, success or inferred human consent.
Harvest canonical events, revisions and provenance; delete replaced judgment defaults; keep Stage 1a evidence states distinct from judgment status.
Golden: public submission→store→reload→consumer preserves pending/verdict; changed subjects lose credit; malformed responses exhaust exactly two fixes.
Regression/gap: prevents lost pending state and stale verdict reuse, neither established by Stage 1a’s trace-only journey; ladder: L0 prerequisite, no promotion.
TRIAGE: BUG|DESIGN — name cause, sibling cases and concrete remedy; repair the shared owner, never add a bypass.
```

**Stage 1b — size router and intent; parallel with 1c after 1j**
```text
CHARTER: serves C3–C10/C21/C22/C24 — uses DV8; proposes no additional I1–I9 exception.
Outcome: size-scaled planning, improved and locked intent, and attributable own-words decisions without fixed semantic recipes.
Own: intake.py, planner_vision.py, approvals.py, approval_migration.py, planner_confirmations.py, planner_consent_views.py.
Also own: planner_confirmation_cards.py, planner_schema.py, mcp_planner.py for these public contracts and projections.
SOLE serial integration owner after 1j: plan_store.py, roundtable.py and tests/python/core/test_golden_path.py; neither lane edits dispatch.py.
Scope shared edits: judgment consumers, consent/intent binding, 1c evidence-packet integration and golden extensions; no broader review/scheduler rewrite.
Fix intake.propose: code gathers baseline/ambiguity/dependency facts; planner judges tiny/small/medium/large and appropriate collapsed process; show user override.
Fix planner_vision.expansion_status: judge improvement adequacy, not 3–7 counts; retain accepted macro/micro improvements and trace links.
Vision Lock records applicable UX/visual, performance, maintainability, architecture, observability and failure criteria; research carries reasons and choices.
For open-loop dreams, record user-agreed metric/provenance and stopping conditions; brownfield maps existing behavior/evidence before change planning.
Fix approvals.record_approval + planner_confirmations._chat_evidence: LLM interprets exact user words; code binds verdict to request, subject/revision and source.
Pull forward PlanStore.accept’s consent repair: nonblank text grants no C authority; human retains A/B/check-in/C decisions and existing C prerequisites.
Fix approvals.intent + PlanStore._classify_vision_edit: gather complete before/after facts; judge intent/impact; narrowing requires visible user-approved deviation.
Enforcement: consume 1j verdicts; missing/stale/inconclusive meaning → pending judgment, never semantic refusal or implicit approval.
Harvest durable confirmation/provenance/migration; delete word-list consent, count-based adequacy and field-subset semantic classification.
Remove budget-bearing decision subjects/presentation while preserving launch provenance; remaining quota machinery belongs to 2b, so DV8 stays open.
Golden: canonical intake→lock→own-words decision→reload demonstrates size override, accepted upgrade, ambiguous consent pending and explicit narrowing decision.
Regression/gap: catches keyword false consent and invisible intent changes beyond Stage 1a trace coverage; add 1c’s golden extension serially in its integration patch.
Ladder: L0 slim process and own-words A/B; L1 brownfield baseline; later L3 metric-search execution remains unproven by these records.
TRIAGE: BUG|DESIGN — identify cause/siblings; fix shared semantic authority, preserve native provenance; no bypass, silent narrowing or invented consent.
```

**Stage 1c — ordinary executable tests; parallel with 1b after 1j**
```text
CHARTER: serves C2–C4/C9/C13/C14/C24/C26 — uses DV4; proposes no additional I1–I9 exception.
Outcome: worker-authored executable tests produce actual observations; typed judgments decide meaningfulness and correct RED.
Own: runners.py, semantic_runner.py, semantic_web.cjs, test_audit.py, proof_imports.py, semantic_schema.py.
Also own: planner_candidate.py and acceptance.py, limited to execution/judgment/evidence consumers; full-dream acceptance remains 2e/4a.
No edits to 1b-owned files, plan_store.py, roundtable.py, dispatch.py or test_golden_path.py; request shared integration from 1b’s sole owner.
Consume Stage 1a test execution.argv/rationale and trace bindings through canonical compilation; preserve its completed graph contract.
Fix semantic_runner.run: remove source-extension/size rules as product eligibility; bounded capture reports omissions without judging the product invalid.
Fix semantic_runner.execute + planner_candidate._semantic_validation: actual exit/output/state observations replace SELDON-STUB/exit-3/marker-coverage RED.
Code gathers test source, requirement links, baseline/candidate identities and observations; flags suspicious patterns without deciding their meaning.
LLM judge issues bound verdicts on meaningfulness, correct failure reason and identified stub/mock gaps; code enforces verdict presence and bindings.
Fix missing-qualitative-judgment→FAIL: absent/inconclusive/unsupported assessment stays pending; observed process failure remains an observation.
Generalize planner_candidate.record_judgment beyond web-only checks to consume 1j records; this does not establish full-quality-bar acceptance.
Fix evidence-relevance row: acceptance.prepare_execution_assessment admits structurally bound evidence without protected-Python-line/ownedCalls eligibility.
Its roundtable._execution_context sibling is integrated only by 1b’s serial owner; judges assess relevance, code verifies hashes/links, no row-closure claim before both.
Harvest process execution, receipts, cleanup, browser observation and provenance; keep language-specific collection optional and non-authoritative.
Delete replaced scenario eligibility, stub RED, AST meaningfulness verdicts and mandatory import/coverage relevance gates; retain useful observation adapters.
Golden extension, applied by 1b: canonical test producer→compile→runner→stored evidence→judge consumer observes missing behavior RED then integrated GREEN.
Include brownfield GREEN preservation, unfamiliar executable/evidence admission, pending judgment and a concrete judged gap; fake providers never fabricate process results.
Regression/gap: catches marker-only RED, unsupported-domain refusal and missing-judgment FAIL; Stage 1a proved trace preservation, not execution.
Ladder: L0 real RED→GREEN; L1 baseline preservation; L2 browser/HTTP and authorized L3 persistence/simulator/HIL/signal paths prove their relevant surfaces.
TRIAGE: BUG|DESIGN — name cause/siblings and remedy; unsure → pending judgment, never refuse; preserve bounded cleanup and provider-owned security.
```

Golden is the first gate; each integrated behavioral patch includes its extension. Prove each behavior once, add no unit tests, report counts against the published base, keep ceilings non-increasing and measure the fast gate ≤10 minutes. Foundations earn no ladder promotion.
No files changed, tests run or providers launched; Stage 1a’s green status was supplied, not independently revalidated.