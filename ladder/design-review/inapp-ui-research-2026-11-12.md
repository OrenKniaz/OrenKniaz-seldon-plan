# In-app UI for Seldon: host capability research (2026-11-12)

Method: official docs fetched 2026-11-12. "unconfirmed" = not stated in official docs I could read (a few items rest on third-party blogs; flagged). Page dates are the docs' own dates where shown. Seldon rule of thumb: assume the LOWEST common denominator unless a row says otherwise.

## 0. MCP spec status (what the protocol offers)

| Capability | Status | Source (date) |
|---|---|---|
| Elicitation, form mode (flat object, primitives, enums; accept/decline/cancel) | In spec 2025-11-25; client must declare `elicitation` capability. Schema is flat only (no nested objects, no arrays of objects). | https://modelcontextprotocol.io/specification/2025-11-25/client/elicitation (fetched 2026-11-12) |
| Elicitation, URL mode (open a browser URL; consent shown to user) | Added 2025-11-25 ("may change"). This is the standard route to the read-only web page fallback. | same |
| 2026-07-28 spec: server-initiated requests (elicitation, sampling, roots) replaced by Multi Round-Trip Requests (server returns `input_required`, client retries with `inputResponses`). Removes `notifications/elicitation/complete`. Stateless protocol, no initialize/session. | Current spec revision. Hosts may be on either 2025-11-25 or 2026-07-28 semantics; SDK must handle both. | https://modelcontextprotocol.io/specification/2026-07-28/changelog |
| Progress notifications (`notifications/progress`) | Still in spec; request-scoped (flow only on the response stream of the tool call they belong to). Cannot reach the user after the call returns. | 2026-07-28 changelog item 4 |
| Resource subscriptions / list_changed | `resources/subscribe` replaced by `subscriptions/listen` (long-lived stream; opt-in toolsListChanged / promptsListChanged / resourcesListChanged / resourceSubscriptions) in 2026-07-28. Host must open the stream. | 2026-07-28 changelog item 4 |
| Logging, Sampling, Roots | Deprecated in 2026-07-28 (still working). Do not build on logging for UI. | 2026-07-28 changelog "Deprecated" |
| Tasks (long-running work) | Moved to official extension `io.modelcontextprotocol/tasks` (poll `tasks/get`, `tasks/update` for input). Client matrix row shows NO listed client supporting it (cells blank). | changelog item 6; https://modelcontextprotocol.io/extensions/client-matrix.md |
| MCP Apps (`io.modelcontextprotocol/ui`: tool declares `_meta.ui.resourceUri` -> `ui://` HTML resource rendered in sandboxed iframe in chat; app can call server tools, host can push fresh results; supports live-monitoring dashboards, forms, approval workflows) | Official extension, spec dated 2026-01-26. Named supporting clients: Claude (web), Claude Desktop, VS Code GitHub Copilot, Microsoft 365 Copilot, Goose, Postman, MCPJam, Archestra. NOT named: Codex, Claude Code CLI, Copilot CLI. | https://modelcontextprotocol.io/extensions/apps/overview.md (fetched 2026-11-12) |
| Client matrix (extensions) | Community-maintained; cells for most clients render blank in my fetch -> treat matrix as unconfirmed, prose lists above as the reliable source. | https://modelcontextprotocol.io/extensions/client-matrix.md |

## 1. OpenAI Codex (CLI, IDE extension, desktop app)

