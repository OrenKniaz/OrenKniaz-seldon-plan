CHARTER: serves C1/C2/C8/C11/C14/C18/C23/C26 — violates no I#.
TRIAGE: DESIGN — repeated whole journeys and shared proof compete with a necessary long-stream regression — siblings: CLI, HTTP, ShelfLife and authority cases.

Read-only Sol HIGH audit of clean candidate `8c104c66d93c09bd181b67451f7a759aadb966c3`. No edits, tests or provider launches. Retained capability audit reviewed; findings below establish automated coverage, not real-provider acceptance.

**1. Coverage and measured wall time**

The suite contains **19 cases: two golden surfaces, 15 authority cases and two structural guards**. Most bundled journeys have **no individual timing**.
`G` = [test_golden_path.py](~/codex-harness/work/sprint-20261027/semantic-cc/tests/python/core/test_golden_path.py); `A` = [acceptance_support.py](~/codex-harness/work/sprint-20261027/semantic-cc/tests/python/core/acceptance_support.py); `P` = [test_approval_v2_journey.py](~/codex-harness/work/sprint-20261027/semantic-cc/tests/python/core/test_approval_v2_journey.py). `U` means unmeasured separately.

| Retained log | HTTP | ShelfLife | Full CLI phase | Isolated web |
|---|---:|---:|---:|---:|
| [host-main-recov1](~/codex-harness/work/sprint-20261027/golden-host-main-recov1.log:5) | 274.16s | 548.95s | **716.05s, passed** | 211.44s |
| [host-main-recov1b](~/codex-harness/work/sprint-20261027/golden-host-main-recov1b.log:273) | 259.20s | **600s timeout** | **871.71s, teardown error** | 277.84s |
| [publish-fix17b](~/codex-harness/work/sprint-20261027/golden-publish-fix17b.log:7) | 213.16s | 516.05s | **598.89s, passed** | 182.62s |
| [publish-sweep1b](~/codex-harness/work/sprint-20261027/golden-publish-sweep1b.log:7) | 219.56s | 443.36s | **531.36s, failed** | 202.73s |

These logs represent different historical candidates. HTTP and ShelfLife already overlap with CLI; their durations cannot be added. The shell subsequently adds web. The internal `golden cli` timer also excludes later interruption/wake/cockpit/cold-start work and fixture teardown.

| Journey / reference | Protected behavior → realistic regression caught | Time | Overlap |
|---|---|---:|---|
| Main CLI, G4846 | Actual words→review→B→observed RED/GREEN→ZIP/delivery→C; exited worker survives judgment/reconnect → duplicate execution, stale credit or wrong delivered bytes | Bundled | Ordinary path repeated in all P cases; fault/recovery details remain unique |
| Fixture ownership, G1362 | CSV→SQLite→served readback, isolated fixtures, cleanup/junction refusal → preview mutates source or consumes wrong data | U | ShelfLife persistence overlaps; fixture ownership does not |
| Planning intent, G1109 | Size override, brownfield facts, expansion, ambiguous consent/narrowing, truncated output → accepted intent silently changes | U | P clarification/frozen setup; distinct semantic-context cases |
| Execution judgment, G1620 | Worker-written verifier and wrong-reason RED rejection→correct RED/GREEN → broken test receives proof credit | U | Main CLI wrong-reason repair; packet/baseline/freshness cases unique |
| Judgment contract, G1885 | Durable pending/verdict, stale candidate/evidence rejection, bounded corrections → old judgment grants credit | U | Automatic retries and real approval/review consumers |
| Trace contract, G2084 | Full/collapsed trace reload, exact downstream staleness and provenance → unrelated branches stale or deleted coverage accepted | U | No equivalent complete trace case |
| Planning surface, G2656 | Public schema, atomic malformed-input rejection, Unicode/transport survival → partial mutation or broken wire | U | Retry shape checks overlap |
| Reviewer order, G2822 | Previous-version producer migration, frozen setup, concurrent writer wins → obsolete question overwrites current truth | U | P frozen-kickoff overlaps setup only |
| Approval order, G3046 | Displayed A→usable public contract→reconnect→same actual-word decision → schema teaching loses approval | U | P reconnect-a; teaching failure differs |
| Automatic retries, G3257 | Two exact fixes, retained-output recovery, exhaustion and late-output quarantine → third retry or stale return advances | U | Judgment/review malformed cases; scheduling/crash seams unique |
| Receipt gaps, G3567 | Interrupted review/acceptance receipts reused; pending disposition holds C → paid work repeats or premature acceptance | U | Shared acceptance receipt checks in both HTTP variants |
| Single build, G3997 | Dependency-free worker creates verifier/product, fallback observed RED→GREEN→C → separate Contracts bead hides missing baseline/test inputs | U | Main CLI uses two beads; not equivalent |
| Recovery twins #1/#2, G4394 | Pause/restart/stop, actual 8s writer contention, packet failure after first/second readmission, exhaustion and unknown launch → retries reset or work escapes stop | U; **16s deliberate contention total** | Repeated setup; distinct failure interleavings |
| Denial / dead review, G4655/G4717 | Durable denial prevents readmission; dead review releases ownership without invented quiescence → denied work reruns or reservation survives forever | U | Happy reconnect cannot prove either |
| Cold start, G962 | Declared wheel→fresh installation→six launchers/modules/MCP/init/check/remove → missing package files or cold import cycle | Historical segment **11.05s**; current U | Source journeys cannot replace it |
| Web, G2445/G4874 | Real browser/API/disk flow, redirect/error/body attribution, prerequisites/screenshots, standalone teardown, unavailable-browser pending state → false UI proof or orphan server | **183–278s total** | HTTP overlaps successful API readback only |
| Cockpit, G3151 | Canonical accepted producer→HTTP→browser, unchanged store → divergent/stale view or viewing mutates truth | Included above | CLI and web repeat HTTP parity; web uniquely proves rendered view |

