CHARTER: serves C1/C4/C9/C16/C23 — violates no I#; preserves I1/I6/I10, retry bounds and REV1B confinement.
TRIAGE: DESIGN — reference eligibility depended on packet selection, and persisted question schemas could disagree with the current consumer. This supersedes TRACE1's inventory/load sufficiency only; the reviewed completeness and confinement behavior is retained.
SIMPLEST: CODE derives structural choices from canonical authority and retires obsolete question contracts at the existing transactional load owner. LLM meaning remains in the current typed question.

| Design point | LLM-or-CODE | Tradeoff |
|---|---|---|
| Eligible references | CODE: consumer kind contracts over canonical Spine plus declared additions; LLM chooses semantic relationships | Correct existing code/results remain selectable; off-slice packet entries contain only id/kind/title. |
| Obsolete saved questions | CODE: run_setup.initialize retires/re-asks; LLM reanswers the current shape | One migration at load, preserving context, rejected edits, repair scope and fixesIssued; no legacy branch in run_content. |

Reference-field inventory (all node-reference populations now use canonical nodes, not the planning slice):

| Field | Eligible source/contract |
|---|---|
| parents | ALLOWED_PARENTS for the node kind, including declared additions |
| decisionRefs | decision |
| researchRefs | research |
| metricRefs | metric |
| stopConditionRefs | stop-condition |
| iterationRefs | iteration |
| batonRefs | baton |
| evidenceRefs | result |
| codeRefs | code |
| testRefs | test |
| resultRefs | result |
| baseline.codeRefs / testRefs / resultRefs | Same TRACE_LINKS contracts as top-level fields |
| dependsOn / lessons | bead / decision |
| sourceRef | discovery, research, result |
| targetRefs | Any canonical/proposed node kind |
| scenario requirementRefs / contractRefs / testRef | requirement / architecture-design-contract / test |
| action target | Canonical vision targets plus declared target handles |
| expansionRefs | Canonical vision upgrade IDs |
| editable ref identities | Requested outline members only; reference eligibility does not grant edit authority |

capabilityRefs are capability identifiers, not node handles. File/module/runtime/test-root/input paths remain their existing path contracts. Snapshot/action identities are still allocated by CODE. No domain vocabulary was closed.

Saved trace/repair retirement uses the existing interrupt/ask owners in one transaction: supersede the old request, advance its generation, retain its context/repair content, re-ask the edits shape, and carry its exact-fix count. Pause/stop remain authoritative; late old answers cannot match the replacement request. No publication/recovery source was changed.

Focused evidence, all runtime temp under C:/seldon/tests/trace1b:
- Pre-TRACE1B source exported from the isolated baseline index: existing authoring journey RED/21.45s at iteration resultRefs, which incorrectly permitted only empty arrays (red-authoring.log).
- Final authoring journey GREEN/30.83s: canonical observed result -> replan/iteration -> B -> revision-bound result readback; existing confinement/freshness/REV1B checks retained (focus2.log).
- Final retained-producer journey GREEN/20.31s: real public 97d059b producers saved awaiting old trace and old repair questions both reconnect to B, retaining identities and exact-fix counts (focus3.log).
- Suite budget and module-size guards: 2 passed/0.24s (guards.log). Zero new cases; ceilings unchanged.

Intermediate fixture corrections: the proposed iteration first was not carried into the replan input; reconnect also initially observed the immediate read-only status snapshot before asynchronous activation. The corrected observer ignores the dead provider offer and waits for the fresh provider boundary. Canonical events confirmed retirement before the observer correction; no product fallback was added. Successful authoring evidence was reused rather than rerun.

Exactly one independent Sol-medium read-only source review: PASS, no P1/P2; it checked reference inventory, transaction/late-answer authority, pause/stop, confinement and retry preservation. It ran no tests. Root owns the focused results above.

GO appeared 2026-11-08 15:47:15 local; polled every 60s with a 60-minute bound. No tests ran before GO. FULL GATE: NOT RUN, as instructed. No commits/pushes, actual-provider launches, shared installs or lane-local commit identities.

