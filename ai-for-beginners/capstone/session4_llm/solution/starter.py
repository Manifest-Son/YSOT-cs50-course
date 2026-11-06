"""Capstone session 4: LLM coach that explains moves in plain English.

Goal: implement LLMCoach.explain_move.

Try changing:
- The system prompt.
"""

import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)

from tools.llm_client import chat, NoModelAvailableError

WINS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
]


def available_moves(board):
    return [i for i, v in enumerate(board) if v == " "]


class LLMCoach:
    def __init__(self, system_prompt=None):
        self.system_prompt = system_prompt or (
            "You are a friendly tic-tac-toe coach. Explain a move in 2-3 short "
            "sentences for a beginner. Do not make up rules."
        )

    def explain_move(self, board, move, player):
        board_text = " | ".join(
            [board[i] if board[i] != " " else str(i) for i in range(9)]
        )
        user_prompt = (
            f"Board (numbers are empty squares): {board_text}. "
            f"Player {player} plays square {move}. "
            f"Explain why this is a reasonable move in plain English."
        )
        try:
            return chat(self.system_prompt, user_prompt)
        except NoModelAvailableError:
            return (
                f"Square {move} is chosen for player {player}. "
                "No language model is available, so this is a placeholder explanation."
            )
