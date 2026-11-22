# Lane leadGuardCovers (Terra 6.1 medium) — Lead only. Small, focused.
Repo: this lane dir = Seldon main 56a024e. Spec: BLUEPRINT-LEAD.md v0.4 section 2a (ratified): the guard walks the user path itself; a missing observation is the guard's job, never a reason for a builder turn or a user question.

## Evidence
x5 on 56a024e: hello 5/5, Foundation 5/5, ShelfLife 4/5 verified C; every run took 5 calls and had 0 faults except one.
1. ShelfLife gs02 (C:/seldon/tests/gwShelf/gs02.log, slot from C:/seldon/tests/gwShelf/slots.tsv): the builder receipt lacked per-promise checks, the RECEIPT correction call still lacked them, then Seldon asked the USER "Supply a check for each new promise and tryItGuide: ..." (inputOwner Seldon, step PROVE). That rule predates v0.4. Fix: when builder checks are missing for a promise, the guard covers that promise in its walk (it already receives every B action, result and notMetIf). Missing builder checks never block and never become a user question. Keep RED on the real base for new behaviour where a builder witness exists; where none exists, the guard's walk on base and candidate is the evidence. Delete the now-dead blocking branch rather than adding a new path.
2. ShelfLife (C:/seldon/tests/leadGuardC-0/REPORT.md): C marked quality:accessible-use "observed" though the walk only used programmatic focus, not Tab traversal or keyboard filter operation. The guard must mark a subject observed only when its recorded actions actually exercise it as the person would; otherwise it lists the subject as partly observed, with what is missing. Prompt-level change in the guard instructions; no new mechanism.
TRIAGE each: FAULT SELDON + BUG|DESIGN. Net production lines must go DOWN.

## Prove
Golden/journey tests only; extend the golden path so a receipt missing a promise's check still reaches C via the guard. Cold imports. Gate: PATH=~/codex-harness/.venv/Scripts:$PATH bash scripts/gate.sh leadGuardCovers (no SELDON_* env; nothing else running).
Real exit, Terra medium: ShelfLife x2 via SRC=<this lane dir> SELDON_MODE=lead SELDON_ROLE_MODEL=gpt-6.1-terra SELDON_ROLE_EFFORT=medium FIRST=medium SLOTP=shelf-gc DREAM=~/codex-harness/work/fight-1/shelflife-brief.md bash /c/seldon/tests/coord3-20261120/cohort2.sh gcShelf gc 2 2 2 (slots and temp under C:/seldon/tests). Both must reach verified C. Report calls, fresh tokens, the per-promise observed/partly/unverified list and guard UI/UX feedback verbatim.
Report: C:/seldon/tests/leadGuardCovers-0/REPORT.md <=25 lines. Leave the diff as lane.diff; do not push. Never open desktop windows.
