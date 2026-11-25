from src.agents.planner import make_plan
from src.agents.analyst import analyze
from src.agents.reflection import critique, revise
from src.evals.evaluator import evaluate_response


def run(decision: str) -> dict:
    plan = make_plan(decision)
    draft = analyze(decision, plan)
    criticism = critique(decision, draft)
    final = revise(decision, draft, criticism)
    evaluation = evaluate_response(final)

    return {
        "plan": plan,
        "draft": draft,
        "critique": criticism,
        "final": final,
        "eval": {
            "score": evaluation.score,
            "checks": evaluation.checks,
        },
    }
