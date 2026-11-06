import os
import sys
import importlib.util

_here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(os.path.dirname(os.path.dirname(_here)))
sys.path.insert(0, root)
_spec = importlib.util.spec_from_file_location("A1_board_basics_test_a1", os.path.join(os.path.dirname(_here), "starter.py"))
starter = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(starter)

def test_available_moves():
    board = ["X", " ", "O", " ", " ", " ", " ", " ", " "]
    assert starter.available_moves(board) == [1, 3, 4, 5, 6, 7, 8]


def test_winner_x():
    board = ["X", "X", "X", " ", " ", " ", " ", " ", " "]
    assert starter.winner(board) == "X"


def test_draw():
    board = ["X", "O", "X", "X", "O", "O", "O", "X", "X"]
    assert starter.winner(board) == "draw"


def test_is_full():
    assert starter.is_full(["X"] * 9) is True
    assert starter.is_full([" "] + ["X"] * 8) is False


# Try changing: modify this file and re-run the tests.
