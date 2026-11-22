# Lane leadWalk (Sol 6.2 medium) — Lead only (Orchestrator paused)
Repo: this lane dir = Seldon main d78cc5e (history rewritten 11-22; old hashes map in ../ladder/COMMIT-MAP-2026-11-22.txt). Spec: BLUEPRINT-LEAD.md v0.4 section 2a (RATIFIED: Walk + Human UI/UX feedback). Evidence and design: ~/codex-harness/work/ladder/design-review/astra62-lead-vs-plain-2026-11-22.md — implement its ranked changes 1, 2 and 4.
Owner's words: "planner should be so thin... a beautiful process of expanding and crystallizing a dream"; "he still owns the results... mainly a subjective semantic guard... he should walk the user path"; "while seldon walks the user path, he also gives human type ui/ux feedback".

## Build
1. Guard walk: on the integrated candidate the guard (the judge call, with tools to act: shell/browser via existing facilities, read-only on product source, product data in a disposable copy) walks the approved surface like the person: real actions incl. restart and one failure case; records action, actual result, screenshot. It may obtain any missing observation itself. One semantic verdict per candidate. Delete whole-tree prompt serialization and repeated per-subject schemas; source on demand.
2. Human UI/UX feedback: the verdict carries short human-style notes (clear/confusing, calm/ugly, awkward, slow, surprising) naming the screen/step. Shown to the person beside the verdict and carried into the next milestone brief. Blocks only when it breaks a B promise.
3. Builder returns ONLY for a demonstrated product defect (with the failing action to reproduce) or a materially broken retained witness. Receipt-only problems are fixed in place on the same candidate, not a full builder turn. Remove the "two builder findings on one tree = same failure" rule.
4. Run each physical witness once per candidate and phase; one receipt entry may serve several promises. Keep fresh RED for new behaviour, GREEN on candidate, earlier retained witnesses.
5. Close Astra's false-done hole: C must read Lead's observations (tagged milestone, not only final); an uncertain semantic finding stays visible.
Net production lines must go DOWN (Astra estimates -55 to -150 net). Report reachable lines from lead.py before/after.

## Prove
Golden/journey tests only (behaviour, no unit tests, no timing asserts). Cold-import every changed module. Gate: PATH=~/codex-harness/.venv/Scripts:$PATH bash scripts/gate.sh leadWalk (no SELDON_* env).
Real exit (Terra medium, from this lane's src via SRC=<lane dir> bash /c/seldon/tests/coord3-20261120/cohort2.sh with SELDON_MODE=lead SELDON_ROLE_MODEL=gpt-6.1-terra SELDON_ROLE_EFFORT=medium FIRST=medium): ShelfLife x1 (DREAM=~/codex-harness/work/fight-1/shelflife-brief.md) and hello x1 (BRIEF=~/codex-harness/work/ladder/briefs/L0/1-hello.json). Report per run: calls by kind, WORK count, JUDGE tokens, walkthrough starts, active minutes, C, and paste the UI/UX feedback the guard wrote. Target ShelfLife: 1 WORK, total <= 2x plain's 237 s and 34k fresh tokens.
Report: C:/seldon/tests/leadWalk-0/REPORT.md <=30 lines. Leave git diff, do not push. Temp only under C:/seldon/tests/leadWalk-0. Never open desktop windows.
