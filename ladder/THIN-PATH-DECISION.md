# Thin A-to-Z path: owner decisions (2026-11-08)

Oren approved all three on 2026-11-08 ("I approve all"), on the evidence in `design-review/should-it-exist-audit.md` (Astra, read-only, audited 4cdafbb).

1. **Build the thin path in this repo, reusing existing owners, then delete what it displaces.** No restart. Success = one fresh real small-app run through A, Spec, B, observed RED/GREEN, judgment, wave check-in, demo and C.
2. **C5 interpretation for small apps: five pre-build node kinds** (`vision`, `feature`, `requirement`, `test`, `bead`). Story meaning lives in the feature; architecture, design and interface contracts are typed sections of the requirement. The meaning stays required; only the separate nodes go. Larger sizes keep the fuller taxonomy, chosen by the size judgment. Research, discovery, metric, iteration, stop-condition and baseline nodes appear only when the dream calls for them.
3. **No migration across Seldon versions.** Runs from an older format get a clear refusal and a fresh start; old artifacts stay as history and are never relabelled. Recovery inside a current-format run stays (C18/C23).

This records an interpretation of the ratified charter v1.2; it does not edit CHARTER.md.

## Order
- Milestone 1: small plan reaches B on a real run (`thin1`), old-run migrations deleted (`nomig`).
- Milestone 2: Build, observe real RED/GREEN through ordinary declared test commands as the only test route.
- Milestone 3: integrate, wave check-in, real demo and guide, C.
- Then delete the displaced paths, ranked in the audit. Gate back under 600s.

## Lane rule until a real run reaches C
Does the charter require it, does the next real run need it, does the provider already do it? No hardening or compatibility work unless a real run is stopped by that problem.
