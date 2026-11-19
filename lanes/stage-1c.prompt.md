Lane STAGE-1C (Seldon reset). This folder = Seldon main with Stage 1a (trace contract) + 1j (typed Judgment record + pending state) + own git. Read CHARTER.md (ratified v1.1, binding), AGENTS.md, then ~/codex-harness/work/ladder/design-review/judge-boundary-1.md and astra-briefs-1bc.md.
Runs IN PARALLEL with the other Stage-1 lane (1b/1c) on DISJOINT files. Edit only the files this brief owns.
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
1j contract to consume: prepare_judgment -> submit_judgment(raw response, source) -> judgment(id, candidate); MCP harness_prepare_judgment / harness_submit_judgment / harness_judgment; consumers read positiveCredit/concreteGap (both false while pending/stale). Do not create a second judgment type.
Golden extension: you may not edit test_golden_path.py. Write your proposed golden-path extension as a separate file ../stage-1c-golden.patch (diff against the lane base) for the 1b integration owner, and prove your behavior meanwhile by running the existing golden gate unchanged (it must stay green).
Lead notes (CC): code gathers + flags, LLM judge issues the verdict, code enforces the verdict exists and is bound; unsure -> pending, never refuse. Delete what you replace (I9). Timebox 90 min, effort high. Report opens with CHARTER then TRIAGE lines and lists which judge-boundary rows are now fixed.
FAST-LANE RULES (append to every Seldon fix brief; binding — Oren: NO unit tests, ever)
- Lane folder comes from work/lanes/make-lane.sh: it contains NO tests except the golden path. Do not write new test files.
- The ONLY test you may run: bash ~/codex-harness/work/lanes/golden-gate.sh <lane> <tag> (stub golden path CLI+web). Run it once at the end, at most twice. Prove behavior by extending golden-path scenarios, never with unit tests.
- Timebox 45 min, effort medium. One or two failure clusters per lane; the brief names the refusal code and the owning file/function — start there.
- Report <=12 lines; exact patch + sha256; no pushes.
- CC rejects any patch whose command log ran another pytest (work/lanes/check-lane-log.sh).
- All scratch/temp/basetemp goes under C:\seldon\tests\<lane> (add it with --add-dir). Never create folders at the C:\ root or under ~\t.
- TRIAGE (Oren 11-04, binding): the report's FIRST line is `TRIAGE: BUG|DESIGN — <why> — sibling cases: <codes/gates with the same shape, or none>`. BUG = local mistake in sound logic: patch it. DESIGN = the rule itself causes the failure, or a 2nd+ blocker of the same shape: fix the shared rule at ONE owner and cover every sibling; never add another special case. CC rejects reports without a TRIAGE line, or BUG with siblings.
Final gate run must be the last thing after your last edit, and green; if not green, say so plainly. Report ../stage-1c-report.md; patch ../stage-1c.patch + sha256 (diff vs lane base). Scratch: C:\seldon\tests\stage-1c.
