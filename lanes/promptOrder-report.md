TRIAGE FAULT SELDON
DESIGN: effic-astra-2026-11-16 cut 4; stable role/schema/example first, scoped agreements next, changing facts last.
Removed: late schema/example placement and agreements after observations; no prompt content removed, no new state/validators/caps.
Files: src/seldon/providers.py; tests/seldon/test_journey.py (existing contract journey extended).
Src Python lines: 4200 -> 4199 (-1); providers.py 251 -> 250.
Gate: bash scripts/gate.sh promptOrder ONCE, venv first PATH; 37 passed in 592.66s, exit 0; cases 37 -> 37; no skips/fixes/re-gate.
Base: supplied clean b3598dd0bcfc3271dd9274fb922e329f5a10161c; requested ab2ae1f object absent; patch is diff vs supplied base.
Proof: rendered-order base RED -> GREEN; recorded sections preserved as sets; no >5min test hang, providers, commits or .env reads. Lead landing/native cache measurement remain.