ShelfLife and ordinary HTTP contain these additional, distinguishable groups:

| Cases / reference | Protected behavior → realistic regression caught | Time / overlap |
|---|---|---|
| Shelf compiler/scenario failures, A699–766 | Missing/multiple/reversed builds refused; missing requirement and unknown intent remain unvalidated → invented coverage/actions | U; unique |
| Shelf importer, A561/A814/A1473 | Mixed-validity/optional/unreadable CSV→SQLite→two server incarnations → data lost or accepted incorrectly after restart | U; HTTP/fixture journey only partially overlaps |
| Shelf review findings, A1236–1736 | Malformed review exhausts correctly; opposing/negative/inconclusive members, partial closure, stale closure, replaced dossiers and shards retain obligations → positive aggregate hides unresolved gap | U; generic retry overlaps, member/shard integration unique |
| Shelf reuse/scope, A1737–1824 | Same-ID change requires judgment; inconclusive blocks; legitimate HOW reuse retains fresh convergence → stale review authorizes changed scope | U; P scope cases partially overlap |
| Shelf stream/recovery, A1877–2011 | Output activity, CPU activity, partial terminal bytes and >120s silence survive; truncated exit quarantines; missing verifier repairs through fresh namespace → premature kill/completion or repeated broken attempt | **≥131s stream floor**; unique dispatch sequence |
| Shelf retained validation/delivery, A2258–2626 | Verifier refresh/rename, protected expanded root, changed candidate/dependency refusal, reconciliation without worker replay, exact delivery ownership → exemptions or stale proof certify changed bytes | U; CLI delivery attacks overlap only some refusal outcomes |
| Shelf WHAT/HOW, A3281–3382 | Design/internal change versus third-party/story scope change routes to correct B behavior → accepted obligations narrow silently | U; classification is scripted; binding/routing is proved |
| HTTP audit/concurrency, A1149–1235/A1493/A1835–2257 | Prospective audit and refinement; parallel A/B, independent recovery allowance, sibling timeout/cancel and descendant cleanup → global retry/deadline kills healthy sibling | **213–274s whole HTTP**; unique |
| Shared HTTP/Shelf proof, A1643/A2628–3082 | Review replacement race; acceptance malformed/session/receipt retries; migration requires fresh disposition/C and template drift invalidates credit → old approval/review revives | U; **same helper/chains run in both variants**; retain each behavior once |

Each authority case has a unique perturbation; **all 15 also repeat the ordinary full path and terminal reconnect**:

