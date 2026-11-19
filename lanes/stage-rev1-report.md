CHARTER: serves C9/C16/C18 — violates no I1/I6/I8/I9.
TRIAGE: DESIGN — recursive reference revisions imposed a DAG on LLM-owned semantic links; parents-only repair could not edit the refused fields. Siblings: test↔stop-condition, test↔decision and other reciprocal trace references.
SIMPLEST / LLM-or-CODE: CODE binds each node to its own canonical content and referenced IDs, excluding referenced revisions. One shared content_revision serves writers/readers; structural ID/kind validation and parents acyclicity remain separate. LLM chooses semantic links. Tradeoff: content edits require no recursive rehash; retained evidence still uses its recorded revision and existing stale checks.

Tree: ~/codex-harness/work/lanes/stage-rev1. Supplied base: Seldon GitHub main aee12fe. Read CHARTER.md, AGENTS.md, r21-diagnosis.md and the cited run DB using mode=ro&immutable=1. Events 121/129/137 confirm the recurring reference-cycle refusal; event 138 pauses. No run state changed.

Changed: spine.py owns content revisions and actionable cycle refusals; run_content.py binds links without traversal; plan_reviews.py and waves.py reuse the shared rule. run_loop.py, run_questions.py, run_schemas.py and run_context.py reuse the full trace schema for repair, retain rejected records/field diagnostics, and keep linked authored decisions available during replanning. semantic_schema.py names refused reference fields. Existing golden/provider support and the source ceiling were updated; the existing capability/discovery ledger records the defect and gate friction.
Deleted: recursive materialization/cycle refusal for semantic references, the parents-only repair consumer/schema/special packet, and duplicate node hashing. No whole files deleted. No commits, pushes, actual-provider launches, shared installs or lane-local commit identities.

Delta versus base: src +58/-84 = **-26 lines**; tests +44/-6 = **+38 lines**, **0 new test cases**. Source ceiling 32165→32139; suite/fast-gate ceilings were not raised.

Behavior evidence: base reciprocal-link replay is RED with “Trace reference cycle; author acyclic links” (C:/seldon/tests/rev1/red.log). Extended existing r18 planning journey reaches B after reciprocal test↔stop-condition and test↔decision links, refuses/unpersists a genuine parents cycle, repairs a wrong-kind testRefs field through that same repair step, reopens with matching content bindings, and replans after a linked edit without changing the referencing node's revision. Focus passes/29.98s; gate execution of this journey passes/49.27s. These outcome assertions catch the r21 recursive-hash and uneditable-repair defects missed by the former acyclic journey. No unit tests added.

Gate command (1 of at most 2 used):
`bash ~/codex-harness/work/lanes/golden-gate.sh ~/codex-harness/work/lanes/stage-rev1 rev1`
**GATE: RED — 2 failed, 9 passed, 1 teardown error in 887.84s; browser 1 skipped in 7.91s; exit 1; wall 898.98s (>600s).**
- Non-timeout: HTTP recovery faultBeads assertion, tests/python/core/acceptance_support.py:2172; its fixture repeats it as the teardown error. An isolated clean base snapshot HTTP journey passes through A/B/C; concurrent failure remains unresolved, with no established patch or host-load causality.
- Pure deadline failure: main CLI journey, mcp_planner_support.py:496, “No provider/user boundary before deadline”; no revision-cycle refusal. Cause unestablished.
- Browser: UNVERIFIED/unperformed, Chromium context.newPage closed. Cleanup verified, activeProcessesAfterTeardown=0. No security or browser settings changed.

Evidence: ~/codex-harness/work/lanes/golden-rev1.log; C:/seldon/tests/rev1/gate-1-time.txt; C:/seldon/tests/rev1/final-focus.log; C:/seldon/tests/rev1/base-http-canonical.log; C:/seldon/tests/rev1/w/web-browser-readiness.json. An earlier mixed-import HTTP comparison is excluded from base evidence. All temporary snapshots/runs are under C:/seldon/tests/rev1.

Last proven outcome: the assigned fake-provider planning/repair journey reaches B with reciprocal semantic links and canonical, nonrecursive revisions. Next unproven step/blocker: a clean full host gate, including classification of the recovery mismatch and CLI deadline; normal-browser and actual-provider r21/full-vision acceptance remain unverified. This patch does not claim product acceptance. Only the ledger changed after the gate; production/test bytes remained frozen. No second full gate was used to retry unrelated failures.

