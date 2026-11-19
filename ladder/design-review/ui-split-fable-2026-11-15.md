# UI split (Fable) 2026-11-15 — T-167: large UI as parallel units, no integrator, no shared-file fights
Read-only design review. Basis: CHARTER v1.8, BLUEPRINT v1.10, src/seldon (plan.py, architecture.py, detail.py, questions.py, schema.py, judgment.py), speed design
2026-11-14 section 5, store of shelflife-683d19b-l01. No provider calls, no tests run. Minute figures are estimates unless marked measured.
**TRIAGE: DESIGN** — family "Built for small dreams". Siblings: any shared structure many units extend (router, registry, plugin table, DI container, CLI command table,
DB migrations list, i18n catalogue). The rule below is written for all of them; UI is the first case.

## 1. What the code already gives (so the design is small)
- Contract kind `ui-structure` exists (schema.py:31) and ShelfLife already uses it (l01: `local-assets`, interface -> 3 consumers).
- DETAIL may answer `subdivide` (sub-areas + their contracts, architecture.subdivision/expand). Splitting a UI area into shell + screens is that path, unchanged.
- Scopes are exclusive and enforced from the observed diff (R6). A screen unit that edits a shell file is already rejected.
- A unit that `reads` a concrete file owned by another unit gets a dependency edge; its worktree base then holds the integrated shell (S1: only a local read waits).
- l01 evidence: interface = one area, one unit, `static/**`, 4 requirements; W_ui 10-11 min / 24-27k tokens (measured, speed design). One screen. Nothing to split.
So nothing structural is missing. Missing: one planner principle, one normalisation, and the look reaching the screen workers and the PRODUCT judge per area.

## 2. The one rule
**A shared structure has one owner, and everyone else extends it by adding files in their own scope, never by editing the owner's files.**
For UI: one small early **shell unit** provides a UI-structure contract and makes it real (shell, router/registration, tokens, shared primitives). A **screen** is the
smallest UI unit; each screen (or tightly coupled screen group) is a unit that consumes the contract, reads the shell's files and writes only `…/screens/<name>/**`.
The shell finds screens by the contract's convention, so no screen ever touches the router, the stylesheet or the tokens. That removes the integrator: integration is a
plain git merge of disjoint paths, and the join is one shell-owned check.
LLM-or-CODE: whether seams exist and where = LLM (ARCHITECT / DETAIL `subdivide`); edges, scope enforcement, image routing, combining verdicts = CODE.

