STAGE-2A REVIEW FIXES (CC). An independent Sol code review REJECTED your candidate (be14e839...). Full review: ../stage-2a-review.md (line numbers refer to the published-tree layout; map them to your lane). One design cause, TRIAGE DESIGN: authority must come ONLY from a current judgment bound to every member, the current revision and the current candidate. Fix all five at that shared rule, not five patches:
1. **HIGH — [roundtable.py:1872](~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/roundtable.py:1872): findings disappear before judgment.**
   Two findings with the same node and normalized finding text, but different suggestions or scope rationales, enter `_merge_finding` → only one source member survives. The later equivalence judge cannot recover the dropped gap or opposing rationale.
   **Fix:** retain every source finding; let the bound equivalence judgment determine grouping.

2. **HIGH — [plan_store.py:3094](~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/plan_store.py:3094): acceptance closure lacks candidate binding.**
   Prepare a disposition against repaired product A; change the product to B without changing plan/template → the assessment facts remain identical, so A’s positive judgment can close the finding after the product changed.
   **Fix:** bind acceptance dispositions to the canonical current acceptance run and product revision, rechecking that binding when applying closure.

3. **MED — [plan_store.py:2132](~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/plan_store.py:2132): fresh reviews inherit closed attempts.**
   Both reviewers exhaust malformed-output fixes without producing findings → unchanged packets retrieve the same terminal judgments on retry. Correct replies then hit `judgment-attempt-closed`; similarly, a retained negative verdict rejects a different fresh verdict.
   **Fix:** allocate judgments per new review invocation; reuse judgment IDs only for that invocation’s retries or recovery.

4. **MED — [plan_store.py:3108](~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/plan_store.py:3108): partial closure hides unresolved members.**
   Group A/B; positively close A alone → default `findings()` projects A’s resolved status, and continuation reports no open finding. Publication reads expanded members and rejects B, leaving ordinary guidance repeatedly recommending advancement.
   **Fix:** derive cluster presentation and continuation from every member’s status, preserving B’s open obligation.

5. **MED — [plan_store.py:2261](~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/plan_store.py:2261): revision repair strands convergence.**
   After three rounds, repair the plan and obtain positive reuse judgments → publication requires a new convergence assessment, but this read uses `prepare=False`. Resolution prepares reuse only; the previous convergence request is stale and continuation still recommends advancement.
   **Fix:** prepare and expose the current convergence request when repaired review credit becomes available.
Prove each with a golden scenario through the scripted judge (no unit tests): same-text findings with different gaps both survive to judgment; a product change after a positive disposition invalidates it; a fresh review after an exhausted malformed attempt gets fresh judgments; partial closure keeps B open in findings() and continuation; repair + reuse exposes a current convergence request.
Allowance: the single golden file via python -m pytest tests/python/core/test_golden_path.py -k cli -x --basetemp=C:/seldon/tests/stage-2a/p3 as needed, then up to 2 full golden-gate.sh runs; the last run comes after your last edit and must be green. Keep PROD net strongly negative. Update ../stage-2a-report.md (TRIAGE+CHARTER first; add a "Review fixes" line per finding), ../stage-2a.patch and sha256 (vs base 652de9f). Timebox 90 min.
