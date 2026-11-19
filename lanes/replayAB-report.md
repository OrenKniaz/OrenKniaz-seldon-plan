# replayAB · T-231 · base 21b6381
From the patched checkout in PowerShell, set `$p='C:/Users/oren/codex-harness/.venv/Scripts/python.exe'; $r='C:/seldon/tests/replayAB-20'`.
Prepare offline · `& $p -B tools/replay_prompts.py prepare $r`
Generate five WORK pairs · `& $p -B tools/replay_prompts.py generate $r --run-terra`
Generate semantic pairs · `& $p -B tools/replay_prompts.py generate $r --run-terra --semantic`
Package offline · `& $p -B tools/replay_prompts.py package $r "$r/packet"`
Give reviewers only the packet. `lock --help` describes independent reruns and ballots. Keep `private/key.sealed.json` in lead custody until the ballot lock.
Offline: all five WORKs and twelve semantic pairs prepared, with one render-only repair. Recorded WORK/folded JUDGE and sealed samples passed in 7.98 s on the final patch.
Sole bare gate: 122 passed, one front-door timeout at the decline wait, 642.44 s. Exact base passed that test alone in 31.65 s. T-211 owns the gate timing.
Patch apply checked on 21b6381. Native sandbox preflight and Terra generation remain unexercised. The offline run establishes replay plumbing.
