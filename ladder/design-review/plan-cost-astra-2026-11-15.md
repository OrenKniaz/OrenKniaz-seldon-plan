Planning cost review — 683d19b / BLUEPRINT v1.10 — 2026-11-15

The largest avoidable loop is missing facts in REVIEW, not missing parallelism or failure to batch gaps.
REVIEW filters contracts by the old architecture endpoints; DETAIL can consume additional existing contracts, and plan.merge records those endpoints correctly. REVIEW then calls an existing agreement missing and sends the run back to ARCHITECT.
Read-only evidence: named design notes, source at 683d19b65310e45da27ea78a2eed3d3435b061e5, calls and SQLite URI mode=ro. No .env, provider execution, tests, or state changes; this report is the sole write.
Measured from recorded attempt start/provider reply finish through the last pre-B reply: b01 28.48 min/70 calls; b02 15.47/37; b03 18.12/46; ef048d4-i01 5.60/13. These include ALIGN; timeline.py's WORK boundary cannot run unchanged on planning-only slots.
b01/b02/b03 are waiting at B with zero step/owner questions; B approval is null. This proves a plan was offered, not owner approval or product acceptance.

Exact b01 sequence (r = question record; each maps through attempt/call_started to its call folder; comma lists are dispatch order, overlapping within a batch).
D=data, S=server, U=ui, L=delivery; E=exact-fix retry. Area REVIEW batches follow completed DETAIL batches; cached verdicts make no provider call.
Start: ALIGN r3 → ARCHITECT r14 → architecture REVIEW r21 (adequate).
R1, revision 2: DETAIL S30,D32,U34,L36→L55E; REVIEW U63,L65,S67,D69 → r95.
Trigger: initial four areas. L review raises absent local-assets plus n032's missing mixed-valid/invalid CSV→real HTTP integration. Others adequate.
R2, revision 4: ARCHITECT r101→105E → architecture REVIEW r112; DETAIL U121,D123,L125,S127→L142E,U146E; REVIEW L158,S160,D162,U164 → r190.
Trigger: r95's two gaps forwarded together. ARCHITECT rewrites areas/contracts/decisions/waves, invalidating all four DETAIL inputs; all four own plans and REVIEW inputs change. U now reports server-command absent.
R3, revision 6: ARCHITECT r196 → architecture REVIEW r203; DETAIL D212,L214,U216,S218→S233E,L237E→L245E; REVIEW D253,S255,L257,U259 → r285.
Trigger: r190 startup-agreement gap. All four DETAIL bases change (D only contracts/wave/decisions); all four REVIEWs refresh. D reports absent server-command/http-api/local-assets and missing real-HTTP contention; U reports missing real-server-stop browser recovery.
R4, revision 8: ARCHITECT r291 → architecture REVIEW r298; DETAIL D307,L309,S312,U314→S324E,L328E,U332E; REVIEW S348,D350,U352,L354 → r380.
Trigger: r285's three gaps. Contract text/endpoints do not change; wave/decisions change for every area, responsibilities also for U/L, so all four DETAILs rerun. S needs real Repository↔HTTP query/error proof; L requests fresh-folder integration, targeting guide.
R5, revision 9: DETAIL S384,D387→D391E; REVIEW S403,D405,U407,L409 → r435.
Trigger: r380 routes S's gap to S and guide to D (guide's hosting area), although D cannot edit the generated guide. S/D plans change; U/L local plans are retained but their S/D peer checks change. U finds keyboard search/filter coverage missing; L finds real importer→HTTP proof missing and stale named peer checks.
R6, revision 10: DETAIL L439,U441→L446E→L454E; REVIEW D462,U464,S466,L468 → r494.
Trigger: r435's two gaps, batched. L/U change; D refreshes for L peer text, S for L/U peer text. Only U has a gap: link existing n027 labels/contrast evidence to quality:006.
R7, revision 11: DETAIL U498; REVIEW L506,U508,S510 → adequate r530 → B request r532.
Trigger: r494's quality link. U also rewrites check purposes/evidence, so L/S receive changed U peer text; D's verdict r487 is reused. This is three reviews, not a full four-area re-review.

What was actually redundant (overlapping categories must not be added):
21 logical DETAIL jobs + 12 exact-fix retries = 33; 4 architecture REVIEWs + 27 area REVIEWs = 31; 4 logical ARCHITECT jobs + 1 retry = 5; ALIGN=1.
Zero byte-identical repeated questions; zero repeated successful DETAIL jobs with both unchanged basis and unchanged correction; zero same-area REVIEWs with identical supplied inputs.
Six REVIEW calls have unchanged LOCAL plans: U407/L409, D462/S466, L506/S510. All six have changed peer text; four return adequate, two reveal gaps. Zero are demonstrated refreshes with wholly unchanged consumed input.
Full four-area reviews occur after two changed local plans in R5/R6; when only U changes in R7, two consumers refresh and D is reused. Adequate is not evidence of redundancy: 22/31 verdicts are adequate, including all four architecture reviews.
The three false missing-agreement routes occupy 39 calls and 16.09 min (r101 through r378), including real repair work; 12 of those are regenerated DETAIL jobs, 12 are area reviews, 8 DETAIL retries, 4 ARCHITECT calls, 3 architecture reviews. These are gross exposed cost, not 39 safely deletable calls.
Exact proof of the projection bug: revision 2 delivery consumes local-assets; revision 4 ui consumes server-command; revision 6 data consumes http-api/server-command/local-assets. All are in merged contract nodes, absent from their REVIEW Contracts facts.
All 13 exact-fix retries total 12.29 provider-minutes (overlap makes this larger than wall savings): seven reject a check naming its own provided csv-entry/local-assets contract; five reject supplied owner-qualified peer checks in quality coverage; one rejects ui also appearing among its own contract consumers.
Those are structural-normalisation opportunities, not repeated semantic reviews. In particular, peer coverage must resolve against the final canonical owner/check; blindly deleting references would discard promised proof. R5 also spends two D calls on the misrouted guide gap.

