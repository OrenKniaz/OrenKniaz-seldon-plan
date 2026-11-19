CHARTER: serves C1–C26 — violates no I#. This designs staged implementation, not a claim of full-charter completion.

**Seldon clean core — design decision**

Build a new Python package with one deterministic loop, one canonical plan, one question builder, and one execution route. Runtime dependencies are stdlib plus the approved MCP SDK; installation is `pip install .`. Git, authenticated provider applications, and product-specific verification tools are environmental prerequisites, not another Seldon runtime.

Use the shape of GenAI-Final-Project’s [`run_turn`](https://github.com/OrenKniaz/GenAI-Final-Project/blob/main/app/modules/agent_router.py): code constructs context, asks a constrained question, consumes the answer, and chooses the next operation. Do not copy its recruiting policies, dependencies, or “last attempt returns anyway” behavior.

The first real outcome is an approved, demonstrated page whose Play button displays “Hello, world!”, followed by ShelfLife through the same machinery. Larger products add records and scheduling, not another execution model.

Basis: [Charter v1.3](C:/Users/oren/codex-harness/work/sprint-20261027/semantic-cc/CHARTER.md), [clean-core decision](C:/Users/oren/codex-harness/work/ladder/CLEAN-CORE-DECISION.md), [inventory](C:/Users/oren/codex-harness/work/ladder/design-review/what-the-code-does.md), and [existence audit](C:/Users/oren/codex-harness/work/ladder/design-review/should-it-exist-audit.md). The clean-core decision supersedes the audit’s recommendation to retain a thin path through existing owners.

TRIAGE: DESIGN — the old core repeatedly makes models reconstruct structure, maintains competing approval subjects, and lacks executable exits from uncertainty. Siblings: unciteable facts in r27, incomplete questions in r28, provenance failures in r29/r32, projection-induced stale B in r30, held RED in r31, and unexpressible replanning plus recursive context in [r33](C:/Users/oren/codex-harness/work/fight-1/r33-diagnosis.md).

**1. THE LOOP — one-page contract**

One controller owns the run. A transition transaction saves its input, result, and next action together. Long operations execute outside the transaction under a recorded attempt and deadline.

Schemas below are closed objects: required fields, no additional properties, explicit nullable values, bounded arrays/text. Every LLM answer includes `why:string` and `citations:FactRef[]`. CODE supplies identities, bindings, phases, provider selection, deadlines, and the continuation; the LLM never echoes them.

| State | One question / strict answer payload | CODE validates; saves | Next state |
|---|---|---|---|
| **ALIGN** | “What improved dream should we agree to?” `VisionProposal{size:tiny\|small\|medium\|large, understanding, users[], scopeIn[], scopeOut[], improvements[], quality[], unknowns[]}` | Shape, complete quality entries; saves proposed Vision Lock and size recommendation. | `DECIDE(A)` |
| **DECIDE(gate)** | Show the actual subject; interpret the user’s verbatim reply. `Decision{choice:approve\|revise\|decline\|unclear, requestedChange:string|null}` | Reply belongs to current request and subject; saves words, origin, interpretation, approval or refusal. | A→PLAN; B→WORK(tests); check-in→next wave/final validation; C→ACCEPTED. Revise/decline→REPAIR; unclear→clarify this same decision. |
| **PLAN** | “What work and semantic checks deliver this accepted vision?” `EditBatch{edits:Edit[]}` | Typed bodies, links, coverage, acyclic dependencies, ownership; atomically saves draft plan. | REVIEW |
| **REVIEW** | “Does this plan deliver the accepted dream?” `Review{verdict:adequate\|gap\|uncertain, gaps:Gap[], neededFacts:FactNeed[]}` | References, verdict consistency, reviewer provenance; saves independent verdict against exact plan. No implementation evidence required here. | Adequate→DECIDE(B); gap→REPAIR; uncertain→STEER. |
| **WORK(task)** | “Complete this assigned test/build/repair/guide task.” `WorkReport{outcome:done\|blocked, summary, artifactPaths[], discoveries:Discovery[]}` | Current B authorization, attempt ownership, actual changed files; saves report and observed diff. A report never proves success. | Tests→OBSERVE(RED); implementation→INTEGRATE; guide→OBSERVE(demo); blocked→STEER. |
| **OBSERVE(purpose)** | No LLM question. Execute the plan’s ordinary command. `Observation{exitCode:int|null, timedOut:bool, executionStarted:bool, outputRefs[], artifactRefs[], cleanupVerified:bool|null}` | Command binding, candidate, deadline and actual outputs; saves observation. | JUDGE(purpose) |
| **JUDGE(purpose)** | “What does this evidence establish for this obligation?” `Judgment{verdict:satisfied\|gap\|uncertain, assessments:Assessment[], gaps:Gap[], neededFacts:FactNeed[]}` | Exact requested assessment inventory, citations, current evidence; saves semantic verdict. | Valid RED→WORK(build); GREEN→STEER(wave-end); final satisfaction→WORK(guide); demonstrated candidate→DECIDE(C); gap→REPAIR; uncertain→STEER. |
| **INTEGRATE** | No LLM question. Integrate owned changes. `Integration{candidateRef, changedPaths[], conflictPaths[]}` | Base, ownership, merge result and delivered bytes; saves integrated candidate. | Success→OBSERVE(GREEN); conflict→REPAIR. |
| **REPAIR** | “What minimal edits resolve this recorded cause?” `EditBatch{edits:Edit[]}` | CODE binds cause and preimage; validates complete proposed graph. Saves proposal. | Semantic impact judgment→apply within authorization, or DECIDE(scope); then affected REVIEW/WORK/OBSERVE. |
| **STEER** | “What concrete next work resolves this situation?” `Direction{choice:gather\|repair\|continue\|next_wave\|research\|needs_user\|cannot_continue, targets:FactRef[], action:ActionSpec}` | Action matches supplied facts and authorization; saves direction. `continue` requires a new executable action, not rejudging unchanged evidence. | Named state/action; wave-end continuation first passes DECIDE(check-in). |
| **ACCEPTED / INCOMPLETE / STOPPED** | No LLM question. `Outcome{accepted:bool, reason, lastProvenResult, nextAction:ActionSpec|null}` | ACCEPTED requires current C eligibility and actual approval. Saves final baton; releases ownership. | Explicit new user input starts/resumes applicable work; never silently restarts. |

`ActionSpec` is a tagged union of a fact read, ordinary command, repair target, user decision, or resume prerequisite. It has no arbitrary “set phase” operation.

**Universal exits:** malformed answers receive two exact-fix retries containing all structural errors, the rejected answer, and the original facts; exhaustion goes to STEER. Semantic refusal carries one concrete correction and goes to REPAIR/STEER. Native permission denial is recorded, never bypassed or blindly retried.

Transient provider failures receive at most two recoveries for the same work, then STEER. Authentication failure immediately tries an already-authorized available provider; otherwise the attempt ends INCOMPLETE with the exact authentication action. Failed steering itself ends INCOMPLETE rather than recursively calling steering.

An inconclusive judge causes a fact-gathering action or repair with changed inputs. The same question/evidence cannot cycle unchanged. If no executable route exists, finish INCOMPLETE with the unresolved judgment and resume prerequisite.

Human decisions are event-driven: save the request and release execution resources. Silence grants nothing. Pause/stop are explicit user controls, not failure-handling states. “No holds” means no leased worker, pending effect, or semantic dead end without an exit; it cannot mean manufacturing approval when the user, provider, or required evidence is absent.

**Ownership:** CODE owns transitions and structure—predictable, but must supply complete facts. LLM owns proposals and judgments—handles meaning, but its conclusions require provenance and observed evidence. This is I1/I2/I10, not an agent framework.

**2. MODULE LIST — milestone 1**

Milestone 1 means a fresh real Hello-world run through actual C, including tests-first, independent plan review, one wave check-in, same-scope repair, interruption recovery, demo and guide. It does not certify the full charter.

Targets count physical source lines, including schemas, prompts, comments and blanks.

| Module under `src/seldon/` | Single job | Charter | Target |
|---|---|---|---:|
| `loop.py` | Own state transitions and next actions. | C1/C16/C18/C23 | 450 |
| `schema.py` | Define and validate the small record/question contracts. | C4/I3/I10 | 650 |
| `store.py` | Commit canonical records, revisions and run cursor transactionally. | C4/C23/I6 | 450 |
| `plan.py` | Apply typed edits, traverse trace, calculate affected records and approval subjects. | C9/C10/C21 | 500 |
| `questions.py` | Build bounded, phase-specific questions and decode semantic answers. | C3/C5/C6/C11/I10 | 550 |
| `providers.py` | Invoke native providers and extract terminal responses. M1 implements the selected provider. | C1/C20 | 350 |
| `processes.py` | Own bounded subprocess lifetime, capture and cleanup. | C18/C20/C25 | 700 |
| `work.py` | Admit owned worktrees and integrate worker changes. | C12/C13/C19 | 450 |
| `evidence.py` | Execute declarations and bind observations to candidate/requirements. | C14/C15/C26 | 500 |
| `frontdoor.py` | MCP chat/status and a read-only status/demo projection. | C8/C20/C25 | 350 |
| Package entry points, registration data and small view assets | Installation and presentation only. | C20 | 200 |
| **M1 production total** | | | **5,150** |

Allow **1,000–1,500 additional lines** for the golden journey and fixtures: approximately **6,150–6,650 authored lines altogether**. These are estimates, not a ceiling that excuses omitted behavior. Ten modules are a starting ownership map; split a genuinely separate responsibility before creating a god file.

For the **full charter**, plan on **11,000 production lines**, with a credible **9,000–14,000** range; approximately **3,000–4,000** further test/fixture lines. The uncertainty is mainly provider behavior, Windows recovery, concurrency and heterogeneous verification.

I disagree with the inventory’s **19–22k** because its estimate starts by retaining approximately 10.8k “KEEP” lines and shrinking existing subsystems. A required responsibility does not imply its current implementation survives. This design eliminates the second graph, scenario interpreter, publication/review/acceptance subprotocols, provider telemetry accounting, and old-format migration.

I also disagree with promising the **entire charter in 3–5k**. Concurrency, current-run recovery, brownfield preservation, multiple native providers and truthful proof have real implementation cost. M1 can be a few thousand lines; the complete product probably cannot.

**Ownership:** CODE for these boundaries; benefit is one visible owner per truth, cost is explicit integration work rather than delegating orchestration to the model.

**3. DATA — one plan and bounded facts**

Use project-local `.seldon/state.sqlite3` and an adjacent immutable artifact directory. Four tables suffice:

| Table | Contents |
|---|---|
| `run` | Current state, plan revision, candidate, active attempts, outstanding decision, continuation and generation. |
| `plan_revision` | Immutable canonical plan document, parent revision and content digest. |
| `record` | Immutable typed messages, questions/answers, reviews/judgments, approvals, edits, attempts, observations and outcomes. |
| `artifact` | Content digest, relative location, producer record and media type for logs, screenshots and delivered files. |

SQL indexes serve lookup; no vector database, event-sourcing framework, separate finding database, or Markdown authority. The current plan is a pointer to one immutable revision. Views never write it.

The minimum plan contains:

- **Vision:** understanding, accepted improvements, scope, quality criteria and assumptions.
- **Feature:** story meaning and acceptance intent.
- **Requirement:** observable obligation, relevant design and interface-contract sections.
- **Test:** requirement links, semantic purpose, ordinary command, required environment and expected evidence.
- **Bead:** task, owned paths, dependencies and requirement/test links.
- **Wave:** bead membership, preceding result links and check-in.
- Execution records add actual code/results to these links after work exists.

For tiny products, story/design/contract meanings are typed sections with addressable references, rather than compulsory separate nodes. Each still has matching verification links. Large plans split those sections into separately addressable records using the same reference mechanism. This exercises C5 without deleting C9.

No product-domain vocabulary is closed. “Browser”, “DSP” or “Python” are facts about a particular plan, never admission categories.

**Approval binding**

- **A** binds the canonical Vision Lock.
- **B** binds the reviewed plan revision and its authorized execution scope.
- **Check-in** binds the completed wave, integrated result and proposed continuation.
- **C** binds the accepted scope, exact delivered candidate, evidence and walkthrough.
- Reviews bind the canonical content actually reviewed and observed reviewer identity. Markdown generation, timestamps and reviewer availability do not alter product meaning.

A within-scope execution repair may inherit B authorization only through a recorded semantic impact judgment connecting before and after. The original approval remains unchanged; the new revision points to its authority and impact verdict. Changed accepted meaning returns to the user. A pending reply never silently transfers to a changed subject.

CODE detects changed content and dependencies; the LLM decides whether a semantic edit preserves authorized scope. Hashes establish identity, not semantic equivalence. For M1, any semantic plan edit receives a fresh compact plan review; later, affected-subgraph review reuses unaffected verdicts.

**Question construction**

Every question gets one flat fact table: `FactRef → {sourceRecord, revision, boundedContent}`. Every supplied fact—including failed attempts and rejected answers—is citeable through this table. There is no second citation allowlist.

Supply the original relevant user words, current obligations, setup facts, target records, pertinent before/after content, and newest relevant observations. Historical records remain references; never embed an earlier question’s entire context inside a later one.

Start with a **64 KiB request-content cap**, lowered when the provider requires it. Reserve room for schema and answer. CODE pages oversized subjects into bounded questions with explicit coverage; it never silently truncates an accepted obligation. A judge requesting missing facts receives a new question after CODE retrieves them.

Each question includes a small valid example and an uncertainty example. Paths, interpreter identity, available tools, provider roles and current references come from setup/store—not model discovery.

**Ownership:** CODE owns identity, retrieval, coverage and persistence; LLM owns interpretation. Benefit: bounded, reproducible inputs; cost: deliberate question-specific projections.

**4. REPAIR — the same mechanism before and after B**

One `EditBatch` works for initial planning, review findings, failed RED, failed GREEN, discoveries and rejected C:

```text
Edit =
  Put {kind, targetHandle, typedBody}
  Retire {targetHandle, replacementHandles[]}
  ReplaceLinks {targetHandle, relation, targetHandles[]}
```

Bodies use the record’s strict schema. These are record-level edits, not arbitrary JSON paths or a general graph-editing language. Temporary handles name newly proposed records; CODE assigns durable IDs and resolves links.

CODE attaches the triggering record, current revision, authoring invocation and original evidence. A review, judgment, observation or user message is already a valid cause. No fabricated “discovery” node is required to make provenance legal.

Apply the complete batch atomically against its preimage. Validate the resulting graph, not partially applied edits. This permits bead consolidation, ownership transfer, dependency removal and acceptance-link transfer in one operation.

Before B, plan defects are ordinary edits; only changes to accepted vision need the user. After B, the same edits receive impact judgment: implementation changes within authorization proceed; changed scope returns for approval. Uncertainty gathers facts and never counts as authorization.

CODE stale-marks reachable affected evidence. Existing observations retain their original provenance; they are neither deleted nor relabeled as fresh. Repairing code under an unchanged test does not repeat valid RED. Changing the test’s semantics requires a new meaningful baseline.

A gap closes only through subsequent evidence and judgment, not because the repair author says “resolved.”

**Ownership:** LLM proposes changes and judges semantic impact; CODE binds, applies and invalidates. Benefit: r29/r32/r33 share one repair route; cost: atomic edits must express structural replacement completely.

**5. TESTS FIRST — including missing products and missing browsers**

A test worker writes ordinary semantic tests before implementation. Seldon executes their declared commands and records what happened. No AST proof, import instrumentation, source-pattern oracle, synthetic stub markers, or Seldon browser-action language.

A nonzero exit is an observation. The judge determines whether it demonstrates the intended missing behavior. **A test failing because the product does not exist is valid RED** when the test’s own prerequisites work and its attempted product interaction establishes the absence.

| Product/situation | Correct RED and verification |
|---|---|
| **No server** | Invoke the actual CLI/library/file/data workflow. Missing executable, module or expected product artifact can be correct RED. GREEN must demonstrate the promised behavior with real inputs and outputs. |
| **Browser product** | Run an ordinary browser test against the intended user path. For Hello-world: open the page, find Play, activate it, observe “Hello, world!”. A static page may use `file://`; Seldon does not require an HTTP server. |
| **Product server not built yet** | A functioning client failing to connect to the declared absent product can be valid RED. First distinguish absent product from broken browser/client tooling. |
| **Browser unavailable** | Record the actual failed/missing capability. Run other valid checks and continue authorized implementation, but browser obligations remain unverified. Obtain an existing authorized browser path or a real human-operated browser walkthrough; never substitute HTML inspection for interaction. |

The core does not implement a browser driver to satisfy its dependency limit. Worker-written tests use an available standard browser tool or the provider’s configured browser capability. Required product tooling is declared honestly; `pip install .` installs Seldon, not every possible product environment.

Zero tests executed, all skipped, collection failure, or missing test tooling do not establish GREEN. They also do not automatically establish product RED. Raw receipts retain these distinctions; semantic judgment handles unfamiliar runner output.

For the Play page, the quality bar includes clear control labeling, visible response, keyboard activation where accepted, and a usable walkthrough. An exit code cannot establish visual quality; the judge needs actual browser evidence.

At C, **“couldn’t verify” means exactly**:

```text
accepted = false
verification_complete = false
evidence_state = awaiting       # stale when applicable
reason = observed unavailable verification path
next_action = the concrete way to obtain the missing evidence
```

It means neither “the product is broken” nor “the product passed.” An informational C report may expose that outcome, but **full C acceptance is unavailable** while a required C15/C26 obligation remains unverified. User willingness to take an unverified artifact is recorded as such; it does not rewrite proof.

This is the necessary reading of I2 alongside C15/C26. Waiving full-C evidence would require an explicit charter deviation/change, not an implementation shortcut.

**Ownership:** CODE runs and binds observations; LLM judges meaningful RED, adequacy and quality; user accepts the demonstrated result. Benefit: truthful verification; cost: some environments cannot complete C.

**6. STUB TESTING — the main test**

Extend the existing `tests/python/core/test_golden_path.py`; it remains the first gate. Use one journey driver with scripted provider replies selected by question kind and occurrence.

The offline journey uses real SQLite, real transitions, real temporary worktrees, real subprocesses, real failing/passing product tests, actual integration and the real C eligibility path. Only provider reasoning and user conversation are scripted.

Scripted workers materialize test/product files into their assigned worktrees. They do not write receipts, set phases, return canned test results, or call acceptance internals. The fake judge supplies semantics; independent journey assertions check the delivered behavior and canonical state.

**Day-one portable fixture:** a small command product, allowing complete A→B→observed RED→implementation→integrated GREEN→check-in→demo→C without browser installation. The Hello-world browser twin uses a real installed browser. Its absence produces the incomplete branch, never a fake UI pass.

Target **about 60 seconds** for the portable journey: no provider latency, polling sleeps or unnecessary server. That is a measured future target, not evidence obtained in this design task.

Reuse the same journey for these consequential faults:

| Journey variation | Behavior protected / realistic bug | Why the happy path misses it |
|---|---|---|
| Review gap → repair; later execution gap → repair | Both phases consume real causes, preserve ownership and reach C after repair. Catches r29/r32/r33. | Successful initial answers never exercise edits. |
| Inconclusive RED, missing browser, provider timeout | Every uncertainty gets an action or honest incomplete outcome. Catches r28/r31 and false GREEN. | Available tools hide missing-exit defects. |
| Interruption plus changed approval subject | Resume committed work once; reject stale replies and late results. Catches duplicated work and r30-style binding failures. | An uninterrupted run never challenges identity. |

Keep these inside the existing semantic journey structure; add no unit-test layer and do not raise the existing suite ceiling of 19. Mark the fast gate and measure it against the ten-minute limit.

**Recorded-answer regression:** capture question schema, bounded facts, raw terminal answer, provider/version, and resulting source artifacts during authorized real runs. Replay those answers through the ordinary decoder and loop; rerun actual commands against reconstructed workspaces.

A recording matches its question contract and facts. A changed contract produces a fixture mismatch, not silent historical migration. Redact private material before committing fixtures. Old r27–r33 answers that use obsolete contracts remain diagnostic examples; they are not advertised as exact new-core replays.

Recorded answers catch real model-output assumptions that hand-authored fixtures miss. They do not establish current provider availability or fresh product acceptance. Ladder L0→L3, ShelfLife comparison and Oren’s real project remain outside-suite acceptance.

**Ownership:** CODE executes the journey; scripted/recorded LLM outputs replace inference only. Benefit: fast whole-loop regression; cost: real-provider evaluation remains indispensable.

**7. REUSE — a closed lift list**

Default: rewrite. Import nothing from `codex_harness.core`.

| Exact old source | Lift | Why cheaper than rewriting |
|---|---|---|
| [`audit_process.py`](C:/Users/oren/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/audit_process.py) | `process_observation`, `_BOOTSTRAP`, `_WindowsJob`, `_run_portable_process`, `run_audit_process` into `processes.py`, with process-oriented naming. | Self-contained stdlib process lifetime code; Windows handle, pipe and descendant cleanup details are expensive to rediscover. No plan/audit engine comes with it. |
| [`process_launch.py`](C:/Users/oren/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/process_launch.py) | `hidden_process_kwargs`. | Eleven-line Windows launch behavior; no semantic concepts or dependencies. |
| [`provider_response.py`](C:/Users/oren/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/provider_response.py) | The Codex structured-terminal extraction portion of `_response`. | Already distinguishes final agent output, completion and provider failure. Retain that small parsing behavior, not the whole multi-provider fallback contract. |

These are source lifts, not transferred acceptance claims. Windows privilege-dependent behavior must be demonstrated in the new integration; denied or unperformed checks remain explicit.

Rewrite graph/store/approvals/questions/provider command construction. Their responsibilities survive; their overlapping representations do not. Do not lift `managed_paths`’ historical-path fallback, `worker_packet_budget`’s fixed provider budgets, scenario runners, AST inspectors, review-reuse machinery, or old-format continuation code.

The existing golden journey remains the test entry point, but its old internal orchestration is replaced. Historical diagnostic fixtures are evidence, not production dependencies.

**Ownership:** CODE primitives only. Benefit: retain hard-won OS behavior without importing the old product model; cost: integration still needs proof.

**8. BUILD ORDER**

| Milestone | Deliverable and acceptance |
|---|---|
| **Day one: complete stub spine** | New package, minimal contracts/store/loop and portable scripted journey from A through actual C eligibility. Real RED/GREEN and delivered output; no direct store seeding to skip states. |
| **M1a: repair and continuity** | Same journey handles pre/post-B repair, unchanged-evidence uncertainty, stale approval and interruption. Every exit has a next action. |
| **M1b: real Hello-world — M1 complete** | Native provider writes tests/product; independent plan review is honestly labeled; real browser demonstration and Oren’s C. Target production total: 5,150 lines. |
| **M2: ShelfLife** | Fresh run from its actual brief, same plan and question shapes. Exercise persistence, importer/API/UI obligations from that brief, repair and full-dream assessment. Recorded answers become regression inputs. |
| **M3: concurrency and successive waves** | Independent beads run concurrently; conflicting ownership waits with a reason; integration, check-in and next-wave planning consume previous results. |
| **M4: remaining charter journeys** | Research, brownfield, open-loop search, cross-provider operation and sourced memory demonstrated through the extension points below. Full ladder and real-project acceptance close the charter. |

New production code lives in **`src/seldon/` in this repository**. No `clean_core` mode, legacy adapter, import bridge, or parallel public command family. Development uses the new package directly; installable entry points switch together at cutover.

Freeze the old core now. Preserve its history and retained run artifacts. At the **ShelfLife cutover**, remove `src/codex_harness/core/`, old-only entry points and obsolete test support after checking repository callers. Do not keep dead implementations merely because later capabilities remain to be rewritten.

Deferred charter capabilities remain explicitly missing in the capability audit; ShelfLife cutover is not full-charter release. If an intermediate deployment claims those capabilities, register the necessary time-bounded deviations first. Existing deviations do not automatically authorize this replacement or extend their expiry.

Future discoveries go into the existing discovery/capability ledger, with owner and exit behavior. No new evidence-packet system.

**Ownership:** CODE for packaging/cutover; owner for reset approval and real-run authorization. Benefit: an executable slice every milestone; cost: old-core retirement and incomplete-charter status must remain explicit.

**9. WHAT THE CHARTER REQUIRES LATER**

These are required capabilities, not speculative infrastructure. Each extends one existing boundary.

| Later capability | One extension point | What changes |
|---|---|---|
| Elastic parallel beads — C12 | `work.py` ready-work selection | Admit all dependency-ready, nonconflicting work within observed machine/provider availability; no fixed product bead cap. |
| Successive waves — C17 | `loop.py` wave-end continuation | Existing STEER/check-in creates the next wave using prior integrated results. |
| Research — C7 | `WORK(task)` | Execute evidence-gathering tasks; use DECIDE(research) for real choices and explicit prototype authorization. No disguised pre-B product implementation. |
| Brownfield — C24 | `plan.py` baseline records | Map existing features/tests/evidence before change planning; preserve demonstrated GREEN obligations. |
| Open-loop work — C22 | `STEER` question contract | Add metric observations and agreed stop conditions; iterations use ordinary work and evidence records. |
| Advanced crash/transport recovery — C18/C23 | Recorded attempt lifecycle | Reconcile committed outcomes before retry; fence late results; retain completed work. Never relaunch uncertain owned writers until quiescence is established. |
| Project lessons and mail — C19 | `record` kinds | Add sourced advisory lessons and blocker/question/discovery/handoff messages; question builder cites any lesson used. |
| Claude/Copilot and provider pins — C20 | `providers.py` invocation boundary | Native launch/result adapters, actual capability observations and honest independence labels; no sandbox/chat replacement. |
| Large plans and deeper review — C5/C9/C11 | `questions.py` bounded projections | Split meaningful subjects with explicit coverage; same review and judgment records. |
| HW/DSP/audio/mobile — C7/C22/C26 | Test command/evidence declaration | Ordinary simulators, measurements and device tools produce artifacts for semantic judgment; no new product-type gate. |
| Richer read-only cockpit — C20/C25 | `frontdoor.py` status projection | Show existing trace, workers, reasons and evidence; add no mutation authority. |

Pause, resume, stop, scope changes and basic current-run recovery exist in M1. Later milestones expand their coverage; they do not introduce their first implementations.

**Ownership:** CODE extends execution and records; LLM extends semantic questions. Benefit: the loop remains stable; cost: each new capability still requires its own end-to-end behavior proof.

**10. THREE BIGGEST RISKS — and early detection**

1. **The clean design recreates the old general framework.**  
   Detect on day one: more than one plan representation, model-authored provenance, an LLM choosing phase transitions, or schema fields that cannot express the scripted repair. Stop and simplify the owning contract; do not add a reconciliation layer. Track production size against the responsibility estimate, not an arbitrary “few thousand” promise.

2. **Scripted success hides real provider/context failures.**  
   Detect immediately after the stub spine with a real planning call and then the complete Hello-world run. Inspect rejection frequency, actual prompt size and whether every supplied fact is citeable. Real recorded replies must replay through the unchanged decoder. Do not spend weeks completing abstractions before the first native call.

3. **Verification or recovery prevents delivery—or falsely declares it.**  
   Detect in M1 with missing-product RED, all-skipped output, absent browser, killed controller and late worker completion. Require either demonstrated continuation or explicit incomplete outcome with a usable next action. Cleanup uncertainty never permits duplicate writers; missing UI evidence never earns C.

**Needs Oren:** approval of this reset design and staged scope; task-specific authorization/provider pins for real runs; actual A/B/check-in/C decisions. No charter weakening is proposed. Any waiver allowing full C with missing required verification needs a separate explicit charter decision.

This design task made no edits and ran no tests. The retained diagnoses’ last demonstrated product progress is B followed by test-worker execution; application implementation and C remain unproven. The first implementation acceptance is the day-one whole-loop stub, followed promptly by the real Hello-world path.