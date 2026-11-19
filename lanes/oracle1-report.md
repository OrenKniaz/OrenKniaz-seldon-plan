T-151: backed up `oracle_ui.py` to `oracle_ui.py.bak-1114b`; added enabled-control waits, confirmation within the item's semantic row, and Tab traversal bounded by focusable-element count until expiry is focused; scoring/favicon/console checks unchanged.
Totals below are pass/fail/unverified, old -> new.
Native: 36/3/1 -> 36/3/1; product: `/favicon.ico` 404 still fails both layout/console checks and healthy-interactions console ([evidence](../fight-1/oracle-m2-native-v3.json)).
f02: 36/3/1 -> 38/1/1; delete and expiry-focus now pass; search clearing remains an oracle failure ([score](../fight-1/oracle-m2f-f02-v2.json)).
f03: 37/2/1 -> 39/0/1; delete and expiry-focus now pass; no remaining failures ([evidence](../fight-1/oracle-m2f-f03-v2.json)).
f05: 39/0/1 -> 39/0/1; expiry input explicitly reached and focus passes; no remaining failures ([evidence](../fight-1/oracle-m2f-f05-v2.json)).
f02 search: empty input leaves the filtered list; clicking visible “Apply filters” restores Later oats and No expiry, proving the rig missed submission; left outside this repair ([DOM/UI evidence](C:/seldon/tests/oracle1-5/search-apply-diagnostic.json)).
Final runs: 10.1/14.8/11.8/10.4 seconds; 900-second ceiling with stricter 300-second stop; scratch only `C:/seldon/tests/oracle1-<n>` via launch-time TESTS redirection, oracle.py unchanged; no LLM calls; each retains one unverified visual-design check.
