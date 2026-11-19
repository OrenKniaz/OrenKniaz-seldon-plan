CHARTER: serves C1–C6, C8–C19, C23–C26 — violates no I# in this read-only audit.

TRIAGE: DESIGN — the loop repeatedly asks models to reconstruct facts and ownership that code already knows. Sibling failures: premature guide judgment in 03, unavailable verification in 04, disputed RED in 09, and missing evidence linkage in 12.

**Decision: keep the thin core, but fix its ownership boundaries before adding more prompt patches.** Its foundations are useful. Its present execution model is a whole-product serial pipeline with several global semantic vetoes; it is not yet a sound basis for a much larger application.

Audited HEAD `d4cb94c`, all `src/seldon`, the journey, requested design documents, history, and retained run reports/calls. No edits, tests, or provider launches. Run 12 was active; its evidence below is bounded to **2026-11-09 21:40 UTC**.

The last completed success is run 11’s retained browser verification and **SCRIPTED_C**, not owner acceptance. Runs 01–11 contain five scripted completions and six incomplete outcomes across changing implementations. That is useful diagnosis, not a measured reliability rate. [RUNS.md](~/codex-harness/work/ladder/RUNS.md)

**1. Landed fixes: rules versus patches**

| Commit/change | Judgment | Design that removes the recurring patch |
|---|---|---|
| `f6d8aac` — phase facts and review brief | **Real rule**, with prompt reinforcement: answer the current phase’s question using supplied facts. | Explicit obligation inventories per phase. Review feasibility before construction; assess delivered behavior afterward. |
| `c4eb182` — typed pre-B repair | **Real rule:** repair the actual plan against its recorded cause, without inventing an amendment ceremony. | One atomic edit mechanism with cause/preimage binding. Preserve this principle. |
| `6448db1` — canonical semantic snapshot | **Real rule; the strongest deletion in this history.** It removes an LLM decision about whether unchanged content can retain review credit. | Code-owned identity and evidence applicability. Apply the same principle to clean-core verification reuse. |
| `cbfb8d5` — charter clean-code rule | A governing requirement, **not an executable fix**. | Judge changes by eliminated failure classes, not smaller files or added instructions. |
| `5ee57f1` — clean-core spine | Useful architectural reset: one store, plan and loop. **A scripted spine is not recovery or scale.** | Keep the owners; replace global execution assumptions with scoped work records. |
| `2fd12fa` — schemas, native calls, receipts, exact-fix retries | **Real rules.** Structure is checked; process evidence is observed. | Keep these boundaries. Ending malformed/provider failures INCOMPLETE does not implement the promised recovery. |
| `7259029` — common repair and CODE-owned ordering | Atomic repair and authority binding are **real rules**. “Three repairs per origin” merely bounds damage. | Repair a named cause through its responsible owner; require relevant new evidence. Changed bytes alone are not progress. |
| `2034943` — argv, observed failures, product-only planning | **Mostly real rules:** eliminate shell ambiguity, supply actual failures, compile workflow. | Separate installed verification tools from product outputs. `shutil.which()` on every command rejects legitimate not-yet-built product executables. The Python fallback suggestion is another domain assumption. |
| `b12ffe6` — phase-specific judgments, constrained repair, scripted outcome | **Real fixes:** GREEN no longer demands the later guide; repair cannot rewrite workflow; code labels scripted acceptance; unchanged plans skip IMPACT. | Retain those contracts. The extra “check-in is workflow” and “scripted approval is interpretable” sentences compensate for questions that still expose unnecessary decisions. |
| `51dd878` — observable quality | **Prompt patch, currently contradicted by the producer:** ALIGN receives only dream words, not setup, yet is told to use “supplied setup.” | Supply actual capabilities before Vision Lock; bind each quality obligation to a feasible verification route. Unavailable verification must remain visible, not silently lower the dream. |
| `51dd878` — discoveries no longer stop done work | Correct distinction, **incomplete implementation**. Previously every discovery stopped delivery; now discoveries are retained without a consuming steering path. | Completion and discovery are separate facts. Route unresolved discoveries to the affected obligation without blocking unrelated completed work. |
| `6bae98f` — attach screenshots | **Real producer/consumer repair.** Run 05 had image paths but a judge unable to inspect them. | Deliver the actual evidence in the modality the consumer can use. Keep this. |
| `d4cb94c` — missing-product RED | **Correct semantic principle, implemented as an answer-specific prompt patch.** It leaves the same judge in control and the same broken repair routing underneath. | Establish product absence, tool readiness and candidate identity in code; ask only the remaining semantic question. |
| Taste additions in `b12ffe6`/`d4cb94c` | Asking for craft is legitimate semantic guidance. A global blacklist of system fonts, pills and colors is **not a reliability rule**. | Establish a product-specific visual direction in the accepted quality bar; workers inspect it and judges assess it. Delete late, unaccepted aesthetic requirements. |