Delta is ONLY against the complete pre-follow-up working tree (TRACE1 patch c1628d7a), captured before edits in C:/seldon/tests/trace1b/baseline-index with isolated objects. Repository index/history untouched. Src +25/-4 = +21 lines; tests +44/-2 = +42; discovery ledger +2. Patch whitespace and reverse-apply checks PASS.

Last proven outcome: both requested transitions reach B through the real canonical producers/consumers with fake semantic providers. Next unproven step: CC integration/host gate and authorized actual-provider replay; full-vision acceptance remains unverified.

Patch SHA-256: 3653ff746e0e1618d2919f8d61d4fdd13c7d2664e5b1ef70f964ba327a8311ed


## Round 2

CHARTER: serves C1/C4/C9/C14/C16/C23 — violates no I#; preserves I1/I6/I10 and REV1B confinement.
TRIAGE: DESIGN — r23 permits an incomplete answer, then reveals required fields one node per attempt. Read r23-diagnosis.md and run events 86–137/198–240 read-only. The previous inventory/load fixes stand; this section supersedes the previous completeness claim and artifact identity.
SIMPLEST: CODE owns one consumer completeness contract. Require all outstanding typed properties, retain the envelope, and collect independent structural violations before spending an exact-fix attempt. LLM owns their meaning.

The current trace answer is `{edits: {"handle:section": typedValue}, rationale, reply}`. Each allowed property is tied to a requested member/section; ordinary JSON Schema `required` lists all outstanding properties. Canonical retained sections need no copy. The shared decoder merges retained edits before validation; schema omissions and invalid values collect into one refusal with editable scopes. This uses ordinary object schemas for Codex/Claude and the same local decoder for Copilot; no schema flag is assumed for Copilot. No actual-provider execution is claimed.

| Question field/design point | LLM-or-CODE | Tradeoff |
|---|---|---|
| edits property identities, outstanding membership and required sections | CODE, from canonical envelope plus semantic_schema.required_fields | Requires every missing section in the first answer; retained sections stay sparse. |
| parents and every reference-field value | LLM chooses meaning; CODE constrains eligible handles using canonical consumer kind contracts | Preserves Round 1's complete reference inventory and compact off-slice id/kind/title facts. |
| module/level, bead fields, source, metric values, stop/iteration fields, amendment/baton fields | LLM supplies meaning; CODE shares required types/nonempty rules with Spine | Removes duplicate completeness rules. Semantic test levels remain semantic/e2e; legacy permits unit. |
| target/scenario values, baseline and execution bodies | LLM supplies declared behavior; CODE retains identities and validates typed shape/links | Missing executable sections are mandatory together; remaining independent graph/root/provenance refusals collect together. |
| rationale | LLM explains the meaning | CODE requires nonblank text. |
| reply | LLM supplies user-facing wording | CODE retains its string contract; phase/authority stay canonical. |
| exact-fix scope, count and saved-question retirement | CODE | Exactly two fixes remain unchanged. Retired full-envelope and edit-array questions re-ask under the same request context at run_setup.initialize, preserving fixesIssued and confinement. |

Required-field inventory at this phase: test module/level; bead ownedFiles/dependsOn/lessons plus semanticPhase (legacy proofModule); discovery source; metric definition/unit; stop-condition metricRefs/condition; iteration metricRefs/resultRefs/stopConditionRefs; amendment sourceRef/targetRefs/proposedChange/rationale/decisionRefs; baton currentState/nextSafeAction/rationale/assumptions/openQuestions/decisionRefs. Other authored kinds require their retained parents but no additional mandatory fields in the canonical consumer. Results require machine-owned evidence and remain outside the authored kind set; existing evidence validation stays authoritative. Nested baseline/execution contracts remain typed and their independent field refusals are collected. Round 1's reference-field inventory above still applies in full.

Deleted surfaces: optional edit-list discriminators, duplicated required-field checks, incomplete consumer preflight, and first-node-only field refusal handling. No new state machine, framework, store or consumer compatibility branch. Publication/recovery code and retry counters are unchanged.

