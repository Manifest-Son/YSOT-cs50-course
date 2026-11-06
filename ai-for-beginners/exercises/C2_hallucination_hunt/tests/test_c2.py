import os
import sys
import importlib.util

_here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(os.path.dirname(os.path.dirname(_here)))
sys.path.insert(0, root)
_spec = importlib.util.spec_from_file_location("C2_hallucination_hunt_test_c2", os.path.join(os.path.dirname(_here), "starter.py"))
starter = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(starter)

def test_supported():
    src = "minimax searches all positions and never learns"
    ans = "Minimax searches all positions."
    assert starter.unsupported_sentences(ans, src) == []


def test_unsupported():
    src = "minimax searches all positions"
    ans = "Minimax learns from data."
    out = starter.unsupported_sentences(ans, src)
    assert len(out) == 1


# Try changing: modify this file and re-run the tests.
