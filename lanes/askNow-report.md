T-162 askNow: uncommitted on cefecc8 (b2f0f13 golden-only); askNow.patch changes scheduler.py, run.py and test_journey.py.
Questions are handled inside the active scheduler; explicit direction resumes that unit in-wave; unanswered questions drain useful work before WAITING.
src +24/-24 net 0; collected journeys 74 -> 76; both new outcomes also extend clean_core_golden.
RED askNow-1: old scheduler fails sibling-still-WORKING outcome (98.76s); GREEN askNow-2: immediate direction + dev non-gate WAITING, 2 passed/17.67s.
GREEN askNow-3: unchanged rule3_scale50_journey, asked_unit_journey[4] reopen/direction, contract_fix_journey[user]: 3 passed/148.85s; scale reaches SCRIPTED_C.
Swept ALL lane and semantic-cc/tests/seldon assertions; no stale assertions found. AST, diff-check and reverse-apply check pass.
No commits, gate.sh, real providers, dependencies, forbidden-source/doc edits or >5-minute terminal hangs; temp only C:/seldon/tests/askNow-{1,2,3}.
Tracking T-162 remains in_progress, delivered for lead review/gate/landing; real-provider latency and product acceptance are unproven.
