Lane STAGE-1A (Seldon reset, Stage 1a: full trace contract). This folder = Seldon main dcfaedf + own git. Read CHARTER.md (repo root, ratified v1.1 by Oren; binding) and AGENTS.md first.
Context: the plan is C:/Users/oren/codex-harness/work/ladder/design-review/astra-reset-1.md as amended by astra-reset-2.md (same folder). Read both; this lane is Stage 1a only.
CHARTER: serves C4/C9/C10/C22–C24/C26 — uses DV1/DV4/DV9; proposes no additional I1–I9 exception.
Outcome: one complete, domain-open trace contract consumed through the canonical producer/store/compiler path.
Own: src/codex_harness/core/{spine,graph,semantic_schema,planner_schema}.py.
Serial integration owner alone edits plan_store.py, necessary mcp_planner.py bindings, and tests/python/core/test_golden_path.py.
Do not edit roundtable.py or dispatch.py; their later stages retain serial ownership.
Trace: dream→features→stories→requirements→architecture/design→contracts→tests→beads→code→results; decision/research side links.
Evidence states: awaiting, failed, stale, integrated, validated live; bind evidence to item revision, candidate, source and observation.
Integrated does not imply validated live; missing proof stays awaiting; historical/fake-provider evidence cannot establish real-provider acceptance.
Brownfield: ordinary existing-feature nodes link baseline code, behavior, rationale, tests and observed evidence before change planning.
Amendments: typed discovery/source, upstream target revisions, proposed change, rationale and decision links; preserve exact impact.
Include metric definition/stop-condition/iteration-result links and canonical baton references; add no separate stores or execution engines.
Harvest legacy test nodes, traversal, impact calculation, baseline provenance and canonical revision/evidence binding.
Delete replaced mode-specific topology, closed product vocabulary and unit-test assumptions; preserve historical provenance.
Golden extension: public producer→store→reload→compiler consumes full/brownfield trace and amendment; exact affected evidence becomes stale.
Protect against lost existing features, dropped evidence links and broad invalidation; current scenario journeys do not prove this full contract.
Ladder: L0 collapsed and L1 full/brownfield trace preserve IDs, baseline evidence and exact impact; contract proof alone earns no promotion.
TRIAGE: BUG|DESIGN — name cause and sibling cases; repair shared-rule DESIGN at its owner, never bypass admission or invent proof.
Lead notes (CC): the trace contract is the foundation every later stage builds on, so get the shape right once (I3: strict on shape/IDs/links, open on domain; would an HTTP/UI/mobile/pipeline/library/HW-DSP-audio product fail any field? then make it open). Keep it thin: no new stores, no new engines, no god files (I9). Tests are graph nodes (C9/DV1).
Timebox for this lane: 120 min, effort high (overrides the 45-min default below). Gate may run at most twice.
Report first lines: `CHARTER: serves C# — violates no I# (or uses DV#)` then `TRIAGE: ...`. Also list which DV1/DV4/DV9 parts are now restored and what remains.
FAST-LANE RULES (append to every Seldon fix brief; binding — Oren: NO unit tests, ever)
- Lane folder comes from work/lanes/make-lane.sh: it contains NO tests except the golden path. Do not write new test files.
- The ONLY test you may run: bash C:/Users/oren/codex-harness/work/lanes/golden-gate.sh <lane> <tag> (stub golden path CLI+web). Run it once at the end, at most twice. Prove behavior by extending golden-path scenarios, never with unit tests.
- Timebox 45 min, effort medium. One or two failure clusters per lane; the brief names the refusal code and the owning file/function — start there.
- Report <=12 lines; exact patch + sha256; no pushes.
- CC rejects any patch whose command log ran another pytest (work/lanes/check-lane-log.sh).
- All scratch/temp/basetemp goes under C:\seldon\tests\<lane> (add it with --add-dir). Never create folders at the C:\ root or under C:\Users\oren\t.
- TRIAGE (Oren 11-04, binding): the report's FIRST line is `TRIAGE: BUG|DESIGN — <why> — sibling cases: <codes/gates with the same shape, or none>`. BUG = local mistake in sound logic: patch it. DESIGN = the rule itself causes the failure, or a 2nd+ blocker of the same shape: fix the shared rule at ONE owner and cover every sibling; never add another special case. CC rejects reports without a TRIAGE line, or BUG with siblings.
Report ../stage-1a-report.md; patch ../stage-1a.patch + sha256. Scratch: C:\seldon\tests\stage-1a.
