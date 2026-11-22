# Lane leadGuardC (Sol 6.2 medium) — Lead only. Continues leadWalk + leadGuardRun.
Repo: this lane dir = Seldon main 61cfce8 WITH C:/seldon/tests/leadGuardRun-0/lane.diff applied (leadWalk + leadGuardRun; read C:/seldon/tests/leadGuardRun-0/REPORT.md and leadWalk-0/REPORT.md). Spec: BLUEPRINT-LEAD.md v0.4 section 2a, ratified.

## Where it stands
Real Terra runs now take 5 calls and 1 WORK. The guard walks the product (Hello 3.9 min/53k tokens, ShelfLife 6.8 min/74k; plain is 3.9 min/34k) and writes good human UI/UX feedback. But verified C is 0/2:
1. ShelfLife: C flagged the empty state, the full keyboard path and source completeness as unverified. The guard walked a lot but not every approved promise. The guard should get the list of approved results + notMetIf it must observe and cover each one itself (one walk, obtain any missing observation itself, no builder turn). Anything it truly cannot observe is labelled with why, and the person sees it at C. It is never silently dropped and never forces a rebuild.
2. Both runs used the retained-failure label for completed behaviour (wrong label at C).
3. Hello: the witness receipt overlaid hello.py onto the base, so the base check also passed and RED was not really observed. RED for new behaviour must run on the real base tree, with no candidate files overlaid.
TRIAGE each: FAULT SELDON + BUG|DESIGN. Fix at the root with the smallest change; prefer deleting. Net production lines must not grow.

## Prove
Golden/journey tests only. Cold imports. Gate: PATH=~/codex-harness/.venv/Scripts:$PATH bash scripts/gate.sh leadGuardC (no SELDON_* env). Do not overlap real runs with the gate (the last gate took 842 s because it ran alongside runs).
Real exit, Terra medium via SRC=<this lane dir> bash /c/seldon/tests/coord3-20261120/cohort2.sh with SELDON_MODE=lead SELDON_ROLE_MODEL=gpt-6.1-terra SELDON_ROLE_EFFORT=medium FIRST=medium: hello x1 and ShelfLife x1 (BRIEF=~/codex-harness/work/ladder/briefs/L0/1-hello.json; DREAM=~/codex-harness/work/fight-1/shelflife-brief.md), then Foundation x1 (default DREAM). All three must reach VERIFIED C. Report calls by kind, WORK, total fresh tokens, guard actions/PNGs, active minutes, C state, the per-promise observed/unverified list, and the guard's UI/UX feedback verbatim.
Report: C:/seldon/tests/leadGuardC-0/REPORT.md <=30 lines. Leave the combined diff vs 61cfce8 as lane.diff; do not push. Temp only under C:/seldon/tests/leadGuardC-0. Never open desktop windows.
