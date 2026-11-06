"""One helper for talking to an LLM.

Works with any OpenAI-compatible API (OpenAI, OpenRouter, Azure, local servers)
and with Ollama through its OpenAI-compatible endpoint. Configuration is read
from a .env file so secrets never live in code.

Endpoints are tried in order: the configured OpenAI-compatible one (only if a
key is set), then Ollama. If one fails for ANY reason (rate limit, bad key,
network down, empty reply) the next one is tried, and if all fail the error
says what went wrong with each.

Try changing:
- DEFAULT_SYSTEM: the default personality of the assistant.
- TIMEOUT_SECONDS / OLLAMA_TIMEOUT_SECONDS: how long to wait before giving up.
"""

import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

# Load .env from the project root (one level up from tools/).
_PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(_PROJECT_ROOT / ".env")

TIMEOUT_SECONDS = 30
# A local model on a CPU needs time to load and to write its answer.
OLLAMA_TIMEOUT_SECONDS = 180
MAX_RETRIES = 1
DEFAULT_SYSTEM = "You are a helpful, concise tutor for beginner programmers."

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1").strip()
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini").strip()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1").strip()
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2").strip()


class NoModelAvailableError(RuntimeError):
    """Raised when no LLM endpoint can be reached."""


def _candidates():
    """Endpoints to try, in order: (label, base_url, api_key, model, timeout)."""
    found = []
    if OPENAI_API_KEY and OPENAI_API_KEY != "sk-your-key-here":
        found.append(
            ("openai-compatible", OPENAI_BASE_URL, OPENAI_API_KEY, OPENAI_MODEL, TIMEOUT_SECONDS)
        )
    found.append(("ollama", OLLAMA_BASE_URL, "ollama", OLLAMA_MODEL, OLLAMA_TIMEOUT_SECONDS))
    return found


def _make_client(base_url, api_key, timeout):
    return OpenAI(base_url=base_url, api_key=api_key, timeout=timeout, max_retries=MAX_RETRIES)


def _describe(exc):
    """Short one-line description of an exception (never includes the API key)."""
    status = getattr(exc, "status_code", None)
    where = f" (HTTP {status})" if status else ""
    text = " ".join(str(exc).split())
    return f"{type(exc).__name__}{where}: {text[:200]}"


def _no_model_error(problems):
    details = "\n".join(f"  - {p}" for p in problems)
    return NoModelAvailableError(
        "No language model is reachable. "
        "Set OPENAI_API_KEY in your .env file, or start Ollama with "
        "'ollama serve' and 'ollama pull llama3.2'. "
        "See SETUP.md for help.\n"
        f"What went wrong:\n{details}"
    )


def get_client():
    """Return (client, model_name, source_label) for the first endpoint that answers.

    Note: this only checks that the endpoint lists its models. Some providers
    (OpenRouter) allow that without a valid key, so use ask() for a real test.
    Raises NoModelAvailableError with a plain-English message if none work.
    """
    problems = []
    for label, base_url, api_key, model, timeout in _candidates():
        try:
            client = _make_client(base_url, api_key, timeout)
            client.models.list()
            return client, model, label
        except Exception as exc:
            problems.append(f"{label}: {_describe(exc)}")
    raise _no_model_error(problems)


def ask(system_prompt, user_prompt, temperature=0.7):
    """Send one system + one user message; return (text, source_label, model).

    Tries each endpoint in turn and falls back on any failure.
    """
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]
    problems = []
    for label, base_url, api_key, model, timeout in _candidates():
        try:
            client = _make_client(base_url, api_key, timeout)
            response = client.chat.completions.create(
                model=model, messages=messages, temperature=temperature
            )
            text = response.choices[0].message.content
            if text and text.strip():
                return text, label, model
            problems.append(f"{label}: the model returned an empty reply")
        except Exception as exc:
            problems.append(f"{label}: {_describe(exc)}")
    raise _no_model_error(problems)


def chat(system_prompt, user_prompt, temperature=0.7):
    """Send one system + one user message and return the assistant's text."""
    text, _source, _model = ask(system_prompt, user_prompt, temperature)
    return text


if __name__ == "__main__":
    # Real self-check: sends a tiny message, so a bad key or a rate limit shows up.
    try:
        text, source, model = ask("Reply with one short word.", "Say ok.", temperature=0)
        print(f"Model answered: {model} via {source}: {text.strip()[:60]!r}")
    except NoModelAvailableError as exc:
        print(f"NOT reachable: {exc}")
        sys.exit(1)
