Lane STAGE-2P (Seldon reset, Stage 2 prerequisite; serial, lands first). This folder = Seldon main 5f7dbc6 (Stage 1 complete) + own git. Read CHARTER.md (ratified v1.1, binding), AGENTS.md, then C:/Users/oren/codex-harness/work/ladder/design-review/astra-briefs-2.md (your brief = section 2p; later lanes 2a..2e depend on your harness).
**Binding terms carried by every brief below**
File stems mean `src/codex_harness/core/<stem>.py`; **G** means `tests/python/core/{test_golden_path,test_approval_v2_journey}.py`.
Each lane must be **NET-NEGATIVE in production lines**, counting new files and deletions together; report `PROD +/−/net; TEST +/−/net; cases versus base; runtime`. No cosmetic deletions or moving code outside the count.
Use only existing **1j prepare/submit/read**, its canonical bindings, pending state and two exact-fix retries; no second judge store, retry counter or inferred semantic approval.
Golden is the first gate; every behavior change extends it in the same patch through canonical producers/consumers. Script provider replies only; observe execution, persistence and cleanup. Name the regression and existing coverage gap.
Retain the ≤19-case ceiling, mark/measure the ≤10-minute fast gate, reuse unaffected evidence, and record discoveries in `docs/legacy-capability-audit.md`. Ladder claims require actual authorized runs.
One serial integration owner controls `plan_store`, `roundtable`, `dispatch` and G throughout Stage 2. Other owned files below transfer only after the preceding lane lands GREEN.
**2p — Land shared prerequisites first**
CHARTER: serves C3/C4/C13/C14 — uses DV4/DV9; preserves I1–I9.
Own: `worker_packet` + G; production deletion is the obsolete Contracts stub/exit-3/DOM-marker and Build “unit tests” instructions.
Prerequisites: retain existing 1j/schema/pending contracts; extend the shared scripted-provider harness for explicit review verdicts, equivalence/reuse judgments and later loop/acceptance replies. Keep real process observations and ordinary executable tests.
Close the worker-packet C14 instruction defect **here, before 2a**, including web instructions; DV4 remains partial. Contracts asks workers for meaningful semantic tests and observed behavioral RED, never manufactured marker RED.
Golden: generated packet → worker-authored test → ordinary failing execution → 1j assessment → Build → GREEN; prove the shared harness works before downstream lanes depend on it.
Ladder: L0 must use this actual packet/worker path. TRIAGE: DESIGN — producer still requests deleted stub semantics — siblings: web markers, exit 3, unit-test instructions.

Lead notes (CC): the golden scripted judge must be the ONE shared test harness for all of Stage 2. Make it general (any 1j question: review verdicts, equivalence/reuse, loop/acceptance replies), and keep it test-only. Timebox 75 min, effort high.
FAST-LANE RULES (append to every Seldon fix brief; binding — Oren: NO unit tests, ever)
- Lane folder comes from work/lanes/make-lane.sh: it contains NO tests except the golden path. Do not write new test files.
- Report <=12 lines; exact patch + sha256; no pushes.
- CC rejects any patch whose command log ran another pytest (work/lanes/check-lane-log.sh).
- All scratch/temp/basetemp goes under C:\seldon\tests\<lane> (add it with --add-dir). Never create folders at the C:\ root or under C:\Users\oren\t.
- TRIAGE (Oren 11-04, binding): the report's FIRST line is `TRIAGE: BUG|DESIGN — <why> — sibling cases: <codes/gates with the same shape, or none>`. BUG = local mistake in sound logic: patch it. DESIGN = the rule itself causes the failure, or a 2nd+ blocker of the same shape: fix the shared rule at ONE owner and cover every sibling; never add another special case. CC rejects reports without a TRIAGE line, or BUG with siblings.
- SIMPLER, NOT BIGGER (Oren 11-04, binding from Stage 1b): every lane is NET-NEGATIVE in production lines (src/) — replaced static semantic code is deleted in the same lane. Report `PROD: +a/-b (net n) · TEST: +c/-d`. Net-positive production only for a genuinely new charter capability, justified in one line; CC rejects otherwise.
- ONE JUDGE PATH (binding): semantic decisions use the 1j Judgment contract only (prepare_judgment -> submit_judgment -> judgment). A gate supplies its question + evidence bindings; no per-gate judge prompts/schemas/stores/glue.
- The ONLY tests you may run: bash C:/Users/oren/codex-harness/work/lanes/golden-gate.sh <lane> <tag> (max 3 runs), or a single golden/journey file via python -m pytest <file> -x with --basetemp=C:/seldon/tests/stage-2p/p. No other pytest. Never write unit tests.
Final gate run must come after your last edit and be green; if not green, say so plainly. Report ../stage-2p-report.md; patch ../stage-2p.patch + sha256 (diff vs lane base). Scratch: C:/seldon/tests/stage-2p.
