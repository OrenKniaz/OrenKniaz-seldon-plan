TRIAGE FAULT SELDON + DESIGN — T-212, checkContract on d56dc7b (exact source tree).
Root cause: src/seldon/proof.py:97 sent WAVE-VERIFY failures only to the writer's handoff owner. src/seldon/decisions.py:104 labeled repeated check failures as Seldon faults.
Fix: checkContract sends provider–consumer disputes evidenced by check handoffs through the existing ARCHITECT correction, then schedules both sides against the revised contract. Repeated product checks get planner-framed change, leave-out and pause options. Controller faults retain their fault question.
doneUnitsRedone: wave 2 and 3 extensions are explicit at r522–526 and r834–838. Every listed redo is a verification REWORK retry, including service at r300; zero WORKING reopen transitions and no DONE resume redo.
Files: src/seldon/{decisions,features,fixups,plan_review,proof}.py and tests/seldon/test_journey.py.
Source: 5,015 → 5,105 lines. Base RED: four service fixups and a fault message; unfixable product check also mislabeled. Strict-schema focused GREEN: 5 passed, including both endpoint patches and the genuine controller fault. Cold imports: 27 passed.
Gate: bash scripts/gate.sh checkContract ran once with the harness venv first on PATH. 84 passed (83 base cases plus one), 362.60 s. Patch applies to d56dc7b.
Main landing and real-provider validation remain pending.