Patch SHA-256: `4b5b3af8f63546b3b7bed2b6aca55b16a6a2e9e5a8d2a2b1a21205a52be973df`
Deliverables: stage-rev1.patch, stage-rev1.sha256, stage-rev1-report.md in ~/codex-harness/work/lanes.


Round 2

CHARTER: serves C9/C10/C16/C18/C26 — preserves I1/I6/I8. This supersedes Round 1's freshness/repair sufficiency claim.
TRIAGE: DESIGN — nonrecursive identity needs explicit dependency freshness; repair needs CODE-enforced write confinement.
SIMPLEST / CODE: shared dependency capture and currentness check over a visited reference graph, including every top-level TRACE_LINKS field. Check live edge stamps; preserve historical evidence/provenance while binding its captured content. Repair compares the retained rejected answer and permits only named fields; no removal authority or whole-fields fallback. LLM still chooses semantic relationships.

Consumer inventory: retained results and judgments use the shared check; review digests/receipts, global plan/publication/acceptance identity and trace/wave snapshots bind the full node map. Legacy acceptance scenarios and draft subsets capture dependency closure. Worker spec refs include the dependency slice; pinned semantic refs, wave source refs and closure evidence use the same currentness check. Product-intent projections retain their existing exclusions; execution/receipt freshness uses the full snapshot. Historical nested baseline/amendment provenance remains historical. Deleted duplicate impact/preservation walks and the broad repair authority; source ceiling remains 32139.

RED on Round 1 source: repair removed the accepted unrelated leaf; STOP_RESULT remained integrated; the old STOP-only judgment retained positiveCredit (rev1b/red-r1b.log and red-observed.json). Existing planning journey now proves loss of that credit after T changes/rebinds, stale import into an empty store, rejection of unrelated removal/condition edits during metricRefs-only repair, and fresh evidence/judgment with immutable old history. Existing public impact/independent-branch and judgment journeys are reused. No new test cases or unit tests.

Focused final behavior runs: r18 20.69s; trace/public impact 0.72s; judgments 0.12s (rev1b/focus6.log). Independent Sol-medium read-only affected recheck: PASS; reviewer ran no tests. Prior gate reds did NOT reproduce alone on Round 1 source: HTTP reached A/B/C (http-round1-alone.log); CLI main path plus post-C recovery/cockpit/installed-entry checks passed, exit 0/207.56s (cli-round1-alone.log). Original assertion and timeout remain retained; host-load causality is unestablished.

Delta vs supplied base: src +191/-217 = -26 lines; tests +101/-8 = +93 lines; 0 new cases. No lane commits/pushes, actual-provider launches or shared installs. All Round 2 temporary runs are under C:/seldon/tests/rev1b.

One full gate used: `bash ~/codex-harness/work/lanes/golden-gate.sh ~/codex-harness/work/lanes/stage-rev1 rev1b`.
**GATE: exit 0 — 11 passed/597.47s; browser 1 skipped/4.18s; full wall 603.575s. FAST TARGET: MISS by 3.575s (>600s).** No assertion failures or pure deadline timeouts. Browser remains UNVERIFIED/unperformed; readiness diagnostic reports context.newPage closure, cleanup verified and zero remaining processes. Runtime variation has no established cause; no cap/assertion/security changes or retry were used. Gate's extended planning journey passes/45.78s, HTTP/257.55s and ShelfLife/351.34s also pass. Report the functional gate and runtime miss separately; this is not full-vision/product acceptance.
Evidence: ~/codex-harness/work/lanes/golden-rev1b.log; C:/seldon/tests/rev1b/gate-time.txt; focus6.log; http-round1-alone.log; cli-round1-alone-time.txt; w/web-browser-readiness.json. Next unproven step: normal-browser/provider replay and a normal-host full gate within 600s. Only the ledger changed after the gate; production/test bytes stayed frozen.

Last proven outcome: repaired fake-provider planning reaches B, dependent credit expires, and fresh verification resumes with retained history. Actual-provider r21 replay, normal-browser and full-vision product acceptance remain unverified.
Patch SHA-256: `8a16cf2cfff154988c38b2c894b01e0c6706b22226901565c35623b27c5b4e93`. Patch reverse-apply check and checksum match passed. Round 1's supplied base aee12fe is unchanged.


Round 3

