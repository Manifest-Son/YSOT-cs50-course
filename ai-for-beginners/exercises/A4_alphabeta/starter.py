"""Exercise A4: minimax with alpha-beta pruning."""

import math

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


class MinimaxABAgent:
    def __init__(self):
        self.positions_evaluated = 0

    def choose_move(self, board, player):
        self.positions_evaluated = 0
        opp = "O" if player == "X" else "X"
        _score, move = self._search(list(board), True, player, opp, -math.inf, math.inf)
        return move

    def _search(self, board, is_maximizing, ai_player, human_player, alpha, beta):
        self.positions_evaluated += 1
        res = winner(board)
        if res == ai_player:
            return 1, None
        if res == human_player:
            return -1, None
        if res == "draw":
            return 0, None
        best_score = None
        best_move = None
        current = ai_player if is_maximizing else human_player
        for m in available_moves(board):
            board[m] = current
            score, _ = self._search(board, not is_maximizing, ai_player, human_player, alpha, beta)
            board[m] = " "
            if best_score is None or (is_maximizing and score > best_score) or (not is_maximizing and score < best_score):
                best_score = score
                best_move = m
            if is_maximizing:
                alpha = max(alpha, best_score)
            else:
                beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score, best_move


# Try changing: modify this file and re-run the tests.
