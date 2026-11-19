Lane STAGE-1B (Seldon reset). This folder = Seldon main with Stage 1a (trace contract) + 1j (typed Judgment record + pending state) + own git. Read CHARTER.md (ratified v1.1, binding), AGENTS.md, then ~/codex-harness/work/ladder/design-review/judge-boundary-1.md and astra-briefs-1bc.md.
Runs IN PARALLEL with the other Stage-1 lane (1b/1c) on DISJOINT files. Edit only the files this brief owns.
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
1j contract to consume: prepare_judgment -> submit_judgment(raw response, source) -> judgment(id, candidate); MCP harness_prepare_judgment / harness_submit_judgment / harness_judgment; consumers read positiveCredit/concreteGap (both false while pending/stale). Do not create a second judgment type.
You are the serial integration owner of plan_store.py/roundtable.py/test_golden_path.py; 1c will hand you ../stage-1c-golden.patch later — do NOT wait for it; CC integrates it after both lanes land.
Lead notes (CC): code gathers + flags, LLM judge issues the verdict, code enforces the verdict exists and is bound; unsure -> pending, never refuse. Delete what you replace (I9). Timebox 90 min, effort high. Report opens with CHARTER then TRIAGE lines and lists which judge-boundary rows are now fixed.
FAST-LANE RULES (append to every Seldon fix brief; binding — Oren: NO unit tests, ever)
- Lane folder comes from work/lanes/make-lane.sh: it contains NO tests except the golden path. Do not write new test files.
- The ONLY test you may run: bash ~/codex-harness/work/lanes/golden-gate.sh <lane> <tag> (stub golden path CLI+web). Run it once at the end, at most twice. Prove behavior by extending golden-path scenarios, never with unit tests.
- Timebox 45 min, effort medium. One or two failure clusters per lane; the brief names the refusal code and the owning file/function — start there.
- Report <=12 lines; exact patch + sha256; no pushes.
- CC rejects any patch whose command log ran another pytest (work/lanes/check-lane-log.sh).
- All scratch/temp/basetemp goes under C:\seldon\tests\<lane> (add it with --add-dir). Never create folders at the C:\ root or under ~\t.
- TRIAGE (Oren 11-04, binding): the report's FIRST line is `TRIAGE: BUG|DESIGN — <why> — sibling cases: <codes/gates with the same shape, or none>`. BUG = local mistake in sound logic: patch it. DESIGN = the rule itself causes the failure, or a 2nd+ blocker of the same shape: fix the shared rule at ONE owner and cover every sibling; never add another special case. CC rejects reports without a TRIAGE line, or BUG with siblings.
Final gate run must be the last thing after your last edit, and green; if not green, say so plainly. Report ../stage-1b-report.md; patch ../stage-1b.patch + sha256 (diff vs lane base). Scratch: C:\seldon\tests\stage-1b.
