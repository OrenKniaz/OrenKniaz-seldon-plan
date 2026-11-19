CHARTER: serves C1–C8/C11/C13/C16/C18/C20/C23/C25; preserves I1–I3/I6/I10; existing deviations remain explicit.  
Stage 2e — Seldon calls the LLM. Design only; one Sol-high implementation lane.  
Owner: `run_loop` selects questions; existing provider launch/process owners execute; PlanStore commits answers.  
Reviewed clean semantic-cc `a4e7df5cf6e23a64014fd7d71960f01bc2c78094`, Charter v1.2, 2c brief and requested references.  
Last retained transition: r17 recorded A; review stalled before publication or worker execution.  
TRIAGE: DESIGN — external planner still supplies internal setup; siblings: reviewer selection, answer envelopes and gate discovery.  
Rule 1: ask one semantic question per call; supply facts, identities and a few-shot example in code.  
Rule 2: schemas constrain structure; product meaning remains open-domain.  
Rule 3: fresh calls receive the canonical baton; provider conversations never become run authority.  
Rule 4: one chat mutation relays actual user words; Seldon supplies recommendations, questions and transitions.  
Rule 5: preserve C6 pushback, bound A/B/C/check-ins, observed proof and worker-only code authorship.  
Scope: replace caller-supplied semantics and setup; retain existing recovery, concurrency and acceptance owners.  
Acceptance: ordinary chat → autonomous schema calls → existing delivery journey, without planner mutation or gate-selection calls.  
Deletion estimate: net −1,100–1,800 lines; ≤30,000 remains a target, not a supported forecast for this lane alone.  
Delivery limitation: this draft is unsaved; the session’s read-only filesystem prevents creating the requested Markdown file.