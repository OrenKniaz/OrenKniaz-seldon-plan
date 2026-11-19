# Build-vs-buy decision (Oren approved 11-04: "I approve if you think it's correct approach"; CC verified repos 11-04)
- ADOPT official MCP Python SDK (modelcontextprotocol/python-sdk, MIT, active) — Stage 2c/4b; keep ~1-1.5k LOC domain adapters.
- ADOPT Playwright (microsoft/playwright-python, Apache-2.0, active) + ordinary worker-written tests instead of our scenario DSL — Stage 1c/2a/2e.
- ADOPT Beads (gastownhall/beads = former steveyegge/beads, MIT, Go, v1.3.4 2026-11-04, Windows amd64/arm64 builds) — Stage 3a/3d; ~250-450 LOC adapter; Seldon keeps trace + proof provenance; ONE task authority (no dual mutable graphs).
- DO NOT ADOPT MCP Agent Mail: its license "MIT with OpenAI/Anthropic Rider" grants no rights to OpenAI/Anthropic or anyone acting on their behalf, and forbids making it available to them. Seldon wraps Codex/Claude and is built by Codex/Claude agents -> unacceptable risk. KEEP our mail.py (185 LOC), add discovery/handoff kinds + validated trace links in 3c.
- Memory: keep ours, shrink to ~300-450 LOC; fix "confirmed constraints: follow them" (memory is advisory, C19) + add cross-project retrieval — Stage 3c.
- Budgets/quotas: delete from product (C8) — Stage 2b.
