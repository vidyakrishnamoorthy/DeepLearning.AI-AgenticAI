from src.llm import ask_json

SYSTEM = """
You are the planning agent for a decision-support system.
Break a decision into a compact analysis plan.
Do not make the final decision.
"""


def make_plan(decision: str) -> dict:
    return ask_json(
        SYSTEM,
        f"""
Decision:
{decision}

Return this JSON shape:
{{
  "decision": "...",
  "unknowns": ["..."],
  "criteria": ["..."],
  "alternatives": ["..."],
  "analysis_steps": ["..."]
}}
""",
    )
