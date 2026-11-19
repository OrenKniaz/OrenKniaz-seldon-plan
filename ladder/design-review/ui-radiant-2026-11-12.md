# Seldon run page: the Prime Radiant (design, 2026-11-12)
Mockup: `ui-radiant-2026-11-12.html` (one file, no external requests; open from disk). Screenshots: `ui-radiant-narrow.png`, `ui-radiant-full.png`.
Binding: `seldon-cockpit-concept.md` (the concept), `ui-reimagine-brief.md` (5 questions), Charter v1.7 C20 (read-only, built for the browser pane), Blueprint §3 (records and states). It replaces the layout of `ui-mockup-2026-11-12.html`; that file's data model and chat surface (`ui-design-2026-11-12.md`) stand.

## Decisions
1. **The product is the picture.** One radial map: the vision is the centre, capabilities orbit it, then requirements, then work items with their checks. Nothing on the first screen is a list of machinery.
2. **Light means truth.** One ladder of nine states is used on the map and on every dot in every view. A node gets brighter only when its record really moved. State flows upward by the weakest child, so a capability is "proven" only when all of its parts are. The whole map warms with "% proven" (requirements proven in real use).
3. **Narrow first.** At about 400 px the page is one column: header, six tabs, and the map as a square with the capability list under it (the concept's phone form). Full screen (`⤢`): the map takes the stage as a wide ellipse, and the tabs drive a 440 px side panel. The board can take the stage ("board to the stage").
4. **Read-only is visible.** Every "waiting on you" card shows the question, says "Answer in chat", and gives the exact words to type. The inspector ends with the sentence to type in chat. No control on the page changes the run.
5. **Theme never hides meaning.** Each Foundation name has its plain words underneath. `Aa` (plain mode) removes the theme names everywhere, including the tabs and the zoom control.
6. **Type and colour.** Palatino/Iowan serif for names and questions, Cascadia/Consolas mono for data, Segoe UI for prose. Colour is amber to gold for progress, red-violet for the Mule, orange-red for a failing check, cool blue for agreements. Dark is navy-black; light is amber on warm paper. Text is AA in both.
7. **Motion only for change.** Nodes ping when they appear or step up, links draw in, zoom glides, building nodes breathe, and the Vault opens for three seconds at a wave checkpoint (Terminus at acceptance). All of it is off under `prefers-reduced-motion`.
8. **Zoom follows the journey** unless the user picks one: Understand macro, Shape mid, Build micro, Prove mid, accepted macro. Selecting a node dims everything outside its trace.

## Concept element to Seldon record
| Concept | Seldon record or state |
|---|---|
| Vision → Capability → Requirement → Work item → Proof | Vision → Feature → Requirement → Unit → Check. Area is shown in the inspector. Contract is a cool dashed chord between provider and consumer units at micro zoom; a corrected contract is marked. |
| question (dashed) | A Vision Lock unknown or a scope question raised at STEER. It is removed when answered and becomes a Decision in the Chronicle. |
| drafted | Written by ALIGN, ARCHITECT or DETAIL, before its gate. |
| agreed | Vision and features after Gate A. |
| planned | After Gate B (wave 1), or detailed by DETAIL for a later wave. Unit READY. |
| building | Unit WORKING (also REWORK, with the failing mark). |
| built | Unit PROVING, JUDGING or INTEGRATING; the card pips show which. |
| tested | Unit DONE: checks failed before and pass after, judged, integrated. |
| proven in real use | Unit DONE and its wave passed WAVE-VERIFY and flow review. |
| accepted by you | Gate C answered by the user (Terminus). |
| accepted by proxy | A gate answered by a scripted yes: dashed grey ring, "not by you" in Vault and Proof. |
| blocked / the Mule | Unit BLOCKED or FAILED; the Mule when the cause is outside the plan (contract fault, unit steering). |
| failing | Unit REWORK, or a WAVE-VERIFY failure sent back to its unit. |
| known gap | A "not judged" item, attached to its requirement and listed in Proof. |
| Journey bar | Understand = ALIGN, A. Shape = ARCHITECT, DETAIL, REVIEW, B. Build = per wave EXECUTE, WAVE-VERIFY, flow review, STEER, CHECK-IN. Prove = VALIDATE, DEMO, C. |
| Seldon Crisis | Any open gate (A, B, check-in, C) or a scope question (C16, C21). |
| The Vault | One card per gate: Built, Proven, Bumps, Next, and who answered. Sealed until reached. |
| Second Foundation | Plan review, unit judge, flow review, VALIDATE: the Proof view (ledger, first real use, try it, gaps, acceptance). |
| Crew strip and work board | Worker sessions (provider, model, unit, time, stalled flag, slots). Columns: Waiting on you (gate), Blocked, Active (WORKING to INTEGRATING, REWORK), Up next (READY with its wait reason), Done. |
| Waves | Wave records: goal, unit dots, the five wave steps, the current wave's units; outlined waves are dashed. |
| Chronicle | Events with the why, newest first, grouped by stage and wave; "new since you last looked". |
| Inspector | The six lines of `seldon_inspect` (What, Why, Needs, Now, Proof, Who), trace up and down, state history. |

## Samples and replay
- **ShelfLife** (illustrative, default): 4 capabilities, 10 requirements, 3 waves, 15 work items, 47 steps. It shows a question at Gate A, a rework, a stalled worker, the Mule with a contract correction and a fixup unit, a Seldon Crisis on scope, a known gap, and Terminus.
- **Foundation** (the real M1 run): 25 steps with the real ids, commits and failures. Gates A, B and check-in show as accepted by proxy; it ends waiting on the owner at Gate C.
- The dashed bar at the bottom replays a run. It is a mockup control, not part of the page. In the product the same projection (`state.js`) drives the page. Deep links for review: `#s=shelf|foundation&k=<step from 0>&full=1&theme=light&plain=1&tab=map|crew|waves|chron|proof|vault&zoom=macro|mid|micro&sel=<id>&stage=1`.

## Checked, and not
- Headless Chrome: no console errors on load or across a full autoplay of both samples; rendered at 400 px (in a 400 px iframe) and at 1600 × 900, dark and light, plain mode, inspector, board on stage.
- Not checked: clicks by hand, keyboard and screen-reader use, Firefox or Safari (edge paths animate through the CSS `d` property, which is Chromium-only; elsewhere they jump), and measured contrast ratios (colours were chosen for AA and not measured with a tool).
- Open for Oren: (a) Is the bigger default (ShelfLife autoplaying on open) right for the mockup, or should it open on the real Foundation run? (b) Should every open gate be called a Seldon Crisis, or only scope questions, with routine check-ins shown as "the Vault is open"? (c) Encyclopedia (the plan written out) has no view here; the Vault's A and B cards carry the plan summary. Does it need its own view?
