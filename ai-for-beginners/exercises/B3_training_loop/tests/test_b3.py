import os
import sys
import importlib.util

_here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(os.path.dirname(os.path.dirname(_here)))
sys.path.insert(0, root)
_spec = importlib.util.spec_from_file_location("B3_training_loop_test_b3", os.path.join(os.path.dirname(_here), "starter.py"))
starter = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(starter)

class FirstAgent:
    def choose_move(self, board, player):
        return starter.available_moves(board)[0]


def test_train_one_updates_q():
    agent = starter.SimpleQAgent(epsilon=0.2, seed=1)
    opp = FirstAgent()
    r = agent.train_one(opp, agent_player="X")
    assert isinstance(r, float)
    assert len(agent.q) > 0


def test_multiple_games():
    agent = starter.SimpleQAgent(epsilon=0.2, seed=2)
    opp = FirstAgent()
    for _ in range(20):
        agent.train_one(opp, agent_player="X")
    assert len(agent.q) > 5


# Try changing: modify this file and re-run the tests.
