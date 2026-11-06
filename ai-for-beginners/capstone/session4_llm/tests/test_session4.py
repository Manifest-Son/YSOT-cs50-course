import os
import sys
import importlib.util

_here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(os.path.dirname(os.path.dirname(_here)))
sys.path.insert(0, root)
_spec = importlib.util.spec_from_file_location("session4_llm_test_session4", os.path.join(os.path.dirname(_here), "starter.py"))
starter = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(starter)

from tools.llm_client import NoModelAvailableError


def test_explain_move_calls_chat(monkeypatch):
    captured = {}

    def fake_chat(system, user):
        captured["system"] = system
        captured["user"] = user
        return "Because it blocks a win."

    monkeypatch.setattr(starter, "chat", fake_chat)
    coach = starter.LLMCoach()
    board = [" "] * 9
    out = coach.explain_move(board, 4, "X")
    assert out == "Because it blocks a win."
    assert "4" in captured["user"]
    assert "X" in captured["user"]


def test_explain_move_fallback(monkeypatch):
    def boom(system, user):
        raise NoModelAvailableError("no model")

    monkeypatch.setattr(starter, "chat", boom)
    coach = starter.LLMCoach()
    board = [" "] * 9
    out = coach.explain_move(board, 0, "O")
    assert isinstance(out, str) and len(out) > 0
    assert "0" in out


def test_explain_move_not_none():
    # Without patching, may fail if no model; but fallback returns string.
    coach = starter.LLMCoach()
    out = coach.explain_move([" "] * 9, 4, "X")
    assert isinstance(out, str) and len(out) > 0


# Try changing: modify this file and re-run the tests.
