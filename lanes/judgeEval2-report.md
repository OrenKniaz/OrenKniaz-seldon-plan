# judgeEval2 · T-232
Added 10 cases: 3 MUST_CATCH, 3 CONTROL, 3 EVIDENCE_GAP, 1 CODE_QUALITY. Four (40%) went to sealed holdout.
Terra medium, one 23-call tune batch per arm. Control recall 0/6, CONTROL false alarms 0/13, code quality 0/1, evidence gaps 1.
prompts2 recall 0/6, CONTROL false alarms 1/13, code quality 0/1, evidence gaps 1. One historical MUST_NOT_FLAG timed out and was excluded from its rate.
Judging misses: both missed the Stop-specific durable-save race, visible favicon 404s, unclosed SQLite connections and cramped source. prompts2 partially caught the stuck-running worker failure.
Evidence limits: the guide contains the examples and lacks recorded shell-specific execution. The ShelfLife heading oracle matches literal phrasing, and cleanup lacks handle attribution.
The prompts2 alarm exposed a weak historical CONTROL key: acceptance expressly requested a full offline check, and the packet only demonstrated an offline browser reload.
Full [paired report](../ladder/judge-eval/report-tune-2arm.md). Holdout remained sealed.