| Capability | Supported? | How it looks to user | Source (date) |
|---|---|---|---|
| MCP servers (stdio, Streamable HTTP), shared config across CLI/IDE/app via `config.toml` | Yes | Tools callable by agent; no per-server UI described | https://learn.chatgpt.com/docs/extend/mcp (was developers.openai.com/codex/mcp, 308 redirect; page undated) |
| MCP resources, prompts | unconfirmed (page does not mention) | - | same |
| Tool result rendering (text / markdown / images / links) | unconfirmed | - | no official statement found |
| Tool-returned image the user sees | unconfirmed | - | no official statement found |
| Progress notifications shown live | unconfirmed | - | not in docs |
| Server-initiated updates / list_changed / subscriptions | unconfirmed | - | not in docs |
| Elicitation | Probably yes in CLI, gated by approval policy; ONLY third-party blogs + mirrored commits found (Feb 2026 commit said only `codex_apps` advertised it; Apr-May 2026 blogs say form + URL modes, Guardian risk check first). Official docs silent -> unconfirmed. | Inline form in TUI (per blogs) | https://codex.danielvaughan.com/2026/05/08/codex-cli-mcp-elicitations-human-in-the-loop-structured-input/ (third party) |
| MCP Apps | unconfirmed; not on MCP's supported-client list | - | https://modelcontextprotocol.io/extensions/apps/overview.md |
| Tool approval | Yes: `default_tools_approval_mode` auto/prompt/writes/approve; per-tool override; `writes` uses readOnlyHint (CLI 0.144.0 per release note) | Approval prompt per call unless tool marked read-only | learn.chatgpt.com/docs/extend/mcp; https://releases.sh/release/rel_kveOTiuNnrKHJI-9FALB_-codex-cli-0-144-0-adds-writes-app-approval-mode-and-mcp-interactive-auth |
| Timeouts | `tool_timeout_sec` default 60 s; `startup_timeout_sec` default 10 s; both configurable; `tools.<tool>.output_token_limit` | A call longer than 60 s fails unless user raises it | learn.chatgpt.com/docs/extend/mcp |
| Slash commands / custom prompts | Exists ("IDE commands", developer-commands pages); contents unconfirmed | - | https://learn.chatgpt.com/docs/codex/ide |
| Hooks | unconfirmed (hooks page URL I tried returned 404) | - | - |
| Side panel / webview | IDE extension has a Codex sidebar (VS Code/Cursor/Windsurf), chat only; no third-party panel API described | Chat panel | https://learn.chatgpt.com/docs/codex/ide |
| Notifications, status line | unconfirmed | - | - |
| Background work | Cloud tasks exist; no MCP-specific background mechanism documented | - | learn.chatgpt.com/docs/codex/ide |

## 2. Anthropic Claude Code (CLI, desktop app Code tab, VS Code extension)

| Capability | Supported? | How it looks to user | Source (date) |
|---|---|---|---|
| MCP tools / resources / prompts | Tools yes. Resources via `@` mentions (fuzzy search). `ui://` MCP-App resources are hidden from `@` list. Prompts: list refresh documented; `/mcp__server__prompt` syntax not seen in my fetch (unconfirmed). | Tool call rows in terminal/panel | https://code.claude.com/docs/en/mcp (fetched 2026-11-12) |
| Tool result rendering | Text; large results (>25k tokens or >50k chars) are saved to a file and replaced by a path. Warning at 10k tokens. Markdown rendering of results: unconfirmed. | Terminal text | same |
| Image returned by tool | Yes for the MODEL: PNG/JPEG/GIF/WebP shown "inline in the conversation" to Claude and saved under ~/.claude/projects/.../tool-results (v2.1.283+). Whether the USER sees the image in the terminal: unconfirmed (docs say Claude sees it). | Model sees image; user view unconfirmed | same, "Images in tool results" |
| Progress notifications shown live | unconfirmed for display; docs only say progress resets the 5-min (HTTP) / 30-min (stdio) idle timeout and that `/tasks` shows "the latest progress the server has reported" for backgrounded calls. A third-party tutorial claims Claude Code does not even send a progressToken (unverified). | `/tasks` entry text for background calls | same; https://www.bitovi.com/academy/learn-intro-to-mcp-servers/streaming-progress.html (third party) |
| list_changed | Yes: interactive session refetches tools/prompts/resources; `-p` mode refreshes tools only | Silent refresh | same |
| Elicitation | Yes, form + URL (declares `elicitation:{form,url}` on current connections; bare `{}` = form only on claude.ai connectors). Dialog appears automatically in terminal; cloud sessions show a card (Submit / Open link / Decline). Not available in non-interactive `-p` (auto-cancelled). `Elicitation` / `ElicitationResult` hooks can auto-answer. | Interactive dialog in terminal; card in Desktop Code tab / claude.ai | same, "Respond to MCP elicitation requests" |
| Server-initiated push into session | Yes, "Channels": server declares `claude/channel`, user starts with `--channels`; research preview; Anthropic allowlist only unless `--dangerously-load-development-channels`; needs claude.ai/Console auth (not Bedrock/Vertex/Foundry); Team/Enterprise need admin enable. Cannot register if server negotiates MCP 2026-07-28 (use `MCP_PROTOCOL_NEGOTIATION=legacy`). Push lands as a message the MODEL reacts to; terminal shows an inbound line. | `<- source: text` line in terminal; model then acts | https://code.claude.com/docs/en/channels ; https://code.claude.com/docs/en/mcp (push messages) |
| Long-running tool calls | Wall-clock default ~28 h; per-server `timeout` in .mcp.json; idle timeout 5/30 min unless progress. A call still running after 2 min auto-moves to a background task (`CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS`); Claude gets a task id; result arrives as task notification; appears in `/tasks`, user can stop with `x`; does not survive session exit. | `/tasks` list | https://code.claude.com/docs/en/mcp |
| Hooks | Yes: ~30 events incl. Elicitation, ElicitationResult, Notification, Stop, UserPromptSubmit, PostToolUse; `additionalContext` injection (10k chars); async + asyncRewake (wakes Claude on exit 2); MCP tool matchers `mcp__server__tool`. | Invisible to user except injected context | https://code.claude.com/docs/en/hooks |
| Status line | Yes: any shell script, gets JSON on stdin, prints persistent row at bottom of the terminal UI. Can show external data from a script (e.g. read Seldon state file). Refresh cadence unconfirmed. | One-to-few-line text bar | https://code.claude.com/docs/en/statusline |
| Slash commands / skills / plugins | Yes (plugins bundle MCP servers, skills, hooks, commands). Plugin "mods" can DRAW in the VS Code panel (v2.1.299+) - mechanism undocumented in my fetch -> unconfirmed for Seldon use. | Panel content labelled "From the X plugin" | https://code.claude.com/docs/en/vs-code ; https://code.claude.com/docs/en/plugins |
| VS Code extension | Chat panel (sidebar/editor tab), `/mcp` dialog, `/tasks`; tab dot = pending permission request; no OS notifications described. MCP elicitation / MCP Apps rendering in the extension: unconfirmed. | Graphical chat | https://code.claude.com/docs/en/vs-code |
| MCP Apps | Claude (web) and Claude Desktop listed as supporting; Claude Code CLI: NOT listed (and docs say UI resources are hidden from the model/list) -> unsupported/unconfirmed in Claude Code | - | modelcontextprotocol.io/extensions/apps/overview.md ; code.claude.com/docs/en/mcp |

