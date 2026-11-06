import os
import sys
import importlib.util

_here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(os.path.dirname(os.path.dirname(_here)))
sys.path.insert(0, root)
_spec = importlib.util.spec_from_file_location("session1_rules_test_session1", os.path.join(os.path.dirname(_here), "starter.py"))
starter = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(starter)

def test_returns_valid_move():
    agent = starter.RuleBasedAgent()
    board = [" "] * 9
    move = agent.choose_move(list(board), "X")
    assert move is not None, "choose_move returned None; implement the TODO"
    assert isinstance(move, int), "choose_move must return an int"
    assert 0 <= move <= 8, f"move {move} out of range 0-8"
    assert board[move] == " ", f"move {move} is not on an empty square"


def test_wins_if_possible():
    agent = starter.RuleBasedAgent()
    # X can win at square 2 (top row 0,1,2)
    board = ["X", "X", " ", " ", " ", " ", " ", " ", " "]
    move = agent.choose_move(list(board), "X")
    assert move == 2, f"expected winning move 2, got {move}"


def test_blocks_opponent_win():
    agent = starter.RuleBasedAgent()
    board = ["O", "O", " ", " ", " ", " ", " ", " ", " "]
    move = agent.choose_move(list(board), "X")
    assert move == 2, f"expected blocking move 2, got {move}"


def test_never_returns_occupied():
    agent = starter.RuleBasedAgent()
    board = ["X", "O", "X", " ", " ", " ", " ", " ", " "]
    for _ in range(5):
        move = agent.choose_move(list(board), "O")
        assert move in (3, 4, 5, 6, 7, 8), f"move {move} not empty/valid"


# Try changing: modify this file and re-run the tests.
