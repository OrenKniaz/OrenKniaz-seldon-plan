LANE judge-dedupe (ticket T-79). Worktree C:/Users/oren/codex-harness/work/lanes/judge-dedupe-20261112 (Seldon main 6145a1f). Temp only under C:/seldon/tests/dedupe-<n>. Do not commit. No new dependencies. Do not edit CHARTER.md or BLUEPRINT.md. Behaviour-only journeys. No real provider calls.

PROBLEM: real judge questions carry each file twice. Real run C:/seldon/tests/m1/foundation-230667c-c01: PRODUCT question (calls/call-8c793a69b1ba40879e13363e2b031609/question.json) is 72.9 KB: "Files on the delivered revision" 29.9 KB, "Final check sources" 24.4 KB (the same text again), "Check artifacts" 11.5 KB. DEMO call-40a2250d898741b4a24b05cc37880cf7: 12.6 + 12.5 duplicate + 11.0 KB.

RULE: one copy of each fact per question. In src/seldon/judgment.py brief(): remove "Final check sources" (check files are already in "Files on the delivered revision"; mark which files are check sources with a list of paths). For "Check artifacts": keep path, bytes, commit; include text only if it is not already in the observation's bounded output. Same rule wherever questions.py builds WORK/JUDGE briefs, if they duplicate the same way (say if they do).
Add to the journey a size check driven by a real recording (tests/seldon/recorded_work.json pattern, or a small recorded fixture taken from that run) so the real shape is measured, not only scripted 4 KB files. Keep the existing 1-vs-50-unit size assertion.

LEAD DECISIONS THAT MUST SURVIVE (do not change): timing asserts in test_journey.py `scale_seconds < 90` and `seconds < 270` (T-77); owner constants ALIGN_DESIGN, CRAFT, JUDGMENT_LEEWAY word for word; one subject per judge question; DEMO-FACTS/PRODUCT-FACTS states.

DELIVER in C:/Users/oren/codex-harness/work/lanes: judge-dedupe.patch (git diff --binary vs base), judge-dedupe-report.md at most 8 lines: lines changed; DEMO/PRODUCT bytes for the recorded real question before/after; suite result and seconds; anything else duplicated you found.
