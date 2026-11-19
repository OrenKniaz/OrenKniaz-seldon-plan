T-102: requirement-local FLOW fixup; base 785cf55 (5800d4a golden-only), uncommitted.
Each failing requirement gets its own Gap with traced-check owners and only its corrections.
RED: fscope-3/red.log reopened unrelated u002; GREEN journey keeps its DONE row/verdict, repairs u001 and reaches SCRIPTED_C.
Final fast gate: 14 passed (base 13), 193.35s; golden 148.69s, scale50 57.77s; timing assertions unchanged, no skips.
Only flow_review.py + new test_flow_scope.py; patch reverse-apply/check passed; tracking updated.
No dependencies or real providers; ruff unavailable. Lead landing/real-run acceptance remain unperformed.
