Read-only diagnosis (Sol high). Do NOT run pytest or any long command (a quiet-host gate is running). No edits except writing your report as your final message.

Seldon main candidate 4e2c055 (sweep1 + recov1, approved patch b896df64) passed lane gates but FAILED the host publish gate: test_golden_path[cli], tests/python/core/test_golden_path.py:4579 "Packet fault point not reached". Full log: ~/codex-harness/work/ladder/design-review/publish-recov1c-red.log (see lines ~690-723 for the state dump: recovery choice "steer", options [abandon, readmit], held false, faultBeads C "Injected worker failure before product completion", afterPermission STEER, nextAction "Answer the outstanding meaning or authorize its code-selected provider"). Source: ~/codex-harness/work/sprint-20261027/semantic-cc (src/codex_harness/core/planner_recovery.py, planner_jobs.py, run_loop.py _recover, plan_store.py, record_io.py). This is the 4th host-only recov1 failure, each a different ordering (1: successor never launched; 2: dead controller -> unknown launch held; 3: this). Prior diagnosis: work/ladder/design-review/recovery-flake-diagnosis.md.

Answer, concisely:
1. TRIAGE BUG|DESIGN. What exact ordering produced "steer" after the user's explicit resume (send_steer continue, resume=True) instead of readmission reaching the packet fault point? Cite file:line for each step.
2. Is this a product bug (real users could hit it) or a test-only race (test assumes an order the product never promised)? Evidence.
3. Sibling cases: which other pause/resume/recovery orderings share the same shape.
4. The ONE simplest rule that removes the whole class (not a patch for this ordering), with LLM-or-CODE ownership row, and estimated line delta. If the right answer is "the twin asserts an unpromised order", say what outcome-only assertion should replace it.
5. Is it plausibly load-dependent (would a rerun on a quiet host likely pass)?
