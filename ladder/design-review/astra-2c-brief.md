CHARTER: serves C1–C4/C8/C10/C13/C14/C16/C18/C20/C23/C25 — uses DV5 during restoration; proposes no I1–I9 exception.
Stage 2c: one implementation lane, **Sol high**, including SDK transport, deterministic continuation and bounded ownership.
Reviewed `49b1b80da3f5ac2b274f1504dce30d3be3c81e17`, clean checkout; original 2c/CC addendum, r4/r5/r7/r9/r11/r14 and retained capability audit. No files changed, tests run or providers launched.
Last proven product outcome: retained ShelfLife runs demonstrated substantial working behavior; integrated delivery/full acceptance remains unproved. Increasing planner-call allowance would not repair the identified machinery.
TRIAGE: DESIGN — scheduling is distributed across planner instructions, status projections, resume helpers and worker continuation; siblings: phase ordering, recovery successors, assessment preparation and acceptance.
TRIAGE: BUG — `planner_jobs.py:498` and `planner_candidate.py:75` consume `execution`, while the public producer accepts other check names; siblings: accepted answers that no downstream consumer can use.

One owner implements `run_loop`, its typed questions and changes in `plan_store`, `planner_schema`, `mcp_planner`, `plan_cli`, `planner_{jobs,candidate,recovery,execution,resume,guidance,views,consent_views,stdio,connection}`, existing attempt owners and `dispatch`; narrowly adjust approvals and SDK packaging.
Extend the existing golden/approval journeys and their support code in the same patch. Preserve domain owners, provenance, approval binding, candidate evidence and provider protections.
Exclude concurrency restoration, wave-model redesign, legacy-runtime removal, new completeness machinery and unrelated ShelfLife/browser repairs. Existing wave boundaries must feed the same steering path; Stage 3b still owns its wave obligation.

Use **one durable run controller**, extending the existing detached controller, with `run_loop` as its only continuation policy. MCP is its command/view transport.
Reuse `graph.ready_beads`, dispatch integration and existing process owners. Dispatch executes bounded work and returns observations; remove its autonomous continuation/retry decisions. Do not create a competing ready queue, supervisor service or scheduler.
Persist the cursor/substate, pending question and control generation in existing PlanStore transactions/events. Existing phases and views read this authority; do not maintain another independently writable phase model.
On activation, reconcile recorded effects, then perform deterministic steps until a semantic question, bounded active attempt, user decision or terminal outcome remains.

| State | Deterministic transition |
|---|---|
| PLAN | Ask for meaning: understanding, expansion, research, trace and bead content. Save through existing canonical writers; validate structure, compile and prepare review automatically. A remains actual user Vision Lock. |
| REVIEW | Select the planner’s authorized reviewer tuples, prepare exact packets, run reviewers, consume bound verdicts/dispositions/convergence. Concrete gaps return to PLAN/STEER; unresolved meaning stays pending. |
| WAIT_USER | Present A, B, research choices, wave check-in or C with retained context. Approval continues only its bound action; requested changes return to semantics; decline suspends that action. No running attempt is held. |
| BUILD | After applicable approval, advance/publish/admit internally; dispatch eligible work using existing dependency/ownership rules. Terminal observations enter OBSERVE. |
| OBSERVE → JUDGE | Retain candidate, execution observations and cleanup receipts; finish the execution segment before requesting semantic credit. Prepare the exact consuming judgment automatically. |
| STEER | Apply the recorded planner direction: continue, repair, replan, research or ask the user. Changed scope returns to user approval; unchanged evidence is reused under existing rules. |
| NEXT | Accepted Contracts RED releases eligible Build work; integrated GREEN triggers steering/check-in or current acceptance flow. Only actual bound C reaches DONE. |
| PAUSED / STOPPED | Pause prevents new admissions and settles active work through existing cancellation; stop additionally revokes continuation. Explicit resume reconciles canonical state before proceeding. |

TRIAGE: DESIGN — `PlanStore.advance` currently requires B before entering roundtable, contrary to charter review→B; siblings: initial review, rereview and reviewer permissions.
Separate authorization for planning/reviewer invocations from final product-plan B. Preserve explicit provider/model grants and host permissions; missing permission remains an explained prerequisite. Never invent consent or move B earlier merely to satisfy the old guard.