These distinctions are visible in [questions.py](~/codex-harness/work/sprint-20261027/semantic-cc/src/seldon/questions.py:8), [plan.py](~/codex-harness/work/sprint-20261027/semantic-cc/src/seldon/plan.py:102), and the fact construction in [Loop._call](~/codex-harness/work/sprint-20261027/semantic-cc/src/seldon/loop.py:30).

Run 03 demonstrates why this matters: GREEN passed the browser interaction but demanded `TRY.txt` prematurely. Repair then moved guide ownership into build, incurred two schema retries, and introduced `DELIVERY.txt`. **The app needed no such repair; Seldon manufactured work to satisfy its own confused phase contract.** [03 report](C:/seldon/tests/core1/real-lead-03.out)

**2. Variance: where one judgment controls the run**

Different plans and implementations are acceptable. Different interpretations of evidence identity, phase obligations or approval origin are not.

| Decision | Single-model leverage | Present containment |
|---|---|---|
| ALIGN | Invents improvements, quality obligations and verification expectations. Run 04 acquired an actual screen-reader-announcement obligation. | A approval; these runs automatically answered yes. The capability information needed to constrain the proposal was absent. |
| PLAN / REVIEW | Chooses tests and coverage; one reviewer can accept omissions or send the whole plan to repair. | Shape, graph links and one fresh same-provider review. Links do not establish semantic coverage. |
| DECIDE | Can reinterpret the same literal approval as uncertain; run 03 stopped at C for precisely this reason. | Subject binding and scripted-outcome labeling. The interpretation call remains unnecessary for an explicit protocol response. |
| JUDGE | One gap or uncertainty can stop the entire run despite valid work elsewhere. | Actual process outcomes and candidate checks prevent some false passes; they do not prevent false semantic vetoes. |
| IMPACT | Can classify weakened requirements as within scope without a literal Vision change. | Before/after records and subsequent review; neither is deterministic protection against semantic narrowing. |
| WORK | Chooses implementation and what to report as blocked/discovered. | Observed ownership/diffs and integrated checks. Discovery handling and local feedback remain inadequate. |

**RED is sound as a relationship: the new obligation is meaningfully unsatisfied before implementation and satisfied afterward. The current binary RED gate is too coarse.**

Run 09 initially failed at `fs.access(index.html)`—that established absence, but did not establish browser readiness. The first judge had a legitimate evidentiary distinction to make. On the second attempt, however, the browser actually navigated and returned `ERR_FILE_NOT_FOUND`; the judge still demanded a loadable page and an interaction assertion. That contradicts the approved missing-product RED rule.

The worse defect followed: all three REPAIR answers returned no plan edits and requested the missing implementation. `_resume_repair()` selected **tests again because no valid RED existed**. Four test-worker calls changed diagnostics while `index.html` remained absent. Later tests even encoded the judge’s mistaken claim that product absence was not interaction evidence. Records: observations `r53/r85/r117/r149`, judgments `r61/r93/r125/r157`. [09 report](C:/seldon/tests/core1/real-lead-09.out), [repair routing](~/codex-harness/work/sprint-20261027/semantic-cc/src/seldon/loop.py:441).

**Code should establish more of RED:** exact baseline, declared product outputs, observed tool readiness, command execution and test inventory. The LLM should judge whether the attempted check meaningfully challenges the obligation. Do not replace that judgment with stderr keyword matching, and do not fabricate a stub to appease it. Existing GREEN obligations must remain GREEN; demanding every test fail is invalid for brownfield and later waves.

Run 12 exposes the same ownership mistake elsewhere. Demo judgments `r118`, `r150` and `r182` rejected functional evidence from candidate `r73` because the current candidate differed. I compared the retained manifests: **every earlier file was unchanged; only `TRY.txt` was added**. `_eligible()` already knows how to check that, but the judge receives neither the old manifest nor the established applicability fact. The loop repeatedly rewrote the guide to fix missing evidence linkage. The judge was right about its incomplete packet; Seldon assigned the wrong repair. [12 first judgment](C:/seldon/tests/core1/real-lead-12/calls/call-c8b375e76ca7495aa7a9eca974684662/answer.txt), [eligibility](~/codex-harness/work/sprint-20261027/semantic-cc/src/seldon/loop.py:142).

Do not add majority voting everywhere. Remove deterministic questions from judgment, constrain findings to the assigned obligation, and gather the missing evidence before commissioning product changes.

