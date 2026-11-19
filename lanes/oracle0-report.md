T-144 rig: oracle_ui.py:130-132,222-281 scopes add/validation fields to the quantity-bearing form and submits unchanged search/filter views; backup: oracle_ui.py.bak-1114.
Totals below are pass/fail/unverified out of 40; scoring policy and favicon/console checks unchanged.
native: old 36/3/1 -> new BLOCKED: supplied C:/seldon/tests/fight-1/m2-native-src has no server.py (harness checkout); traversal stopped at 128.73s; correct product path requested.
c01 (m2c-c01-v2): old 30/9/1 -> new 35/4/1; all six previously failing search/filter/add/validation/consume/delete checks now pass.
c02 (m2c-c02-v2): old 36/3/1 -> new 36/3/1.
Remaining c01-only observation: UI visible keyboard focus fails on expiry-date INPUT: focusVisible=false, outline=none, shadow=none; evidence: C:/Users/oren/codex-harness/work/fight-1/oracle-m2c-c01-v2.json:321-323.
Both rescored contenders retain the same three favicon.ico 404 console failures; calm-design review remains unverified. Fresh receipts: oracle-m2c-c01-v2.json and oracle-m2c-c02-v2.json in fight-1.
Runs used timeout 900 plus a 300s watchdog, no LLM calls; scratch TESTS overridden only in memory under C:/seldon/tests/oracle0-1 through oracle0-6; initial path-quoting startup diagnostics retained in oracle0-1..3 (not product scores).
