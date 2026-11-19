TRIAGE FAULT SELDON
DESIGN: strict required gap severity; must-fix alone routes repair; nit/pre-existing remain notes at C; shared FLOW prompt, no new state/caps.
Base deaad8d tree b5706478e27ff20cc4a2e4c67b20b0752b81bb2b equals supplied clean 4a464a2 snapshot; patch src+tests only, 11 files.
Src lines 4644 -> 4671 (+27); semantic cases 64 -> 66; golden note twins and retained must-fix owner repairs PASS; 25 cold imports PASS.
Sole bash scripts/gate.sh judgeEval, venv first PATH: 66 passed, 0 skipped, 390.30s; no post-gate src edits/re-gate or observed individual test hang.
Eval tune ONCE: Codex gpt-6.1-terra medium, 19 calls, 18 valid answers; recall 0/3 (0%); false alarms 0/15 answered negatives (0%); 1 timeout/unscored control.
Per kind: JUDGE recall0/3 FA0/5; FLOW recall N/A FA0/6; PRODUCT recall N/A FA0/4 plus1 timeout. Semantic key adjudication, no keyword matching/grader calls.
Cases34: MUST_CATCH6 / MUST_NOT_FLAG8 / CONTROL20; tune19 (3/4/12), holdout15 (3/4/8,44.1%) sealed/unrun. Eight-positive target NOT met; correlated closure cases only (T-204).
Timeout300.141s: cleanupVerified=true, quiescenceVerified=true, activeProcessesAfterTeardown=0; no retry. Source/corpus frozen; scoring-only denominator correction recorded in manifest.
Tooling: work/ladder/judge-eval/{cases,tune,holdout}.jsonl, eval.py, README.md, report.md; T-202 source/eval delivery awaits lead review; no commit/.env reads; all temp judgeEval-1..3.