**3. Scale: change the shape, defer the machinery**

The [design](~/codex-harness/work/ladder/CLEAN-CORE-DESIGN.md) promises bounded projections, recorded attempts and extensions to waves. The implementation often has global state where those extension points need scoped records.

| State / owning module | What breaks first at 1,000× | Shape to correct now; implementation correctly deferred |
|---|---|---|
| ALIGN — `questions.py`, `schema.py` | A whole-product prose vision accumulates unverified obligations; quality has positional identities such as `quality:3`. | Stable obligation identities and capability-informed verification commitments. Defer elaborate research/onboarding interfaces. |
| DECIDE — `loop.py` | Full-plan subjects grow; synchronous user callbacks and repeated interpretation add latency at every wave. | Persist one bound decision request/response independently of execution. Defer rich chat/cockpit presentation. |
| PLAN — `plan.py` | Three universal beads, one wave, and global product/test file lists cannot express independent work. `apply()` links **every bead to every requirement and test**, destroying selective impact. | Preserve local requirement/test/ownership relationships; tiny work is one valid instance. Defer parallel scheduling, not the ability to represent locality. |
| REVIEW — `questions.py`, `providers.py` | Whole-plan reviews hit the question limit and one dispute blocks everything. | Explicit reviewed coverage, canonical subject identity and affected review scope. Defer parallel reviewer orchestration; retain honest same-provider labeling. |
| WORK — `loop.py`, `work.py` | `ready[0]`, global `task`, `bead`, `assignment` and `changed` allow only one operation. Frozen initial file lists cannot accommodate repair-created files. | Durable assignment/attempt records with explicit scope and amendable ownership. Keep execution serial initially. |
| OBSERVE — `evidence.py` | Executes every stage declaration serially, with a fixed default timeout, and assumes the product tree never changes during verification. | Commands bound to immutable candidate inputs and specific obligations; scratch/output declarations separate from product inputs. Defer distributed execution and tool adapters until needed. |
| JUDGE — `loop.py`, `questions.py` | Global inventories exceed 128 assessments/64 KiB; source is silently truncated to 8 KiB per artifact; one verdict gates all work. | Complete bounded evidence per assigned obligation, retrievable artifacts, code-owned applicability. Defer paging optimizations; never treat truncation as complete inspection. |
| INTEGRATE — `work.py` | Every worker copies the whole project into an orphan worktree; repeated scans hash all files. Integration writes files individually inside a DB transaction that cannot roll back filesystem writes. | Real base revisions, changed-file patches and a recoverable candidate publication boundary. Defer sophisticated merge automation. |
| REPAIR / IMPACT — `plan.py`, `loop.py` | State-origin counters group unrelated failures; any valid RED can satisfy global resume logic; unchanged plans still get new revisions and forced file changes. | Bind cause, affected obligation, responsible owner and expected new evidence. Identity repairs should preserve identity. Defer advanced replanning policy. |
| STEER — `loop.py` | It is a fixed check-in transition after **all waves**, not semantic steering or successive-wave planning. | A continuation consumes the current wave’s results and unresolved causes. Defer elastic multi-wave execution. |
| ACCEPTED / INCOMPLETE / STOPPED — `loop.py`, `store.py` | There is no usable reopen/resume constructor, STOPPED state or control path. “Before resuming” is currently a promise without implementation. | Reopen canonical state and persist executable continuation/attempt reconciliation. Defer cross-version migration; current-run recovery is already required. |
| Store — `store.py` | Whole JSON cursor/history and duplicated full plans grow; in-memory execution state cannot be recovered from them reliably. | Keep SQLite and one writer; make attempts/results independently addressable. Defer a database replacement or event framework. |
| Process lifetime — `processes.py` | Large concurrent output accumulates in memory; observation cleanup failure can still reach judge/repair rather than stopping new effects. | Preserve the existing OS lifetime owner; make unverified cleanup a controller boundary. Defer process-runtime replacement; bound/stream logs when exercised. |
| Provider boundary — `providers.py` | All roles launch the same hardcoded model; worker ambient configuration adds hidden context, latency and variance. | Invocation and provenance must consume the same explicit role configuration. Defer additional providers; do not build another permission system. |
| Package — `__init__.py` | No issue: it is appropriately trivial. The planned `frontdoor.py` is absent. | Keep imports thin. Defer the UI; do not describe its missing control behavior as implemented. |

The 32 new-handle slots and 64 KiB cap can be sensible **batch limits**. Without incremental composition, they become product-size limits. Raising them postpones the failure. [schema.py](~/codex-harness/work/sprint-20261027/semantic-cc/src/seldon/schema.py:49)