Every question contains `requestId`, role, purpose, current revision/candidate binding, actual evidence references, answer schema and rationale/context. Code supplies identity namespaces and check labels.
Use four question families; closed options describe control outcomes, while product content, research and rationale remain domain-open:

| Question and state | Typed options | What code does |
|---|---|---|
| **Planner: author the requested meaning**, PLAN | `draft`, `ready`, `research`, `ask_user`, with canonical node/amendment payload | `draft` saves work; `ready` runs structural prerequisites and the appropriate review/A transition; `research` records criteria and launches only authorized research; `ask_user` records the real question and suspends. |
| **Judge: assess this bound subject**, REVIEW/JUDGE or semantic ambiguity | Existing 1j `positive`, `negative`, `inconclusive`, `unsupported`, with purpose-specific typed meaning | Positive credit goes only to its named consumer; negative names concrete gaps and triggers steering; inconclusive/unsupported release the invocation and retain pending meaning. New evidence/direction is required before another attempt. |
| **Planner: choose direction**, failures/stalls/discoveries/wave ends, and unsolicited anytime | `continue`, `repair`, `replan`, `research`, `ask_user`, `pause`, `stop` | Continue uses existing eligible work; repair creates worker-owned changes; replan applies semantic amendments/re-splits and deterministic stale-marking; research/user/control choices follow their existing authority boundaries. None overrides failed proof. |
| **Judge: interpret retained user words**, WAIT_USER | `approve`, `changes_requested`, `decline`, `unclear` | Existing confirmation owner records the interpretation against the exact subject. Approval requires actual words/provenance; changes return to planning; decline suspends; unclear asks clarification. No semantic answer authenticates a human. |

The judge family retains explicit schemas for review/convergence, finding disposition/reuse, scope impact and execution meaning; it is not a generic free-text “what next?” prompt.
For Contracts and Build, prepare **`check="execution"`** with the observed phase and immutable `evidenceBinding`; the answer cannot choose another label or substitute a hash for an evidence-record ID.
Reuse 1j prepare/submit/read and its two exact-fix retries, then recorded steering. Add no judge store or parallel retry counter.
Planner/judge invocations use the existing provider-normal launch path and authorized role tuples, returning structured semantics; native chat remains the conversation surface. **Do not assume MCP itself can initiate host-model completions.**
Planner steering is accepted in every nonterminal state, including during an invocation. Commit the interrupt first, prevent affected new launches, settle affected attempts, invalidate superseded answers and preserve unaffected work. Semantic changes never become planner-authored source code.

Shrink planner mutation tools to **`harness_plan_start`, `harness_loop_answer`, `harness_steer`**; retain useful read-only schema, status, node, packet, judgment, review and mail inspection.
`loop_answer` submits only the outstanding typed question; `steer` carries unsolicited direction, semantic amendments, actual user control and structured mail through existing writers.
Delete planner-facing `advance`, `compile`, `publish`, `roundtable`, readiness/audit launch-and-poll, worker start/status polling, acceptance launch/rebind/review/assess orchestration, recovery resolution and `plan_resume`. Their domain operations become internal steps.
Fold node/reviewer/finding/scenario/question/assumption/confirmation writer aliases into typed answers; preserve their canonical implementations. Remove planner source-edit routes such as `revise_test`; workers own code/tests.
CLI and cockpit read the same cursor/baton; CLI controls enter the same controller. No alternate CLI continuation policy. Native confirmation transport retains its distinct provenance.
Adopt the official MCP Python SDK in this lane; delete replaced JSON-RPC framing/session machinery while retaining workspace binding, confirmation identity and domain checks.

The C23 baton references canonical decisions, assumptions, questions, accepted vision, current revisions, retained candidate/attempts, pending semantic request, next safe action and why.
Commit answers/control/cursor atomically before acknowledgement; record effect identity before launch. Reconciliation consumes existing receipts instead of repeating completed effects. An ambiguous launch is not blindly retried.
MCP restart reattaches to the live controller or resumes the same authorized run after ownership reconciliation. Context replacement reads the same baton; paused/stopped runs remain paused/stopped.
Transport loss preserves durable request identity and pending state; reconnect uses a fresh wire ID. Lost replies neither approve nor cancel; stale wire or subject replies cannot grant authority.
On wake, detect the elapsed-time gap from persisted observation/deadline times and reconcile in-flight attempts **before dispatch**: completed→consume; verified live within deadline→reattach; expired→existing cleanup/release; unknown→quarantine.
Sleep does not reset attempt deadlines or recovery counts. No process can write while the host sleeps; expired ownership is materialized on the first resumed controller turn. Never change OS power settings.

