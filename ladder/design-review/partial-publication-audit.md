CHARTER: serves C2/C18/C23/C26 — violates no I#.

**TRIAGE: DESIGN — publication lacks a consistently enforced owner boundary.** Individual writes are atomic; the logical fact spanning them is not. This does **not** establish one cause for all five reds: the ordinal-shifted twin was an observer assumption.

Audited HEAD `e2daa3fe3bcaf193a6662ab30041483c110b4374`. No tests, edits, or long commands. References below are relative to `src/codex_harness/core/`.

**1. Split-publication inventory**

| Fact | Separate writes, in order | Readers exposed to the gap | Consequence |
|---|---|---|---|
| **Validation and delivery completed** | `planner_candidate.py:437` publishes VALIDATED/finishedAt → `candidate_delivery.py:57` retained pointer → root files `:116` → ZIP `:141` → complete run `:146`. Initial dispatch has the same split: `dispatch.py:834` → `planner_jobs.py:561`. | `worker_job_status` `planner_jobs.py:397`; cockpit `status_api.py:98`; `acceptance_support.py:450–454` | **Observed test-only inference:** VALIDATED does not establish delivery. Product exposes validation before delivery, but C checks delivery separately. `run["delivery"]` at `:117` is only an in-memory mutation; publication is `:146`. |
| **Current candidate selection** | Revalidation receipt `planner_candidate.py:397` → run `:437` → retained pointer `candidate_delivery.py:57` | `current_job_run` `planner_candidate.py:106–123`; acceptance/status/judgment consumers | **Product:** old pointer/new run can temporarily produce “candidate inconsistent/unavailable.” An interruption can preserve that disagreement. |
| **Root product/package available** | Individual root writes/deletions `candidate_delivery.py:114–116` → ZIP replacement `:141` → delivery receipt `:146` | User-running product; `delivered_candidate` `:164–184`; acceptance byte/revision readers | **Product:** partially updated root; old receipt can remain during replacement. Byte checks prevent this becoming proven current delivery/C. |
| **Segment completed and safe to recover** | Payload terminal `planner_jobs.py:782`, or monitor fallback `planner_recovery.py:416` → segment quiescence `:429` | `segment_status` `planner_jobs.py:715–730`; `retained` `planner_candidate.py:29–35`; recovery inspection | **Old writer-order defect repaired:** outcome now precedes release. **Residual reader risk:** `segment_status` reads terminal before quiescence, allowing a mixed-time observation; dead-owner handling can then select recovery. Source-supported, unreproduced here. |
| **Public job outcome** | Segment terminal/quiescence → root quiescence `planner_recovery.py:430` → root terminal mirror `:432` | Loop reads segment; public/internal job status reads root `planner_jobs.py:384–392`; execution-evidence admission `dispatch_attempts.py:458–487`; planner recovery context | **Product:** completed segment versus running/older public job. A crash before mirroring makes disagreement durable and can block evidence admission. |
| **Admitted build has its request and owner** | Loop effect commit `run_loop.py:960` → segment cursor attachment `planner_jobs.py:638` → request `:647` → Popen `:669` → launch record `:678` → payload entry `:742` | Reconciliation `segment_status`; `latest_segment`; recovery `inspect` `planner_recovery.py:210`; reattachment | **Product:** readers can select an admission whose required files do not yet exist. Crash recovery can encounter missing request/launch records rather than a complete owner outcome. Presence of intent is not launch certainty. |
| **Attempt/process outcome and its summaries** | Canonical result `dispatch_attempts.py:388` → group request `:391` → requirement request/result copies `:399/:401` → bead/run projection `dispatch.py:748` | Cancellation, recovery outcomes, resume, execution-evidence admission, raw test readers | **Mixed:** root result-first ordering is sound; stale summaries are observable. Requirement copies publish terminal request before result. Consumers must use the canonical process result. Existing permission guard already rereads it. |
| **Integration completed** | Integration receipt `dispatch_integration.py:251/:296` → repository fast-forward `:346` → bead status `:376` → run publication `dispatch.py:748`; revalidation repeats this at `planner_candidate.py:397–437` | Receipt/repository readers; recovery/evidence inspection; run/status projections | **Product availability gap:** validated candidate receipt can precede integration/run completion. Receipt validation must not be interpreted as completed integration. |
| **Revalidation completed and continuation consumed it** | Run/delivery publication → recovery validation event `planner_recovery.py:377` → cursor update `run_loop.py:1233` | Job status; reconnect `_reconcile`/`_consume_completed_effect` | **Product recovery gap:** a durable result can precede cursor settlement. `_consume_completed_effect` handles review, semantic and acceptance effects, but has no `judgment-continuation` completion branch; interruption can quarantine completed work. |
| **Compiled plan materialization current** | Reference/generated files `plan_store.py:444/:449` → compiled event `:453`; standalone renderer also writes files sequentially `spine_render.py:200` | Manifest/freshness reconstruction `plan_store.py:494`; planner/cockpit views; execution-input readers | **Product:** mixed file generations can appear stale/unavailable. SQLite snapshots do not snapshot these filesystem writes. |
| **Mail delivered / lesson promoted** | Mailbox commit `mail.py:119–132` → plan settlement `:89`; memory entry/confirmation `memory_promotion.py:112/:163` → run summary `dispatch.py:748` | Inbox versus plan events; memory search versus run summary | **Benign projection lag:** mailbox IDs are idempotent; memory is advisory. Read their owners, not settlement summaries, for the fact. |

