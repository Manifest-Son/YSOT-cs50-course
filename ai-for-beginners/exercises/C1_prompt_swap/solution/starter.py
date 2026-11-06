"""Exercise C1: swapping system prompts."""

import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, ROOT)

from tools.llm_client import chat, NoModelAvailableError


def answer(question, system_prompt="You are a helpful tutor."):
    try:
        return chat(system_prompt, question)
    except NoModelAvailableError:
        return "No model available."


# Try changing: modify this file and re-run the tests.
