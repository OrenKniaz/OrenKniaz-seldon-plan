RECOVERY-1 | base 068a864; lane HEAD 02d14080a603cc0a972ba83176825045f11a0db2; no commit/push.
Fix: planner_recovery.monitor/resolve ends the owned Job, bounds UNKNOWN to ABANDONED, quarantines the old namespace, and readmits within B; delivery is locked against quarantine.
Proof: hung Build descendant reaped (zero active Job members), missing receipt abandoned, clean successor reaches C in three decisions; no poisoned writes delivered.
Final gate: 18 passed + 1 web failure (19 cases vs base 19); core delta 0, tools delta 0; first web passed. Final gate is NOT green.
Blocker/next: unchanged semantic_runner._cleanup raised WinError 2 on Chromium lockfile after verified teardown; cleanup-owner repair/authorized recheck. Actual-provider recovery unproven.
Patch: recovery-1.patch | SHA256 2a9f40469da18a53dd8666efa8d9a3dc00e126c87f4a33440905014bb76b5161
FAST-LANE RULES (binding): NO unit tests, ever; no new test files; extend golden scenarios only.
ONLY test command: bash ~/codex-harness/work/lanes/golden-gate.sh ~/codex-harness/work/lanes/recovery-1 recovery-1; run twice, no third run.
45-minute timebox, medium effort; one recovery cluster, starting at refusal recovery-readmit-requires-VERIFIED-QUIESCENT in planner_recovery.resolve.
Report <=12 lines; exact patch + SHA256; no pushes.
CC command-log rule: reject any other pytest; none was invoked. Initial structural ceiling failure fixed without raising the ceiling.
Scratch/temp/basetemp: C:/seldon/tests/recovery-1 (already writable/add-dir scope); no C:/ root or ~/t folders.
