CHARTER: serves C1/C8/C20/C23 — violates no I#; preserves I6/I10.
TRIAGE: DESIGN — P duplicated host permissions before understanding/A and advertised own-words replies while consuming /authorize. Siblings: planner/judge/reviewer bootstrap, changed models, mismatched approval-card consumers.
SIMPLEST: CODE owns invocation authority from frozen kickoff role/provider/model/effort choices; provider hosts own permissions and denials. No LLM decides invocation authority. Tradeoff: later setup edits cannot expand a running run's model choices.

Workspace: C:/Users/oren/codex-harness/work/lanes/stage-noP. Base: user-designated Seldon GitHub main c7219cb, golden-only copy.

Deleted surfaces: approvals.py P kind/effect/subject/explicit-permission record; planner_confirmations.py invocation gate and permission_command; run_chat.py /authorize/native-bootstrap handling; mcp_planner.py P native branch; run_loop.py P requests/continuations; run_setup.py P adoption/readers. Invocation, readiness and review consumers now check frozen kickoff choices, including whole-roster refusal before any unselected reviewer launches. Model restrictions and host execution/denial owners remain intact; semantic-call errors expose the host diagnostic and release the effect without inventing success.

A/B/C retain semantic interpretation. Golden journeys start with understanding, make A the first decision, accept the exact words “yes”, and reach bound C. Moving P's pause/reconnect coverage to A exposed a request bound to generation 1 while its cursor was generation 2; control now saves the new generation before preparing the refreshed A/B request. The same journey proves the repair. Discovery disposition is recorded in docs/legacy-capability-audit.md.

Delta: src +70/-172 = -102 lines; tests +73/-80 = -7 lines; audit +19 lines. Collected tests: 12 base → 12 candidate; no unit tests added. Source ceilings ratcheted down.

Gate command (exactly two runs): bash C:/Users/oren/codex-harness/work/lanes/golden-gate.sh C:/Users/oren/codex-harness/work/lanes/stage-noP noP.
Run 1: 9 passed, 2 failed, 1 teardown error in 414.17s; corrected P-dependent fixture setup and control timing. Web skipped.
Run 2: PASS, exit 0; CLI/approval/guards 11 passed in 537.16s (8m57s); web 1 skipped in 4.52s, browser unavailable. Relevant focused golden corrections passed before run 2. Final source was unchanged during run 2; only the audit's supersession wording/report link was corrected afterward.

Cold start: required python -I -c "import codex_harness.core.seldon_mcp, codex_harness.core.run_chat, codex_harness.core.run_loop" with PYTHONPATH=src PASS using the gate-installed candidate at C:/seldon/tests/noP/p/popen-gw2/w0-cold-start/installed/Scripts/python.exe. The shared interpreter's initial literal check could not locate codex_harness.core because -I ignores PYTHONPATH; isolated explicit-source imports also PASS. All temporary installs/data stayed under C:/seldon/tests/noP; no shared environment install.

Limits/next: fake-provider journeys establish the changed integration behavior, not actual-provider acceptance. Normal-host web proof and a fresh authorized real-provider replay remain unperformed. No runtime state migration or modification of retained r19 was attempted.

Artifacts: stage-noP.patch and stage-noP.patch.sha256. Patch SHA-256: 5c4ac171511813ade796684bc780d2f0beced932f63f93a73c6919577f1f6eb8.


Round 2

CHARTER: serves C1/C8/C20/C23 — violates no I#; restores I6/I10 for retained runs.
TRIAGE: DESIGN — review P2 correctly rejected recovery's reconstruction of invocation authority from mutable setup.json/defaults. This supersedes the earlier retained-run authority claim for the rejected patch.
SIMPLEST: CODE reads frozen kickoff or refuses continuation; settings/defaults can establish authority only when no retained cursor exists. Tradeoff: a run that lost its kickoff must start again in a new workspace with chosen roles.

Owner/scope: run_setup.py deletes adopt and retained-role completion; frozen_setup supplies the single actionable frozen-kickoff-missing refusal for initialization and invocation checks. run_chat.py checks continuation before handling words and sends activation errors as visible MCP notifications, rather than losing them in the startup thread. Pause/stop controls remain available. Host permissions and A/B/C interpretation are outside this repair.

Sibling inspection: reconnect/activation/MCP restart enter run_loop.start → initialize; loop recovery and native/user replies also reach initialize. Existing cursors cannot replace setup even when a caller supplies new settings. Fresh chat/start still freezes validated kickoff normally. Discovery is extended in the lane capability audit; the central ledger is outside current writable roots.

Focused evidence (all scratch under C:/seldon/tests/noP):
- missing_kickoff_golden: RED on the rejected candidate (normal reconnect baton, no refusal); GREEN in 2.84s. A real kickoff reaches A, its frozen authority is removed as a persistence-loss fault, settings change, and actual stdio reconnect emits an actionable refusal. harness_chat returns the same refusal; the real provider-boundary launch log is unchanged.
- reviewer_order_golden: PASS in 8.61s; fresh pinned roles survive changed settings, pause/resume and reconnect through B.
- pytest tests/python/core/test_approval_v2_journey.py::test_canonical_plan_contracts_red_build_validation_pass[frozen-kickoff] -p no:cacheprovider -q -s --basetemp=C:/seldon/tests/noP/round2-focused: 1 passed in 108.74s; ordinary frozen kickoff, recovery through bound C and automatic retry/restart journeys pass.