| P case(s) | Unique protected outcome → missed regression | Time / overlap |
|---|---|---|
| clarification | Exact answer persists and authoring resumes → clarification disappears | U; planning-intent partial overlap |
| frozen-kickoff | Edited setup cannot retarget calls; scope change renews B → new provider/model gains authority | U; reviewer-order partial overlap |
| decline-a / decline-b | Each gate pauses without dispatch until explicit resume → refusal treated as consent | U; separate gate boundaries |
| change-a / change-b | Each gate returns to planning without approval → requested change starts work | U; separate gate boundaries |
| stale-a | Old A rejected; same-ID WHAT change invalidates pending B → binding checks IDs only | U; frozen/delivery scope overlap |
| reconnect-a | Durable request/fresh wire, stale response ignored, paused late response rejected → old elicitation grants consent | U; native path unique |
| reconnect-b | HOW amendment plus transport death preserves original B words → lost words or silent reapproval | U; frozen setup differs |
| replay-a / replay-b | Replayed answer creates no second approval → duplicate credit | U; separate gate boundaries |
| missing-b | Retired mutation commands cannot start workers → alternate ingress bypasses B | U; surface inventory partial overlap |
| reconnect-c | Pending C survives replacement transport → missing/duplicate final decision | U; common DONE reconnect occurs later |
| refused-c | Changed delivery refuses C; changes-requested returns to planning → C ignores revision or user rejection | U; delivery overlaps bytes, not changes-requested |
| delivery | Fresh B retires inconclusive hold; missing/changed root/source refuses C; post-C change revokes acceptance → retained repository certifies wrong delivered product | U; main ZIP proof differs |

Structural guards protect suite policy and source-size ratchets, respectively; they are not product proof. Their separate runtimes are absent.

**2. Assertions that can pass while the claimed feature is broken**

| File:line | Weakness | Outcome replacement |
|---|---|---|
| [test_golden_path.py:2622](~/codex-harness/work/sprint-20261027/semantic-cc/tests/python/core/test_golden_path.py:2622) | Empty screenshot artifacts bypass every hash/375px check | Require the requested screenshot artifact set, then valid nonempty PNGs, dimensions and hashes |
| [test_golden_path.py:4356](~/codex-harness/work/sprint-20261027/semantic-cc/tests/python/core/test_golden_path.py:4356) | Expected tier uses production `review_tier`; broken classifier agrees with itself | Fixture-declared literal tier in subject and displayed card |
| [test_golden_path.py:1971](~/codex-harness/work/sprint-20261027/semantic-cc/tests/python/core/test_golden_path.py:1971) | Eight generated examples round-trip generated meaning; consumer semantics may be disconnected | Exercise each distinct schema through its actual consumer: approval withheld/granted, publication held/released, size applied, stale authority rejected; retain generic durability once |
| [test_suite_budget.py:37](~/codex-harness/work/sprint-20261027/semantic-cc/tests/python/test_suite_budget.py:37) | Raising editable `CEILINGS["suite"]` makes the guard accept its own increase | Enforce current ceiling ≤ committed baseline, using existing module-ratchet precedent |

Fixture-supplied HOW/WHAT, verdicts and fabricated native telemetry prove consumption/binding, not semantic intelligence or actual provider execution. Repeated `accepted`, `linkedRed`, terminal-file-count and RED-negative assertions add negligible coverage or runtime value.

**3. Where time goes**

- **Known ShelfLife floor: ≥131s**, G834–876: 3s output activity + 3s CPU activity + **125s real partial-JSON silence**. Shortening it loses the former 120s idle-kill regression.
- ShelfLife executes **9 explicit roundtables / 19 synthetic review returns**: initial malformed/conflicting/positive rounds, three replacement-race rounds, three verifier-refresh rounds. These returns are synchronous doubles, **not 19 provider subprocesses**.
- Additional explicit work: **8 readiness returns**, **12 acceptance-review returns**, three execution starts and five revalidation requests. Only **two** refreshes perform fresh semantic validation; rejected product changes and delivery retries do not represent five full reruns.
- HTTP servers, importer/verifier children, controller/monitor startups and repeated canonical projections are real costs, but logs do not separate their seconds. Server restart and descendant cleanup are protected outcomes.
- One-second execution observation, short marker polls and bounded joins are mostly conditional waits. A 600s sleeper is a cancellable fault payload, not evidence of 600s spent. Reducing poll intervals can increase store contention.
- **Exactly one wheel build/venv/install exists**, G999–1011, outside ShelfLife. Cross-journey wheel/venv reuse currently saves **0 duplicated builds**.
- Retained profiling reported 15.33s duplicate projection within 29.74s execution-scope work; the capability audit says this was already fixed. It cannot be credited again.

