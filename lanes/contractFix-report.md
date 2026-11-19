TRIAGE: DESIGN - T-149 / Fable 9.1 Lane G; uncommitted candidate on ebaa953 (Lane F included).
Files: src/seldon/{schema,units,questions,fixups,plan,run,judgment,decisions}.py; tests/seldon/{test_journey,test_fixups,contract_fix_journey}.py. Net src +83 (new capability; shared exact-B provenance/check-in wiring exceeds ~+30 estimate).
contract_fix_journey: 4 passed / 45.96s (contractFix-2): DONE provider fixed once, pending provider brief, user WAITING, f01-style real HTTP server-date twin; zero discoverer recoveries, scripted C and visible check-in changes.
Selector 'blocked_discovery_ask_twin or blocked_owner_journeys or (contract_fix_journey and user)': 4 passed / 82.01s (contractFix-3); final user-request shape rechecked.
self_owned_blocked_reopen_journey: 1 passed / 13.61s (contractFix-4); AST parse and git diff --check pass. No gate.sh, commits, dependencies or real providers; lead owns the full gate.
Stale assertions: searched ALL Python tests/support in lane and semantic-cc/tests/seldon; fixed own-scope recovery, mixed local/foreign blocker, and retained kill-blocked expectations in lane.
Limits: f01-style twin, not a recorded r211 replay or real UI acceptance; T-152 stale requirement prose remains with contract-node authority explicit in briefs; running-provider correction not covered by these journeys.
Tracking blocked: writes to ladder/TICKETS.json and validator refresh of STATUS.json denied PermissionError; no retry. Lead must update T-149/lane status on review/landing.
