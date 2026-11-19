Lane STAGE-2b (Seldon reset; runs IN PARALLEL with another Stage-2 lane). This folder = Seldon main 8964f75 + the Stage 2a candidate (0311b80a, not yet landed; see ../stage-2a-report.md) committed as your lane base. Read CHARTER.md (binding), AGENTS.md, then ../ladder/design-review/astra-briefs-2.md (your brief = section 2b, plus the CC addendum at the end), and ../stage-2a-report.md for the one-owner finding design you must keep.

**Binding terms carried by every brief below**
File stems mean `src/codex_harness/core/<stem>.py`; **G** means `tests/python/core/{test_golden_path,test_approval_v2_journey}.py`.
Each lane must be **NET-NEGATIVE in production lines**, counting new files and deletions together; report `PROD +/−/net; TEST +/−/net; cases versus base; runtime`. No cosmetic deletions or moving code outside the count.
Use only existing **1j prepare/submit/read**, its canonical bindings, pending state and two exact-fix retries; no second judge store, retry counter or inferred semantic approval.
Golden is the first gate; every behavior change extends it in the same patch through canonical producers/consumers. Script provider replies only; observe execution, persistence and cleanup. Name the regression and existing coverage gap.
Retain the ≤19-case ceiling, mark/measure the ≤10-minute fast gate, reuse unaffected evidence, and record discoveries in `docs/legacy-capability-audit.md`. Ladder claims require actual authorized runs.
One serial integration owner controls `plan_store`, `roundtable`, `dispatch` and G throughout Stage 2. Other owned files below transfer only after the preceding lane lands GREEN.

**2b — Delete product budgets, preserve launch authority**
CHARTER: serves C8/C18/C20 — targets DV8; preserves I4–I6.
Own: `provider_call_budget`, `approvals`, `approval_migration`, `planner_confirmations`, `planner_jobs`, `planner_execution`, `planner_review`, `planner_candidate`, `planner_refusals`, `acceptance_recovery`, `plan_store`, `roundtable`, `dispatch`, `mcp_planner`, `plan_cli` + G.
Before deleting the budget module, retain its job/run/attempt verification in the existing job/provenance owners (`attempt_provenance` included); consumers must use those owners directly.
Delete spending/call/review quotas, reservations, renewals and budget-bearing B subjects; preserve historical records without reauthorizing them. Keep attempt deadlines, provider context capacity and development-only usage metrics.
NET-NEGATIVE: remove the module and its product plumbing. Golden: approved launch→review→delivery without renewal; stale/unapproved subjects still refuse with one remedy. This protects authority accidentally removed with quota code.
Ladder: L0 needs no budget decision and respects current B; DV8 closes after proof. TRIAGE: DESIGN — quota and authorization share an owner — siblings: worker starts, review starts, acceptance assessment.

Lead notes (CC):
- PARALLEL: another lane edits plan_store/roundtable/dispatch/G at the same time. Keep edits in those shared files minimal and local to your concern; never reformat or move code there. CC integrates.
- DELETION TARGET: -685 (budget module + plumbing) nonblank src/ lines (numeric, binding). Report the actual number.
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
- The ONLY tests you may run: bash ~/codex-harness/work/lanes/golden-gate.sh <lane> <tag> (max 3 runs), or a single golden/journey file via python -m pytest <file> -x with --basetemp=C:/seldon/tests/stage-2b/p. No other pytest. Never write unit tests.
Final gate run must come after your last edit and be green; if not green, say so plainly. Report ../stage-2b-report.md; patch ../stage-2b.patch + sha256 (diff vs lane base). Scratch: C:/seldon/tests/stage-2b.
