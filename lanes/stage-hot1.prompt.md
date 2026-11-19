HOTFIX LANE HOT1 (Seldon; URGENT — main cannot init a project). This folder = Seldon main 50a5e3f + own git. Read CHARTER.md, AGENTS.md.
**Binding terms carried by every brief below**
File stems mean `src/codex_harness/core/<stem>.py`; **G** means `tests/python/core/{test_golden_path,test_approval_v2_journey}.py`.
Each lane must be **NET-NEGATIVE in production lines**, counting new files and deletions together; report `PROD +/−/net; TEST +/−/net; cases versus base; runtime`. No cosmetic deletions or moving code outside the count.
Use only existing **1j prepare/submit/read**, its canonical bindings, pending state and two exact-fix retries; no second judge store, retry counter or inferred semantic approval.
Golden is the first gate; every behavior change extends it in the same patch through canonical producers/consumers. Script provider replies only; observe execution, persistence and cleanup. Name the regression and existing coverage gap.
Retain the ≤19-case ceiling, mark/measure the ≤10-minute fast gate, reuse unaffected evidence, and record discoveries in `docs/legacy-capability-audit.md`. Ladder claims require actual authorized runs.
One serial integration owner controls `plan_store`, `roundtable`, `dispatch` and G throughout Stage 2. Other owned files below transfer only after the preceding lane lands GREEN.

Real failure (ShelfLife round 10, 0.36s): `python -m codex_harness.core.seldon_cli init …` → ImportError: cannot import name 'PROVIDER_TOKEN_BUDGETS' from partially initialized module 'codex_harness.core.roundtable' (circular import). Chain: seldon_cli → project_init → preflight → roundtable → approvals → planner_jobs → (approvals, dispatch) → dispatch → worker_packet → roundtable. consent1 added approvals → planner_jobs, closing the cycle. Full traceback: ~/codex-harness/work/fight-1/receipts/20261106T065009-c82dfb/20261106T065009-c82dfb-001-shelflife/init.err. The golden never cold-imports entry points, so it passed.
TRIAGE: DESIGN — a shared constant/owner lives in a high-level module, creating import cycles — siblings: every console/MCP entry point (seldon_cli, seldon_mcp, mcp_planner, plan_cli) and any constant imported "down" from roundtable/approvals.
Fix: break the cycle at its cause — move shared leaf data (e.g. PROVIDER_TOKEN_BUDGETS and anything similar imported downward) into the lowest module that owns it (or a tiny leaf module), so imports point one way; no function-local import hacks unless genuinely necessary (justify).
Guard (fault twin, not a unit test): extend the existing golden so it launches EVERY installed entry point (seldon_cli init/--help, seldon_mcp startup handshake) in a FRESH subprocess interpreter (-I, no preloaded modules) and asserts it starts. This would have caught r10.
PROD net ≤ 0. Timebox 40 min, effort high. Single golden-file runs while iterating; ONE full `bash ../golden-gate.sh . stage-hot1` after the last edit, GREEN.

FAST-LANE RULES (append to every Seldon fix brief; binding — Oren: NO unit tests, ever)
- Lane folder comes from work/lanes/make-lane.sh: it contains NO tests except the golden path. Do not write new test files.
- Report <=12 lines; exact patch + sha256; no pushes.
- CC rejects any patch whose command log ran another pytest (work/lanes/check-lane-log.sh).
- All scratch/temp/basetemp goes under C:\seldon\tests\<lane> (add it with --add-dir). Never create folders at the C:\ root or under ~\t.
- TRIAGE (Oren 11-04, binding): the report's FIRST line is `TRIAGE: BUG|DESIGN — <why> — sibling cases: <codes/gates with the same shape, or none>`. BUG = local mistake in sound logic: patch it. DESIGN = the rule itself causes the failure, or a 2nd+ blocker of the same shape: fix the shared rule at ONE owner and cover every sibling; never add another special case. CC rejects reports without a TRIAGE line, or BUG with siblings.
- SIMPLER, NOT BIGGER (Oren 11-04, binding from Stage 1b): every lane is NET-NEGATIVE in production lines (src/) — replaced static semantic code is deleted in the same lane. Report `PROD: +a/-b (net n) · TEST: +c/-d`. Net-positive production only for a genuinely new charter capability, justified in one line; CC rejects otherwise.
- ONE JUDGE PATH (binding): semantic decisions use the 1j Judgment contract only (prepare_judgment -> submit_judgment -> judgment). A gate supplies its question + evidence bindings; no per-gate judge prompts/schemas/stores/glue.
- The ONLY tests you may run: bash ~/codex-harness/work/lanes/golden-gate.sh <lane> <tag> (max 3 runs), or a single golden/journey file via python -m pytest <file> -x with --basetemp=C:/seldon/tests/stage-hot1/p. No other pytest. Never write unit tests.
Final gate run must come after your last edit and be green; if not green, say so plainly. Report ../stage-hot1-report.md; patch ../stage-hot1.patch + sha256 (diff vs lane base). Scratch: C:/seldon/tests/stage-hot1.
