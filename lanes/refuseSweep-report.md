TRIAGE FAULT SELDON + DESIGN
T-238 · Shared handle resolution prefers exact handles, then local trace and unique aliases. The answer transaction records derivations. A shows vision notes, B shows plan notes, and check-in shows work notes. DECIDE text cleanup is recorded and can appear on a subsequent A request.
Exact base 0f41344, tree edfca51d. Seldon src 6,712 → 6,853 lines (+141), Python 6,568 → 6,709.

| Base file:line | Check | Class | Candidate behavior |
|---|---|---|---|
| answers.py:6,23–29 · questions.py:1001–1021 · schema.py:139–172 | Reply parsing, typed shape and error carriers | B/M | Preserve rendered ALIGN literals. DETAIL may leave a sole unit's links empty. Other malformed replies use exact schema corrections. |
| questions.py:232–291 | ALIGN duplicate IDs, constraint links, sources and affected subject | B/M | Deduplicate identical records, resolve handles, keep a question on the vision when its subject is unavailable. Re-ask for missing constraints and conflicting values. |
| run.py:267 | Model size differs from the user's choice | B | Use the selected size and record its authority at A. |
| questions.py:313–323 | DECIDE choice text | B/M | Remove surplus text on listed choices. Re-ask for the missing verbatim direction on Other. |
| architecture.py:78–83,182 | Repeated IDs and area/contract namespace collision | B/M | Collapse identical entries. Re-ask for conflicting definitions or distinct handles where one durable ref would overwrite another. |
| architecture.py:157,165,169,175 · inference.py:90 | Area commitments, horizon and first runnable slice | B/M | Resolve aliases, assign omissions to the sole area or final wave, record derived steering waves. Ask for missing work ownership, stage goals or genuinely unknown commitments. |
| architecture.py:188 · plan.py:26,61,433,441,464 | Product scopes | B/M | Remove duplicate paths and redundant guide ownership. Ask for a usable scope or a decision about overlapping writers. Preserve path confinement. |
| architecture.py:195,199 | Contract ends and decision areas | B/M | Resolve definite area aliases, remove duplicate/self readers, preserve runtime text as an assumption. Ask for unknown product endpoints. |
| architecture.py:212,219,227 · plan.py:403,410 | DETAIL edit IDs and feature/requirement references | B/M | Coalesce identical edits and resolve trace links from commitment to feature. Ask for unlinked or conflicting definitions. Keep canonical reference checks. |
| architecture.py:238,242 · plan.py:436,447,452 | Unit requirement assignments and order | B/M | Resolve links through features and commitments, fill sole ownership, collapse repeated dependencies and remove a sole unit's self-reference. Ask for ambiguous owners, unknown positions and actual cycles. |
| architecture.py:235,261,263,269,275,284 | Missing area scope and subdivision | B/M | Normalise child links and duplicate rows. Ask for missing commitments, new owners, or unapproved/colliding scopes. |
| architecture.py:50,56,61,63,68 · plan.py:423,426 | Compiled plan has no valid owner, path or trace | M | Preserve final validation. Ask for the missing area, scope, requirement or valid agreement. |
| detail.py:147 · plan.py:374 | Merge failure and disputed contract binding | M | Keep area-local corrections for unresolved providers and overlapping writers. |
| plan.py:131,138 | WORK update/retire IDs and check requirement links | B/M | Retiring an already retired owned ID is idempotent. Resolve links through the approved trace, including guide checks. Ask about unknown/foreign check IDs or links. |
| inference.py:95,126 · plan_review.py:27–39 | Verdict and correction data | B/M | Derive verdict from recorded findings. Ask for missing substantive findings. Keep rollback and R17 escalation. |
| inference.py:154 · decisions.py:325,333,403,407,453,487 | Candidate binding, user receipts and displayed selections | Guard | Retain candidate and user authority checks. |
| units.py:144 · fixups.py:18,22,40 · proof.py:118 | Guide artifacts and fixup evidence/owner | Guard | Require the real guide, current evidence and the approved writer. |
| judgment.py:112,125,129,132,199,209 · flow_review.py:25,27,39,103,113 · run.py:38–64,79,186 | Evidence, candidate, closure and run admission | Guard | Preserve proof and operating invariants. These checks consume durable state or observed execution. |

Base RED · Retained r114 WORK and r378 runtime-contract twins reproduce the reported failures.
Candidate · Both replay through scripted C. Reference and sole-ownership twins reach B; empty product scope gets a specific re-ask. The owner-size override reaches A/B.
Cold imports · 28/28. Patch applies to the exact base and reverse-checks against the lane.
Gate · Sole bare gate 140 passed in 403.89 s (405.14 s wall), baseline 135. Test-only follow-up: subdivision and reference 2 passed, restart and repeated retirement 1 passed after correcting the fixture to survive reopen. No re-gate or subsequent source edits.
Scope · Scripted product proof. Lead review, landing and an authorized Terra rerun remain.
