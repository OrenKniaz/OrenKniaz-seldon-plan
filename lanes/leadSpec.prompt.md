# Lane leadSpec (Sol 6.2 medium) — Lead only
Repo: this lane dir = Seldon main d78cc5e (history rewritten 11-22; old hashes map in ../ladder/COMMIT-MAP-2026-11-22.txt). Spec: BLUEPRINT-LEAD.md v0.4. Evidence: ~/codex-harness/work/ladder/design-review/astra62-lead-vs-plain-2026-11-22.md — implement ranked change 3 only.
Problem: 29 milestone plans for 5 one-milestone ShelfLife dreams; 15 rewrites because the schema allowed omitting notMetIf (421 s); MILESTONES writes a spec AND a separate brief; REVIEW makes it repeat contracts the builder already gets verbatim.
## Build
- The reviewed spec IS the builder brief (one rendered document). User's exact constraints and guide obligation by reference with their text shown. Planner writes outcome, design choices, action/result and notMetIf once.
- Bound schema REQUIRES notMetIf; promise ids restricted to approved promises (normalise derivable fields, never refuse).
- One independent REVIEW of the rendered document; a material gap amends the named line, not a whole-plan rewrite. Unresolved coverage stays visible at B.
- Delete the separately authored brief and resubmission of unchanged plan text. Net production lines DOWN (est. -25 to -40).
Touch only lead.propose/review/render_builder, schema.lead_plan_schema and their prompt text; another lane (leadWalk) owns judgment/proof/build/fail — do not edit those.
## Prove
Golden/journey tests only. Cold imports. Gate: PATH=~/codex-harness/.venv/Scripts:$PATH bash scripts/gate.sh leadSpec (no SELDON_* env).
Real exit Terra medium (as leadWalk brief describes cohort2.sh with SRC=<lane dir>): Foundation x1 (default DREAM) and ShelfLife x1. Report MILESTONES/REVIEW call counts and seconds, plan rewrites, C.
Report: C:/seldon/tests/leadSpec-0/REPORT.md <=25 lines. Leave git diff, do not push. Temp only under C:/seldon/tests/leadSpec-0. Never open desktop windows.
