# Efficiency review — Astra, 2026-11-16

Another 30% reduction in the supplied token-cost proxy is plausible; 50% is not supported. A 30–50% wall-time cut is also not supported by these recordings. The strongest measured deletion saves about 10% of that proxy and 8% of elapsed time. Aim first for roughly 20–30% less proxy cost and 10–20% less wall time, then measure.

I read CHARTER, BLUEPRINT R2/R9/R15/R16, the three earlier speed reviews, current source, all 835 recorded questions/answers/usage streams, and the 20 stores read-only. Only this review was written; no providers or tests were launched.
Source references below are relative to work/sprint-20261027/semantic-cc/src/seldon at ab2ae1f. Cohort source was e57b218; the intervening change adds judgment guidance, not measured savings.
Evidence paths are C:/seldon/tests/m1/shelflife-main-e57b218-zNN/calls/call-PREFIX…; prefixes below identify calls. Times run from first question.json to last stdout.bin modification, excluding subsequent acceptance and unrecorded waiting.
The supplied completion claim needs qualification: 19 stores contain SCRIPTED_C; z11 still contains EXECUTE. Their retained final feature/quality verdicts total 100 satisfied and 106 not judged. Oracle 36–39 is reported by the brief, not independently rescored here. Scripted C does not establish complete semantic closure.

Across the cohort: 33.126M input tokens, 24.137M cached (72.9%), 8.989M uncached, 0.783M output. Median recorded span is 10.99 minutes, range 8.34–17.27.
“Cost” percentages below use the brief's proxy, uncached input + output = 9.773M tokens, not money. Cached input still costs something and output has its own rate; no invoice saving is established. In price units, total cost is 8.989*p_input + 24.137*p_cached + 0.783*p_output, with token counts in millions.
WORK uses 28.9% of the proxy, FLOW 19.6%, PRODUCT 18.9%, JUDGE 15.1%, DETAIL 7.6%, REVIEW 6.8%; everything else is 3.1%. WORK emits 72.4% of all output and has 90.0% input caching. FLOW caches only 22.0%, JUDGE 22.7%, PRODUCT 48.8%. Total input alone makes WORK look more dominant than uncached work does.

The current critical path is ALIGN → ARCHITECT → parallel DETAIL → parallel REVIEW, sometimes repair/review → parallel workers and their local proof/judges → guide → integrated checks → FLOW → PRODUCT.
Planning to first WORK takes a median 2.06 minutes. A guide call takes a median 1.12 minutes; it still waits for every product unit. The span from first FLOW to last answer is a median 1.89 minutes, including later repairs.
z01 makes the serialization visible: plan 0–2.94; product workers/judges 2.94–5.88; guide 5.89–6.84; integrated checks/dispatch to 7.39; FLOW batch 7.39–7.60; serial FLOW re-asks to 8.03; PRODUCT batch 8.04–8.33; serial PRODUCT re-asks to 9.27.
FLOW and PRODUCT already fan out within their stages. They could inspect the same frozen candidate concurrently; PRODUCT facts do not consume FLOW answers. Preserve the user check-in and apply no repairs until the candidate's replies are collected. Independent missing-fact resolutions could also overlap, but unchanged-fact calls should disappear.
Do not count the old guide-parallelism proposal as a new finding: plan.py:299–313 and units.py:139–144 still impose a delivered-product guide stage. Its old 4–7-minute saving is now inapplicable. The kit, ignored user config, and medium effort are also already present.
z19's 17.27 minutes includes real ordering, check-sensitivity and mobile-filter repairs after first FLOW at 9.09. Those minutes are not all orchestration waste.

