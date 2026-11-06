"""Tic-tac-toe with a minimax AI that never loses.

Run: python demos/tictactoe.py

The AI (O) uses minimax with alpha-beta pruning? No pruning here, just
plain minimax, so you can count exactly how many positions it examines.
A position counter is printed after each move.

Try changing:
- Change PLAYER_X / PLAYER_O to swap who goes first.
- Remove the position counter and see if you miss it.
"""

import sys
from pathlib import Path

# Make sure project root is importable when run directly.
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

EMPTY = " "
X = "X"
O = "O"

WINS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
]


class TicTacToe:
    def __init__(self):
        self.board = [EMPTY] * 9
        self.positions_evaluated = 0

    def print_board(self):
        b = self.board
        print(f" {b[0]} | {b[1]} | {b[2]} ")
        print("---+---+---")
        print(f" {b[3]} | {b[4]} | {b[5]} ")
        print("---+---+---")
        print(f" {b[6]} | {b[7]} | {b[8]} ")
        print()

    def winner(self):
        for a, b, c in WINS:
            if self.board[a] == self.board[b] == self.board[c] != EMPTY:
                return self.board[a]
        if EMPTY not in self.board:
            return "draw"
        return None

    def available_moves(self):
        return [i for i, v in enumerate(self.board) if v == EMPTY]

    def make_move(self, idx, player):
        self.board[idx] = player

    def undo_move(self, idx):
        self.board[idx] = EMPTY

    def minimax(self, is_maximizing, ai_player, human_player):
        """Return (score, move). Score: +1 win for ai, -1 loss, 0 draw."""
        self.positions_evaluated += 1
        result = self.winner()
        if result == ai_player:
            return 1, None
        if result == human_player:
            return -1, None
        if result == "draw":
            return 0, None

        best_score = None
        best_move = None
        for move in self.available_moves():
            self.make_move(move, ai_player if is_maximizing else human_player)
            score, _ = self.minimax(not is_maximizing, ai_player, human_player)
            self.undo_move(move)
            if best_score is None or (
                is_maximizing and score > best_score
            ) or (
                not is_maximizing and score < best_score
            ):
                best_score = score
                best_move = move
                if is_maximizing and best_score == 1:
                    break
                if not is_maximizing and best_score == -1:
                    break
        return best_score, best_move

    def best_move_for(self, ai_player, human_player):
        self.positions_evaluated = 0
        _score, move = self.minimax(True, ai_player, human_player)
        return move


def play_demo():
    game = TicTacToe()
    # AI plays both sides? Here X is "AI X", O is "AI O", both minimax.
    # To make it a real contest, X plays first with a fixed opening and O responds.
    # Simpler: X uses minimax too (so game is a draw).
    players = [X, O]
    turn = 0
    print("Tic-tac-toe: minimax vs minimax (always a draw).\n")
    while game.winner() is None:
        player = players[turn % 2]
        opponent = players[(turn + 1) % 2]
        move = game.best_move_for(player, opponent)
        print(f"{player} plays square {move} (evaluated {game.positions_evaluated} positions)")
        game.make_move(move, player)
        game.print_board()
        turn += 1
    result = game.winner()
    print("Result:", "Draw" if result == "draw" else f"{result} wins!")


if __name__ == "__main__":
    play_demo()
