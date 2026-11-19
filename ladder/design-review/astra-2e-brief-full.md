CHARTER: serves C1–C8/C10–C20/C23–C26 and I1/I2/I3/I6/I10 — proposes no invariant exception.
**Stage 2e: Seldon asks; providers answer; code advances. One Sol-high implementation lane.**
Reviewed clean `semantic-cc` HEAD `a4e7df5cf6e23a64014fd7d71960f01bc2c78094`, Charter v1.2, 2c brief, named core modules, GenAI reference and retained fight evidence. No writes, tests or inference launches; `.env` unread.
Last proven outcome: r14 demonstrated backend behavior, but integrated acceptance remained unproved. r16 stalled after 338s/41 planner calls; r17 after 747s/66 calls.
TRIAGE: DESIGN — broad “author content” questions still delegate configuration and protocol assembly to chat; siblings: reviewer selection, approval binding, evidence labels and gate discovery.
`run_invocations` already reuses the provider launcher, but only requests JSON in prose. `_automatic_question` silently returns when its role is absent; `CONTENT_SCHEMA` contains optional properties and unconstrained objects.

**Ownership and scope.** Tier 2; one `gpt-6.1-sol` high owner, exactly one independent reviewer. Extend `run_loop`, `run_questions`, `run_invocations`, shared provider launch/response handling, existing canonical writers and MCP/CLI ingress; update existing goldens.
Replace the 2c public semantic-answer interface. Preserve its bounded attempts, recovery, transactions and evidence binding. Exclude scheduler redesign, legacy-runtime removal, new sandboxing and unrelated product repairs.
Acceptance: actual user words plus provider answers drive the canonical producer→consumer path; chat supplies zero planner records, hashes, reviewer tuples or transition calls.

**Question contract.** One question per invocation, with a specific schema, few-shot examples and required `rationale`; include `reply` when speaking to the user. Code attaches request identity, generation, subject revision and evidence binding.
H = authorized high-end planner, proposed default Astra high; M = Sol medium; R = authorized independent reviewer, high for consequential work. Preserve provider/model pins; these are role defaults, not availability claims.
`Decision` = `{decision: approve/changes_requested/decline/unclear, requestedChanges:string, rationale:string}`. `Verdict` = `{verdict: positive/negative/inconclusive/unsupported, gaps:Gap[], rationale:string}`; each Gap cites supplied subjects/evidence.

| Question chosen by the loop | Answer schema | Facts supplied by code | LLM or CODE; benefit / cost | Tier |
|---|---|---|---|---|
| Align: what does this person want? | understanding, assumptions[], openQuestions[], reply | Exact words, setup, existing behavior/test map, cited memory | LLM: understands intent / may overlook constraints | H |
| Align: what process size fits? | size: tiny/small/medium/large, rationale | Understanding, consequences, user override | LLM: consequence-aware sizing / judgment varies | M |
| Expand: what should we improve before A? | upgrades[{kind:micro/macro, proposal, impact}], qualityCriteria[], metrics[], stopConditions[], reply | Dream, constraints, alternatives/research, earlier reactions | LLM: preserves C6 pushback / needs discussion | H |
| A: what do these words decide? | Decision | Exact displayed understanding/Vision Lock, actual words and provenance | LLM interprets; CODE records consent: natural speech / ambiguity remains pending | M |
| Research: what uncertainty needs evidence? | choice: proceed/research/ask_user, criteria[], investigation, reply | Known facts, unknowns, available observations, prototype authorization | LLM: identifies useful investigation / can over-research | H |
| Spec: author this trace level or affected slice | Typed feature/story/requirement/design/contract/test records with links | Accepted vision, upstream nodes, brownfield baseline, supplied reference IDs | LLM: authors meaning / needs coverage review | H |
| Plan: how should work be divided? | beads[{objective, ownedFiles[], contractRefs[], dependsOn[], testRefs[], capabilityNeeds}], waveObjectives[] | Trace, repository map, dependency facts, user priorities | LLM: meaningful decomposition / possible poor splits | H |
| Setup/admission: which configured resources run it? | Resolved role tuples, IDs, eligible work and wait reasons | Kickoff pins, supported defaults, resource/conflict observations | CODE: reproducible configuration / cannot judge task difficulty | None |
| Review: does this plan deliver the dream? | Verdict + findings[{subjectRef,severity,classification,issue,remedy}], depthRationale | Exact plan, Vision Lock, coverage, candidate-bound packet | LLM: finds semantic omissions / additional latency | R |
| Review: how should this finding be disposed? | disposition: resolved/rejected/deferred/open, rationale | Finding, response, changed evidence; related findings when needed | LLM: judges substance / may rationalize gaps | H |
| Review: is another round useful? | action: revise/review_again/ready/ask_user, rationale | Recorded independent verdicts, dispositions, changes, round history | LLM: avoids ritual rounds / must not waive concrete gaps | H |
| B: what do these words decide? | Decision | Reviewed plan, execution scope, displayed subject and actual words | LLM interprets; CODE admits: natural approval / requires exact binding | M |
| Build judge: what does this observation establish? | Verdict + requirement assessments | Actual RED/GREEN, test intent, integrated candidate, evidence content; code fixes `check=execution` | LLM: judges meaningful failure/proof / cannot manufacture observations | H |
| Steer: what direction resolves this event? | action: continue/repair/replan/research/ask_user/pause/stop; amendments[], rationale | Failure/stall/discovery, attempts, accepted scope, affected graph | LLM chooses meaning; CODE applies: adaptive recovery / scope judgment can err | H |
| Wave end: what follows from what we built? | nextObjectives[], amendments[], recommendation, reply | Integrated results, remaining vision, user wave preferences | LLM: adapts next wave / needs sufficient context | H |
| Check-in: what does the user want next? | Decision + requestedChanges | Wave result, recommendation, exact user words | LLM interprets; CODE schedules: conversational steering / adds a user wait | M |
| Acceptance: is the whole accepted dream demonstrated? | Verdict + featureAssessments[], qualityAssessments[], stubOrMissingGaps[] | Complete accepted-feature inventory, coverage, integrated real-path evidence, quality bar | LLM judges meaning; CODE verifies coverage: catches green-but-incomplete / evidence can be insufficient | H + R |
| C: does the user accept this demonstrated result? | Decision | Completed evidence checks, live walkthrough, try-it guide, displayed candidate, actual words | LLM interprets; CODE closes: genuine acceptance / cannot replace the user | M |

