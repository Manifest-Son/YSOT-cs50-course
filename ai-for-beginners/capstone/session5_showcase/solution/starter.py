"""Capstone session 5: showcase tournament.

Goal: run a round-robin tournament between agents and print a scoreboard.
"""

import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT)


def run_tournament(agents, games_per_pair=4):
    if isinstance(agents, dict):
        items = list(agents.items())
    else:
        items = [(getattr(a, "name", f"agent{i}"), a) for i, a in enumerate(agents)]
    names = [n for n, _ in items]
    scores = {n: 0.0 for n in names}
    for i, (n1, a1) in enumerate(items):
        for j, (n2, a2) in enumerate(items):
            if i == j:
                continue
            for g in range(games_per_pair):
                # alternate who is X
                if g % 2 == 0:
                    result = play_game(a1, a2)
                    if result == "X":
                        scores[n1] += 1
                    elif result == "draw":
                        scores[n1] += 0.5
                        scores[n2] += 0.5
                    else:
                        scores[n2] += 1
                else:
                    result = play_game(a2, a1)
                    if result == "X":
                        scores[n2] += 1
                    elif result == "draw":
                        scores[n1] += 0.5
                        scores[n2] += 0.5
                    else:
                        scores[n1] += 1
    return scores


def play_game(agent_x, agent_o):
    # reuse standard tic-tac-toe
    WINS = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6),
    ]

    def winner(b):
        for a, c, d in WINS:
            if b[a] == b[c] == b[d] != " ":
                return b[a]
        if " " not in b:
            return "draw"
        return None

    def avail(b):
        return [i for i, v in enumerate(b) if v == " "]

    board = [" "] * 9
    current = "X"
    while winner(board) is None and avail(board):
        agent = agent_x if current == "X" else agent_o
        move = agent.choose_move(list(board), current)
        if move is None or board[move] != " ":
            raise ValueError(f"Invalid move {move}")
        board[move] = current
        current = "O" if current == "X" else "X"
    return winner(board)


# Try changing: modify this file and re-run the tests.