Each admitted attempt has a persisted finite deadline and owner generation. Existing process owners terminate/drain their own children and retain receipts; a silent model is not killed by a new inactivity heuristic.
Delete `execute_worker_job`’s post-execution judgment wait and the original-PID-only continuation dependency. A bound answer resumes the retained run in a fresh bounded controller segment, without relaunching completed bead work.
**The active run_loop releases a dead/expired owner**, using existing recovery writers; after controller death, its replacement performs the same transaction. Expired generations cannot integrate, deliver or acquire new credit.
Release logical ownership separately from process quiescence. Missing cleanup evidence records `ownershipReleased=true`, `quiescenceVerified=false`, quarantine, reason and one concrete next action; it never fabricates exit.
Late receipts may improve the recorded liveness observation, but cannot resurrect an abandoned attempt. Unknown old namespaces are never reused; authorized recovery uses isolation and a verified source.
Use the existing per-bead recovery lineage: two automatic recoveries, then planner steering. Revision changes must not reset that allowance for unchanged work. Genuine permission denials are not retried automatically.
No watchdog scheduler: the run controller consumes completion/deadline events; existing process owners perform cleanup. Pending user/semantic work owns no process, reservation or indefinite claim.

Deletion target against this base: **retire ≥3,000 obsolete `src/` lines; net remove ≥2,000 after all replacements**. Baseline is 34,707 physical / 32,413 nonblank lines; target ≤32,707 / ≤30,413.
Target ≥1,800 obsolete lines in MCP tool wrappers, `_next`, `resume_*`, `handle_line` and manual session orchestration; ≥550 in competing view/consent continuation logic.
Delete `planner_guidance.py`, `planner_resume.py`, replaced `planner_stdio.py` machinery (287 current lines), and `plan_cli.next_command` (165); retire remaining duplicate worker waits, recovery navigation and advisory-only steering orchestration.
Preserve useful observations at their existing owners; replace heuristic steering authority with recorded planner decisions. Moving code, minifying it or deleting unrelated behavior earns no deletion credit.

Golden is the first gate; extend existing cases, retain the ≤19-case ceiling and measure the ≤600-second fast gate. Each extension names its regression and why current coverage misses it:
- **Autonomy:** canonical planning answers→review→B→publication→Contracts/Build→integrated evidence→current acceptance boundary, through SDK stdio. Existing golden manually supplies the choreography, so it cannot prove C1.
- **Bound judgment continuation:** actual Contracts process exits and releases ownership; its exact execution question is answered; Build resumes once from retained state. Include wrong/stale answer refusal with one remedy. Existing scripted answers supply the correct label and conceal r14.
- **Recovery/continuity:** real controller/MCP death and dropped responses around admission/completion, plus a simulated wake gap, preserve direction and completed work; dead ownership releases once; late results gain no credit; the third bead failure reaches steering. Existing twins require caller-directed recovery.
- **Anytime steering:** interrupt active work, pause/resume/stop, re-split within approved scope, and request scope change. Verify affected admission stops, stale credit cannot return, and user-required changes await actual words. Advisory mail alone does not prove C16.
Count **all planner MCP calls per phase**, including reads/polls currently excluded from “happy” counts; report judge calls separately without relabeling planner traffic. Assert zero planner choreography/poll calls, zero happy-path ordering refusals, and fewer calls in every choreography-bearing phase than its retained baseline.
The happy path needs at most one answer submission per emitted question, plus start; interruptions/reconnects are separately measured. These are development acceptance metrics, never product call budgets.

Risks: SDK reconnection can lose wire context; process launch cannot be made transactional with SQLite; late owners can write after expiry; obsolete views can retain hidden authority. The journeys above must exercise these boundaries, not mock their answers.
Do not add a workflow framework, second scheduler/store, generic reconciliation layer, planner-authored code, product budgets, new confinement or weakened approval/proof gates. Preserve browser-unavailable and privilege-dependent outcomes truthfully.
No second lane is needed for this coherent change. Stronger dream acceptance remains 2e/4a; wave restoration remains 3b. DV5 expiry stays **2026-11-18**; scripted goldens alone do not close it.
Next unproven step: implement this lane, then obtain task-specific authorization for an exact-candidate real-provider replay demonstrating autonomous continuation and bounded recovery.