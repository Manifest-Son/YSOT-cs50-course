import os
import sys
import importlib.util

_here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(os.path.dirname(os.path.dirname(_here)))
sys.path.insert(0, root)
_spec = importlib.util.spec_from_file_location("session5_showcase_test_session5", os.path.join(os.path.dirname(_here), "starter.py"))
starter = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(starter)

import importlib.util

rb_spec = importlib.util.spec_from_file_location("rb", os.path.join(root, "capstone", "session1_rules", "starter.py"))
rb = importlib.util.module_from_spec(rb_spec); rb_spec.loader.exec_module(rb)
mm_spec = importlib.util.spec_from_file_location("mm", os.path.join(root, "capstone", "session2_minimax", "starter.py"))
mm = importlib.util.module_from_spec(mm_spec); mm_spec.loader.exec_module(mm)


def test_tournament_returns_scores():
    agents = {"rules": rb.RuleBasedAgent(), "minimax": mm.MinimaxAgent()}
    scores = starter.run_tournament(agents, games_per_pair=2)
    assert isinstance(scores, dict)
    assert set(scores.keys()) == {"rules", "minimax"}
    assert scores["minimax"] >= scores["rules"], scores


def test_tournament_nonempty():
    agents = [rb.RuleBasedAgent(), mm.MinimaxAgent()]
    scores = starter.run_tournament(agents, games_per_pair=1)
    assert len(scores) == 2


# Try changing: modify this file and re-run the tests.
