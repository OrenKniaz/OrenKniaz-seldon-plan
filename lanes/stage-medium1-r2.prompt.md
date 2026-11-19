Round 2. Your diagnosis stands: review_prerequisite treats absent convergence as complete, so medium stops after one review round. Owner decision: fix it here, smallest change, because medium must keep three rounds and this is on the next real run's path.

Fix it at the existing owner (plan_acceptance.review_prerequisite and/or the review loop in plan_reviews): an unfinished review for this size is not complete, and the ordinary loop continues to the next round. No new state, no new records, no size special cases outside the existing rounds rule. Tiny/small stay at one round. Keep the 3-round assertion exactly as it is.

Time-box: if this needs more than about 30 net src lines, stop, change nothing further, and say why in the report.

Run only: bash C:/Users/oren/codex-harness/work/lanes/fast-gate.sh <this tree> medium1
Then regenerate stage-medium1.patch (cumulative against base) and stage-medium1.patch.sha256, and rewrite stage-medium1-report.md (at most 12 lines: TRIAGE, siblings, change, net src/tests lines, fast-gate result with seconds). Do not commit.
