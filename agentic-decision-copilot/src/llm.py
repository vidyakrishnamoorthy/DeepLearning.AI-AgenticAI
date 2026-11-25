import json
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")


def ask(system: str, user: str) -> str:
    response = client.responses.create(
        model=MODEL,
        instructions=system,
        input=user,
    )
    return response.output_text


def ask_json(system: str, user: str) -> dict:
    """Small explicit JSON helper. We validate defensively rather than hiding logic."""
    text = ask(system + "\nReturn ONLY valid JSON.", user)
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Model did not return valid JSON:\n{text}") from exc