**Already protected—not additional publication defects:** acceptance receipt/result/terminal state share the transaction at `planner_acceptance.py:238–296`; review rows, terminal attempts and completion event share `review_rounds.py:357–391`; acceptance-review findings/result/event share `acceptance_reviews.py:118–156`. Consent and ordinary answer/cursor updates likewise commit together. Multi-write source code alone does not establish an observable gap.

**2. One rule**

> **An owner publishes one identity-bound terminal outcome last, after its required artifacts exist. Every consumer—including tests—reads that outcome; earlier records mean pending.**

| Owner | LLM-or-CODE | Tradeoff |
|---|---|---|
| Existing admission, process, completion and consent owners | **CODE** publishes/consumes terminal structure; **LLM** supplies semantic verdicts only | Deletes competing completion interpretations; requires explicit pending handling. Serves I1/I6/I9 without a new framework. |

**3. Apply first, ranked by product impact**

1. **Admission and recovery:** complete admission binding; publish outcome plus cleanup through the segment owner; consume it directly instead of root mirrors. Remove absence-based certainty before that outcome.
2. **Revalidation recovery:** consume its retained terminal result after interruption, then settle the cursor.
3. **Validation/delivery:** publish delivery completion once; preserve validation as a separate observation. Remove the premature completion inference.
4. **Materialization and advisory projections:** consumers follow the owner’s completed selection rather than rebuilding truth from partially updated files.

Estimated production delta: **roughly −40 to −100 lines overall**, chiefly deleting mirrors, precedence branches and duplicate completion interpretation. Admission reordering should be approximately line-neutral. These are design estimates, not an implemented diff.

**4. Observer fixes versus product fixes**

- **Today’s KeyError:** `acceptance_support.py:451–454` reads a raw intermediate run and infers delivery from VALIDATED. Read the completion owner’s settled delivery outcome. Its preceding segment cleanup belongs to the earlier worker segment, not necessarily the ongoing revalidation.
- **Historical ordinal twin:** test-only ordering assumption. At this candidate, `test_golden_path.py:454–467` acknowledges actual packet entry, and `:4252–4258` counts same-work recoveries. The old ordinal defect is already removed in source.
- **Monitor release-before-outcome:** historical product defect; writer ordering is repaired at `planner_recovery.py:415–429`. Root mirroring and mixed-time reading remain separate concerns.
- **Launch-before-entry:** absence of `started.json` is an intermediate observation. Use the owner’s terminal launch outcome; raw inspection before termination cannot establish terminal certainty.
- **Actual product work remains:** admission completeness, segment/root disagreement, interrupted revalidation consumption, candidate/run publication consistency, and partial filesystem materialization. A test-observer correction alone does not close those gaps.