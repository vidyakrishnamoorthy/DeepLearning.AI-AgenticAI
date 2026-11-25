# Agentic Decision Copilot

A hands-on companion project for DeepLearning.AI's **Agentic AI** course.

Instead of copying course labs, this repo applies the same core patterns to one
product: a decision copilot that takes a messy decision, clarifies it, plans an
analysis, uses tools, critiques its own answer, and returns a recommendation.

## Course → project mapping

| Course concept | This repo |
|---|---|
| Task decomposition | `src/agents/planner.py` |
| Reflection | `src/agents/reflection.py` |
| Tool use | `src/tools/decision_tools.py` |
| Evals/error analysis | `src/evals/evaluator.py` |
| Planning | `src/agents/planner.py` |
| Multi-agent workflow | `src/workflow.py` |

## Setup

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r ../requirements.txt
cp .env.example .env
```

Add your OpenAI API key to `.env`.

## Run

```bash
python main.py
```

Try:

> Should our team build an internal AI support assistant now, or wait six months?

## Learning path

### Stage 1 — Baseline
Run the direct-generation version and inspect the answer.

### Stage 2 — Reflection
Enable the critic/reviser loop. Compare the original and revised recommendation.

### Stage 3 — Tools
Let the agent call deterministic decision tools instead of doing arithmetic itself.

### Stage 4 — Evals
Create test cases and score whether recommendations contain assumptions, risks,
alternatives, and a concrete next action.

### Stage 5 — Planning + multi-agent
Use a planner, analyst, critic, and synthesizer as separate roles.

The code intentionally stays small and explicit so you can see the agentic loop.

## Suggested portfolio extensions

1. Add Streamlit UI.
2. Add web research as a tool.
3. Persist decision history.
4. Add structured clarifying questions before planning.
5. Build a 20–30 case eval dataset and publish before/after scores.
6. Add traces for latency, token usage, and tool calls.
7. Later, reimplement the workflow in an agent framework and compare it with this
   first-principles implementation.