## 3. GitHub Copilot in VS Code (agent mode)

| Capability | Supported? | How it looks to user | Source (date) |
|---|---|---|---|
| MCP tools | Yes, under session tool availability + approval policy (readOnlyHint must NOT be assumed to bypass approval) | Approval prompts per tool | https://code.visualstudio.com/api/extension-guides/ai/mcp (dated 11/11/2026) |
| Resources | Only readable for MCP Apps; native servers' resources do not appear in the resource browser | none | same |
| Prompts | `/mcp.<server>.<prompt>` flow NOT exposed in Copilot sessions (docs recommend agent-plugin skills) | none | same |
| Elicitation | Yes: form + URL, during an active turn; cancelled in Autopilot; declined when no turn is active | Form in chat | same |
| MCP Apps | Yes, EXPERIMENTAL (`chat.mcp.apps.enabled`; "might change or be removed"); VS Code: inline display only, no camera/mic/geolocation. Shows forms/visualizations next to tool result; resources readable for Apps. | Interactive iframe panel beside the tool result in chat | https://code.visualstudio.com/docs/copilot/customization/mcp-servers (dated 11/11/2026); https://code.visualstudio.com/docs/agents/reference/mcp-configuration |
| Tool result rendering (images/markdown) | unconfirmed in official docs (a Copilot Chat changelog mirror mentions structured content like images/resources in results) | - | no official page confirmed |
| Progress notifications | unconfirmed (docs silent; third-party says progressToken sent, display not shown) | - | - |
| list_changed / subscriptions | unconfirmed ("tool-list refresh varies by client") | - | same MCP page |
| Sampling | Supported (deprecated in MCP), per-server approval | Approval dialog | same |
| Extension webview / side panel | VS Code has full webview API for extensions (general VS Code capability; not verified in this session) - a Seldon VS Code extension could host a panel, but only for VS Code, not the CLI | Own panel / sidebar | not fetched; common VS Code knowledge -> unconfirmed here |
| Timeouts | unconfirmed | - | - |
| Hooks / status line / notifications | unconfirmed | - | - |

## 4. GitHub Copilot CLI

| Capability | Supported? | How it looks to user | Source (date) |
|---|---|---|---|
| MCP servers: stdio, Streamable HTTP, SSE (deprecated); per-server tool filter; config `~/.copilot/mcp-config.json`, project `.mcp.json` / `.github/mcp.json`; folder-trust gate; `--timeout MS` per server | Yes | Terminal | https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-mcp-servers (page undated) |
| Resources / prompts / images / progress | unconfirmed (not on page) | - | same |
| Elicitation | Probably yes in recent versions (release notes mention elicitation prompts dismissible with Ctrl+C); an Apr 2026 third-party write-up said "No in CLI". Conflicting, third-party -> unconfirmed. | TUI prompt | https://microsoft.github.io/entrabot/claude-copilot-cli-channel-port/ ; releasebot mirror |
| MCP 2026-07-28 support | Mirror of v1.0.81 release says yes; unconfirmed from official page | - | https://newreleases.io/project/github/github/copilot-cli/release/v1.0.81 |
| MCP Apps | Not in supported list -> assume NO | - | modelcontextprotocol.io/extensions/apps/overview.md |
| Hooks, status line, plugins, notifications | unconfirmed | - | - |

