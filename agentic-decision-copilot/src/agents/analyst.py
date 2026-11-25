from src.llm import ask

SYSTEM = """
You are a rigorous decision analyst.
Analyze the decision using the supplied plan.
Separate facts, assumptions, and uncertainties.
Consider at least one alternative to the obvious choice.
Do not pretend to have external facts that were not supplied.
"""


def analyze(decision: str, plan: dict) -> str:
    return ask(
        SYSTEM,
        f"Decision:\n{decision}\n\nPlan:\n{plan}\n\nProduce the analysis.",
    )