ONE rule: a question is invalidated only by a change to the canonical facts its subject consumes; an existing agreement is supplied by code, never repaired by an LLM because a projection omitted it.
Keep semantic gap judgment, owner routing, answered-direction recovery, real peer-change refresh, and the single combined B. Compare structured canonical content directly; no new hashes, counters, caps, scheduler, or semantic text-equivalence heuristic.
Keep the existing parallel pools and round batching: observed peak concurrency is 4/4/5 in b01/b02/b03. Removing peer invalidation outright would reintroduce stale approval; deleting answer IDs alone saves zero proven b01 calls because peer text really changed.

Smallest first landing (two production files; one owner; paths under src/seldon):
1. plan_review.py:briefs — delete the outline-endpoint contract filter (lines 26–28). Project each area's provided/consumed agreements from merged unit/contract nodes (existing architecture.contracts_for); preserve original contract handles in the brief. This removes all three demonstrated missing-fact ARCHITECT routes without weakening review.
2. questions.py:peer_checks and its callers — use explicit area-answer snapshots: REVIEW reads document.areaDetails for providers actually consumed in that merged plan; DETAIL supplies its existing eligible prior snapshot. Delete REVIEW's inference of peers from old outline endpoints/latest matching history. Peers must describe the plan being approved.
3. plan_review.py:step — replace whole answer-record IDs in reuse basis with the actual local answer content and consumed peer/proof content, normalised to area-local handles. Retain changed quality links, contracts, decisions, owner words and question/schema changes; exclude transport IDs/global renumbering. Reuse a verdict only for equal inputs, including across reopen.
Acceptance is canonical merge → correct bounded REVIEW facts → real local correction → retained sibling verdicts → B. No run/store/schema/recovery/provider changes belong in this landing.
Estimate, not replay proof: on b01-scale work expect 20–30 fewer calls and 8–12 minutes saved (roughly 40–50 calls/16–21 min), replacing three architecture cycles (39 calls total) with genuine local repairs. The directly avoidable architecture routing alone is 7 calls/~4.96 serial min; replacement local work and different model answers determine net savings.
Do not add the 13 retry savings to that estimate: many retries sit inside those same cycles. Canonical reference normalisation in architecture.py/plan.py is a separate measured follow-up; no blanket foreign-reference acceptance. Global DETAIL invalidation on genuine architecture rewrites also remains; this first landing removes the demonstrated false rewrites, not every possible planning cost.

Outcome journeys (proposed, not executed; extend tests/seldon/test_review.py and gap_owner_journey.py through test_journey.py):
• Existing-contract twin: use retained R1/R2/R3 answers through the real compiler/store; a unit consumes an existing contract omitted from outline consumers. REVIEW receives its exact canonical text and provider proof; the genuine CSV gap repairs locally and B appears. Existing endpoint-aligned fixtures miss this mismatch.
• Missing-contract twin: remove the contract from the canonical producer; the same consumer need must reach ARCHITECT, receive a real agreement, repair and reach B. This catches a projection fix that hides genuine gaps; the existing-contract twin cannot.
• Local-link/no-op twin: repair one local obligation without changing any peer/proof content consumed by siblings, then reopen; the repaired plan reaches B with sibling verdict provenance retained. Re-emit identical content under new IDs/global numbering. This catches ID-driven refresh; existing area-records tests change actual peer text too.
• Changed-peer twin: change an exported check's meaning or remove proof while the consumer plan stays fixed; consumer judgment must see the new facts and withhold B until its concrete gap is repaired. Existing success replay supplies old verdicts again and cannot prove freshness. Include quality-only peer coverage changes: the replacement basis must retain Proof map information when answer IDs are removed.
• Preserve the owner-direction/reopen journey and mixed-gap routing: every direction reaches its planner, unresolved sibling gaps survive, and a real unresolved conflict remains a resumable question rather than false B. The guide→data misroute is an existing risk to track separately, not silently certify away.
For each journey print baseline/candidate DETAIL, REVIEW, ARCHITECT totals by area, retry totals, question bytes and elapsed time; never assert call counts or a duration target. Assert the semantic plan, correct available facts, gap resolution, provenance and B/waiting outcomes.
Recorded-answer journeys establish routing and reuse, not new model convergence or minutes saved. Only a later explicitly authorised planning-only cohort can confirm the estimate; this review launches none.
