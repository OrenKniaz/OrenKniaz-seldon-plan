CHARTER: serves C1/C8–C20/C23–C26 — violates no I#; read-only recommendations preserve all core obligations.

At `97eb786137311bbe71c45850decb28c763063403`, **production core totals 35,055 nonblank lines: 34,663 Python + 392 JS/CJS/HTML/CSS**. Comments/docstrings count; tests, docs and runtime artifacts do not. File stems below mean `src/codex_harness/core/*.py`. Shared files are identified explicitly; category figures must not be added blindly.

**We built our own mailbox, task graph/readiness, memory database/promotion system, MCP protocol handling, approval workflow and extensive execution/proof orchestration. The dedicated cockpit is small.**

TRIAGE: DESIGN — commodity services and Seldon policy share owners, making deletion difficult; sibling cases: dispatch mixes scheduling/mail/memory/proof, MCP mixes protocol/domain routing/confirmation, and memory mixes retrieval/storage protection/promotion. Reset should separate those responsibilities by deleting replacements, not adding another coordinating layer.

1. **Agent mail / inter-agent messaging**
   Files: [`mail.py`](~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/mail.py) **185 LOC**; additional tool declarations/handlers in `mcp_planner` and notifications in `dispatch`—shared totals below.
   Built: SQLite inboxes, threads, send/reply/ack, event deduplication, envelope checks and secret-pattern filtering. C19 needs structured, trace-linked blocker/question/discovery/handoff messages; mailbox infrastructure is commodity.
   **ADOPT [MCP Agent Mail](https://github.com/Dicklesworthstone/mcp_agent_mail_rust) + ~100–180 LOC adapter**, retaining run/bead/trace references and idempotent event mapping. The maintained Rust version documents Windows binaries; the original Python repository is deprecated. **Stage 3c.**
   The local kind list lacks explicit discovery/handoff kinds; arbitrary `refs` are not equivalent to validated trace linkage. Vendor adoption must finish that integration.

2. **Beads / task graph / claims**
   Files: `graph` **318**, `dispatch` **2,663**, `planner_jobs` **413**, `worker_packet` **862** = **4,256 LOC of mixed execution ownership**. Shared planning/trace: `spine` **685**, `plan_store` **3,307**, `waves` **865**, `wave_refine` **702**.
   Built: bead records, dependencies, topological ordering/readiness, file ownership, execution state, scheduling and proof claims. C12 needs concurrency/contracts/ownership; C9/C10 need Seldon’s richer trace.
   **ADOPT [Beads](https://github.com/gastownhall/beads) + ~250–450 LOC adapter** for execution issues, dependencies, readiness and atomic task claims. Keep approved plan/trace references in Seldon; avoid two independently mutable task authorities. **Stages 1a/3a/3d.**
   Crucial distinction: [`dispatch._claim`](~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/dispatch.py:476) binds validation to candidate/input identities. That is **proof provenance**, not a Beads ownership claim; retain it under C15/C26. Beads does not replace integration, capacity control or semantic acceptance.

3. **Memory / lessons / promotion / retrieval**
   Files: [`project_memory`](~/codex-harness/work/sprint-20261027/semantic-cc/src/codex_harness/core/project_memory.py) **624** + `memory_promotion` **160** = **784 LOC**, plus shared dispatch/packet call sites.
   Built: append-only SQLite/FTS5 storage, supersession, confirmation, provenance, search, prompt slicing, lesson promotion and substantial Windows file-pinning machinery. SQLite supplies search; we wrote its surrounding lifecycle.
   C19 requires sourced project knowledge, cross-project lessons and decision citations. Current dispatch uses a **run-local `memory-workspace`**; I found no cross-project retrieval path. Prompt projection retains text but omits structured item provenance.
   TRIAGE: DESIGN — `project_memory.py:101` emits `confirmed_constraints_follow_them`, conflicting with advisory-only C19; sibling consumers are both dispatch packet paths. Fix one projection to supply cited advice subordinate to the accepted trace.
   **KEEP ours but shrink to ~300–450 LOC**, covering shared sourced records, retrieval, promotion and small settings. Use provider-native memory for personal context; [Claude Code memory](https://code.claude.com/docs/en/memory) exists, but an interchangeable cross-provider store satisfying all C19 citation requirements is **unsure**. **Stage 3c**, including the missing cross-project path.

4. **Cockpit / UI / operator views**
   Files: `status_api` **142**, `status_server` **58**, `cockpit.js` **114**, `cockpit.html` **50**, `cockpit.css` **41** = **405 LOC**. Related projections: `planner_views` **1,535**, `planner_audit_views` **91**, `supervision` **592**, `spine_render` **180**, `spine_diagrams` **178** = **2,576 LOC**.
   Built: GET-only localhost status, periodic refresh, raw record details, chat cards, Markdown/Mermaid and supervision reports. C20/C25/C26 need readable trace/progress/evidence and worker inspection.
   **KEEP the cockpit; target ~350–500 LOC, and shrink related projections to ~500–800 LOC.** Use one canonical status projection. Keep chat and interaction in provider apps; [Claude Code desktop](https://code.claude.com/docs/en/desktop) supplies an existing provider UI, but does not replace Seldon’s cross-provider trace. **Stages 2c/2e/4b.**
   `semantic_web.cjs` is a proof runner, **not cockpit/frontend code**. No separate production React/Tauri frontend appeared in this checkout. Source inspection establishes read-only design, not UX quality or live usability.

5. **Other build-versus-buy surfaces**
   
   | Surface and current nonblank LOC | Recommendation and reset stage |
   |---|---|
   | **Worktrees/scheduling:** shared `dispatch` 2,663; `graph` 318; `waves` 865; `wave_refine` 702 | Already invokes [Git worktree](https://git-scm.com/docs/git-worktree); Git itself was not reimplemented. **KEEP ~600–900 LOC scheduling/wave policy**, plus integration below. Beads supplies readiness; Seldon must own elastic capacity, waiting reasons and wave continuation. **3a/3b/3d**. |
   | **Protocol/CLI:** `mcp_planner` 2,806; `planner_stdio` 77; `planner_connection` 118; `plan_cli` 1,366 = **4,367** | Handwritten JSON-RPC negotiation, framing, cancellation and tool routing. **ADOPT official [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk); keep ~1,000–1,500 LOC domain-facing adapters/CLI.** Preserve workspace/revision binding and pending confirmation semantics. **2c/4b**. |
   | **Approval workflow:** `approvals` 258; `approval_migration` 283; `planner_confirmations` 249; `planner_consent_views` 128; `planner_confirmation_cards` 16; `planner_execution` 135 = **1,069**, plus shared MCP handling | These are mostly Seldon decisions, not cloned provider permissions. **KEEP ~400–600 LOC** for revision-bound A/B/check-in/C and execution consent; provider UI renders interactions. Delete obsolete budget subjects/legacy branches after migration. **1b/2b/2c/4b**. |
   | **Provider setup:** `provider_launch` 254; `project_init` 429; `init_hosts/*.py` 284; `preflight` 129; `reviewer_access` 38 = **1,134** | Already wraps installed CLIs. **KEEP ~600–850 LOC** launch/setup/readiness adapters; providers own sandbox, permissions and chat. No replacement host framework. **4b**. |
   | **Process/recovery:** `audit_process` 418; `attempt_control` 134; `attempt_provenance` 267; `workspace_admission` 146; `planner_recovery` 273; `acceptance_recovery` 591; `planner_resume` 324 = **2,153**, plus dispatch integration | **KEEP ~2,000–3,000 LOC including integration** for bounded cancellation, candidate provenance, quarantine/restart and serial Git integration. Provider launch alone does not establish C18/C23/C25. Complete vendor substitute: **unsure**. **2d/3a/3d**. |
   | **Proof DSL/review:** `runners` 1,106; `semantic_runner` 483; `semantic_schema` 465; `semantic_web.cjs` 187; `test_audit` 433; `proof_imports` 122 = **2,796**; `roundtable` 1,973; `acceptance` 1,813; `readiness` 375 | **ADOPT ordinary worker-authored test commands and [Playwright](https://playwright.dev/docs/intro)** instead of a proprietary scenario language. **KEEP ~2,500–3,500 LOC** of observed RED/GREEN, typed semantic judgment, plan review and integrated acceptance. Those meanings remain ours. **1c/2a/2e/4a**. |
   | **Budgets/metrics:** `provider_call_budget` 294; `efficiency` 368; `worker_packet_budget` 23 = **685** | **DELETE product quotas and move development metrics outside runtime** under C8/§6. First retain launch binding and permission-denial observations in their existing owners; `efficiency` contains both metrics and denial parsing. Keep ~100–200 LOC necessary adapter/context-limit logic. **2b/4b**. |

**Realistic target: 14,000–18,000 nonblank production LOC**, approximately half today’s core—not a measured implementation commitment.
A ~16k allocation: plan/trace/decisions **5k**; loop/waves/scheduling **2k**; judge/review/proof **3k**; integration/recovery **3k**; provider/MCP/Beads/mail/memory adapters **2k**; read-only views **1k**. Estimates include replacements and exclude upstream vendor code.

**Three biggest simplification wins, in order:**

1. **One execution model and deterministic loop:** delete legacy/semantic branches, planner transition choreography and repeated CLI/MCP routing—**2c/3d**.
2. **Ordinary tests plus one semantic judgment path:** remove scenario interpreters, heuristic meaningfulness grading and redundant review/acceptance machinery—**1c/2a/2e/4a**.
3. **Vendor-owned coordination with small integrations:** Beads + Agent Mail; shrink sourced memory and shared projections—**3a/3c/4b**. Mail and the dedicated cockpit together are only **590 LOC**.

Stage mappings follow [ASTRA-RESET-1](~/codex-harness/work/ladder/design-review/astra-reset-1.md) and [RESET-2](~/codex-harness/work/ladder/design-review/astra-reset-2.md); no new stage is necessary. Vendor existence is verified; composed Windows recovery/integration is unproven. Next acceptance check: canonical approved plan → vendor issue/mail → overlapping workers → integrated evidence → restart with cited memory. **No files changed, tests run or providers launched; no product-acceptance claim.**