**4. Concrete speed plan — preserve every unique outcome**

Savings below distinguish known relocation from **unmeasured planning estimates**; aggregate logs cannot establish a guaranteed ≤300s result.

| Priority / change | Seconds saved | Coverage risk and required preservation | Files |
|---|---|---|---|
| 1. Move the long stream perturbation into an existing authority/delivery flow with the existing 180s worker deadline; schedule it early on another gate worker | **≥131s off ShelfLife**; CLI saving depends on overlap | Preserve real elapsed silence, raw partial bytes, activity observations, terminal/cleanup receipts and eventual C. Ordinary HTTP’s **15s** deadline makes it unsuitable; do not raise it | G provider host; P delivery; existing collection scheduling |
| 2. Run shared replacement race, acceptance malformed/session/receipt chain and general migration/fresh-C proof once across HTTP/Shelf | Shelf planning estimate **30–90s**, unmeasured | Keep Shelf-specific candidate/dependency checks; retain both distinct legacy migration inputs and real canonical producers. Do not delete either whole HTTP journey | A1643/A2628–3082; G53 |
| 3. Combine compatible authority perturbations at successive A/B/C points; retain separate native/frozen-setup contexts | CLI planning estimate **40–120s**, unmeasured | Preserve every row above, immediate negative outcome and successful recovery. Share live canonical progress; do not clone bound stores or fabricate approved checkpoints | P; mcp_planner_support.py |
| 4. Use existing legitimate review reuse during verifier refresh where unchanged obligations qualify | Shelf planning estimate **5–25s**, unmeasured | Preserve independent verdicts, exact delta judgment and fresh convergence; no injected successful-review state | A2274; existing review consumers |
| 5. Share immutable fixture inputs/provider executable preparation; retain mutable workspaces and isolated cold imports | **0–5s** estimated; wheel reuse **0s** currently | No shared mutable PlanStore, ports, candidate data or acceptance state; one real fresh wheel installation remains | G; mcp_planner_support.py |
| 6. Remove repeated assertions after stronger consumer coverage exists | **<1s** expected | Retain all unique assertions and failure branches; this is clarity work, not the speed solution | G; A |

Moving 131s leaves ShelfLife at approximately **312–418s** on observed runs: consolidation must remove another **12–118s**. Budget ShelfLife to **≤300s** and the remaining CLI critical path to **≤300s**, exploiting existing overlap without adding worker trees. Estimates overlap and must not be summed as measured savings.
First instrument named phases in existing console output; then validate the coherent candidate against original coverage and unchanged caps. No new unit tests, synthetic success fixtures or unrequested evidence files. Neither target is proven by this audit.

**5. Sequence after Stage 2e**

[Stage 2e’s plan](~/codex-harness/work/lanes/stage-2e-plan.md) moves semantic replies to provider-boundary stubs, replaces structured chat answers with `harness_chat(text, reply_to?)`, allocates IDs in CODE and binds fresh per-question context/setup. It rewrites LoopClient, review/order, authoring, retries, receipt recovery and both HTTP fixtures—the same surfaces the speed lane would touch.
Land 2e first; remap this inventory to its actual consumers, measure its new baseline, then consolidate. Preserve Codex/Claude/Copilot decoding, two-fix exhaustion, native permission/control, stale-return rejection, graph repair and packet sufficiency. Existing public-answer/schema-teaching assertions need migrated outcomes, not mechanical retention.
**Last proven outcome:** historical full CLI GREEN at 598.89s; later recovery candidate GREEN at 716.05s and loaded run timed out. **Next unproven step:** post-2e, coverage-preserving consolidation meeting ShelfLife ≤300s and full CLI ≤600s. **Blocker:** missing internal timings prevent defensible attribution of the remaining 12–118s; add those timings before claiming savings.