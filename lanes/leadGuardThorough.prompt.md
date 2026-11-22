# Lane leadGuardThorough (Sol 6.2 medium) — Lead only.
Repo: this lane dir = Seldon main d29d82a. Spec: BLUEPRINT-LEAD.md v0.4 section 2a (ratified). Read C:/seldon/tests/leadGuardCovers-0/REPORT.md and gc01/gc02 summaries first.

## Where it stands
Lead now takes 5 calls and 1 WORK per run, and the guard honestly lists observed / partly observed / unverified at C. Two Seldon faults keep ShelfLife from verified C:
1. T-286 (FAULT SELDON + BUG): in gc01 the guard found real B-quoted product defects (oversized quantity broke the API and the import) but they were listed as "unverified" instead of routed to the builder as a repair with the reproducing action. The evidence text did not match the action key, so the binding dropped them. A demonstrated defect against a B line must go back to the same builder session (resume) with the failing action and expected vs got. Afterwards the guard re-walks only what the repair touched plus the promises the defect affected.
2. Guard thoroughness (FAULT SELDON + DESIGN, coaching not rules): it marked keyboard traversal and contrast "partly observed" although it has full access and a headless browser. Coach the guard to actually do what a person would: press Tab through the page and operate controls by keyboard, compute text/background contrast from the rendered page, inspect the SQLite file when data integrity is promised, and run manual guide steps it was asked to check. "Partly observed" is for what truly cannot be done on this machine (for example real hardware), always with the reason. Prompt and tooling hints only. No new checking mechanism in code unless a helper is clearly simpler.
Net production lines must not grow.

## Prove
Golden/journey tests only; extend the golden path so a guard-found B-quoted defect reaches one repair WORK and then verified C. Cold imports. Gate: PATH=~/codex-harness/.venv/Scripts:$PATH bash scripts/gate.sh leadGuardThorough (no SELDON_* env, nothing else running).
Real exit, Terra medium: SRC=<this lane dir> SELDON_MODE=lead SELDON_ROLE_MODEL=gpt-6.1-terra SELDON_ROLE_EFFORT=medium FIRST=medium SLOTP=shelf-gt DREAM=~/codex-harness/work/fight-1/shelflife-brief.md bash /c/seldon/tests/coord3-20261120/cohort2.sh gtShelf gt 3 3 3. Target: 3/3 verified C (verification_complete=true). Report calls by kind, WORK, fresh tokens, active minutes, the observed/partly/unverified list per run, any repair with its defect, and the guard feedback verbatim.
Report: C:/seldon/tests/leadGuardThorough-0/REPORT.md <=30 lines. Leave the diff as lane.diff; do not push. Never open desktop windows.
