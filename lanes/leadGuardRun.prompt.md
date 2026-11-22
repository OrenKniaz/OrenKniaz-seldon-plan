# Lane leadGuardRun (Sol 6.2 medium) — Lead only. Continues leadWalk.
Repo: this lane dir = Seldon main 61cfce8 WITH the leadWalk patch applied (C:/seldon/tests/leadWalk-0/lane.diff; its REPORT.md explains it). Spec: BLUEPRINT-LEAD.md v0.4 section 2a (Walk + Human UI/UX feedback), ratified.

## Problem
leadWalk got the shape right: real Terra Hello and ShelfLife each took 5 calls with 1 WORK, and ShelfLife ran in 5.2 min and 68k tokens. But the guard never walked: Codex returned "blocked by policy" for every shell command because the guard call runs in a read-only sandbox. Both runs stopped WAITING at PROVE. Without the walk there is no proof and no UI/UX feedback.

## Decision (owner, binding; do not re-ask): Seldon's provider calls run with full access (danger-full-access, no sandbox). Basic-level security only.
Independence comes from WHERE the guard acts, not from a sandbox. The guard walks a disposable copy of the integrated candidate in its own temp dir under the run's temp root, with its own runtime data. Seldon's store and the canonical product checkout are never its working dir. Delete the copy after the verdict. Code (not the LLM) captures and keeps screenshots and outputs the guard produces in that copy.

## Build
1. The guard call gets full access with the disposable copy as cwd. It uses the CLI/API/browser to do what the person would do, including restart and one failure case, and writes screenshots to a known folder that code collects.
2. Keep leadWalk's design: one verdict per candidate, source on demand, human UI/UX feedback into check-in, C and the next brief; builder returns only for a demonstrated product defect or a broken retained witness.
3. Remove any MXC/confined-shell probing that leadWalk added if it is not needed now (T-274 becomes moot). Net production lines must not grow; report them.
4. No desktop windows: headless browsers only, quietDesktop env applies to the guard too.

## Prove
Golden/journey tests only. Cold imports. Gate: PATH=~/codex-harness/.venv/Scripts:$PATH bash scripts/gate.sh leadGuardRun (no SELDON_* env).
Real exit, Terra medium, via SRC=<this lane dir> bash /c/seldon/tests/coord3-20261120/cohort2.sh with SELDON_MODE=lead SELDON_ROLE_MODEL=gpt-6.1-terra SELDON_ROLE_EFFORT=medium FIRST=medium: hello x1 (BRIEF=~/codex-harness/work/ladder/briefs/L0/1-hello.json) and ShelfLife x1 (DREAM=~/codex-harness/work/fight-1/shelflife-brief.md). Both must reach verified C. Report calls by kind, WORK, JUDGE tokens, guard actions and screenshots count, active minutes, and paste the guard's UI/UX feedback verbatim for both runs.
Report: C:/seldon/tests/leadGuardRun-0/REPORT.md <=30 lines. Leave the combined git diff (leadWalk + this) vs base; do not push. Temp only under C:/seldon/tests/leadGuardRun-0. Never open desktop windows.