The answers identify waste much more precisely than “judges always say satisfied”:
- FLOW: 167 calls = 51 satisfied, 12 gap, 104 uncertain. PRODUCT: 210 = 55 satisfied, 5 gap, 150 uncertain. JUDGE: 87 = 19 satisfied, 60 gap, 8 uncertain. REVIEW: 115 = 58 adequate, 57 gap.
- Exactly 107 FLOW/PRODUCT calls carry “Requested facts”: 41 FLOW and 66 PRODUCT. In every case every other fact is unchanged from the preceding same-subject question; all 107 return uncertain again. They consume 971,532 proxy tokens (9.94%) and 1,092 seconds (7.93% of summed recorded spans), about 55 seconds per run.
- These are not useful successful reviews: code eventually labels their result not judged. Deleting the empty second question must retain that uncertainty, never manufacture satisfaction.
- 171/254 uncertain FLOW/PRODUCT answers explicitly mention the source judgment. Final briefs compress its reasons into allSatisfied=false or “0 of N satisfied”; they then ask the model to reconcile a verdict whose findings it cannot see.
- z01 bed61d89 identifies an importer evidence gap because both observations are at T without the importer. FLOW 0cb30eef and re-ask 997957e0 ask for that missing source finding after integrated checks pass. PRODUCT 0bc5e88f repeats the same problem. This is a producer/consumer mismatch, not a reason to remove independent source judgment.
- Review is not redundant by default: 16 later REVIEW calls have exactly identical facts; 12 stay adequate, but four find new gaps. z05 399bc7d1 finds an unassigned visible API-error check; z16 342f47a7 finds broader concurrency coverage. Blanket reuse or deletion has no quality-preservation proof.
- Keep the guide's semantic comparison: 23 guide PRODUCT calls include three gaps, in z02 8a9bf963 and z13 d853fed5 (walkthrough differs from documented stop/import/restart), and z06 cafc4900 (PowerShell CSV encoding differs from the check).
- Keep visual and flow judgment: z09 d9b24b5b catches a clipped phone form; z20 da90e8ee catches unhelpful validation text; z19 65364e93 catches a missing phone filter. Six of the twelve FLOW gaps instead repeat z11's unavailable host-network-isolation demand; the newer R9 guidance addresses that, but has no new cohort evidence here.

Ranked cuts; estimates are whole-run percentages, overlap, and are not measured candidate results:

1. Stop re-asking without new facts; give final judges the actual scoped finding on their first call.
Replace the lossy source summary with each relevant unit's verdict, reason, affected obligation and proof stage. Include provided as well as consumed contracts when the flow needs them: architecture.crossed_contracts currently selects consumers only. Preserve genuine source gaps and distinguish pending integrated proof from a product defect.
If the requested evidence exists, supply it; otherwise retain not judged and its reason immediately. The current “Requested facts” branch only repeats check IDs and screenshot paths. This deletes a redundant turn, not an independent assessment.
Expected cost: 8–10%; wall: 6–8%, grounded in the exact 107-call deletion before changes to first answers. The removed usage is 0.956M uncached, 0.449M cached and 0.015M output tokens.
Touch flow_review.py:19–39,47–97,161–188; judgment.py:40–96,135–180; architecture.py:36–40. Coaching/data correction; src should shrink by removing empty retry branches. Keep existing candidate bindings and explicit unresolved records.

2. Remove accumulated execution history from decision briefs.
WORK “Execution facts” totals 1.137M characters, including 0.903M of full observation history; JUDGE “Proof execution” totals 0.956M, including 0.800M of history, alongside another 0.367M in “Observations”. z13 WORK be13c20a is 103KB; z11 JUDGE 1258460a is 125KB.
execution_facts walks every historical observation for the unit/dependencies, includes full unit rows, and lists every file in the base. Rework also adds failing/historical observations separately. That grows with attempts and, for the guide, with the product.
Supply current scoped evidence once, plus the particular historical RED/failure needed for this decision; retain the complete records in the store. Give workers scoped paths, necessary peer agreements and current corrections, not the entire accumulated execution record. Do not truncate source or discard evidence needed for a verdict.
Expected cost: 5–10%; wall: 1–4%, provisional because characters are not measured token attribution. Strongest scaling benefit: prompt size follows the subject and relevant evidence rather than run history.
Touch questions.py:238–244,247–294,309–344. Coaching/data reduction; src smaller by deleting redundant projections. This builds on the earlier proof-ownership review rather than repeating its stage-fix recommendation.

