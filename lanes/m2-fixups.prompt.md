LANE m2-fixups (M2 lane 3 of 5: local fixups; work/ladder/M2-PLAN.md). Runs in parallel with lane m2-flow (lane 2) on disjoint files. Worktree ~/codex-harness/work/lanes/m2-fixups-20261112 (Seldon main after judge-minimal). Temp only under C:/seldon/tests/m2fix-<n>. Do not commit. No new dependencies. Do not edit CHARTER.md or BLUEPRINT.md. Behaviour-only journeys. No real provider calls. Tickets per work/ladder/TRACKING.md.

Read CHARTER.md v1.7, BLUEPRINT.md v1.5 (3.2: "A WAVE-VERIFY failure becomes a small fixup unit owned by the failing scope; integration itself never waits on the whole suite"; R7 failure is local, a gap re-asks only subjects whose owning units changed; R8; R9; 8.4), work/ladder/M2-PLAN.md (port fixups.assign/checks_for from frozen draft work/lanes/m2-area-20261111 adapted to main), then src/seldon and tests/seldon.

YOUR FILES ONLY: new src/seldon/fixups.py, src/seldon/units.py, new tests/seldon/test_fixups.py. Do NOT edit run.py, states.py, store.py, questions.py, judgment.py, wave_verify.py, flow_review.py or test_journey.py: list the exact wiring you need in your report; the lead wires it. Lane 2 owns wave_verify/flow_review/proof.

INPUT (frozen interface from lane 2): Gap records {"subject", "kind": "flow" | "check", "commit": candidate, "units": [owning unit ids], "correction", "source"}.

DESIGN (decided by the lead; if wrong, stop and say where):
1. fixups.plan(store, gaps) turns each Gap into one fixup on its owning unit(s): the owning unit's own worker session resumes (R8) on the current candidate with the exact correction, inside its own scope. One Gap reaching several units opens one fixup per unit, each with only its part of the correction text (the same text, scoped to that unit). No new planner call.
2. Only the units named in Gaps reopen. Every other unit's verdict, observations and DONE state stay valid; after the fixups integrate, code re-judges only subjects whose owning units' scope trees changed (R7, R9 git tree ids). Fixups count against the unit's two recoveries (C18); exhausted = FAILED, dependants BLOCKED, run INCOMPLETE naming them, as today.
3. Reopen-safe: a kill during a fixup and reopen continues it without redoing DONE units (C23).
4. Replace judgment.fixup's "reset all verdicts" behaviour: expose the function lane-wiring will call instead (fixups.apply(store, gaps)) and say which judgment.py lines it replaces.
DO NOT: new planner calls; fixups outside the owning scope; global re-judgment; rework on uncertain (not judged stays not judged).
LEAD DECISIONS THAT MUST SURVIVE: everything in the judge-minimal brief plus judge-minimal itself.

JOURNEYS in tests/seldon/test_fixups.py (outcome only, importing the existing journey helpers): a check Gap reopens only its unit, others' verdicts unchanged, run reaches C; a flow Gap naming two units opens two scoped fixups; a unit exhausting recoveries via fixups is FAILED with dependants BLOCKED; kill during a fixup then reopen completes without redoing DONE units.

DELIVER in ~/codex-harness/work/lanes: m2-fixups.patch, m2-fixups-report.md at most 10 lines: files and lines; exact wiring for the lead; journeys and seconds; what was ported from the draft; anything wrong.
