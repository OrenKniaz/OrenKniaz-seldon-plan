CHARTER: serves C1/C2/C3/C20/C23 — violates no I#.

**Estimated net deletion: 2,190–2,545 lines**, conditional on fixing the owners below and preserving their required behavior. The largest savings belong to legacy proof and packet construction; **2e alone does not remove them**.

Audited checkout: `a4e7df5cf6e23a64014fd7d71960f01bc2c78094`, clean before and after. Current count: **32,095 Python lines; 32,449 including web assets**. Read-only source inspection; no edits, tests, or provider launches. Implicit state-machine consolidation is excluded.

Ranges below are inclusive physical lines. “Size” identifies the inspected compensation surface; “delete” estimates **net savings after replacement**, with no overlap between entries. All paths are under `src/codex_harness/core`.

**1. Python execution instrumentation compensates for an inadequate proof contract — delete 780–830 lines.**

- **Sites/size:** [runners.py:96–900](/~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/runners.py:96), `1162–1203`: **847 lines**.
- **Compensation:** startup-hook fingerprinting, injected `sitecustomize`, patched `Popen`, frame tracing, AST inspection of `assertEqual`, and callback counting reconstruct what a test actually exercised.
- **Wrong upstream owner → simplest fix:** legacy runner/proof contract supplies a Python suite selector rather than language-neutral execution evidence. Route declared test executions through the existing semantic runner and meaningfulness judgment. CODE records execution; LLM judges relevance (C3/C14, I1/I7).
- **Risk / 2e:** high: preserve observed RED/GREEN, candidate binding and process cleanup. `unittest` itself is not the problem. **No free 2e deletion**; legacy retirement must preserve its useful behavior first.

**2. Worker packets reconstruct information lost by their producers — delete 770–830 lines.**

- **Sites/size:** [worker_packet.py:28–425](/~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/worker_packet.py:28), `566–892`; [proof_imports.py:1–138](/~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/proof_imports.py:1): **863 lines**.
- **Compensation:** reparse generated `PLAN.md`, support old bullet formats, rebuild bead fields, convert lesson representations, infer imports/signatures, and extract selected fixture-table entries to repair oversized context.
- **Wrong upstream owner → simplest fix:** compiler/packet boundary exports several incomplete representations. Supply canonical node text, contracts, execution declarations and declared source bundles once. Keep a small renderer and bounded source inclusion.
- **Risk / 2e:** high: preserve dependency context, ownership and confirmed-memory provenance. The existing semantic packet branch demonstrates a smaller path, not complete legacy replacement. **No; principally Stage 3d work.**

**3. Refusal machinery repairs unstructured errors and repeatedly decorated replies — delete 150–190 lines.**

- **Sites/size:** [planner_refusals.py:1–209](/~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/planner_refusals.py:1); [planner_connection.py:79–87](/~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/planner_connection.py:79): **218 lines**.
- **Compensation:** recover codes from prose, strip previous `Next:` text, recursively infer whether arbitrary payloads represent holds, collect selected fields, and detect already-repaired messages.
- **Wrong upstream owner → simplest fix:** public error producers return inconsistent text and result shapes. Produce `{code, reason, current, nextAction}` at the owning failure boundary; render once. CODE owns this (I6/I8).
- **Risk / 2e:** medium: actionable refusals and workspace identity must survive. **Partial overlap**, but the chat front door still needs errors; replacing planner tools alone does not fix these producers.

**4. Interface inference compensates for contracts lacking authoritative observations — delete 100–130 lines.**

- **Sites/size:** [wave_refine.py:218–355](/~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/wave_refine.py:218), `563–599`: **175 lines**.
- **Compensation:** infer API shapes from Python annotations/JSON, translate `dict/list`, special-case integer-versus-number compatibility, and hold refinement when the inferred interface is unknown.
- **Wrong upstream owner → simplest fix:** refinement treats a limited source projection as contract authority. Supply bound source/observations to the semantic question; retain deterministic IDs and explicit schema checks. LLM judges compatibility when code cannot establish it (I1/I2/I3).
- **Risk / 2e:** medium: retain real contract-conflict detection and immutable blob references. **No**, unless 2e explicitly replaces this refinement question and consumer.

**5. Acceptance migration repairs old evidence identities — delete 100–120 lines.**

- **Sites/size:** [acceptance_revision.py:118–164](/~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/acceptance_revision.py:118); [acceptance_runs.py:197–259](/~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/acceptance_runs.py:197), `295–303`, `335–365`; `plan_acceptance.py:772–775`: **154 lines**.
- **Compensation:** recompute `git-diff-v1`, distinguish old unbound scenarios, backfill node revisions, and expose acceptance rebinding. Rebinding does rerun scenarios; it is not simply relabeling old success.
- **Wrong upstream owner → simplest fix:** historical acceptance producers omitted current identity/binding fields. Current producers should always write the complete format; unsupported historical credit stays historical.
- **Risk / 2e:** medium/high for existing projects. Retire compatibility deliberately without rewriting originals or inventing proof. **No free 2e deletion.**

**6. Impact lookup searches several stores because baseline identity is fragmented — delete 75–95 lines.**

