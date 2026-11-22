# Lane leadPort (Sol 6.2 medium) — Lead only
Repo: this lane dir = Seldon main 56a024e, which already contains a version of leadWalk (guard walks a disposable export, UX feedback, builder returns only for B-quoted defects).
A parallel lane produced round-3 fixes on an older base; its full diff is C:/seldon/tests/leadWalk-0/lane.diff and its report C:/seldon/tests/leadWalk-0/REPORT.md. Port ONLY what 56a024e lacks, smallest change:
1. Guard call uses the WORK deadline class; on a recoverable timeout resume the SAME guard session with completed observations (no cold restart).
2. Windows payload stdout/stderr written to files outside the checkout (pipe-drain fix), status pipe kept; journey that streams >4 MiB on both streams.
3. Guard issues plain one-action commands; never destructive or compound cleanup; Seldon owns cleanup; denied commands are recorded, not retried.
4. Foundation calibration: in round 3 the guard held C open on Foundation over "a missing explicit failure flow" on a page whose B promises have none. A missing observation for something B does not promise must never hold C; only B lines (result, notMetIf) can. Fix in the guard/judge prompt or C rule, whichever is the root.
Do not re-implement what 56a024e already has. Production lines <= 0 net.
Prove: golden/journey only; cold imports; bare gate (PATH=~/codex-harness/.venv/Scripts:$PATH bash scripts/gate.sh leadPort, no SELDON_*). Real Terra medium exits from this lane's src (SRC=<lane> bash /c/seldon/tests/coord3-20261120/cohort2.sh with SELDON_MODE=lead SELDON_ROLE_MODEL=gpt-6.1-terra SELDON_ROLE_EFFORT=medium FIRST=medium): hello x1, Foundation x1, ShelfLife x1 (DREAM=~/codex-harness/work/fight-1/shelflife-brief.md). All three must reach verified SCRIPTED_C, 1 WORK, guard actions > 0.
Report C:/seldon/tests/leadPort-0/REPORT.md <=25 lines incl. UX feedback verbatim. Leave git diff, do not push. Temp only under C:/seldon/tests/leadPort-0. Never open desktop windows.
