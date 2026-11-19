TRIAGE FAULT SELDON BUG — src/seldon/questions.py:299 execution_facts runs Git in cwd=None after repair clears worktree; Git searches Seldon instead of the product.
Base: supplied63a2791 tree d4db4d701fd7149444825849da2a30cc718b3055 equals canonical15682aa; T-206 remains in_progress pending main landing.
Repro: copied original slot to C:/seldon/tests/notTree-2; Run.reopen/step reproduces r439 error with zero provider calls; fixed replay uses recorded r444 and reaches importer UNIT with zero new step failures.
Fix: read committed paths from store.root.parent; step_failure excludes gitwork.git/processes helpers and stores innermost file:line plus function. No new state or caps.
Files: src/seldon/{questions,decisions}.py; tests/seldon/test_journey.py; tests/seldon/fixtures/shelflife_not_tree.json (recorded store projection and exact candidate Git objects).
Src lines: 4657 -> 4660 (+3, all src/seldon files). Base regression 2 RED; fixed normal/missing-object twins GREEN; original waiver journey retained; 25 separate cold imports PASS.
Gate: bash scripts/gate.sh notTree, venv first PATH, once serialized: 66 passed vs base64, 0 skipped, 362.74s; no post-gate changes or re-gate. Patch base-index apply/reverse checks PASS.
Limits: no real providers, delivery commit, .env reads or >5min hang; temp only C:/seldon/tests/notTree-1..6. Main landing and resumed real ShelfLife execution remain unproven.