## 3. Contract shape (kind `ui-structure`, plain text, provider = shell; I3: no new schema fields)
The text settles exactly these, and nothing else (values stay in the shell's files; the contract holds names and paths):
1. **Registration convention**: where a screen lives and what it exports (e.g. `ui/screens/<route>/index.*` exporting `mount` and `meta {title, group, order}`), and
   the statement "a screen is added by files in its own folder only". If the stack cannot discover (some native stacks), the shell writes the full registry up front
   from the route names; either form satisfies the rule.
2. **Route names and nav groups**: names only (cross-screen links use them). Names, not a table: contract text is capped at 2048 chars in planning schemas; ~40 routes fit.
   Beyond that a nav group becomes its own sub-shell with its own contract (same rule, one level down).
3. **Mount signature**: what a screen receives (container/slot, route params, shared services such as API client and notifications) and its cleanup.
4. **Slots**: named regions a screen may fill (page actions, side panel, toasts).
5. **Token and primitive names** (colour, type, space, radius, motion; button, field, table, loading/empty/error states) with the exact shell files screens import.
   Those exact file paths are what screens list in `reads`; they are the dependency edge.
6. **Evidence viewports** for screenshots, so every screen is shot the same way.

## 4. Planner and question changes
| Where | Change | Kind |
|---|---|---|
| `questions.PROMPTS` ARCHITECT + DETAIL (one shared constant, like AGREED_LITERALS) | Principle, as a constraint: "One screen is one unit. Split a UI only when three or more screens touch each other only through shell, navigation and look: then a shell area provides one ui-structure contract (registration convention, route names, mount signature, slots, token and primitive names, exact shell files) and each screen or coupled screen group is its own area that reads those files and writes only its own folder." | prompt principle (R12: principle, concrete range) |
| `plan.merge` (reads loop, line ~319) | Normalise instead of correct: a cross-area `reads` of a file with exactly one planned owner and a consumed contract from that owner gets the edge added by code (today: "needs an explicit dependency edge" -> one DETAIL re-ask per screen area). T-111 family. | code, about -3/+2 |
| `questions.work_brief` | New fact **Look reference**: for a unit consuming a `ui-structure` contract, attach the provider unit's saved screenshots (existing `images` path) | code, ~+10 |
| `judgment` PRODUCT | Subject = (criterion, area), not criterion over all areas; a non-shell area also gets the shell's reference screenshots. Code combines areas. This is R2 as already ratified ("a quality criterion is judged per area"); today `subjects()` is per criterion with every traced check, product-sized at 40 screens. | code, ~+25/-10 |
No new fields in ARCHITECT, DETAIL, PLAN or the unit record: `contract.kind`, `unit.consumes`, `unit.reads`, `unit.scope` carry it. No new question kind.
A screen needing a shared piece that does not exist: it builds it locally from tokens and names it in its handoff; STEER gives the promotion to the shell owner in the
next wave. A real contract error still goes through the existing CONTRACT question. The contract does not grow inside a wave.

## 5. Proof shape under "each behaviour proven once" (v1.10)
| Level | Owner | Proves | Never |
|---|---|---|---|
| unit | shell | shell behaviours on the real browser (nav, slots, responsive, theme, primitive states), fed one **fixture screen** from its check tree that only satisfies the mount signature (contract-shaped data, no logic) | any screen behaviour |
| contract | shell | the real shell honours the contract text: discovers a screen by the convention, exposes every named token and primitive | |
| unit | each screen | that screen's behaviours, mounted in the **real shell** (it is in the unit's base), API fed contract-shaped data; screenshots at the agreed viewports | navigation, other screens, shell states |
| wave | shell (one check) | the join: from the real navigation reach every registered route and see it mounted; one screenshot per route. Data-driven from the registry, so a new screen adds no check code. A failing route names the screen's unit as correction owner (existing fixup path) | any screen state or edge case |
| FLOW | judge | user flows that cross screens, unchanged | |
RED/GREEN unchanged: screen requirements are new in their unit (RED at T by code); the join is RED at wave start, GREEN at WAVE-VERIFY. C15 unchanged: every check
reruns on the integrated commit. A mismatch between fixture and real screens is found locally and cheaply, because each screen runs in the real shell before it returns.

## 6. Taste: how one look survives N writers
1. **One owner of the look.** Tokens, primitives and the visual-direction criterion belong to the shell unit. Its checks save a **specimen**: the shell chrome plus every
   primitive in its states, at the agreed viewports. That is the product's look made concrete once, by one writer with a point of view (CRAFT stays in every brief).
2. **Workers see it, not only read names.** Every screen worker gets the specimen screenshots as images (Look reference) plus the real files in its base.
3. **Screens cannot fork it.** Scope enforcement keeps shared styles out of reach; a screen owns only screen-local layout built from tokens.
4. **Judged against one reference, per area.** PRODUCT asks, per screen area: does this screen meet the accepted direction and belong to the same product as the
   reference? N small parallel questions, each the same size at 3 and at 40 screens; no whole-app coherence call.
5. **The user sees the look before it is copied** (waves, section 7): the specimen and one real screen are shown at the wave-1 check-in.

## 7. Waves
- **Today (one wave, DV3):** shell -> screens is a dependency edge inside the wave. Critical path = PLAN + W_shell + prove/judge/integrate + longest screen + WAVE-VERIFY.
- **M3:** wave 1 (skeleton, 3.3) = shell + one real screen through the whole stack + the join check. Check-in shows the specimen. Waves 2..n: all remaining screens in
  parallel with no wait at all, each DETAILed against the product as it exists (R10). Contract growth and promotions happen at STEER, as a shell unit of the next wave
  (latest path owner, 3.1).
- Each screen-area DETAIL is one more parallel call; ARCHITECT's 12-area bound is met by `subdivide` (UI area -> shell + screens; group -> sub-shell). Planning wall
  stays flat; planning tokens grow linearly with screens.

## 8. When NOT to split
- **One screen: never** (ShelfLife). Components of one screen share state, layout and taste; R1 holds because this is ARCHITECT's judgement by seams, not a size branch.
- **Two screens: no.** Estimate with W1 = one screen's writer time (~10 min measured for ShelfLife's page), shell ~4-5 min + ~1.5 prove/judge/integrate:
  k=1: 10 vs ~16 (split loses 6); k=2: ~16 vs ~16; k=3: ~22 vs ~16; k=12: ~70+ vs ~16-18. Hence "three or more".