3. Judge shared quality evidence once per bounded area, returning separate criterion verdicts.
Of 144 PRODUCT calls excluding requested-fact re-asks, 52 repeat exactly the same final observations and image list as another PRODUCT call in that run. Their entire-call proxy is 481,530 tokens (4.93%); this is an upper bound, since the distinct criterion decisions still need output.
For example, z01's three page-quality criteria share identical evidence, as do two importer-quality criteria. plan.traced_checks already selects all checks in an area for each criterion, so the same area evidence is repeatedly transmitted.
Group those criteria under their area evidence, preserve a verdict for every accepted criterion, and keep the guide's distinct comparison. Split a large subject by its real scope, sending an indivisible subject whole; no count cap or whole-product question.
Expected cost: 3–5%; wall: 0–2% beyond cut 1, because initial calls already overlap. Larger-app benefit depends on maintaining bounded areas.
Touch judgment.py:10–24,40–97,126–189; schema.py:59–79; questions.py:87–90. Coaching; net src reduction is uncertain because a grouped answer needs decoding. Fold into the existing owner, not a new batching layer.

4. Put reusable prompt material before changing facts.
providers.prepare currently places the answer schema and example after subject-specific facts. Later identical contracts/history cannot be assumed cached merely because they repeat in text. The measured low FLOW/JUDGE cache shares make a small prefix-order experiment worthwhile.
Put stable role instructions, schema and example first, then stable scoped agreements, then current observations/corrections. Preserve native sessions and exact evidence; no cache service, synthetic evidence identity or model downgrade.
Expected cost: 2–5%; wall: 0–2%, low confidence until native usage replay. This overlaps cut 2, and counts only tokens shifted from uncached input; actual money saved is proportional to the uncached-minus-cached price.
Touch providers.py:200–202 and questions.py:215–217. Coaching/presentation; src roughly unchanged. Do not claim the native provider's entire fixed context can be removed.

5. Overlap FLOW and PRODUCT on one frozen candidate.
After integrated proof, prepare both sets of independent judgments together, then apply their findings through one controller. Keep per-subject verdicts, scope-tree invalidation, uncertainty and the user check-in. z01's initial batches take about 13 and 17 seconds: ideal overlap removes about 13 seconds, not their combined duration.
Expected cost: approximately 0% without measured repair savings; wall: 2–4% beyond cut 1. Earlier discovery may combine repairs, but I assign no numerical credit to that unproven effect.
Touch states.py:16–23; run.py:165–168; flow_review.py:148–188; judgment.py:126–189; reuse inference.batch:71–89. Scheduling, neither semantic coaching nor refereeing; src reduction uncertain. Do this after the simpler deletions, only if state changes remain small.

The optimistic proxy sum is about 30%; overlap and surviving evidence resolution lower it. I would budget a 20–30% experiment, not promise 30–50% in money. Wall savings are nearer 10–20%; larger reductions would require a newly measured reduction in worker/guide work or real repair frequency.
Preserve independent source review, integrated real-path RED/GREEN and all distinct accepted quality decisions. No hard caps, refusal limits, keyword acceptance, guessed pass states, or cheaper-role claim without replay evidence.
Next proof: replay recorded uncertain pairs and the named real-gap cases with Terra or Luna; first show no lost defect and honest unresolved evidence, then five small-model runs and a comparable 20-run cohort. Require oracle >=36 per completed run, retain unfinished runs, report unresolved judgments, and compare separately uncached/cached/output tokens plus time to the same product transition. A green oracle alone cannot validate deleted semantic coverage.
