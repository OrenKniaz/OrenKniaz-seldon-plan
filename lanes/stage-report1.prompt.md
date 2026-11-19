LANE stage-report1: dev-run findings report for the clean core. Worktree: C:/Users/oren/codex-harness/work/lanes/stage-report1. Temp files only under C:/seldon/tests/report1. You cannot delete folders, so use a new folder name for each retry. Do not commit. No unit tests. Touch nothing under src/codex_harness.

Read section "Dev-run findings" and "LLM question rules" in C:/Users/oren/codex-harness/work/ladder/CLEAN-CORE-DECISION.md, then src/seldon and tests/seldon/real_hello.py. A real run leaves a slot like C:/seldon/tests/core1/real-lead-01 with calls/call-*/{question.json,answer.txt,result.json,invocation.json,stderr.bin,...} and a store under product/.seldon or similar.

BUILD tests/seldon/run_report.py: a dev tool, stdlib only, importing nothing from production code unless a read helper is clearly simpler. Usage: python run_report.py <slot>. It prints a one-page plain-language report and appends one row to C:/Users/oren/codex-harness/work/ladder/RUNS.md (create the header once).

Report, per run:
- OUTCOME: furthest state reached, ACCEPTED or INCOMPLETE and its reason, wall time.
- RED FLAGS, listed first and loud: repair count with each cause; exact-fix retries by schema field and error; refused citations; uncertain answers; repeated questions with unchanged facts; blocked workers.
- REVIEW LOG: every reviewer and judge gap, target and correction text in full, tagged PRODUCT or SELDON-LEAK when mentions of Seldon's own workflow terms (check-in, bead, wave, evidence dir, review process, SELDON_) make that plain; otherwise UNTAGGED. Do not call an LLM.
- SCHEMA: which fields were wrong most often; fields present in the schema that the model filled with empty or placeholder values.
- SEMANTIC: facts supplied but never cited, per state; tests that exited 0 where the judge said gap, and the reverse.
- EFFICIENCY: per state, calls, wall seconds, prompt bytes, answer bytes, and tokens if the provider result has them; plan size in nodes and bytes.

RUNS.md row: date, slot, commit, outcome, furthest state, repairs, retries, gaps, uncertain, wall time, calls, plan nodes, plan bytes. RED FLAG COUNT goes in the row too. A real run with zero repairs and zero retries on hello-world is the target.

Have tests/seldon/real_hello.py call it at the end, whether the run succeeded or not, and never let a report error change the run's own result.

PROOF: run it on the existing slot C:/seldon/tests/core1/real-lead-01, using a RUNS.md path overridden to a temp file under C:/seldon/tests/report1 for the test, and check its numbers by reading the slot: 4 calls, REVIEW gap present. Add one journey assertion only if it is cheap.

DELIVER in C:/Users/oren/codex-harness/work/lanes: stage-report1.patch (git diff against base including new files), stage-report1.patch.sha256, stage-report1-report.md (at most 8 lines, plus paste the tool's output for real-lead-01).
