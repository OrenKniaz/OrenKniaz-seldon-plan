Read-only review of the patch C:/Users/oren/codex-harness/work/lanes/stage-core6.patch, applied in this tree. Do not edit or run tests. Read CHARTER.md, C:/Users/oren/codex-harness/work/ladder/CLEAN-CORE-DECISION.md, and section 3 and change 3 of C:/Users/oren/codex-harness/work/ladder/design-review/clean-core-scaling-audit.md.

This replaces in-memory work state with one durable scoped unit, adds bounded concurrent workers, journaled publication, and a reopen path; it splits loop.py.

Report only P1s, or P2s that would break a real run of a small multi-unit app. Check especially: two concurrent units can never both publish a partial or overlapping result; crash at each publication step leaves a recoverable state; reopen never relaunches an uncertain writer and never loses a finished one; SQLite access is safe across the worker threads; evidence invalidation is really local; hello-world behaviour and prompts are unchanged; no shape that needs a second execution model later; module boundaries are real responsibilities and no god file is forming.
At most 14 lines, starting VERDICT APPROVE or VERDICT REJECT.
