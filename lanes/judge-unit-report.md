T-85/T-87: planner-owned levels, unit JUDGE targets + code AND, bounded FACTS; base 6a7d500; uncommitted.
Lines src/seldon: decisions 82->93; inference 69->72; judgment 223->273.
Lines src/seldon: plan 177->187; questions 269->284; schema 92->99; states 57->59; units 171->171.
Lines tests/seldon/test_journey.py: 1052->1163. No new files; no git add needed.
Golden: 1 pytest passed; journeys 42->48; suite 148.20 s, scale50 57.72 s; timing assertions <270/<90 unchanged.
Largest bytes at 1/50: JUDGE 30738/30738; PRODUCT 5997/5997; re-ask 4143/4143 (each <=2x first ask).
c01 quality:003 replay -> unit JUDGE u001/u002/u003/u004: 41592/23322/23154/24547 B; never PRODUCT; code AND.
Replay reconstructed retained first JUDGE diffs/check sources (junit-7); original Git ownership blocked reading; no trust change/retry.
Rule conflicts: none. Typed evidenceLevel routes source requests; reviewed marking-only correction preserves units/checks and approval binding.
No new lint (10 inherited), dependencies, commits or real providers. Final gate junit-11/gate.txt; lead review/integration + real runs remain.