Focused evidence (all temp under C:/seldon/tests/trace1b; no new cases):

- Pre-round canonical producer RED/3.00s: the existing r18 replay rejects the advertised contract because it permits omitted required sections (round2-red.log).
- Final r18 GREEN/58.76s (round2-final.log): three tests omit module/level together with targets/scenarios and bead/metric/stop siblings; one refusal names every gap, and one sparse exact fix reaches B. Existing observed-result replan/readback, reciprocal freshness and confinement remain. Later refusal combines moved ancestry, duplicate baseline testRefs, duplicate parents and both invalid execution roots; one confined correction reaches B. Unit levels, invented parents and filename codeRefs are refused together.
- Final retained journey GREEN/35.02s (round2-final-retained.log): real published 97d059b full-envelope and 2a833b6 edit-array producers saved at both trace and repair waits resume to B; member identities and exact-fix counts survive. Existing retired-P coverage remains.
- Final suite/source guards: 2 passed/0.26s (round2-guards-final.log). Source total 32,134, under unchanged 32,139 ceiling. Zero new test cases or ceiling changes.

One independent Sol-medium source reviewer: first NONPASS named two P2 (a field refusal hiding independent ancestry; unit levels accidentally admitted to semantic authoring). Both were corrected in one revision and exercised by the same r18 journey. Final source acceptance PASS, no remaining material findings. Review ran no tests/providers and is separate from the focused evidence above. Metadata-only malformed repairs also now preserve the previously refused scope.

Second-order sibling: run event 159 is `operation-error` from harness_show_node("te_c38d259935"), an uncommitted draft test (turn03 receipt). Its owner is planner_schema.inspect_node/MCP read-only inspection, separate from trace authoring. Disposition: reported, unchanged. Practical exit: teach draft-vs-canonical inspection while preserving canonical read/write authority.

GO existed before the first Round 2 test. Focused only; FULL GATE: NOT RUN, as instructed. Source was frozen during each focused run. No commits/pushes, shared installs, actual-provider launches or lane-local commit identities.

Artifact replaces the unlanded Round 1 patch and is CUMULATIVE against published main 2a833b6 content, verified with an isolated temporary index. Cumulative src +237/-200 = +37; tests +95/-37 = +58; ledger +4. This round alone: src +213/-197 = +16 (near-zero net); tests +59/-43 = +16; ledger +2. Whitespace, reverse-apply against the current tree and forward-apply against published-main content all PASS. Repository index/history remain untouched.

SHA-256: d8d061c8b318729a87a5c55c611c86b96ef7c2b88c46b503c8da88349ec1368f

Last proven outcome: both focused planning journeys reach B through canonical producers/consumers with fake semantic providers. Next unproven step: CC integration and authorized r23 actual-provider replay. Full-vision acceptance remains unverified.


## Round 3

CHARTER: serves C1/C4/C9/C14/C16/C22/C23 — violates no I#; preserves I1/I6/I10, confinement and the two-exact-fix allowance.
TRIAGE: DESIGN — per-question output contracts were not valid for the provider's strict grammar, and fresh iterations could require nonexistent results. This section supersedes Round 2's compatibility claim, broad reference-deferral assumption and artifact identity; retained completeness/refusal ownership remains.
SIMPLEST: CODE declares exactly the requested values, compiles shared grammar fragments once at emission, and defers only iteration results that cannot yet exist. LLM supplies meaning; CODE retains identity, membership, stamps and retry authority.

Fresh drafts ask their genuinely missing meaning fields: required fields remain typed/nonnullable, optional collections use typed empty arrays, and optional scalar/object values use required nullable properties. Canonical existing nodes ask only outstanding fields; exact fixes and repairs ask only the refusal's named paths. Thus properties==required for each object, with additionalProperties=false. CODE regenerates an exact-fix schema against the same judgment, binding and fixesIssued; sparse corrections merge into retained edits.

The single shared emission owner is review_provider._launch_review. strict_schema compiles duplicate enum/union fragments into local nonrecursive definitions, validates the result, then passes that exact checked result to Codex and Claude. Copilot has no schema flag and uses the same question/decoder. No schema projection weakens value/handle contracts.

