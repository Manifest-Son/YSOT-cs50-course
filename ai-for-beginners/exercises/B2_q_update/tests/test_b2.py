import os
import sys
import importlib.util

_here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(os.path.dirname(os.path.dirname(_here)))
sys.path.insert(0, root)
_spec = importlib.util.spec_from_file_location("B2_q_update_test_b2", os.path.join(os.path.dirname(_here), "starter.py"))
starter = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(starter)

def test_update_moves_toward_reward():
    q = {}
    state = (" ",) * 9
    starter.update_q(q, state, 4, 1.0, alpha=0.5)
    assert q[state][4] == 0.5


def test_zero_alpha_no_change():
    q = {(" ",) * 9: [0.1] * 9}
    state = (" ",) * 9
    starter.update_q(q, state, 4, 1.0, alpha=0.0)
    assert q[state][4] == 0.1


# Try changing: modify this file and re-run the tests.
