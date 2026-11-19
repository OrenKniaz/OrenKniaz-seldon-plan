Lane STAGE-2A2 (Seldon; parallel with 2b/2d fix rounds). This folder = Seldon main 6114561 (Stage 2a landed) + own git. Read CHARTER.md (DV10 is your target), AGENTS.md, ../stage-2a-report.md (one-owner design: PlanStore.finding_state), ../stage-2a-review5.md (FOLLOWUPS item).
**Binding terms carried by every brief below**
File stems mean `src/codex_harness/core/<stem>.py`; **G** means `tests/python/core/{test_golden_path,test_approval_v2_journey}.py`.
Each lane must be **NET-NEGATIVE in production lines**, counting new files and deletions together; report `PROD +/−/net; TEST +/−/net; cases versus base; runtime`. No cosmetic deletions or moving code outside the count.
Use only existing **1j prepare/submit/read**, its canonical bindings, pending state and two exact-fix retries; no second judge store, retry counter or inferred semantic approval.
Golden is the first gate; every behavior change extends it in the same patch through canonical producers/consumers. Script provider replies only; observe execution, persistence and cleanup. Name the regression and existing coverage gap.
Retain the ≤19-case ceiling, mark/measure the ≤10-minute fast gate, reuse unaffected evidence, and record discoveries in `docs/legacy-capability-audit.md`. Ladder claims require actual authorized runs.
One serial integration owner controls `plan_store`, `roundtable`, `dispatch` and G throughout Stage 2. Other owned files below transfer only after the preceding lane lands GREEN.

Goal — close DV10 (I4/I6): pending findings do not hold publication/C. Today gates (plan_store.py ~2222, review_instructions.py ~22, acceptance.py ~787) block only on `open`; after a plan/product change a retained obligation goes `pending`, and fresh positive reviews then permit publication/C with no current disposition of it.
TRIAGE: DESIGN — gates consume a severity-like state instead of the owner's prerequisite — siblings: publication, C acceptance, continuation guidance.
Rule (one owner): finding_state exposes ONE prerequisite "every retained obligation has a current bound positive disposition"; publication, C and continuation consume only that. Pending is a WAIT, not a refusal (I2): continuation names the exact judgment request to prepare (by obligation id) and publication explains which ones remain (I8). Delete any gate-local open-only checks.
Golden (scripted judge): negative finding → repair → plan changes → obligation pending → fresh positive reviews alone do NOT publish; guidance names the pending disposition; after a positive bound disposition, publication proceeds and C is reached. Same for product change after a positive closure.
Target: PROD net ≤ -50 (delete the gate-local checks). Timebox 75 min, effort high.
Machine shared with 2 lanes: single golden-file runs (-k cli) while iterating; ONE full `bash ../golden-gate.sh . stage-2a2` after your last edit, GREEN (max 2). Timing-only failure on an untouched case: report the line, don't chase.

FAST-LANE RULES (append to every Seldon fix brief; binding — Oren: NO unit tests, ever)
- Lane folder comes from work/lanes/make-lane.sh: it contains NO tests except the golden path. Do not write new test files.
- Report <=12 lines; exact patch + sha256; no pushes.
- CC rejects any patch whose command log ran another pytest (work/lanes/check-lane-log.sh).
- All scratch/temp/basetemp goes under C:\seldon\tests\<lane> (add it with --add-dir). Never create folders at the C:\ root or under ~\t.
- TRIAGE (Oren 11-04, binding): the report's FIRST line is `TRIAGE: BUG|DESIGN — <why> — sibling cases: <codes/gates with the same shape, or none>`. BUG = local mistake in sound logic: patch it. DESIGN = the rule itself causes the failure, or a 2nd+ blocker of the same shape: fix the shared rule at ONE owner and cover every sibling; never add another special case. CC rejects reports without a TRIAGE line, or BUG with siblings.
- SIMPLER, NOT BIGGER (Oren 11-04, binding from Stage 1b): every lane is NET-NEGATIVE in production lines (src/) — replaced static semantic code is deleted in the same lane. Report `PROD: +a/-b (net n) · TEST: +c/-d`. Net-positive production only for a genuinely new charter capability, justified in one line; CC rejects otherwise.
- ONE JUDGE PATH (binding): semantic decisions use the 1j Judgment contract only (prepare_judgment -> submit_judgment -> judgment). A gate supplies its question + evidence bindings; no per-gate judge prompts/schemas/stores/glue.
- The ONLY tests you may run: bash ~/codex-harness/work/lanes/golden-gate.sh <lane> <tag> (max 3 runs), or a single golden/journey file via python -m pytest <file> -x with --basetemp=C:/seldon/tests/stage-2a2/p. No other pytest. Never write unit tests.
Final gate run must come after your last edit and be green; if not green, say so plainly. Report ../stage-2a2-report.md; patch ../stage-2a2.patch + sha256 (diff vs lane base). Scratch: C:/seldon/tests/stage-2a2.
