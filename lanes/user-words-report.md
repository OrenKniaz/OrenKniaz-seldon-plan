T-130: focused journeys GREEN on b2965c1 (base ad3a8a6 golden-only); detail.py caller authorized by lead.
Files: src/seldon/{questions,schema,inference,run,plan_review,detail}.py; tests/seldon/{test_architect,test_journey}.py; +149/-16, net +133.
Env: harness .venv/Scripts first on PATH; PYTHONPATH=src;tests/seldon; PYTHONDONTWRITEBYTECODE=1; TEMP/TMP/TMPDIR under each uwords-N.
python -m pytest -x -q tests/seldon -k test_user_words_journeys -p no:cacheprovider --basetemp=C:/seldon/tests/uwords-5/pytest => 1 passed/17 deselected, 4.09s suite / 5.52s wall.
python -m pytest -x -q tests/seldon -k test_planning_size_journey -p no:cacheprovider --basetemp=C:/seldon/tests/uwords-6/pytest -rP => 1 passed/17 deselected, 5.53s suite / 6.81s wall.
Existing size journey: same-area REVIEW 5918/5918 bytes at 1/50 units; ARCHITECT 4239/4239, DETAIL 12437/12437. Growing-area REVIEW maxima 6044/13703.
Twin and fault twin reach approved B with dream literals, two A + two B revises in order, and a decision; uncertain ARCHITECT rejected once. 18 collected vs 16 base (+2 narrow entrypoints).
Earlier caller blocker resolved; no known focused failure. No commit, dependencies, real providers or full gate; replay fixtures untouched, lead serial gate/replays remain pending.
