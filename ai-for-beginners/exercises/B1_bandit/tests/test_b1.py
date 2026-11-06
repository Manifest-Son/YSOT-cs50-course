import os
import sys
import importlib.util

_here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(os.path.dirname(os.path.dirname(_here)))
sys.path.insert(0, root)
_spec = importlib.util.spec_from_file_location("B1_bandit_test_b1", os.path.join(os.path.dirname(_here), "starter.py"))
starter = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(starter)

def test_determinism():
    r1, c1 = starter.run_bandit(0.1, seed=5)
    r2, c2 = starter.run_bandit(0.1, seed=5)
    assert r1 == r2 and c1 == c2


def test_epsilon_zero_sticks_to_first_arm():
    avg, counts = starter.run_bandit(0.0, seed=1, n_pulls=2000)
    # with zero initial values, greedy picks the first arm and never explores
    assert counts[0] == 2000


def test_returns_tuple():
    avg, counts = starter.run_bandit(0.1, seed=1, n_pulls=10)
    assert isinstance(avg, float)
    assert len(counts) == 3


# Try changing: modify this file and re-run the tests.