- **Sites/size:** [plan_store.py:555–677](/~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/plan_store.py:555): **123 lines**.
- **Compensation:** search compilation events, revision snapshots and audits; register multiple hashes; infer missing baselines; finally reconstruct impact from manifest bead dependencies.
- **Wrong upstream owner → simplest fix:** compilation/publication records do not provide one uniformly addressable baseline. Store one canonical snapshot per revision and resolve it directly. Imported manifests should carry their trace snapshot.
- **Risk / 2e:** medium: preserve imported-plan comparison, removed links and protected-file invalidation (C10). **No**; keep the actual impact algorithm.

**7. Candidate revalidation repairs coupling between product and verifier snapshots — delete 60–90 lines.**

- **Sites/size:** [planner_candidate.py:272–447](/~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/planner_candidate.py:272): **176 lines**, chiefly the overlay branch at `319–388`.
- **Compensation:** create another worktree, transplant changed verification files, commit them, recheck preserved product bytes, then update several run/receipt projections.
- **Wrong upstream owner → simplest fix:** candidate/publication packaging couples retained product identity to mutable verification inputs. Bind an immutable product snapshot and a separate verifier bundle when creating the execution request.
- **Risk / 2e:** high: verifier refresh and evidence reuse are legitimate requirements. Delete reconstruction, not revalidation or candidate checks. **No free 2e deletion.**

**8. Generic judgment parsing repairs insufficiently specific LLM requests — delete 40–80 lines.**

- **Sites/size:** [planner_schema.py:140–266](/~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/planner_schema.py:140); `run_questions.py:18–25`; `run_invocations.py:59–62,86–89`: **143 lines**.
- **Compensation:** one open `meaning` object requires question-specific validation after return; the model copies judgment IDs, bindings and candidate identities; malformed provider text gets another decoding route.
- **Wrong upstream owner → simplest fix:** invocation construction does not enforce the actual question schema. Use the schema-bound call; attach known identities from the admitted invocation rather than asking the LLM to reproduce them (I10).
- **Risk / 2e:** medium: retain local validation, referential integrity and C4’s two exact-fix retries. **Yes, partially by design**; most of this surface cannot simply disappear.

**9. Review readers compensate for missing launch reservations and evolving tables — delete 45–70 lines.**

- **Sites/size:** [plan_reviews.py:168–316](/~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/plan_reviews.py:168), `427–495`: **218 lines**.
- **Compensation:** probe table/column existence, fall back from reservation order to completion order, and handle mixed reserved/unreserved provenance.
- **Wrong upstream owner → simplest fix:** review admission/schema initialization should guarantee one reservation before every launch and a current schema before ordinary readers run.
- **Risk / 2e:** medium/high for retained reviews. Preserve unresolved-attempt holds, native identity and judged reuse; those are not deletion targets. **No**, unless admission is explicitly unified too.

**10. Packet compaction repairs duplicated canonical content — delete 40–60 lines.**

- **Sites/size:** [review_packets.py:69–110](/~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/review_packets.py:69), `208–228`, `300–305`; `worker_packet_budget.py:16–25`: **79 lines**.
- **Compensation:** small dossiers include four rendered documents plus canonical JSON; large dossiers switch representation. Workers deduplicate rendered paragraphs. Reviews deliberately remain multi-shard even when removing duplication would make them fit.
- **Wrong upstream owner → simplest fix:** packet construction should emit each canonical fact once, then partition only when necessary.
- **Risk / 2e:** low/medium: preserve global context, coverage and explicit truncation. Context limits and real overflow recovery remain. **Partial overlap**, not automatic savings.

**11. Reference repair compensates for loose source/finding contracts — delete 15–25 lines.**

- **Sites/size:** [review_packets.py:112–126](/~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/review_packets.py:112); [review_findings.py:7–26](/~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/review_findings.py:7): **35 lines**.
- **Compensation:** discover the full brief through prose regex/legacy filename; rewrite unknown finding subjects to `plan` and expand scenario aliases after return.
- **Wrong upstream owner → simplest fix:** vision ingestion should persist an explicit brief reference; review questions should supply canonical subject IDs and validate returned links.
- **Risk / 2e:** medium: unresolved brief coverage and invalid finding subjects must remain visible. **Partial** for typed finding IDs; the brief producer needs its own fix.

**12. Historical receipt branches compensate for pre-registration review formats — delete 15–25 lines.**

- **Sites/size:** [acceptance_recovery.py:585–726](/~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/acceptance_recovery.py:585): **142 lines**; only schema-1 alternatives are candidates.
- **Wrong upstream owner → simplest fix:** original receipt production lacked launch-registration lineage. Use schema-2 registrations uniformly for active credit.
- **Risk / 2e:** high for historical continuity. Delete only after compatibility retirement; preserve sealed originals, session reservations and duplicate-session rejection. **No free 2e deletion.**

**Deletion order and target:** the numbered list ranks approximate savings. Items **1–2 provide 1,550–1,660 lines** but require legacy capability preservation; item **3** is the next substantial independent simplification. Items **4–12** remove smaller producer/consumer mismatches.

The combined estimate yields **29,550–29,905 Python lines**, or **29,904–30,259 including web assets**. That supports approaching the **30k** end; this audit does **not** substantiate reaching **27k**. Most savings are conditional on owner fixes, not already-dead code.

**Retain:** C18 crash recovery, C17 vision resync, C10 stale-marking, confirmation reattachment, sealed-receipt checks, BASIC denial handling and bounded Windows replacement retries. Their names resemble compensation, but deleting them would remove required behavior. No savings from the parallel state-machine audit are included.