CHARTER: serves C20 — violates no I#; shared policy follows I6/I9.
TRIAGE: BUG — detached-controller console children steal focus; sibling Git, Python, shell and provider launches share the fix.
CODE: process_launch.hidden_process_kwargs ORs CREATE_NO_WINDOW with existing flags on Windows; returns {} elsewhere.
Sites: acceptance_revision(3), package_provenance(3), test_audit(2), wave_refine(1), supervision(1), steering(1).
Sites: project_init(1), dispatch_repository(1), semantic_runner(1), runners observer(1); generated observer embeds the same helper.
Exceptions: planner_jobs controller flags unchanged; audit_process unchanged (Windows launches already hidden; other launches POSIX-only); semantic_web.cjs already windowsHide:true.
Static checks: 11 files and generated observer compiled; launch grep + AST review found no uncovered launch outside listed exceptions; diff whitespace check passed.
Net src lines: +41 (43 added, 2 removed); tests added/deleted: 0/0; no gate, suite or provider run; no commit.
Runtime focus behavior remains unproven; lead gates integrated patch after the active run.
