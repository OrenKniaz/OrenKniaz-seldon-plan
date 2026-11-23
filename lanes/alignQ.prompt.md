# Lane alignQ (Terra 6.1 medium): analysis only, no code changes
Question: on S1-doorcount, Seldon Lead's ALIGN asked the person zero questions, although the brief has real ambiguities. For example, does "the last four Fridays" mean four Friday shifts, or every shift between two dates? Shaping the dream with the person is the planner's core job (CHARTER-LEAD, BLUEPRINT R18 grow-and-align, R17 ask user with options + Other).
Evidence:
- ALIGN question and answer: C:/seldon/tests/m1/s1b-doorcount-cfb3438-s1b01/calls/call-b3bb414a62724c0180e06add06c02a8a/
- Run logs: C:/seldon/tests/s1LeadB/s1b01.log and C:/seldon/tests/lsbbS1/a01.log
- The sim-user setup: SELDON_SIM_USER and SELDON_USER_SCRIPT in C:/seldon/tests/cohort2.sh
- Source: ~/codex-harness/work/lanes/land-wt/src/seldon (run.py ALIGN, questions.py, any grow/align code)
Find out:
(1) Did ALIGN have any way to ask, i.e. is there a field or path for a question to the person, and did the prompt invite one?
(2) Did the sim user or a script suppress questions, or did the planner choose not to ask?
(3) Across other recent Lead runs (C:/seldon/tests/m1/*/calls with an ALIGN answer), how many questions were asked per run?
(4) What is the smallest prompt-level reason for zero questions? Quote it.
Write C:/seldon/tests/alignQ-0/REPORT.md, max 15 lines. Do not edit any repo. Temp files only under C:/seldon/tests/alignQ-0. Never read C:/seldon/sealed/.
