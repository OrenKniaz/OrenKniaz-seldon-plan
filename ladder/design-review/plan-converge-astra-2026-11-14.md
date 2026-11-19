Planning convergence, 14 November 2026

The wall is real, but it is not one missing global planner. Repairs reach the wrong owner, reviews lack facts, and recovery asks before applying a repair.
Reviewed 54eaab44431c1c7e3f98cbfa700c8caeb109a210 against CHARTER v1.8 and BLUEPRINT v1.10. The checkout is on cc/expansion-teach, at the supplied commit.
Evidence: k02/k04/k05 state.sqlite3 opened with URI mode=ro, their m2k logs, current source and the named landings. No providers or stored runs were executed or changed.
All three stores have B=null and no execution units. Their last completed transition is A into planning; the next unproven transition is a reviewed plan offered at B.

1. What actually prevents convergence

k02: the final reviewer question is whether delivery can depend on docs/try-it.md, not whether README should replace it.
At r182 it asks for the guide's owner, path and availability, or removal of that dependency. DETAIL r168 already supplied those exact code-owned facts; REVIEW r176 omits them.
questions.build supplies the guide fact only to DETAIL; plan_review.briefs explicitly excludes the guide unit. This is a missing-fact problem, not a missing product contract.
The allowed REVIEW answer has a free-text target. Its target is "architecture: contract_gap for the Seldon-owned final guide"; plan_review.step routes to ARCHITECT only on exact equality with "architecture". r186 therefore routes it back to delivery.
The README-only directions are simulated-owner words r188/r198, not reviewer verdicts. DETAIL can rewrite delivery's records but cannot remove the guide: plan.add_guide always inserts it and validate_owned_work reserves its path.
More immediately, neither direction gets a DETAIL call. r196/r206 record proposed repairs and immediately ask again at r197/r207; revision stays 5. There is no evidence those directions failed after execution.

k04: r268 correctly finds overlapping validation, query and concurrency matrices: persistence n008/n010/n011 and server n020.
But the proposed correction says to keep server's matrix and narrow persistence. plan_review.step assigns every non-architecture gap to the reviewing area, so r272 targets server alone.
DETAIL can replace server-local records, subdivide that area, or return contract_gap. architecture.local_plan forbids writing another area's records/scopes; the persistence plan and its adequate verdict remain reusable.
There is another constraint: validate_owned_work requires a local check for each owned requirement. Simply deleting persistence's duplicate matrices can leave its requirements unprovable under that rule.
The reviewer also overreaches: n020 is a wave check containing the full validation/query/race matrix, contrary to v1.10's one agreement path. Moving every case into that wave check is not the fix.
Use ARCHITECT's existing authority to regroup inseparable server/persistence behaviour into one backend owner, then DETAIL can place the required real-HTTP matrix locally once. Keep UI/importer work independent.
Again the directions never run: r282/r292 ask at r283/r293 without DETAIL or a new revision. The final plan is still revision 5, not six successively repaired plans.

k05: interface REVIEW r82 asks it to reuse backend query coverage for quality:5. Interface DETAIL returns contract_gap at r95/r130 because it cannot name that coverage.
The check is not missing: backend r99 already covers the real HTTP query rules; r146 explicitly plans new:backend-query-check with its provider requirement. Neither record is supplied to interface DETAIL or ARCHITECT.
architecture.local_plan rejects foreign quality-check references: "Quality coverage must name local checks". ARCHITECT can answer only areas/contracts/decisions/waves; its schema cannot create a check or a requirement link.
Thus r108/r155 defer an "existing evidence" reference that belongs to planning structure. ARCH-REVIEW r164/r182/r200 then demands that very check from the outline-only question.
The smallest valid answer already fits today's schema: backend links its own query check to criterion 5; interface links its own presentation checks; plan.merge unions both owners' quality coverage.
Read-only, in-memory verification: the foreign interface reference is rejected; merging retained backend/interface/delivery answers with backend's extra criterion-5 link succeeds and produces the combined proof map. This is structural feasibility, not B or reviewer acceptance.
After r167, owner answers only trigger new ARCH-REVIEW calls on unchanged revision 4. No ARCHITECT call follows either answer; the last architecture answer is r155.

The shared recovery defect is exact: recovery.failed asks on bool(state["answer"]) or stage>=2; answered clears waiting but retains answer and stage.
planning invokes that test before advance. REPAIR therefore asks before reaching DETAIL; ARCH-REVIEW asks before reaching ARCHITECT. Routing the same gap through REPAIR and DETAIL also charges it twice.
Four recorded routing events are treated as failed approaches even when they describe different gaps or the same handoff. These are not demonstrated fixed points.

2. One rule

Repair the smallest complete ownership slice of the canonical plan, then judge that changed slice: the repair must reach every owner whose records must change.
LLM decides semantic adequacy, duplicates and responsibility changes; code resolves owners, supplies existing facts, merges links and applies the chosen route. No prose parsing or automatic semantic deduplication.
Existing ARCHITECT changes responsibilities/contracts/scopes; existing per-area DETAIL changes the affected records. Do not add a whole-product rewrite call or a new planning phase.
A missing fact is retrieved; an existing provider check is linked by its provider; a cross-area ownership conflict goes through ARCHITECT. An outline reviewer cannot require DETAIL records before DETAIL exists.
Ask the user only after a completed correction leaves the same unresolved obligation with no available within-scope move, or a semantic decision needs changed commitments. Counts and renames establish neither condition.
An answered question must resume its pending correction once before any recurrence judgment. Preserve history and reopen safety; do not reset it to buy another allowance.

