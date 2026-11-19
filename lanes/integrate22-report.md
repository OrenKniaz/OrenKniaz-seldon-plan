Base ee02415; 114 -> 115 collected (existing area helper exposed for narrow selection). Uncommitted; no deps/providers/gate.sh; lead full gate remains.
BUG test_detail_correction_journeys: accumulated owner words invalidated valid siblings; exclude words from DETAIL reuse basis, retaining targeted correction/resume routing.
TEST test_contract_owner_journeys: crossings are not provider proof; trace only u004 and retain all crossed contracts in integrates; scoped repair still reaches DONE.
TEST test_shared_page_flows: crossed provider is not a repair target; expect u002, preserving candidate-bound failed-check evidence.
TEST test_clean_core_golden: original contract assertion fixed; sole run then exposed blanket sibling-path ban; allow Peer checks, retain local-fact confinement; add existing DETAIL resume journey.
Files: src/seldon/detail.py; tests/seldon/{test_architect,test_contract_owner,test_flow,test_journey}.py. Source +1/-1 net0; both full test trees scanned; AST/diff/reverse-apply/tracking PASS; T-170/T-164 remain in_progress.
Env: .venv/Scripts first PATH; PYTHONPATH=src;tests/seldon. Commands: python -m pytest -x -q tests/seldon -k "<selector>" -p no:cacheprovider --basetemp=C:/seldon/tests/integrate22-<n>/pytest (TEMP/TMP/TMPDIR under same slot).
n=1 selector="detail_correction_journeys or contract_owner_journeys or shared_page_flows": 3 passed/111 deselected,49.55s; n=2 selector="planning-detail or planning-architecture or planning_coverage_repair_journey or planning_peer_review_journey": 5 passed/109 deselected,6.12s.
n=3 selector="test_clean_core_golden": 1 failed/113 deselected,295.49s; TEST assertion above repaired afterwards; full golden NOT rerun, not claimed GREEN; no terminal hang.
n=4 selector="test_area_product_journey or test_rule3_scale50_journey": 2 passed/113 deselected,84.01s; area reaches scripted C with reopen/sibling reuse, 50-unit execution passes. Next: lead gates/lands this exact patch.
