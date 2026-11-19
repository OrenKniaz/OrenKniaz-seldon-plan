Built fight.py, oracle.py, oracle_ui.py and blind.py using Python standard library only; no real contender launches.
Both sides use gpt-6.1-sol / medium, farm.user_reply, and farm receipt scoring; native disables Seldon MCP and skips init.
Farm is imported without source edits or its lock; local .fight.lock and receipts isolate this tooling; farm verification is deferred to oracle.
Verified: python fight.py seldon --dry-run and python fight.py native --dry-run; 3 turns, 2 decisions, 300 input / 30 output tokens each.
Verified: python oracle.py C:\seldon\tests\fight-1\fake selftest-final; 39 pass, 0 fail, 1 unverified; HTTP/import/restart/concurrency/UI exercised.
Screenshots: C:\seldon\tests\fight-1\selftest-final-375.png and selftest-final-1440.png.
Verified: python verify_blind.py; two real fixture evaluations, private A/B assignment, label-only comparison and four screenshots.
Blind smoke artifacts: blind-smoke/20261101T145437-5e1413/compare.md and blind-key.json (fake fixtures only; key for CC).
Use later: python blind.py <first-product-dir> <second-product-dir>; creates oracle-A/B.json, compare.md and private blind-key.json.
Oracle copies are never overwritten; use fresh labels. Farm result slot identifies the nested Seldon product directory.
Token counts cover outer receipts only; UI semantic discovery failures are reported; visual design/contrast require blind screenshot review.
Completed within 45 minutes; brief unchanged; only fake Codex, fixture servers and isolated headless Chromium were launched.
