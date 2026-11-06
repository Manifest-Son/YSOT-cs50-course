import os
import sys
import importlib.util

_here = os.path.dirname(os.path.abspath(__file__))
root = os.path.dirname(os.path.dirname(os.path.dirname(_here)))
sys.path.insert(0, root)
_spec = importlib.util.spec_from_file_location("session2_minimax_test_session2", os.path.join(os.path.dirname(_here), "starter.py"))
starter = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(starter)

def test_position_counter_increments():
    agent = starter.MinimaxAgent()
    board = [" "] * 9
    move = agent.choose_move(board, "X")
    assert move is not None, "choose_move returned None; implement minimax"
    assert agent.positions_evaluated > 0, "positions_evaluated should be > 0"


def test_never_loses_all_first_moves():
    # Opponent (X) tries every possible first square; AI (O) must not lose.
    for first in range(9):
        board = [" "] * 9
        board[first] = "X"
        agent_x = starter.MinimaxAgent()
        agent_o = starter.MinimaxAgent()
        # Now play optimally from both sides.
        current = "O"
        while starter.winner(board) is None and starter.available_moves(board):
            agent = agent_x if current == "X" else agent_o
            move = agent.choose_move(list(board), current)
            assert move is not None and board[move] == " ", f"bad move {move}"
            board[move] = current
            current = "O" if current == "X" else "X"
        result = starter.winner(board)
        assert result != "X", f"AI lost when opponent opened at {first} (result={result})"


def test_center_or_corner_first_move():
    agent = starter.MinimaxAgent()
    move = agent.choose_move([" "] * 9, "X")
    assert move in (0, 2, 4, 6, 8), f"first move {move} not a corner/centre"


# Try changing: modify this file and re-run the tests.
