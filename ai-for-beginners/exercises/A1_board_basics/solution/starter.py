"""Exercise A1: board basics (available moves, winner, draw)."""

WINS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
]


def available_moves(board):
    return [i for i, v in enumerate(board) if v == " "]


def winner(board):
    for a, b, c in WINS:
        if board[a] == board[b] == board[c] != " ":
            return board[a]
    if " " not in board:
        return "draw"
    return None


def is_full(board):
    return " " not in board


# Try changing: modify this file and re-run the tests.