The table defines separate question types, not a universal optional-content envelope. Review equivalence/reuse and scope-impact judgments retain their own small schemas when needed.
CODE owns phase order, IDs, link integrity, stale-marking, resource scheduling and proof-state transitions: predictable / requires explicit contracts. Semantic uncertainty invokes a judge under I2.
Wave and full-dream questions must connect to existing owners; this lane does not claim to finish the separately deferred wave/concurrency/completeness capabilities.

**Call mechanism — CODE: reuse one launch path; less machinery / provider-specific decoding remains.**
Extend `provider_launch.get_adapter(...).provider_normal_command` and the existing bounded process owner; `run_invocations` supplies question/schema/context. Workers keep their execution mode; semantic calls get a read-only role.
Verified installed help: Codex CLI **0.164.0** supports `exec --output-schema <FILE> --json`, stdin `-`, `--ephemeral`, and `exec resume --output-schema`; Claude Code **2.1.291** supports `-p --json-schema <schema> --output-format json`, `--no-session-persistence`, `--resume`, and `--tools ""`.
Use Codex `exec --sandbox read-only --output-schema <file> --json -`; use Claude `-p --json-schema <JSON> --output-format json --tools ""` with prompt on stdin. Preserve subscription authentication and provider protections.
Parse Codex’s final response and Claude’s `structured_output`, not arbitrary earlier text or Claude’s ordinary `result`. Missing output/refusal is not semantic success. Claude documents a 10MB stdin cap; help exposes no schema-file alternative. [Claude headless contract](https://code.claude.com/docs/en/headless)
Codex schemas use an object root, every property required, nullable values for absence, and `additionalProperties:false` on every object; documented limits include 5,000 properties and 10 nesting levels. The existing schemas need replacement, not merely a new flag. [OpenAI Docs](https://developers.openai.com/api/docs/guides/structured-outputs)
I3 remains intact: close control enums and record shapes; leave behavior, technology, metrics, selectors and rationale as open strings. Use typed record arrays for dynamic metadata; never hide executable interfaces or the whole answer inside a JSON string.
Code supplies IDs and bindings instead of asking the model to echo them. Allocate new IDs canonically; resolve proposed links through supplied handles. Retain one boundary decoder plus canonical referential, authorization and evidence checks.
C4: original attempt + two exact-fix retries against the same question, with precise validation diagnostics; then one steering question. A failed steering question leaves an explained pending/user state, never recursive retry loops.
Reuse the existing retry owner. Claude documents an internal default of five attempts: configure and verify one provider attempt per outer attempt so retries do not multiply; transport recovery remains separate. [Claude retry contract](https://code.claude.com/docs/en/env-vars)

**Context — CODE-built fresh call + canonical baton: restartable and provider-neutral / repeated prefill and launch cost.**
Each packet contains the accepted vision, relevant graph slice, recent actual dialogue, decisions/open questions, cited memory and actual evidence content. References alone are insufficient for a tool-free judge.
Do not resume planner sessions by default. Resume offers cache/local conversational continuity but retains stale facts and provider-specific hidden state; both CLI resume modes still require a process launch.
Illustrative sizing, not measurements: 12 calls × 6k input + 0.8k output = **72k input/9.6k output**; resumed history starting at 6k and growing 1.5k/turn totals **171k input** before cache discounts.
Illustrative latency: 12 × (2s startup + 10–40s inference) = **144–504s**, excluding users, workers and reviews; high-end planning may exceed this. Measure startup, inference, cached tokens and retries separately.
Retained r16/r17 outer input totals were **3.565M/7.395M**, of which **3.441M/7.241M were cached**; they are not comparable per-question benchmarks. Subscription dollar cost is unestablished; no invented per-call price or product budget.

**Front door — CODE transports; LLM converses: natural interaction / one more semantic hop.**
Expose one mutation tool, `harness_chat(text, reply_to?)`; the transport supplies workspace/message identity and an opaque displayed-subject token. Code hashes words, resolves setup/defaults and retains provenance.
The provider-app agent relays actual user words and displays Seldon’s replies, questions, progress and results. It neither authors planner JSON nor chooses gates. Keep useful read-only inspection and the read-only cockpit.
A/B/C/check-in use the same ingress; the server prepares the subject, interprets words and applies the existing confirmation owner. Native responses preserve their distinct provenance; silence or transport loss grants nothing.
A question about the proposal is conversation, not approval. The internal planner must answer, challenge assumptions, offer micro/macro improvements and revise the proposal; C6 must remain visible before Vision Lock.
Pause/resume/stop and reprioritization enter that same path; code applies recorded control before new admissions. Use host notifications where supported, read-only status otherwise; continuation never depends on chat polling.

**Deletions — CODE owns the protocol: fewer exposed choices / canonical checks remain necessary.**
Remove public `harness_loop_answer`, structured `harness_steer`, and planner-authored setup from `harness_plan_start`; replace their MCP/CLI branches with chat ingress. Keep internal answer application.
Delete `CONTENT_SCHEMA`/`apply_options` as universal mutation dispatch, reviewer-selection questions, echoed-identity envelopes, duplicate shape checks and obsolete schema-teaching/gate-discovery guidance.
Retain canonical writers, consent/candidate binding, C4 validation, process cleanup and useful views. Provider schema enforcement does not justify deleting these.
Measured baseline: **32,449 physical src lines**. Preliminary net estimate: **−800 to −1,400**, yielding **31,049–31,649**; schema definitions consume part of the savings.
The **≤30,000** target needs at least **2,449 net deletions**. This inspection does not substantiate that saving from 2e alone; do not double-count 2c deletions or remove required behavior to hit it. Legacy removal remains its existing assignment.

**Golden journeys and decision eval — CODE checks outcomes; humans label meaning: reproducible / stubs cannot establish judgment quality.**
Move stub answers to the provider boundary, selected by typed question and supplied facts; run real context assembly, decoding, canonical writes, scheduling and consumers. The chat fixture sends only user words.
Extend existing journeys for autonomous A→review→B→build→C, C6 changes, r16 subject binding, r17 setup defaults, r14 execution binding, exact-fix exhaustion and restart/control continuity; reuse existing coverage and case ceilings.
Each extension names its protected behavior and realistic regression; current manually assembled answers conceal the protocol failures. Assert resulting user behavior, not private call sequences.
Add **44 labeled decision turns**: 8 Align/Expand, 8 user decisions, 8 spec/review, 8 execution/steer, 6 waves/scope changes, 6 acceptance; include brownfield and HW/DSP examples.
Like GenAI’s action-versus-slot eval, score choice accuracy separately from factual grounding, coverage and rationale. Require zero false approval, false completion or silent narrowing; report confusion by question/tier, latency and tokens.
Goldens prove orchestration with stubs; authorized real-provider replay proves schema compatibility and semantic behavior. Neither alone closes full product acceptance.

**Principal risk:** a schema-valid answer is wrong because the fresh packet omitted a decisive fact. Make packet sufficiency and grounded decisions the central acceptance test.
This is not simpler if “one question” becomes dozens of atomized calls, if prompts reproduce the entire store, or if generic metadata recreates an untyped tool language.
Copy GenAI’s bounded typed decisions and code-supplied facts; do not copy its domain routing rules or add an advisor/synthesis cascade to every step.
Next unproven transition: complete this one lane, pass the affected goldens and decision eval, then perform an authorized exact-candidate real-provider replay; this review establishes design only.
**CC addendum (Oren 11-07, binding for the lane):**
- Copilot CLI 1.0.100 is installed: `copilot -p <prompt> --model <m> --output-format json` (JSONL). It has no schema flag, so the shared boundary decoder validates the answer against the question schema and C4's exact-fix retries apply. Add it as a third adapter on the same launch path.
- Per-role provider+model: each question row's tier (H/M/R/None) maps to a role (think/plan, write, review, judge, mechanical) with a provider+model from kickoff pins/defaults. Prefer a different provider for R than for H (C11). Judges/acceptance stay owner tier; downshifts need paired-run proof. Record the provider+model used per answer.

---
## CC ADDENDUM 2 (2026-11-07): ownership map from three read-only audits — BINDING for 2e
Sources (read them first): `state-machines-audit.md` (18 implicit machines), `truth-dupes-audit.md` (27 duplicated facts), `compensating-code-audit.md` (12 compensation surfaces, 2.2–2.5k deletable). All audited at a4e7df5.

**Rule:** one CODE owner per fact; everything else is a projection that reads it. No giant state machine, no new reconciliation service, no generic state framework. Small declared transition tables live with their owners.

**2e MUST do (in scope, mostly free with "Seldon calls the LLM"):**
1. Request lifecycle: run_loop alone chooses the outstanding question, ONLY from answerable requests. The cursor stores the judgment ID, never a copied judgment. Submission reads the current disposition (SM#1, TD#3; explains the fix17 host "Read the retained judgment").
2. Displayed decision identity: ingress supplies words plus an opaque reference; code attaches request/revision/subject/hash (TD#1, r16).
3. Provider/model/role: kickoff resolves once into canonical role assignments; approvals freeze subsets; every reader uses that (TD#2, SM#5, r17).
4. LLM never echoes IDs/bindings: the schema-bound call attaches known identities from the admitted invocation (CC#8).
5. Pause/resume/steer, retry exhaustion and permission-return continuation are one declared loop transition table (SM#6, SM#2-3 scheduling only; consent evidence stays with its owners).
6. Refusals: producers return `{code, reason, current, nextAction}` at the failure boundary, rendered once; delete planner_refusals' prose-recovery (CC#3).
7. Report the deletion per owner; target ≥ the brief's −800 to −1,400 lines, plus CC#3/#8.

**Out of 2e scope (separate lanes, do NOT fold in):**
- SWEEP (BUG, small, own lane now): recovery `ownershipReleased` always True (SM#4); pending acceptance displayed "fail" (SM#5); readiness pass with pending blockers (SM#7); ordinary review credit keeps an older pass after a later failed review vs policy holding it (TD#4, AUTHORITY); jobId==publicationRevision equality rejects valid recovered successors (TD#5; candidate cause for the :4149/:4259 recovery flake).
- Stage 3d: worker packet reconstruction (CC#2, ~800) and Python execution instrumentation (CC#1, ~800). Preserve behavior first.
- Later: producer-complete definitions unified (SM#6), job status precedence (TD#6), candidate locator (TD#12), acceptance migrations (CC#5).
**Size path:** 2e (~1.0–1.6k) + 3d (~1.6k) + rest ≈ 29.5–30k. The 27k end is NOT substantiated by audit; don't promise it.

## CC ADDENDUM 3 (2026-11-07 21:40): r18 acceptance case — BINDING
Real run r18 (main a3f1e2e) passed A, then BLOCKED in plan after 21 min. Diagnosis: ../../fight-1/r18-diagnosis.md. Chain: trace question → graph rejection "Invalid parent kind for R_ACCEPTANCE" → the planner reported the defect via the universal `content.findings` envelope (which means *dispose existing findings*) → rejected → `run_loop._record_answer → _steering` forwarded only the error string with context {jobId,observation,publicationRevision all null} → repeated steering questions 121→147→173→199→225→314→384, same packet, each with a fresh C4 allowance → asks the user to invent a member id.
2e MUST, with a golden replay of this order (outcome-only): (a) graph/authoring failures recover with a question that carries the rejected relationship + allowed parent kinds, answered by a schema for that repair; (b) a disposition question is never prepared without a canonical finding member (code supplies it); (c) steering is non-recursive: after C4 exhaustion → one steering question → explained pending/user state; a new request for the same unresolved subject with an unchanged packet is refused by a cross-request no-progress rule (same subject + same facts digest = no new allowance); (d) the user is never asked for internal IDs; (e) packets include only relevant nodes, not all spine IDs.
