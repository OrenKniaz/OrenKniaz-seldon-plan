# Bird's-eye evidence, 2026-11-13 (M2 exit cohorts)

Seldon main 050f3e8 (repo ~/codex-harness/work/sprint-20261027/semantic-cc). Binding: CHARTER.md v1.7, BLUEPRINT.md v1.5. Tickets: ~/codex-harness/work/ladder/TICKETS.json. Run folders: C:/seldon/tests/m1/foundation-<sha>-<id> (product/, store), logs C:/seldon/tests/m2exit<N>/<id>.log.

Exit bar: 8/10 canonical Foundation runs reach C.
- Cohort #2 on 2b5ff9e: 0/10 (cross-area REVIEW uncertain was fatal) -> T-116 landed.
- Cohort #3 on 9eddbb9: 7/10. Failures: z04, z05 worker blocked by defect in DONE sibling's file counted as own failure (-> T-118 owner fixup); z06 four areas invented four accessible names for one button (-> T-119 agreed literals, Fable rule).
- Cohort #4 on 050f3e8 (T-118 + T-119 landed): 4/10. Failures, all different:
  - x03, x06: "Candidate changed outside integration: ? checks/seldon/.fixture-XXXX/" — a check does fs.mkdtemp(path.join(__dirname,'.fixture-')) inside the product checkout; leftover untracked dir refuses the candidate. Not seen in cohort #3. Family T-12 (checks write into the tree).
  - x01: flow/integrated check n010 (checks/greeting/integrated.cjs) fails; fixup assigned to u001 (page) whose write scope cannot touch it; u001 exhausted. Family T-102 (fixup ownership).
  - x04: u002 answered blocked: its integration check n011 needs the canonical HTML producer, absent in its checkout; discovery target "n011 integration prerequisite" (not a path), so no owner handoff. Family T-61 (a unit's check needs sibling behaviour).
  - x07: u004 "unit too large to judge; split it". Family T-56.
  - x09: u002 failed: "Use a project-relative path or pattern: 'Correction assignment: n015 and n020'" — prose in a path field refused. Family T-50 (normalise, not refuse).

Pattern the lead sees: each cohort removes one wall and the next walls are different, mostly at the unit/check/integration boundary in EXECUTE (who owns a check, where it runs, what it may write, how big a unit is), not in planning. Variance at n=10 is large (7 -> 4 with mostly unrelated failures).
