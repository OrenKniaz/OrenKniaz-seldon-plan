Round 2. An independent review found two issues. Fix both at their owners, smallest change.

P1: when every provider fails authentication, reselection stores reviewers=[], plan_acceptance `complete=bool(node)` is true, and B can proceed with no review while looking complete. Keep the owner rule that a missing verifier degrades to a labelled tier and never blocks delivery, but record it honestly: an explicit unavailable state that is not review credit. Do not report the review as complete-with-credit; let delivery continue only through the existing labelled-tier route, and make the B wording state that no independent review ran.

P2: run_loop.py:161 clears run.effect before _record_answer on both normal completion and recovery, so the saved-facts lookup returns None and a judge citing a supplied facts.dialogue message ID is refused. Pass the completed invocation's facts explicitly.

Keep the net src lines as low as you can. Run ONLY the small journey as before, using a NEW folder because you cannot delete: C:/seldon/tests/review1/small-plan-r2 (use -r3 and so on for retries). Add the all-providers-fail outcome to the existing authentication twin only if it is cheap.

Regenerate stage-review1.patch (cumulative against base) and stage-review1.patch.sha256, and write the delta alone to stage-review1-r2.patch. Rewrite stage-review1-report.md (at most 10 lines, with the journey result and seconds). Do not commit.
