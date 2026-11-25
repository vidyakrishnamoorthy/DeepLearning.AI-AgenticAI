# Course Notes → Build Notes

Use this file while watching the course.

## Module 1 — Agentic workflows
- What problem benefits from multiple steps?
- What parts should remain deterministic?
- What does success mean?
- Baseline result:

## Module 2 — Reflection
Experiment:
- Run a decision without reflection.
- Run it with critic + revision.
- Which failure modes improved?
- Which did not?

## Module 3 — Tool use
Current deterministic tools:
- weighted_score
- rank_options

Build next:
- Make the LLM decide when a scoring tool is appropriate.
- Log every tool request and result.
- Reject malformed tool arguments.

## Module 4 — Evals
Start with `data/eval_cases.json`.

Track:
- task success
- missing assumptions
- unsupported claims
- useful next action
- latency
- cost

Do not optimize prompts blindly. Categorize failures first.

## Module 5 — Planning and multi-agent
Current roles:
- Planner
- Analyst
- Critic/Reviser

Experiment:
- Compare direct answer vs planned answer.
- Compare no reflection vs reflection.
- Determine whether separate roles improve quality enough to justify added cost/latency.

## Portfolio write-up
Capture:
1. Problem
2. Baseline
3. Agent architecture
4. Evaluation methodology
5. Failure analysis
6. Iterations
7. Quantified improvement
8. Tradeoffs