CHARTER: serves C9/C16/C18 — preserves I1/I6/I8. H2 confirms both Round 2 P1s closed; this supersedes only its repairability sufficiency claim.
TRIAGE: DESIGN — a later execution/path refusal omitted its editable scope, so CODE confinement rejected the correction. Duplicate parents were a reachable sibling.
SIMPLEST / CODE: structural validators record the refused node/section and editable fields. The shared run_content graph-refusal boundary recovers missing editable scope from that independent location and records repairScopeDefect=true plus an explicit CODE defect message. If an owner supplies neither scope nor location, it raises a CODE defect before the refusal can grant unrestricted direction. No removal, unrelated-node or whole-fields fallback is granted. LLM semantics, shared nonrecursive hashing, visited freshness and evidence-history rules remain unchanged.

Changed: semantic_schema.py adds the shared refusal annotation and labels its trace/execution validators; spine.py names structural fields and gathers invalid bead fields instead of a generic validity flag; run_content.py enforces the nonempty scope invariant. Deleted the redundant proposed-node map and duplicate evidence-outcome comparisons. The existing planning journey and discovery ledger were extended; no whole files deleted.

Validator inventory:
- validate_trace_fields: text and reference shape/ID/kind/revision; baseline ownership/shape/nonempty links/observations; evidence shape/item kind/candidate/source flags/state/observation consistency; amendment required fields/targets; discovery/metric/stop-condition/iteration/baton values. Each refusal names its field or section.
- Test execution owner: object shape and launch failures name fields.execution (entry/module are jointly exclusive); testRoots shape and delegated graph._string/_file_path failures name fields.execution.testRoots; rationale names fields.execution.rationale. Delegated semantic_runner.launch/path covers entry/module/runtime/argv, candidate ownership and path confinement, including traversal, aliases and linked ancestors. No confinement rule was weakened.
- Spine: unknown/invalid/duplicate parents; parent and bead dependency cycles; test module/level; bead contract/capabilityRefs/dependency/lesson shape and kinds; result ancestry; baseline descendant ownership; observed-evidence/baseline preservation; planMode. These carry named scopes, with independent cycle location retained for defect fallback.
- The JSON/schema/identity decoder owns malformed output and membership exact-fix errors before node validation. Global malformed spine/duplicate-ID/vision-count and nonfinite JSON invariants cannot be produced by a schema-valid trace answer with CODE-owned identities. Scenario/HTTP/web observation validation retains its existing pending-judgment behavior; this repair does not turn semantic uncertainty into structural refusal.

Outcome evidence: the final extended existing r18 journey repairs a genuine parent cycle, wrong-kind testRefs and testRoots=["../outside"] in sequence, then reaches the public B plan-execution card. Reciprocal links, retained evidence/judgment invalidation and unrelated accepted-content preservation remain exercised. The same journey on retained Round 2 production source is RED: the retained failure says "Repair only the refused fields {}; preserve all other nodes/content and remove nothing", exhausts its allowance, and never reaches B (rev1c/red-final.log and its read-only observed event record). The fixture stays within the existing two exact fixes; no retry allowance or assertion was weakened. No new cases or unit tests.

FOCUSED: PASS — planning 19.11s; trace/public impact 0.89s; judgments 0.12s; existing source-ceiling guard PASS. Log: C:/seldon/tests/rev1c/final-focus.log. Independent Sol-medium affected read-only review PASS; reviewer ran no tests. All Round 3 temporary files/runs are under C:/seldon/tests/rev1c.
Delta vs supplied public base aee12fe: src +267/-293 = -26 lines; tests +105/-10 = +95 lines; 0 new cases. Incremental Round 3: src net 0, tests net +2. Lowered TOTAL_CEILING remains 32139 and passes unchanged.

GATE: NOT RUN in Round 3, as instructed; CC owns the host gate. The Round 2 gate remains historical evidence, not a fresh gate for these bytes. Last proven outcome: fake-provider sequential structural repair reaches B and the affected journeys pass. Next unproven step: CC host gate; actual-provider r21 replay, normal-browser and full-vision product acceptance remain unverified. No lane-local commit identities, commits/pushes, actual-provider launches or shared installs.

Patch SHA-256: `17eb67fe61cf91ffed92499d68662a4fb83182a21a5b4091954b65c0be002ef1`. Patch reverse-apply, exact diff bytes, checksum and diff whitespace checks verified. Deliverables remain stage-rev1.patch, stage-rev1.sha256 and this report.
