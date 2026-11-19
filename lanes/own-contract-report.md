T-113: cross-area consumer endpoints only; provider-area units receive shared contract text without consuming it.
Exactly one provider and explicit file dependencies remain enforced; source changes confined to architecture.py and agreement facts.
Added bd6d374-c01 raw replies and replay; all four recordings reach REVIEW and approved B; original three unchanged.
Gate: bash scripts/gate.sh ocon-2, harness venv first on PATH: 14 passed in 210.93s (base 14); timing assertions intact.
own-contract.patch: 4 files, against e6faafe (base 36f04fe golden-only); reverse-apply check passed; tracking updated.
No commit, new dependencies or real provider calls. Planning regression proven; next: lead review/landing and authorized real-run validation.
