T-82/T-83: owner/seam briefs, fact-hash reuse, executed guide paths/argv; every multi-owner subject gets its seam question.
Lines: gitwork.py 144->146; judgment.py 180->134; plan.py 173->177; questions.py 255->256; run.py 208->205.
Lines: finalfacts.py 0->189; guide.py 0->37; test_journey.py 858->1048; recorded_final.json 0->793; pytest tests 1->1.
Retained golden owner-7: 1 failed, 346.87s; behavior assertions passed; scale 115.70s failed <90; <270 assertion unreached. Affected empty-seam journey owner-12 passed, 11.11s.
Current tiny 1/50 (owner-11): DEMO 4501/4501, PRODUCT 5638/5638 bytes; scale 152.31s; frozen base 103.86s (also >90).
Realistic 1/12: largest DEMO 15646/14883, PRODUCT 15554/14791 bytes; 8.83/111.58s; seam names all 12 owners: max 10092 bytes.
c01 non-guide replay: DEMO 80350->42320, PRODUCT 86205->41741 bytes; seams 32723/32144 bytes name all 4 owners (6 rows).
Final calls: tiny 1/50 unchanged at 4/53; realistic 1/12: 4/183 (pre-split shape 4/15); c01/pass 9->45; guide repair 6 incl FACTS, 8 reuses, 0 unchanged reasks; missing-path/prose/reopen passed.
Review findings closed; focused Ruff passed (inherited plan import-order finding remains); patch applies to 731f336; temporary Git index/objects used because worktree metadata is read-only.
NOT READY on timing: next lead action is an isolated <90s scale/<270s suite gate. No remaining rule conflict, commits, dependencies, real provider calls, or CHARTER/BLUEPRINT edits.
