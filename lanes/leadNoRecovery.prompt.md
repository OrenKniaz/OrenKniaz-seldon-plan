# Lane leadNoRecovery (Sol 6.2 medium, one lane, Codex quota ~7% — be economical)

Repo: this lane dir (copy of Seldon main 54c774c). Binding: CHARTER.md, CHARTER-LEAD.md v1.1, BLUEPRINT-LEAD.md v0.2. Read work/ladder/AMBITION.md rules section if present in ~/codex-harness/work/ladder/.

## Problem (observed, census-lead-1.md)
EVERY Seldon Lead run logs at least one `lead_failure` fault record and exactly 1 recovery before reaching C, even the trivial hello dream (lh01-lh05, lf01-lf05). A plain agent needs none. So this is FAULT SELDON by default (blocker triage rule): something in Lead's own flow fails on the first try every time.

Evidence stores (read-only): C:/seldon/tests/coord3-20261120/leadHello7/lh0{1..5}/ and leadFound7/lf0{1..5}/ — each has summary.json and a product/.seldon/state.sqlite3. Do NOT read C:/seldon/sealed/.

## Do
1. From the stores, find the FIRST lead_failure in each hello run: which step, what Seldon expected vs what it got, and why. One shared cause or several? Write TRIAGE: FAULT SELDON + BUG|DESIGN + theme.
2. Fix at the root with the smallest change, coach-not-referee: normalise derivable things instead of refusing, fix what the prompt asks for, or remove a check that should not exist. Prefer deleting lines. Never weaken a real proof.
3. Behaviour-only test: extend the golden path / journey test if needed (no unit tests, no timing asserts).
4. Gate: PATH=~/codex-harness/.venv/Scripts:$PATH bash scripts/gate.sh leadNoRecovery (no SELDON_* env vars). Cold-import every changed module.
5. Exit evidence (required, Astra pattern 5): ONE real Lead hello run on Terra from this lane's code:
   cd /c/seldon/tests; SELDON_MODE=lead SELDON_ROLE_MODEL=gpt-6.1-terra SELDON_ROLE_EFFORT=medium FIRST=medium BRIEF=<path to ladder/briefs/L0/1-hello.json> SLOTP=<this lane src> bash cohort2.sh nr-hello nr 1 1 1
   (adapt to cohort2.sh's actual arguments — read it first). Report fault records and recoveries for that run. Target: 0 lead_failure, 0 recovery, C verified.
6. If quota drops below 2%, stop cleanly and write what is left.

## Report (C:/seldon/tests/leadNoRecovery-0/REPORT.md, <=25 lines)
Cause, TRIAGE line, diff summary with src lines +/-, gate result, real-run fault/recovery counts, what remains. Leave the diff as `git diff` in this lane dir; do not push.
Temp files only under C:/seldon/tests/leadNoRecovery-0. Never open editors, browsers or windows on the desktop.
