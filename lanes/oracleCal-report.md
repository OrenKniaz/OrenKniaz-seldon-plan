# Quiet Bench oracle calibration
Totals (pass/fail/unverified) · Seldon 2/8/2 → 10/1/3 · plain Codex 5/5/2 → 10/0/4. Below, P/F/U follow the same product order.
- Server start · P→P / P→P · Dream “python server.py --port PORT --data DIR” (L11). Same launch with bytecode disabled.
- CLI/API · F→P / F→P · Interface-specified (L51–52, L85). Any creation 2xx, poll async completion, check same-ID storage and bands by bounds.
- Fixed wave 1 · F→P / P→P · Dream “one tone through a fixed filter, saved and shown” (L11). One tone, documented coefficients when needed, API readback.
- Hidden attenuation · F→P / F→P · Dream “adaptive canceller (LMS family)” and “cancelled in each frequency band” (L11), interface L84–85. Independent WAV/path/energy checks, convergence and a fixed filter frozen on the public path. Full-record DFT with 1.5 dB tolerance is a derived measurement.
- Safety (old combined F/F) · hold level P/P, divergence U/U, one-block stop F/U · Dream “limiter must hold” and “stop switch ends a run at once” (L11), interface L52, L71–72, L85. No demonstrated divergence trigger. Seldon acknowledged stop at 32,768 requested samples and remained running at 128. Plain stopped at 1,536 but exposed no request-time cursor.
- Save/restart/reload · P→P / P→P · Dream “Every session is saved … with its settings and results” (L11). Exact JSON equality through API and CLI after restart.
- CSV/bad WAV · F→P / F→P · Interface-specified CSV and PCM WAV (L51, L84). Match exported samples or bands by meaning. Invalid input must report failure and leave the session list intact.
- Compare · F→P / P→P · Interface-specified (L52). Use distinct saved runs and match B minus A by band bounds regardless of order.
- Page parity · F→P / P→P · Interface-specified (L86). Match control labels by meaning, verify run/reload/compare results, and allow displayed numeric precision. Viewports are observational.
- Guide · F→P / F→P · Interface-specified (L86). Run documented start and four CLI commands in fresh copies with confined placeholder paths, then verify exit and loss of HTTP after Ctrl+C.
- Legacy · U→U / U→U · Interface-specified (L85). Actual wave-1 stores and session snapshots were unavailable.
- Page craft · U→U / U→U · No craft rubric or viewport criterion in the builder text. Screenshots confer no score.
Evidence · C:/seldon/tests/oracleCal-4/{oracle-qb2,oracle-qbplain}/oracle.json. Baselines are the supplied -ev/oracle.json files. Brief line references use briefs/L3/4-quietbench.json.
