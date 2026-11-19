TRIAGE FAULT SELDON
DESIGN: Fable 2026-11-16 sections 1/4 Lane C + Oren 11-16 obligations removal; base c8cc0f0b213ca4e1ee5496743da9c4597d8caede.
Removed shackles 11/12: gap-derived requirement verdicts, no judge booleans/consistency refusals; area-derived consumers, provides only for multi-unit providers; obligations.py and no-op ARCH-REVIEW deleted.
Files: src/seldon/{architecture,decisions,detail,flow_review,inference,judgment,obligations(deleted),plan,plan_review,questions,run,schema,states}.py; tests/seldon/{test_journey.py,recorded_judge_minimal.json}.
Src Python lines 4365 -> 4237 (net -128); including kit assets 4444 -> 4316. Suite cases 23 -> 24; contract fan-out proves canonical architecture/detail -> worker briefs -> real integrated checks -> scripted C.
Focused: python -m pytest -x -q tests/seldon/test_journey.py -k 'unit-rework or parallel-contract or contract-fanout or flow-fault or product-fault' -p no:cacheprovider --basetemp=C:/seldon/tests/thinJudgePlain-2/pytest: 5 passed/18 deselected, 55.87s; -1 had 2 passed/1 test-label failure, corrected.
Gate ONCE: venv Scripts first on PATH; PYTHONPATH=src;tests/seldon; python -m pytest -x -q tests/seldon -p no:cacheprovider --basetemp=C:/seldon/tests/thinJudgePlain-3/pytest: 24 passed, 491.55s; no timing assertions or >5min hang. Diff/reverse-apply checks pass.
Retained judge question/schema/example migrated once; no recorded-answer judge replay test exists here. T-179/STATUS updated; no providers, gate.sh, commits or .env reads. Lead review/landing and real-provider validation remain.
