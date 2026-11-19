TRIAGE FAULT SELDON + DESIGN · T-215 · growVision · base 0bf6cb9, verified tree 1fd98450b0bea9fedfda77bf59015215eaaa98c3.
Root cause: questions.py:57 folds exact inputs into generic scope; plan.py:209 replaces every feature’s origin with the same vision link.
Fix: strict ALIGN rounds and batch DECIDE, two worked examples, and stable story handles carry rank, exact constraints and reply sources through ARCHITECT, area DETAIL, merge and B. Saved legacy visions use their recorded shape.
Files: src/seldon/{questions,schema,architecture,plan}.py (430→566, 124→159, 260→276, 391→410 lines) and tests/seldon/test_architect.py. Total Seldon Python source 4,936→5,142 lines.
RED: recorded Quiet Bench r170 shows four generic edges. On the pinned base, strict counterfactual Quiet Bench reached B with “compare the shared interval” recorded and the comparison feature still ending at the generic vision.
GREEN: strict B journey traces the comparison to its exact counterfactual reply and recorded launch literal after reorder; the stopped-run story keeps its own source. Exact corrections reject rig inventory as a constraint and a wrong-area feature reference.
Gate: bash scripts/gate.sh growVision · 84 passed in 337.98 s (83 base cases, one added); 27 cold imports passed; patch application and reverse checks passed.
Next: growLoop wires the shared growAlign switch and A lock, then gates the merged tree. The blinded cohort still has to measure planning quality. No real provider calls or delivery commit.
