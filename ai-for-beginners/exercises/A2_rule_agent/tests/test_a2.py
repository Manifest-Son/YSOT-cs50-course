import os
import sys
import importlib.util

_here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(os.path.dirname(os.path.dirname(_here)))
sys.path.insert(0, root)
_spec = importlib.util.spec_from_file_location("A2_rule_agent_test_a2", os.path.join(os.path.dirname(_here), "starter.py"))
starter = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(starter)

def test_wins_if_possible():
    agent = starter.RuleBasedAgent()
    board = ["X", "X", " ", " ", " ", " ", " ", " ", " "]
    assert agent.choose_move(list(board), "X") == 2


def test_blocks():
    agent = starter.RuleBasedAgent()
    board = ["O", "O", " ", " ", " ", " ", " ", " ", " "]
    assert agent.choose_move(list(board), "X") == 2


# Try changing: modify this file and re-run the tests.
