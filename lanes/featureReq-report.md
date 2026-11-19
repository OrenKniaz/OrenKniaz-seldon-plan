TRIAGE FAULT SELDON · BUG · T-236
DETAIL root at src/seldon/plan.py:264 on 7be4158. Reusing edit positions as trace IDs in an executed wave stranded older features and tripped line 409.
ALIGN root at src/seldon/questions.py:233. The kickoff contained the recorded runtime literal across the line break after Node 20. The matcher now stores the original source span.
DETAIL preserves started-wave trace IDs. Unlinked answers get a targeted re-ask. A repeated mismatch reached the planner and then a resumable Stop.
Recorded ALIGN r11 and DETAIL r44/r139 reproduced the step failures on base and reached EXECUTE on the patch. Both correction and repeat journeys passed.
Sole bare gate passed 129 in 426.39 s, four cases added. All 28 cold imports passed. Patch applies to exact base 7be4158.
The DETAIL replay seeds the integration boundary. Lead landing and authorized real continuation past EXECUTE remain pending.