## 5. What this means, per need

1. STATE (what is running / waiting and why). Universal route: an MCP tool `seldon_status` returning compact markdown text. Works in all four hosts (text is the common denominator). Anything better needs a per-host surface: Claude Code status line (script reads a Seldon state file, passive), Copilot-in-VS-Code MCP App (rich, experimental), Claude Desktop MCP App. Codex and Copilot CLI: text only.
2. PROGRESS (live while running, or unprompted later). Weakest area everywhere. No host documents live display of `notifications/progress`; spec says progress is tied to a single in-flight call. Only Claude Code documents anything usable: background MCP tasks (`/tasks`, after 2 min) and Channels (push into a running session, research-preview, allowlist-gated). Design rule: Seldon runs are DETACHED daemon jobs; tools are short (start/status/stop, return in under 60 s, the Codex default). Never hold a tool call open for a run.
3. GATE QUESTIONS (approve vision A / plan B / demo C; approve/revise/decline). Use `elicitation` (form: enum action + free-text note) as the first choice: documented and automatic in Claude Code (CLI dialog; cloud card), documented in Copilot for VS Code (form+URL), probably in Codex CLI and Copilot CLI (unconfirmed officially). Elicitation is request-scoped (needs an active tool call/turn; VS Code declines it when no turn is active), so the gate must be raised from inside a tool the agent calls (`seldon_gate`), not from a background daemon. The three-action model maps well: accept+content = approve/revise, decline = decline, cancel = ask later. Universal fallback: the agent asks in chat and calls `seldon_answer_gate(id, choice, note)` with the reply; also keep the gate persistently pending in Seldon so a missed card is not lost. Under 2026-07-28 this becomes `input_required` + retry; SDK upgrade is required, design the tool so a retry is idempotent.
4. EVIDENCE / SCREENSHOTS. Tools can return image content. Claude Code: the model definitely sees it; user-visible rendering unconfirmed. Copilot VS Code: possible via MCP App (experimental) or structured content (unconfirmed). Codex, Copilot CLI: unconfirmed. Robust plan: always return text summary + absolute file path + `file://` or local-web-page URL; add image content as a bonus; use MCP App (VS Code Copilot, Claude Desktop) where available. Large check outputs: Claude Code spills >50k chars to a file, so keep results short and link to files.
5. PAUSE / RESUME / STOP. Plain tools (`seldon_pause`, `seldon_resume`, `seldon_stop`) work in all hosts, subject to each host's approval prompt (Codex `approval_mode`, Copilot approval; set tool annotations honestly: pause/resume/stop are non-read-only so they WILL prompt, which is acceptable). Claude Code adds `/tasks` + `x` to kill a backgrounded call, but this kills only the call, not the daemon. No host offers a persistent button without MCP Apps or a custom extension.

Bottom line by host: Claude Code CLI/desktop = best for gate questions and unprompted updates (elicitation + channels + status line + hooks + background tasks) but no rich UI; Copilot in VS Code = only host with a documented rich in-chat UI (MCP Apps, experimental) plus elicitation; Codex = least documented, tool + text only until proven otherwise; Copilot CLI = text + maybe elicitation. The read-only web page stays necessary for: persistent live dashboard, screenshots in Codex/Copilot CLI, anything not fitting a flat form.

## 6. Biggest blockers (hard limits)

1. No documented live progress/unprompted updates in Codex, Copilot (any), and only research-preview Channels (allowlisted, `--channels`, auth-gated, incompatible with 2026-07-28 negotiation) in Claude Code. A true "run dashboard that updates itself" is not possible in-app on most hosts; use status line (Claude Code), MCP App (Copilot VS Code / Claude Desktop), or the web fallback.
2. Elicitation is request-scoped and not officially documented for Codex or Copilot CLI; VS Code declines it when no turn is active, Claude Code cancels it in `-p` mode, and VS Code Autopilot cancels it. Gates must be raised from inside an active agent turn, with chat + `answer_gate` tool as fallback.
3. Image/screenshot display to the USER is unconfirmed everywhere except via experimental MCP Apps (Copilot VS Code, Claude Desktop); MCP Apps are absent for Codex, Claude Code CLI, Copilot CLI. Also Codex tool timeout is 60 s default, so tools must return fast.

Secondary: spec churn (2025-11-25 vs 2026-07-28 stateless/MRTR; tasks extension has no listed client); Copilot VS Code doesn't expose MCP prompts or resource browsing; Claude Code VS Code extension elicitation/MCP-App rendering unconfirmed.
