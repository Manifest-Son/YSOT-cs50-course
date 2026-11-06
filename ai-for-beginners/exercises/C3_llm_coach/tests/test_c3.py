import os
import sys
import importlib.util

_here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(os.path.dirname(os.path.dirname(_here)))
sys.path.insert(0, root)
_spec = importlib.util.spec_from_file_location("C3_llm_coach_test_c3", os.path.join(os.path.dirname(_here), "starter.py"))
starter = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(starter)

def test_fallback(monkeypatch):
    from tools.llm_client import NoModelAvailableError
    def boom(system, user):
        raise NoModelAvailableError("x")
    monkeypatch.setattr(starter, "chat", boom)
    coach = starter.LLMCoach()
    out = coach.explain_move([" "] * 9, 4, "X")
    assert isinstance(out, str) and "4" in out


# Try changing: modify this file and re-run the tests.
