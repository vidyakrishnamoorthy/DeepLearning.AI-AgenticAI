from src.llm import ask

CRITIC_SYSTEM = """
You are a skeptical reviewer of decision recommendations.
Find unsupported assumptions, missing alternatives, weak reasoning,
unaddressed risks, and vague next steps.
Be concise and specific.
"""

REVISER_SYSTEM = """
You are the senior decision advisor.
Revise the analysis using the critic's feedback.
The final response must contain:
1. Recommendation
2. Why
3. Key assumptions
4. Risks
5. What would change the decision
6. Next action
"""


def critique(decision: str, analysis: str) -> str:
    return ask(
        CRITIC_SYSTEM,
        f"Decision:\n{decision}\n\nDraft analysis:\n{analysis}",
    )


def revise(decision: str, analysis: str, criticism: str) -> str:
    return ask(
        REVISER_SYSTEM,
        f"""Decision:
{decision}

Draft:
{analysis}

Critique:
{criticism}

Return the improved final recommendation.
""",
    )
