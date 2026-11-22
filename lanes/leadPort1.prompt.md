# Lane leadPort1 (Sol 6.2 medium): port the robustness fixes from the other session's leadFix1. Lead only.
Repo: this lane dir = Seldon main 8c9ccdc. Source of the fixes: ~/codex-harness/work/lanes/leadFix1 (base 56a024e; `git -C <that dir> diff` shows the patch) and its report C:/seldon/tests/leadFix1-0/REPORT.md. Main has since landed leadGuardCovers (T-284: the guard walks missing checks) and leadGuardThorough (T-286 repair routing, thorough guard).
## Port (re-implement against current main, do not blind-apply):
1. Foundation crash: NameError at the failed-check return from PROVE (evidence C:/seldon/tests/wkFound/wf02.log).
2. WORK deadline and same-session guard resume after a timeout.
3. Windows: provider/guard stdout and stderr go to files (pipe-drain hang).
4. Plain one-action guard commands.
DROP leadFix1's receipt-correction part (it conflicts with T-284; main's design wins). Skip anything main already does. Net production lines should not grow; report them.
## Prove
Golden/journey tests only. Cold imports. Gate: PATH=~/codex-harness/.venv/Scripts:$PATH bash scripts/gate.sh leadPort1 (no SELDON_* env, nothing else running).
Real exit, Terra medium, from this lane's src (SRC=<lane dir> SELDON_MODE=lead SELDON_ROLE_MODEL=gpt-6.1-terra SELDON_ROLE_EFFORT=medium FIRST=medium bash /c/seldon/tests/coord3-20261120/cohort2.sh ...): Foundation x2 (default DREAM, SLOTP=found-p1, dir p1Found prefix pf) and hello x1 (BRIEF=~/codex-harness/work/ladder/briefs/L0/1-hello.json, SLOTP=hello-p1, dir p1Hello prefix ph). All must reach verified C. Report calls, WORK, fresh tokens, active minutes, C state.
Report: C:/seldon/tests/leadPort1-0/REPORT.md <=20 lines. Leave the diff as lane.diff; do not push. Never open desktop windows.
