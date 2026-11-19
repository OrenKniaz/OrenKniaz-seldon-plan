# ShelfLife fight — round 1 (2026-11-01, Seldon 068a864 vs plain Codex)

Same brief, model (gpt-6.1-sol medium), machine and simulated user. Run concurrently with a 4-run farm loop (load).

| | Seldon | Plain Codex |
|---|---|---|
| Product | none (backend half-written, UI incomplete) | delivered |
| Black-box oracle | 0/7 acceptance scenarios ran | 36/40 pass; 3 fails = one CSP bug (blocked `data:,` image -> console error) |
| Wall | 2,401 s (40-min limit) | 368 s |
| Input tokens | 20.57M (20.37M cached) | 0.44M (0.41M cached) |
| Output tokens | 41k | 14k |
| Calls | 138 planner MCP / 276 MCP / 324 tool | 20 tool |
| User decisions | 3 (+5 stuck turns, 1 bypass request refused) | 0 |
| Design (CC) | n/a | ~8.5/10: calm, clear hierarchy, good phone reflow |

Blindness: not applicable — only one product existed.

## Why Seldon lost
1. Build worker tool calls stalled (likely Codex sandbox exec failure under load).
2. Recovery deadlock: `recovery-readmit-requires-VERIFIED-QUIESCENT; UNKNOWN stays held` — Seldon could not prove the stalled worker was gone and refused to readmit forever. Violates "never block delivery". Fix lane: RECOVERY-1.
3. Earlier friction: plan audit could not recognize the tests' HTTP-server subprocess pattern.

## Strategic read
At this size, Seldon costs ~50x tokens and ~6x time before counting the failure. Seldon must win on quality for larger work or get much leaner. Rerun after RECOVERY-1, with no farm load, and again after parallel waves.

# Round 2 (2026-11-01 16:31-17:11, Seldon ae8e0f1 alone, no farm load)
Seldon: no product again. A and B took plain yes (2 decisions); then the prospective test audit could not recognize the HTTP integration tests (subprocess server + urllib; prospective-no-interface-assertion x27). Review, publish and build never started; 117 planner calls, 3.56M input tokens, 40-minute limit. Round-1 deadlock did not recur. Fix lane: AUDIT-HTTP-1 (unclassifiable proof -> labelled lower evidence tier, never a block; recognize subprocess-server interface tests). Plain Codex round-1 result stands (36/40, 6 min).
