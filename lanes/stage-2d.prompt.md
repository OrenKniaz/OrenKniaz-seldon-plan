Lane STAGE-2d (Seldon reset; runs IN PARALLEL with another Stage-2 lane). This folder = Seldon main 8964f75 + the Stage 2a candidate (0311b80a, not yet landed; see ../stage-2a-report.md) committed as your lane base. Read CHARTER.md (binding), AGENTS.md, then ../ladder/design-review/astra-briefs-2.md (your brief = section 2d, plus the CC addendum at the end), and ../stage-2a-report.md for the one-owner finding design you must keep.

**Binding terms carried by every brief below**
File stems mean `src/codex_harness/core/<stem>.py`; **G** means `tests/python/core/{test_golden_path,test_approval_v2_journey}.py`.
Each lane must be **NET-NEGATIVE in production lines**, counting new files and deletions together; report `PROD +/−/net; TEST +/−/net; cases versus base; runtime`. No cosmetic deletions or moving code outside the count.
Use only existing **1j prepare/submit/read**, its canonical bindings, pending state and two exact-fix retries; no second judge store, retry counter or inferred semantic approval.
Golden is the first gate; every behavior change extends it in the same patch through canonical producers/consumers. Script provider replies only; observe execution, persistence and cleanup. Name the regression and existing coverage gap.
Retain the ≤19-case ceiling, mark/measure the ≤10-minute fast gate, reuse unaffected evidence, and record discoveries in `docs/legacy-capability-audit.md`. Ladder claims require actual authorized runs.
One serial integration owner controls `plan_store`, `roundtable`, `dispatch` and G throughout Stage 2. Other owned files below transfer only after the preceding lane lands GREEN.

**2d — Finish bounded owner lifetimes before the loop consumes them**
CHARTER: serves C4/C18/C23/C25 — preserves I2/I4/I5/I6; no standalone DV closure.
Own: `planner_acceptance`, `planner_audits`, `planner_review`, `planner_recovery`, `acceptance_recovery`, `planner_resume`, `attempt_control`, `planner_jobs`, `plan_store`, `roundtable`, `dispatch` + G.
Give every attempt/claim/hold a bounded terminal disposition through existing owners; expose durable completion/recovery observations for 2c. Two automatic bead recoveries, then recorded steering; remove competing counters and indefinite holds.
Transport loss grants neither success nor consent. Uncertain cleanup ends in truthful abandonment/quarantine, excludes abandoned evidence and releases logical ownership without claiming process quiescence. Awaiting the user owns no running attempt.
NET-NEGATIVE: delete duplicate retry/hold/resume rules. Golden fault journeys use real crash/stall/transport-loss observations, supported cleanup and canonical recovery; reach C or an explicit released pending/steering state.
Ladder: L1 fault twins prove bounded recovery and preserved direction; 2c adds autonomous consumption. TRIAGE: DESIGN — terminal ownership lacks one rule — siblings: review, audit, acceptance, worker and confirmation waits.

Lead notes (CC):
- PARALLEL: another lane edits plan_store/roundtable/dispatch/G at the same time. Keep edits in those shared files minimal and local to your concern; never reformat or move code there. CC integrates.
- DELETION TARGET: -400 (duplicate retry/hold/resume rules) nonblank src/ lines (numeric, binding). Report the actual number.
- Known, out of scope: web golden timing flakes are owned by lane stage-2a-flake. If a full gate fails only on a web/time-limit case your diff does not touch, say so with the log line; do not chase it.
- Iterate with single golden-file runs (-k cli where possible); the machine is shared, so run at most 2 full gates, the last after your last edit.
- Timebox 120 min, effort high.

FAST-LANE RULES (append to every Seldon fix brief; binding — Oren: NO unit tests, ever)
- Lane folder comes from work/lanes/make-lane.sh: it contains NO tests except the golden path. Do not write new test files.
- Report <=12 lines; exact patch + sha256; no pushes.
- CC rejects any patch whose command log ran another pytest (work/lanes/check-lane-log.sh).
- All scratch/temp/basetemp goes under C:\seldon\tests\<lane> (add it with --add-dir). Never create folders at the C:\ root or under ~\t.
- TRIAGE (Oren 11-04, binding): the report's FIRST line is `TRIAGE: BUG|DESIGN — <why> — sibling cases: <codes/gates with the same shape, or none>`. BUG = local mistake in sound logic: patch it. DESIGN = the rule itself causes the failure, or a 2nd+ blocker of the same shape: fix the shared rule at ONE owner and cover every sibling; never add another special case. CC rejects reports without a TRIAGE line, or BUG with siblings.
- SIMPLER, NOT BIGGER (Oren 11-04, binding from Stage 1b): every lane is NET-NEGATIVE in production lines (src/) — replaced static semantic code is deleted in the same lane. Report `PROD: +a/-b (net n) · TEST: +c/-d`. Net-positive production only for a genuinely new charter capability, justified in one line; CC rejects otherwise.
- ONE JUDGE PATH (binding): semantic decisions use the 1j Judgment contract only (prepare_judgment -> submit_judgment -> judgment). A gate supplies its question + evidence bindings; no per-gate judge prompts/schemas/stores/glue.
- The ONLY tests you may run: bash ~/codex-harness/work/lanes/golden-gate.sh <lane> <tag> (max 3 runs), or a single golden/journey file via python -m pytest <file> -x with --basetemp=C:/seldon/tests/stage-2d/p. No other pytest. Never write unit tests.
Final gate run must come after your last edit and be green; if not green, say so plainly. Report ../stage-2d-report.md; patch ../stage-2d.patch + sha256 (diff vs lane base). Scratch: C:/seldon/tests/stage-2d.