No full gate was run in Round 2; CC owns host gating. Round 1's broad result belongs to that earlier candidate, not a fresh full pass here. Collected test count remains 12; one semantic journey is added inside the existing golden case, with no unit tests. Source ceiling reduced to 32146.

Round 2 delta versus rejected delivery: src -6 lines; tests +44 lines. Cumulative versus the designated base: src +93/-201 = -108; tests +117/-80 = +37; audit +24 lines. Same owner, tree and candidate lineage; no commits/pushes or lane-local commit identifiers.

Updated artifacts: stage-noP.patch and stage-noP.patch.sha256. Patch SHA-256: be8ae86543ec076ea4dad01dbfc82b76dff35b003bf4cf1404f1671e92e2e756. Actual-provider acceptance and normal-host web proof remain unperformed.


Round 3

CHARTER: serves C8/C14/C20/C23/C26 — violates no I#; preserves I6/I8/I10.
TRIAGE: DESIGN — deleting P's consumers left a base-produced reviewer P cursor waiting forever. Prior Round 2 P2 (missing frozen authority) remains closed; this supersedes the prior claim that every retained P continuation was covered.
SIMPLEST / LLM-or-CODE: CODE retires obsolete invocation requests at run_loop.cursor and resumes the recorded return state under frozen kickoff. Historical P events remain provenance, not authority; pause/stop states and pending semantic questions are preserved. No new state or P gate is introduced.

Item 1: the cursor projection clears obsolete gate=invocations / subject.kind=P requests and restores the recorded PLAN/REVIEW destination for WAIT_USER. The next normal cursor save persists the retirement. Confirmation readers use the same loop-owned obsolete-request rule: pending P judgments are skipped, stale P completions are superseded, and obsolete native elicitation cancellation cannot restore P approval. Missing frozen kickoff still emits the existing actionable refusal before any provider launch.

The new retired_permission_golden runs the untouched designated base source through actual kickoff, A, reviewer-P production and native elicitation, then restarts with the candidate source. Reconnect advances to B with the frozen reviewers and no new P card. The old native response is ignored and the old chat token is rejected without replacing B. This is real canonical producer-to-consumer evidence through stdio, not a hand-built P cursor.

TRIAGE: BUG — LoopClient accepted active RPC snapshots after supplying a provider response. A repeated-Contracts product loop remains unproven; the supplied diagnosis lacked complete identities.
Item 2: progress now skips active/unsettled RPC snapshots after an answered offer and waits for a settled user/terminal result or the next provider boundary. The existing request/effect matching and exact-fix identity checks remain the provider-offer owner. Named fault barriers cannot return the answered effect. The Contracts-to-Validation phase assertion now JSON-renders the full answered/current requestId, judgment id and evidenceBinding, avoiding abbreviated dictionaries. Product phase logic was unchanged for this item.

Focused results, all scratch/basetemp under C:/seldon/tests/noP:
- retired_permission_golden: RED on be8ae865 (reconnect still displayed invocations); GREEN 6.64s.
- missing_kickoff_golden: PASS 2.62s, including actionable refusal and zero new launches.
- planning_surface_golden: PASS 5.58s, including a legitimate exact-fix offer.
- reviewer_order_golden: PASS 10.39s.
- frozen-kickoff pytest journey: 1 passed in 92.12s (journey 91.52s; automatic retry subjourney 7.19s), basetemp C:/seldon/tests/noP/round3-frozen.
- receipt_gaps_golden: PASS 88.25s; one acceptance run/two review slots retained across four real MCP deaths.
- test_golden_path[web]: 1 skipped in 4.07s; browser UNVERIFIED, launch diagnostic C:/seldon/tests/noP/round3-web/web-browser-readiness.json. No browser retry, install or security change.

No full gate was run in Round 3; CC owns host gating. Earlier full-gate receipts remain scoped to their earlier candidate. The observer correction is covered by focused non-browser journeys; the web-specific race correction still requires the normal-host web run. Collected test count remains 12; no unit tests were added. The source-size ceiling remains below the designated base ceiling (32165 versus 32256).

Round 3 delta versus Round 2: src +19 lines; tests +56 lines; audit +8 lines. Cumulative versus the designated base: src +115/-204 = -89; tests +175/-82 = +93; audit +32 lines. Discovery is extended in the existing lane audit. Same owner/tree; no commits/pushes or lane-local commit identifiers.

Updated artifacts: stage-noP.patch and stage-noP.patch.sha256. Patch SHA-256: 1d4cd88287403b0d3cfecf4349dac3d97a916267e74fa779a3312d791de8e7b9. Actual-provider acceptance and normal-host browser validation remain unperformed.
