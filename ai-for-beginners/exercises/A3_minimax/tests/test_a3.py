import os
import sys
import importlib.util

_here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(os.path.dirname(os.path.dirname(_here)))
sys.path.insert(0, root)
_spec = importlib.util.spec_from_file_location("A3_minimax_test_a3", os.path.join(os.path.dirname(_here), "starter.py"))
starter = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(starter)

def test_never_loses():
    for first in range(9):
        board = [" "] * 9
        board[first] = "X"
        ax = starter.MinimaxAgent()
        ao = starter.MinimaxAgent()
        current = "O"
        while starter.winner(board) is None and starter.available_moves(board):
            agent = ax if current == "X" else ao
            move = agent.choose_move(list(board), current)
            board[move] = current
            current = "O" if current == "X" else "X"
        assert starter.winner(board) != "X"


# Try changing: modify this file and re-run the tests.