- **Screens that share live client state** the mount signature cannot express (wizard steps, master-detail in one view): one screen-group unit.
- **No navigable structure** (one canvas, editor, DSP control panel): split by panels only if a slot contract passes the same test; otherwise one unit.
- **The test the planner applies:** can each screen's requirements be written naming only its own files and contract text? A screen whose DETAIL returns `contract_gap`
  against the shell twice is not a seam: merge it with its neighbour.

## 9. Risks
1. **Wrong shell, copied N times.** Mitigation: shell is small and judged first; in M3 the user sees it at check-in before fan-out. Residual: single-wave runs gate on
   the shell's unit JUDGE only.
2. **Contract change restales every screen.** `architecture.stale_consumers` marks all consumers on any text change; at 40 screens an added token name reopens 40
   units. Section 4 avoids in-wave growth; M3 should treat an additive change as proven by WAVE-VERIFY (all checks rerun) rather than reopening DONE units. Open point
   for the M3 STEER lane; not designed here.
3. **Misapplied to small apps** (+6 min on ShelfLife). Guard: the principle is worded as a constraint with a concrete range; cohort report counts UI units per run.
4. **Judge calls grow** (PRODUCT per area). Parallel and bounded, and it replaces one product-sized call that would breach R2; watch total judge bytes in P11.
5. **Local duplicates** of a primitive across screens within one wave. Accepted; promotion at STEER when two screens report the same need.
6. **Stack without discovery.** Covered by the up-front registry form; the shell then needs the full route list at wave 1, which ARCHITECT has.
7. **The normalisation in plan.merge** may have a reason I did not find for being a correction (cycle risk is already caught by the cycle check). Verify in the lane.

## 10. Minimal implementation slice
**L-UI-1 (Sol, medium; can land before M3 waves; files disjoint from run/scheduler lanes):** `questions.py` (shared principle constant in ARCHITECT and DETAIL, Look
reference fact in `work_brief`), `plan.py` (edge normalisation). Net src about **+15 lines**. Proof, behaviour only, scripted provider, one journey (~60 lines in
tests): a UI area subdivided into shell + 3 screens -> screens become READY only after the shell integrates, then run concurrently; no screen diff touches a shell path;
the plan merges with no re-ask for the cross-area read; the screen WORK question carries the shell's screenshots; the shell-owned join check is RED at wave start and
GREEN at WAVE-VERIFY. Hello-world and the recorded replays must be unchanged (one area, one unit, no new fact).
**L-UI-2 (Sol or Opus; with the first multi-screen dream):** `judgment.py` PRODUCT per (criterion, area) with reference images; net about **+15**. Journey: 1 and 12
screen areas produce PRODUCT questions of the same size; one failing screen re-asks only its own subject (R7).
**Real signal (P4):** the first dream with three or more screens, run both ways on one commit (principle on / single UI unit): compare longest writer minutes, wall time,
oracle score and the PRODUCT verdict on the visual direction. ShelfLife cohorts must show exactly one UI unit and unchanged times.
Not in the slice: sub-shell nesting (falls out of `subdivide`), promotion at STEER and the stale rule (M3 waves).

## 11. Draft BLUEPRINT text (only Oren ratifies; L-UI-1 does not depend on it, the sentences keep later builders on the rule)
**R4, append:** "A shared structure (application shell, router or registry, design tokens, shared styles) has one provider unit. Consumers extend it by adding files
inside their own scope under the contract's convention and never edit the provider's files; where a stack cannot discover additions, the provider writes the full
registry up front from the contract. *Prevents:* parallel units fighting over one router or stylesheet; an integrator unit that rewrites what others built."
**3.3, append after the skeleton sentence:** "A user interface of one screen is one unit. A larger interface is split only along a UI-structure contract; its shell,
with one real screen, belongs to the skeleton, and its look is shown at that wave's check-in before the remaining screens are built."
No charter change. R2's per-area quality judgment is already ratified; L-UI-2 implements it.

## 12. Not verified
No code or journey was run. The break-even figures are arithmetic from one measured single-page writer time. The claim that cross-area file `reads` already order
execution correctly comes from reading plan.merge and architecture.validate, and from l01 where server reads `static/*` and depends on the interface unit. Whether a
screen worker given specimen screenshots holds the look better than one given token names alone is unknown until the A/B run. I read one store (l01) only.
