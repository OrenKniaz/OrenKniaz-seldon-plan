TRIAGE: DESIGN — T-150 / Fable 9.2: owner wave RED at wave start; wave GREEN stays at WAVE-VERIFY.
Files: proof.py, questions.py, units.py (net src 0); test_journey.py, test_architect.py, wave_red_journey.py, recorded_f04_delivery.json.
Journeys: -k "wave_red" 3 passed / 20.40s; -k "wave_red_journey or rule3_scale50_journey" 3 passed / 102.79s (50-unit unchanged); +3 collected vs base.
Stale assertions: grepped all lane + semantic-cc tests/seldon; corrected two check-owner assumptions (pre-verify absence / all observations GREEN).
Cost printed, never asserted: one extra owned wave-start run in f04 and one in preservation twin; no new timing assertions or caps.
Replay: original n027 helper hit denied taskkill; portable subprocess helper twin used, recorded n028 unchanged. Initial missing basetemp parent corrected.
Tracking blocked: STATUS.json write and tracking.py hit PermissionError; lead must update STATUS/T-150 with delivery and evidence.
No commit, gate.sh, real provider calls or dependencies. Candidate base 7649759 (260584f golden-only); lead gate and real-run acceptance pending.