The journey exercises real storage, commands and integration, which is valuable. Its fake judge nevertheless supplies satisfaction, and some branches manufacture gaps based on packet shape. It cannot establish judgment stability, current-run recovery or large-app behavior. No crash/reopen case appears in its current case list. [test_journey.py](~/codex-harness/work/sprint-20261027/semantic-cc/tests/seldon/test_journey.py:87)

**4. Wasted LLM work, ranked**

1. **Repairing orchestration/evidence defects through product workers.** Run 09 spent 232.860 seconds across four test-worker calls, plus repeated judgment and repair. Run 12 rewrites a guide to repair omitted candidate linkage. Route missing facts to the evidence owner and implementation faults to their actual writer.
2. **Fresh workers without a local check-and-fix loop.** “Report, do not prove” is being interpreted literally: run 04 explicitly reports no execution. Successful runs’ worker traces show reads/writes, not browser inspection or product execution; run 09 includes a syntax check, so “never” is slightly too absolute. Let workers execute the assigned checks and inspect the UI before returning; Seldon still owns integrated acceptance.
3. **A separate guide worker with fresh provider context.** In successful runs 06–11 it costs roughly **37–49 seconds**, comparable to building the page. Keep the worker’s delivery session responsible for its guide, with finalization scheduled after check-in; do not re-onboard another writer merely to explain three files.
4. **Four LLM calls to read “yes.”** Successful runs spend roughly **28–35 seconds** here—four of thirteen calls. Consume a bound scripted decision directly. For real users, support an exact confirmation protocol for the currently displayed subject; use semantic interpretation only for free-form or qualified replies.
5. **Repeated verification and evidence interpretation.** `plan.create()` clones the first verification command into a walkthrough when none is supplied. This repeats work and hides the missing evidence-reuse contract that run 12 exposed. Reuse applicable functional evidence; execute only the additional walkthrough obligations.
6. **Repeated broad context and schema overhead.** Run 11’s guide call reports 78,578 input tokens, including cached traffic, for an 8,381-byte task prompt. These totals are not a cost estimate, but they expose substantial provider-context overhead. Supply bounded task facts and remove unnecessary ambient instructions through the provider boundary. [11 report](C:/seldon/tests/core1/real-lead-11.out)

**5. The three changes to make, in order**

1. **Make evidence applicability and execution facts authoritative in CODE.**  
   CODE establishes candidate/test/input identity, execution status, coverage and evidence reuse; LLM judges meaningful behavior and accepted quality. Resolve RED’s product/tool distinction explicitly. Supply these established facts to judgments and acceptance from one owner.  
   **Delete:** model judgments about unchanged bytes, redundant interpretation of scripted decisions, missing-product exception accumulation, and duplicate functional walkthrough execution.  
   **Measure in RUNS.md:** deterministic-fact disputes, avoidable reruns and repairs must reach zero; retain correct refusal for broken tooling, skipped verification and changed inputs. Track identical-evidence verdict flips separately from legitimate semantic disagreement.

2. **Make each worker finish a locally checked result; route repairs by cause.**  
   **CODE owns** execution, ownership and routing; **LLM owns** implementation and visual craft. Return local command/browser feedback to the responsible worker. Judge the integrated result afterward. A missing fact gathers evidence; it does not force file edits. A discovery receives a disposition.  
   **Delete:** “Report, do not prove,” forced changed-byte progress, guide rewrites for evidence defects, and empty REPAIR calls whose only effect is rescheduling the same wrong task.  
   **Measure:** first integrated GREEN rate, escaped defects, local versus orchestration repair time, repeated-cause count, and whether workers inspected the actual UI. Preserve the accepted visual bar while reducing total calls and time.

3. **Make one scoped, durable work contract the unit of the loop.**  
   **CODE owns** identities, dependencies, attempts, integration and invalidation; **LLM owns** semantic decomposition. Preserve local links and recoverable results. A tiny app can still have one serial unit; larger products compose those units without another execution model.  
   **Delete:** blanket bead-to-everything links, global latest-result assumptions, volatile assignment authority, and duplicated whole-plan facts. Keep SQLite, the thin provider wrapper and the process owner.  
   **Measure:** obligations invalidated per change, unaffected evidence retained, bytes per question, work repeated after interruption, and whether two independent scopes remain independent. No large scheduler is needed to expose these properties.

For all three, record the exact source commit, question-contract digest and locked-vision identity in the existing run row. Compare runs against the same accepted obligations, report scripted versus owner acceptance separately, and retain failures. **The next proof is a repeatable Hello-world journey whose failures produce the right action—not another lucky zero-repair pass.**