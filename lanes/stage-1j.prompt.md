Lane STAGE-1J (Seldon reset). This folder = Seldon main with Stage 1a (trace contract) + own git. Read CHARTER.md (ratified v1.1, binding), AGENTS.md, then ~/codex-harness/work/ladder/design-review/judge-boundary-1.md (shared repairs 1-2) and astra-briefs-1bc.md (1b/1c will consume your record next; give them a clean contract).
CHARTER: serves C2/C3/C4 — violates no I1–I9.
Outcome: one canonical typed judgment contract and durable pending-judgment state, available to both lanes.
Own: plan_store.py, mcp_planner.py, planner_schema.py; sole serial owner of tests/python/core/test_golden_path.py during 1j.
Record: judgment ID, subject IDs/revisions, candidate when applicable, evidence/source bindings, verdict, rationale and concrete gaps.
Code gathers facts/flags and checks structure/bindings; the LLM supplies meaning; no positive credit without a current, bound verdict.
Shared repairs 1–2: absent/inconclusive/unsupported meaning → pending-judgment; malformed output → two exact-fix attempts, then steer.
Persist retry/steering disposition; release attempt ownership; pending never becomes product failure, success or inferred human consent.
Harvest canonical events, revisions and provenance; delete replaced judgment defaults; keep Stage 1a evidence states distinct from judgment status.
Golden: public submission→store→reload→consumer preserves pending/verdict; changed subjects lose credit; malformed responses exhaust exactly two fixes.
Regression/gap: prevents lost pending state and stale verdict reuse, neither established by Stage 1a’s trace-only journey; ladder: L0 prerequisite, no promotion.
TRIAGE: BUG|DESIGN — name cause, sibling cases and concrete remedy; repair the shared owner, never add a bypass.
Lead notes (CC): keep it small and thin (I9): one record type, one pending state, at the one owner; no new store/engine. Judgment status stays separate from Stage 1a evidence states. Timebox 60 min, effort high. Report opens with CHARTER then TRIAGE lines.
FAST-LANE RULES (append to every Seldon fix brief; binding — Oren: NO unit tests, ever)
- Lane folder comes from work/lanes/make-lane.sh: it contains NO tests except the golden path. Do not write new test files.
- The ONLY test you may run: bash ~/codex-harness/work/lanes/golden-gate.sh <lane> <tag> (stub golden path CLI+web). Run it once at the end, at most twice. Prove behavior by extending golden-path scenarios, never with unit tests.
- Timebox 45 min, effort medium. One or two failure clusters per lane; the brief names the refusal code and the owning file/function — start there.
- Report <=12 lines; exact patch + sha256; no pushes.
- CC rejects any patch whose command log ran another pytest (work/lanes/check-lane-log.sh).
- All scratch/temp/basetemp goes under C:\seldon\tests\<lane> (add it with --add-dir). Never create folders at the C:\ root or under ~\t.
- TRIAGE (Oren 11-04, binding): the report's FIRST line is `TRIAGE: BUG|DESIGN — <why> — sibling cases: <codes/gates with the same shape, or none>`. BUG = local mistake in sound logic: patch it. DESIGN = the rule itself causes the failure, or a 2nd+ blocker of the same shape: fix the shared rule at ONE owner and cover every sibling; never add another special case. CC rejects reports without a TRIAGE line, or BUG with siblings.
Final gate run must be the last thing after your last edit, and green; if not green, say so plainly. Report ../stage-1j-report.md; patch ../stage-1j.patch + sha256 (diff vs the lane base commit). Scratch: C:\seldon\tests\stage-1j.
