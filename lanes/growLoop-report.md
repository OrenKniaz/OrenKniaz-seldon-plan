TRIAGE FAULT SELDON + DESIGN · T-216 · growLoop · integrated base a827513 (main 548e1d1 + three siblings).
Root cause `src/seldon/run.py:137` installed the first ALIGN proposal as vision, and `src/seldon/decisions.py:210` offered scalar approval at A.
Fix grouped A retains partial choices and exact reply origin; replay folds once. A change plus done displays another proposal. Explicit done locks the displayed draft atomically, and scope re-entry requires fresh A and B.
Files and lines `run.py` 261→308, `decisions.py` 364→491, `test_journey.py` 2,501→2,693. Seldon Python 5,312→5,486. Patch checked forward and reverse against the pinned base and candidate.
RED both grouped journeys hit the scalar ALIGN schema on base. The exact recorded Quiet Bench answer and scripted r10 replay through the scalar control; recorded r170 is the scalar B control.
GREEN strict counterfactual partial selection, size override and “printable result” plus done survive interruption and replay. A stays open until fresh done; first ARCHITECT and B use the identical lock. Tiny locks on its first round.
Gate `bash scripts/gate.sh growLoop` · 91 passed in 355.41 s (89 retained, 2 added); 27 cold imports passed. Retained scalar fixtures ran with `SELDON_OFF=growAlign`; new journeys enabled grouped ALIGN.
Next lead landing and paired Terra comparison. Keep the switch pending that result. No live Terra evidence or delivery commit.