Schema audit: all 18 static question contracts and 41 current r18 emitted schema artifacts pass; maximum serialized union declarations is 15. The check covers nested required/closed objects, root type, supported keywords/types, local acyclic definitions, ten-level depth, 5,000 properties, 1,000 enum values, 120,000 schema-name/enum characters and the large-enum string bound. The portable constraints use minItems only 0/1 and the simple nonblank pattern; minLength/maxItems and recursive DATA are not sent. Bounds follow the [OpenAI strict-output specification](https://developers.openai.com/api/docs/guides/structured-outputs#supported-schemas) and [Anthropic's schema subset and complexity limits](https://platform.claude.com/docs/en/build-with-claude/structured-outputs#schema-complexity-limits). Shared definitions reduce declared grammar repetition; actual provider compilation remains unverified, including provider internal complexity limits.

| Field / design point | LLM-or-CODE | Tradeoff |
|---|---|---|
| edits property names, requested sections, object closure | CODE | Only fresh meaning or exact outstanding/refused paths are declared and required; no canonical envelope is copied. |
| parents and all reference values | LLM chooses relationships; CODE supplies eligible canonical/proposed handles | Round 1's complete reference inventory remains. Missing mandatory non-result relationships produce one named outline refusal, not an impossible question. |
| iteration.resultRefs | CODE owns phase availability; LLM chooses eligible results when authoring | An absent awaiting link remains readable when a first observation arrives; authoring requests it once results are available. Other mandatory references stay mandatory. |
| module/level, bead, discovery, metric, stop, amendment and baton fields | LLM meaning; CODE's shared required_fields contract | Keeps the completed Round 2 completeness definition; semantic test levels remain semantic/e2e. |
| baseline / evidenceRefs and current reference stamps | CODE | Historical stamps remain unchanged; current semantic edges are resolved without LLM copying. Existing freshness assertions retain old evidence/judgment staleness. |
| target/scenario/execution values and literal JSON | LLM meaning; CODE types, handles and decoding | Literal data is JSON-encoded text, locally syntax-validated with other gaps, then decoded at the canonical boundary; no recursive provider schema or artificial application-data depth vocabulary. |
| rationale / reply | LLM | Existing nonblank rationale and string reply contracts remain. |
| schema compilation/audit, supersession and exact-fix scope/count | CODE | One emission boundary and existing transactional load owner; no new framework, state machine or store. |

Retirement remains loader-only. Valid old literal DTOs become current JSON strings. Malformed DTOs or wrappers remain rejected values and their enclosing section is re-asked, preserving every other edit and the existing allowance. Both main's edit-array questions and older full-envelope questions use the current consumer; there is no legacy branch there.

Deleted/consolidated surfaces: recursive DATA grammar; optional edit-property declarations; duplicate bead/required-field checks; passive duplicate Judgment DTO/alias declarations (canonical writer and runtime guards unchanged); obsolete refusal-scope alias/fallback machinery. Publication/recovery code is untouched. The judgment writer file changes only internal type annotations.

Focused evidence, all temp under C:/seldon/tests/trace1b, zero new cases:

- Retained pre-round emitted trace: 229 declared edit properties but only 43 required; the current emission audit rejects it. Actual pre-round canonical fake-provider replay of a fresh iteration reports required resultRefs minItems=1/maxItems=0, RED/3.03s (round3-red-iteration.log).
- r18 GREEN/42.58s (round3-revision3.log): ordinary trace passes actual emission, mutated non-strict output is blocked before schema-file emission, all omissions/invalid JSON get one refusal and one sparse fix reaches B, and an initial iteration reaches B with zero results. Real canonical observations then support replan/result readback. HISTORY preserves its original evidence stamp across result staleness. Missing metric/source declarations are refused together before trace emission. Existing confinement/freshness remain; independent ancestry/duplicate/root refusal aggregation is exercised at the real canonical batch boundary, where unasked existing-node mutations belong.
- Final retained journey GREEN/43.31s (round3-loader-final.log): real published 97d059b and 2a833b6 trace/repair waits resume to B with IDs and fixesIssued retained, and literal JSON is read back with its original meaning. The same journey saves a published-main exact-fix answer containing both malformed entries and a malformed outer wrapper; one corrected section completes B under the remaining allowance.
- Final suite/source guards: 2 passed/0.24s (round3-guards-accepted.log). Total source 32,137 <= unchanged 32,139; suite ceiling unchanged. All18/41 schema audit evidence was reused after the final loader-only repair.

One independent Sol-medium reviewer stayed with the candidate. Review closed union complexity, evidence-history rebinding and overbroad deferral findings, then the same loader-root malformed-answer findings. Final source acceptance PASS; reviewer ran no tests, providers or writes. Root owns the focused results. An intermediate B-only resume had exposed retained literal DTO leakage; final readback coverage closes that gap. No intermediate result is promoted to provider or product acceptance.

GO existed before Round 3 tests; source stayed frozen during each focused run. FULL GATE: NOT RUN, as instructed. No commits/pushes, shared installs, actual-provider launches or lane-local commit identities.

CUMULATIVE delta against published main 2a833b6: src +375/-335 = +40; tests +168/-39 = +129; ledger +6. Round 3 alone against the retained pre-round tree: src +186/-183 = +3; tests +97/-26 = +71; ledger +2. Whitespace, reverse-apply against the current tree and forward-apply against published-main content PASS; the forward check uses an isolated temporary index. Repository index/history remain untouched.

SHA-256: ad604a02f3f939aff1263de4304c9bb4bf7fe34cb8461326f4f9d8c156dc78cb

Last proven outcome: the requested planning and retained-retry transitions reach B through canonical producers/consumers with fake semantic providers. Next unproven step: CC integration/host checks and authorized actual-provider compilation/replay. Full-vision acceptance remains unverified.


## Round 4

CHARTER: serves C1/C4/C9/C14/C23 — violates no I#; preserves I1/I6/I9/I10, complete refusals, confinement and exactly two exact fixes.
TRIAGE: DESIGN/BUG — CC's integrated host gate on 4cdafbb exposed source-budget overflow (32,162 > 32,139) after RESUME1, and the web fixture assumed nullable testRef was directly declared rather than referenced. This supersedes Round 3's integration sufficiency; its independent approval is retained.
SIMPLEST: reuse canonical contracts and traversal, and project fixture values through the schema actually asked.

Ported first using published-main diff 2a833b6..4cdafbb, applied cleanly, including RESUME1 source and journey changes. Its source owners were not modified. No publication/recovery code was added to this lane's delta.

Real simplification removed 25 source lines: test execution reuses LAUNCH; authored kind inventory comes from canonical ALLOWED_PARENTS; baseline and web operand validation dispatch through their shared contracts; review packets reuse their question's example; direction context shares the existing default branch; inspection uses Spine.children/descendants instead of recomputing graph closure. No line joining, ceiling changes or source relocation. Required web operands, HTTP checks, fill string validation and inspection outputs stay enforced.

| Design point | LLM-or-CODE | Tradeoff |
|---|---|---|
| Authored kinds, launch/operand shapes and review examples | CODE | Removes duplicate contracts while preserving the question's meanings and strict shape. |
| Graph children and descendant inspection | CODE, canonical Spine | One graph owner replaces a second traversal implementation; draft-node inspection remains separately reported. |
| Nullable fixture values behind references | CODE, fake-provider fixture projection | Reads the advertised schema, supplies null only when allowed, and still rejects omitted required scalar meaning. LLM meaning ownership is unchanged. |
| Trace meanings, refusal scopes and retry allowance | LLM meaning; CODE structure/authority | Approved Round 3 contracts remain. |

Web-only static sweep covered plan_content(web), UX6 input, provider_answer/provider_shape, advance_meaning/main_path, web_evidence_golden, cockpit_golden, and semantic_runner_support's direct observer documents. Historical records/edit-array reads are confined to the advertised legacy producer fixture/retirement journey; current trace projection uses keyed edits. Direct observer documents retain their canonical observation shape. No test assertion was removed or relaxed; zero new cases.

Focused results (all temp under C:/seldon/tests/trace1b; GO existed; source frozen during runs):

- Existing r18_authoring_golden PASS/B, 38.61s; retained_permission_golden PASS/B, 54.62s; trace_contract_golden PASS, 1.66s (round4-focused.log). Includes complete refusal/sparse fix, initial no-result iteration, observed-result replan and saved old trace/repair questions.
- The existing web authoring path was invoked separately through its real canonical fake-provider producer/consumer up to B, before browser use: PASS, every target/scenario retained and no unvalidated scenario (same log). This reproduces the host's pre-browser authoring boundary without replacing browser evidence.
- Web pytest: 1 skipped/5.94s, only at actual browser readiness; browser UNVERIFIED (round4-web.log and round4-web/web-browser-readiness.json). Full browser behavior remains for CC's host.
- Suite/source guards: 2 passed/0.28s (round4-guards.log). All 18 static question schemas still pass the strict audit. Source **32,137 <= 32,139**, unchanged ceiling.

Same independent source reviewer: PASS, no material regression; read-only, no tests/providers/writes. FULL GATE: NOT RUN, as instructed. No commits/pushes, shared installs or actual-provider calls.

CUMULATIVE versus published main 4cdafbb: src +396/-381 = +15; tests +178/-42 = +136; ledger +8/-0. Round 4 alone: src +32/-57 = -25; tests +11/-4 = +7. Whitespace, reverse apply against current tree, and forward apply against 4cdafbb using an isolated temporary index PASS. Repository index/history untouched.

SHA-256: 4e99e4d8667c0f8c5ad70525b8038f2940134f20241a31e6f163131be377a02c

Last proven outcome: both planning/resume journeys and web canonical authoring reach B; source fits the integrated budget. Next unproven step: CC host web execution/integration gate. Actual-provider and full-vision acceptance remain unverified.


## Round 5

CHARTER: serves C4/C9/C14/C16/C18/C23 — violates no I#; preserves I1/I6/I9/I10, canonical authority, confined repair and exactly two exact fixes.
TRIAGE: DESIGN — latest-fault filtering could discard retained recovery subjects; physical segment counts confused valid controller replacement with repeated product work. This section supersedes Round 4 integration sufficiency.
SIMPLEST: CODE supplies the captured job's attempt history and canonical graph meaning, while tests account for native work/handoffs rather than raw controller counts.

The explicit direction branch is restored. recovery_context projects attempts for every bead in the already-captured canonical job record and uses those subjects when selecting relevant prior directions; direction packets include their canonical graph nodes and ancestors. Latest affectedNodeIds remains the recovery owner's current fault set. Job terminal facts are retained as observed, without relabeling historical failures as current. The small unused review_instructions.status forwarding function was deleted; no source ceiling increased.

The Round 4 direction guard was logically equivalent to its earlier branch. The original host twin1 symptom did not reproduce locally: unchanged baseline replay PASS97.16s. A concrete sibling was reproduced through the existing canonical controller-loss journey: with latest fault B-only after three pre-entry controller deaths, the old producer drops C attempts and graph meaning (round5-red-launch.log). Final assertions require both retained C and unchanged B-only fault scope. This is the proved packet defect; the exact host failure's root remains unproven because host run directories are access-denied.

| Field / design point | LLM-or-CODE | Tradeoff |
|---|---|---|
| job, attempts, priorDirections and graph recovery subjects | CODE from canonical job, judgment and Spine owners | Preserves the context needed to change approach without asking the model to reconstruct history. Latest fault scope stays distinct. |
| Steering choice, proposed repair and rationale | LLM | Meaning ownership, current typed answer and retry/confinement rules stay unchanged. |
| Expected physical segments and permitted extras | CODE in the existing golden journey | Requires expected Contracts/Build segments, closed admission/work/generation/receipt identities, verified expected exits, and only event-justified unentered extras. No count/name exemption. |

The shared test helper replaces initial, validation and final physical segment counts in both surfaces. Extras require no started.json, certain non-entry/retained-work outcomes, native same-job readmit ownership release/resume evidence, and a matching recorded dead controller or no launch. Earlier exit observations can justify a later explicit steering handoff for the same segment. Continuation effect IDs are resolved to physical segments through jobs.latest_segment. Missing receipts, unexplained entered/unentered segments and Contracts reruns still fail. The existing real controller-loss journey exercises three permitted extras through C.

Sibling count sweep: final current-attempt count becomes the exact expected bead-ID set. The one-new-Build-attempt and no-new-attempt-after-delivery assertions remain; they protect product execution rather than controller count. Same-work two-recovery bounds, stale-evidence Contracts rerun counts and unique acceptance/review attempt identities remain unchanged. No assertion was weakened; zero new cases.

Focused evidence (all temp C:/seldon/tests/trace1b; GO existed; source frozen during runs):

- Existing controller_launch_interruption(afterStarted=False, stale=False): PASS/C119.25s, including B-only packet subjects, retained Contracts, three event-backed unentered extras and ordinary continuation.
- Exact failing startup-steering path controller_interruptions(twin1): PASS88.41s.
- Existing r18_authoring_golden: PASS/B37.83s; retired_permission_golden: PASS/B41.80s; trace_contract_golden: PASS1.28s. Full selected invocation exited0 (round5-green-final.log).
- Guards: 2 passed/0.29s (round5-guards.log); source **32,135 <= 32,139**, unchanged ceiling. Valid guard results reused after test-helper-only corrections.

Same independent reviewer: final affected static review PASS; no tests/providers/writes by reviewer. FULL GATE: NOT RUN. No new browser run: CC's retained web phase/outcome evidence motivates the assertion correction, and fresh host web execution remains unverified. All local semantic providers are fake; actual-provider/full-vision acceptance is unverified.

CUMULATIVE versus published main4cdafbb: src +398/-385 = +13; tests +241/-52 = +189; ledger +10/-0. Round 5 alone: src +5/-7 = -2; tests +63/-10 = +53. Whitespace, reverse apply and isolated-index forward apply against4cdafbb PASS. Publication/recovery source untouched by this round; no commits/pushes, shared installs or lane-local commit identities.

SHA-256: 83c9f1020d522613c54bd91b2a549935477447da08b9174e8f0e64ea7788b799

Last proven outcome: restored recovery subjects support steering and controller replacement reaches C with retained Contracts; planning/resume journeys reach B. Next unproven step: CC host replay, including the original CLI symptom and web continuation.


## Round 6

CHARTER: serves C1/C4/C9/C14/C16/C18/C23/C26 — violates no I#; preserves I1/I6/I9/I10, confinement and two exact fixes.
TRIAGE: DESIGN — recovery packets followed the latest publication admission instead of the admitted work's observed attempts. This supersedes Round 5's sufficiency claim; its B-only projection fix and the host-passed web segment assertions remain.
SIMPLEST: reuse original immutable observations matched by the canonical work ID, in the existing question-history scan. No new store, state machine, scheduler or retry allowance.

Copied host DB diagnosis (read-only): question event379, retained cursor384, follows no-progress event374. Ready terms are startupFailure=false, attempts=false, priorDirections=true, contractsInGraph=true. The first false term short-circuits the old predicate; attempts are also absent. Current job b8a901 has no dispatch run and only not-launched outcomes. Earlier job a7fa23, captured at question259, contains the actual Injected-worker-failure observation and C attempts. Their admitted work IDs match. Event334 admits a new publication, rather than a recovery-successor edge, so job-chain-only lookup would miss it. Local replays passed when that new controller reached dispatch and produced a current record; the copied host controller exited before entry. No assertion is made about the underlying host process-exit cause.

recovery_context now supplements missing observed attempts from original question snapshots whose per-bead outcome work ID matches the current admission. Retained rows and outcomes carry event/job/segment/work provenance and historical=true. Previously enriched rows are excluded, preserving the original source and flat history. Current terminal scalar fields/outcomes and native quiescence/recovery authority remain unchanged; explicitly labeled retainedWorkObservations supplies past outcomes. The source event identity is immutable, so repeated unchanged words still hit no-progress rather than gaining allowance. No keyword is used by product code to judge failure meaning.

| Field / decision | LLM-or-CODE | Tradeoff |
|---|---|---|
| Current job, recovery, fault work and quiescence | CODE, existing native owners | Keeps current not-launched/unknown truth; history cannot grant authority or proof credit. |
| Retained attempts and retainedWorkObservations | CODE, exact native work ID matching | Makes prior actual work visible across publications without guessing from bead names or inaccessible old files. |
| eventId, jobId, segmentId, workId, historical | CODE, immutable source references | Preserves origin, prevents recursive recopying and labels historical observations explicitly. |
| Steering meaning, repair and rationale | LLM | The model can change approach from the supplied observations; typed action, confinement and retry contracts remain. |
| Outstanding fields and memberships | CODE, existing consumer definition | Deletes a duplicate inventory/traversal; schema owner uses the same merged envelope and required-field rule. |

Budget simplification: delete the sole-caller run_content.outstanding_sections helper and its second inventory/full traversal. author_contract computes the same node and target/scenario obligations in its existing loops. Retained rejected edits, canonical values, authoring=True, absent-vs-empty editable scopes, fresh-node optional fields and group-specific memberships are preserved. No line joining, source relocation or ceiling increase.

The existing CLI journey now uses its existing real controller-death socket hook after the downstream amendment to force the copied host window. It proves the new job has no run, leaves the readiness predicate intact, and reports each false term directly. Success additionally compares the current terminal to the native producer and validates retained outcome provenance against the original event/job/segment/work. No state or attempt data is fabricated; zero new cases.

Loaded evidence (all temp C:/seldon/tests/trace1b; GO existed; source frozen during each run):

- Initial natural loaded baseline: 3 passed/1083.09s (round6-loaded-baseline.log); the new controller reached dispatch, so it did not reproduce the missing record.
- Deterministic host-window replay on unchanged Round 5 product source: 1 failed, 2 passed/999.43s. Same missing startupFailure/attempts terms at local question378 (round6-loaded-red.log; retained snapshot round6-loaded-red.sqlite3).
- Fixed source, same loaded invocation: **3 passed/1035.76s** (round6-loaded-green.log). Includes the full CLI, planning/resume/confinement/retry journeys, native empty-successor recovery, and both companion cases.
- Gate interpreter reused read-only: ~/codex-harness/.venv/Scripts/python.exe, pytest8.4.2/xdist3.8.0. Command: python -B -m pytest 'tests/python/core/test_golden_path.py::test_golden_path[cli]' 'tests/python/core/test_approval_v2_journey.py::test_canonical_plan_contracts_red_build_validation_pass[http-domains]' 'tests/python/core/test_approval_v2_journey.py::test_canonical_plan_contracts_red_build_validation_pass[delivery]' -n 4 -p no:cacheprovider -q -s --basetemp=C:/seldon/tests/trace1b/r6.
- Structural guards: 2 passed/0.30s (round6-guards.log); source **32,136 <= 32,139**, ceiling unchanged.

Same independent reviewer: final affected source/test review PASS; no tests, writes or providers by reviewer. No full gate, new browser run, actual-provider calls, shared installs, commits or pushes. Publication/recovery source remains untouched by this round. Host web PASS on Round 5 is retained evidence, not a fresh Round 6 browser result.

CUMULATIVE versus published main4cdafbb: src +400/-386 = +14; tests +281/-56 = +225; ledger +12/-0. Round 6 alone: src +24/-23 = +1; tests +40/-4 = +36. Whitespace, reverse apply and isolated-index forward apply against4cdafbb PASS; repository index/history untouched.

SHA-256: 87614f033f6126fa86f30bb8f3b84599aee9f6a3df4cfa373778574d4139d4b1

Last proven outcome: the loaded CLI reaches C on its ordinary path; the captured empty-successor branch recovers to execution with truthful current and retained observations. Both companion cases pass. Next unproven step: CC host integration and actual-provider/full-vision acceptance.
