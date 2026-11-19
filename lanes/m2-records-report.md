Base 97c69519a577ae29fed188ae9c70f507e3363ed9; uncommitted binary patch includes new architecture.py and obligations.py.
Production: 17 modules/2849 lines -> 19/3037; journey 1163 -> 1328 lines (physical lines).
Modules before->after: plan 187->212; schema 99->113; architecture 0->67; obligations 0->30; questions 284->304; scheduler 53->54; store 219->235; states 59->59; judgment 273->282; run 227->233.
Ported/adapted from area draft 6733da7: architecture contracts_for/endpoint/area_decisions/crossed_contracts, ownership/link checks; obligations for_area/remaining. No flow-draft abfd4a5 code ported.
Journeys 48->56; pytest 1->8: shared-page C/contract briefs, invalid links/reads/scopes, skeleton open/closure, contract repair/reopen/re-judgment, unrelated docs repair, hello-world and contracts at scale.
Final gate 8 passed/178.28 s (golden 176.50; scale50 61.14; records 13.26); base 1 passed/180.86 s. <90/<270 assertions and all owner constants retained.
Largest WORK/JUDGE bytes at 1 unit: 3267/30734; at 50 with a build-time file-format contract: 3267/30734. Recorded DEMO/PRODUCT replay: 15785/17065 B.
T-90 closure-on-new-final-commit bug repaired locally; T-91 Windows Git object-write denial remains open (not reproduced in final gate); T-10/T-11 await landing/cohorts. Evidence: C:/seldon/tests/m2rec-12/gate.txt.
Contract repair is tested from a prepared existing REPAIR entry through the canonical writer, REVIEW/B and reopen; automatic post-B steering remains outside this lane. No real provider calls, dependencies, commits or document edits.
Brief ambiguity: M2-PLAN reserves wiring/journey edits for the lead, but this assignment requires them; patch includes minimal scheduler/brief/revision/gate hooks for lead review. Patch reverse-apply and whitespace checks passed.
