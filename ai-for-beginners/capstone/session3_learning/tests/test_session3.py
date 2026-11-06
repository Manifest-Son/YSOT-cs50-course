import os
import sys
import importlib.util

_here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(os.path.dirname(os.path.dirname(_here)))
sys.path.insert(0, root)
_spec = importlib.util.spec_from_file_location("session3_learning_test_session3", os.path.join(os.path.dirname(_here), "starter.py"))
starter = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(starter)

import importlib.util

# load minimax agent from session2
spec = importlib.util.spec_from_file_location(
    "minimax_starter",
    os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))), "capstone", "session2_minimax", "starter.py"),
)
mm = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mm)


def test_seed_determinism():
    a = starter.EpsilonGreedyAgent(epsilon=0.1, seed=123)
    b = starter.EpsilonGreedyAgent(epsilon=0.1, seed=123)
    board = [" "] * 9
    m1 = a.choose_move(list(board), "X", training=True)
    m2 = b.choose_move(list(board), "X", training=True)
    assert m1 == m2, "same seed should give same move"


def test_trains_and_does_not_lose():
    random_seed = 7
    import random
    random.seed(random_seed)
    agent = starter.EpsilonGreedyAgent(epsilon=0.2, alpha=0.5, seed=random_seed)
    opp = mm.MinimaxAgent()
    agent.train(opp, games=300, agent_player="X")
    # evaluate greedily
    losses = 0
    games = 40
    for _ in range(games):
        board = [" "] * 9
        current = "X"
        while starter.winner(board) is None and starter.available_moves(board):
            if current == "X":
                move = agent.choose_move(list(board), "X")
            else:
                move = opp.choose_move(list(board), "O")
            board[move] = current
            current = "O" if current == "X" else "X"
        if starter.winner(board) == "O":
            losses += 1
    assert losses == 0, f"agent lost {losses}/{games} games to minimax"


def test_q_table_nonempty_after_training():
    agent = starter.EpsilonGreedyAgent(epsilon=0.2, seed=1)
    opp = mm.MinimaxAgent()
    agent.train(opp, games=50, agent_player="X")
    assert len(agent.q) > 0, "q-table empty after training"


# Try changing: modify this file and re-run the tests.