3. Keep, narrow, delete

Keep v1.10 and provenOnce's purpose. Narrow the proof map: plan.merge currently expands a crossed contract to every requirement of its provider unit, and briefs reconstructs crossings from those broad links.
That creates false proof claims: k02 r90 flags static-entry proof attached to accessibility/presentation. Separate agreement crossings from explicit behaviour coverage; never infer that all a provider's requirements were proven.
Keep c486ed0's return to ARCHITECT and derived local reads. Replace its exact-string target switch and the caller-area default; do not revert to endless local contract repairs.
Keep depGraph b2f0f13. Nothing in these traces justifies restoring dependencies for contract text or wave-check authoring.
Keep durable lineage; delete planning's attempt-count escalation and its answer-present shortcut. Count completed failed corrections for diagnostics, not routing handoffs or successful subdivisions.
Keep guideUnit's parallel writing and WAVE-VERIFY walkthrough. Its new scheduling is not the demonstrated k02 fault; expose its canonical owner/path/stage to REVIEW as well as DETAIL.
The hard-coded separate guide cannot honor the saved README-only directions. Do not call an old k02 resume successful while ignoring them. Reusing a planned documentation owner is a separate guide-policy simplification, not necessary to repair the original reviewer gap.
Do not roll back the whole 03694dc bundle or demand more tests/provider rounds to compensate for these structural faults.

4. Smallest complete planning change list, delete first (paths below are under src/seldon)

recovery.py, decisions.py: remove pre-dispatch count/answer gates for planning; persist the pending correction and its answered continuation. Judge recurrence after the correction result, preserving the existing lineage.
plan_review.py, detail.py: remove double charging, broadcast user-direction repairs and routing by the reviewer's area. Dispatch record-targeted corrections to their actual owners; ownership changes use ARCHITECT. Retain unresolved sibling corrections when an architecture correction runs.
schema.py, questions.py: replace free-text REVIEW routing targets with supplied record/area handles plus architecture; correction remains plain words. Supply bounded peer proof records and the code-owned guide fact, not whole sibling plans.
run.py: resume the chosen pending planning route after a step answer instead of re-running the failed gate; ARCHITECT receives the affected ownership slice and existing planned proof facts.
plan.py, schema.py: delete blanket provider-requirement expansion; retain crossed-contract links separately from explicit check coverage. Reuse today's per-owner quality lists and merge; do not add foreign-check authoring or an evidence-handoff subsystem.
plan_review.py: remove proof-dependent verdict reuse that ignores changed peer proof. Its current basis deliberately excludes Proof map; key affected review reuse on the contributing canonical area records, without global handle-renumber churn.
architecture.py needs no new cross-area editing power: its existing outline and local ownership contracts suffice. No scheduler, worker, provider, budget or contract-text compatibility layer is needed for this planning repair.

5. Outcome journeys and the next cohort

Extend tests/seldon/test_review.py and wire through test_journey.py; replace the insufficient planning recurrence case in lineage_journey.py. Use recorded plans and the real compiler/router/store, with scripted semantic responses clearly labelled.
k02-shaped: replay the pre-question delivery plan; REVIEW receives the already-declared guide agreement; the corrected fresh-folder check and one guide walkthrough reach B without a repair question. Existing guide tests miss DETAIL/REVIEW fact disagreement.
k04-shaped: replay the conflicting proof owners; a named ownership correction combines only the backend responsibility; DETAIL emits one local HTTP matrix and agreement-only crossings; affected reviews refresh and B appears. Existing provenOnce deletes a duplicate inside one owner and misses this transfer.
k05-shaped: replay r82 with the retained backend check; route criterion-5 coverage to backend, merge with interface coverage, retain browser checks and reach B without asking ARCHITECT to invent a check. Existing contract-gap tests cover an absent contract, not an existing check hidden from its consumer.
Across those journeys, interrupt/reopen after one owner answer and prove the requested correction actually runs before another question. Existing recurrence tests check a new question/history, not successful continuation after direction.
One fixed-point twin must retain a real unresolved semantic conflict, show the attempted correction, ask once, remain resumable and never offer B. A changed wording or increasing attempt count is not its oracle.
Replays start before simulated-owner intervention. The saved README-only k02 direction remains unsupported until guide ownership is simplified; do not silently resume that slot as though its direction were honored.
Before another cohort: one coherent candidate passes these observable B journeys, recorded-answer replay and the existing golden/50-unit gate; the old missing-contract path still repairs, and unchanged sibling work is reused.
One owner should integrate this planning repair; no third prompt-only patch, arbitrary retry increase, weakened review or forced B. The reviewer must inspect the resulting plans, especially wave matrices and false coverage links.
No new cohort until these checks pass on its exact candidate and an explicitly authorized real planning replay settles whether the revised briefs actually converge. Scripted B proves the machine, not model behaviour or C.
