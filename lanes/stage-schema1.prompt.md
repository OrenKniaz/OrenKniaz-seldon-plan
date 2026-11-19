Lane STAGE-SCHEMA1 (Seldon; small; I8 every refusal teaches). This folder = Seldon main 6aff167 + own git. Read CHARTER.md, AGENTS.md, and ~/codex-harness/work/fight-1/r5-diag.md item 3.
**Binding terms carried by every brief below**
File stems mean `src/codex_harness/core/<stem>.py`; **G** means `tests/python/core/{test_golden_path,test_approval_v2_journey}.py`.
Each lane must be **NET-NEGATIVE in production lines**, counting new files and deletions together; report `PROD +/−/net; TEST +/−/net; cases versus base; runtime`. No cosmetic deletions or moving code outside the count.
Use only existing **1j prepare/submit/read**, its canonical bindings, pending state and two exact-fix retries; no second judge store, retry counter or inferred semantic approval.
Golden is the first gate; every behavior change extends it in the same patch through canonical producers/consumers. Script provider replies only; observe execution, persistence and cleanup. Name the regression and existing coverage gap.
Retain the ≤19-case ceiling, mark/measure the ≤10-minute fast gate, reuse unaffected evidence, and record discoveries in `docs/legacy-capability-audit.md`. Ladder claims require actual authorized runs.
One serial integration owner controls `plan_store`, `roundtable`, `dispatch` and G throughout Stage 2. Other owned files below transfer only after the preceding lane lands GREEN.

Problem: in a real run the planner burned a turn guessing the nested shape of vision.fields.scenarios / setup / targets from successive validator errors (malformed scenarios; unique ids + verdict all; setup only allows dirs/files/snapshots; asked harness_schema for a nonexistent tool 'semanticScenarios'; used harness_accept_scenarios instead of upsert_node; omitted execution.testRoots).
TRIAGE: DESIGN — schema answers describe fields but show no accepted example, and errors don't name the writer — siblings: every nested planner write.
Rule: harness_schema returns, for each planner write tool, ONE minimal ACCEPTED example generated from (or checked against) the same validator, including vision.fields.scenarios with setup/targets and a build bead with execution.testRoots. Unknown tool names in harness_schema list the valid ones. Each validator refusal names the field path, the allowed keys, and the correct writer tool (one remedy, I8). No new validator rules; do not loosen any.
Golden: extend the existing CLI golden so the scripted planner reads harness_schema and submits the returned example shapes successfully on the first try; one wrong-writer call gets the remedy naming upsert_node. PROD net-negative preferred (examples generated, not duplicated). Timebox 45 min, effort medium. Single golden-file runs while iterating; ONE full `bash ../golden-gate.sh . stage-schema1` after the last edit, GREEN.

FAST-LANE RULES (append to every Seldon fix brief; binding — Oren: NO unit tests, ever)
- Lane folder comes from work/lanes/make-lane.sh: it contains NO tests except the golden path. Do not write new test files.
- Report <=12 lines; exact patch + sha256; no pushes.
- CC rejects any patch whose command log ran another pytest (work/lanes/check-lane-log.sh).
- All scratch/temp/basetemp goes under C:\seldon\tests\<lane> (add it with --add-dir). Never create folders at the C:\ root or under ~\t.
- TRIAGE (Oren 11-04, binding): the report's FIRST line is `TRIAGE: BUG|DESIGN — <why> — sibling cases: <codes/gates with the same shape, or none>`. BUG = local mistake in sound logic: patch it. DESIGN = the rule itself causes the failure, or a 2nd+ blocker of the same shape: fix the shared rule at ONE owner and cover every sibling; never add another special case. CC rejects reports without a TRIAGE line, or BUG with siblings.
- SIMPLER, NOT BIGGER (Oren 11-04, binding from Stage 1b): every lane is NET-NEGATIVE in production lines (src/) — replaced static semantic code is deleted in the same lane. Report `PROD: +a/-b (net n) · TEST: +c/-d`. Net-positive production only for a genuinely new charter capability, justified in one line; CC rejects otherwise.
- ONE JUDGE PATH (binding): semantic decisions use the 1j Judgment contract only (prepare_judgment -> submit_judgment -> judgment). A gate supplies its question + evidence bindings; no per-gate judge prompts/schemas/stores/glue.
- The ONLY tests you may run: bash ~/codex-harness/work/lanes/golden-gate.sh <lane> <tag> (max 3 runs), or a single golden/journey file via python -m pytest <file> -x with --basetemp=C:/seldon/tests/stage-schema1/p. No other pytest. Never write unit tests.
Final gate run must come after your last edit and be green; if not green, say so plainly. Report ../stage-schema1-report.md; patch ../stage-schema1.patch + sha256 (diff vs lane base). Scratch: C:/seldon/tests/stage-schema1.
