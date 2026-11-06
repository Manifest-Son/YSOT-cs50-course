import os
import sys
import importlib.util

_here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(os.path.dirname(os.path.dirname(_here)))
sys.path.insert(0, root)
_spec = importlib.util.spec_from_file_location("C1_prompt_swap_test_c1", os.path.join(os.path.dirname(_here), "starter.py"))
starter = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(starter)

def test_answer_calls_chat(monkeypatch):
    def fake(system, user):
        assert system == "pirate"
        return "arr"
    monkeypatch.setattr(starter, "chat", fake)
    assert starter.answer("hi", "pirate") == "arr"


def test_fallback(monkeypatch):
    from tools.llm_client import NoModelAvailableError
    def boom(system, user):
        raise NoModelAvailableError("x")
    monkeypatch.setattr(starter, "chat", boom)
    assert starter.answer("hi") == "No model available."


# Try changing: modify this file and re-run the tests.
