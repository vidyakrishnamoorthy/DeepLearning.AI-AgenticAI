from dataclasses import dataclass


@dataclass
class EvalResult:
    score: int
    checks: dict


REQUIRED_SIGNALS = {
    "recommendation": "recommend",
    "assumptions": "assumption",
    "risks": "risk",
    "decision_change": "change",
    "next_action": "next",
}


def evaluate_response(text: str) -> EvalResult:
    """Simple deterministic component eval.

    This is deliberately basic. Replace it later with richer rubric-based
    and LLM-as-judge evals after establishing a baseline.
    """
    lowered = text.lower()
    checks = {
        name: signal in lowered
        for name, signal in REQUIRED_SIGNALS.items()
    }
    return EvalResult(score=sum(checks.values()), checks=checks)
