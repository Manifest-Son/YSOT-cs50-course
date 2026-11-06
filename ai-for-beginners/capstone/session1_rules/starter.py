"""Capstone session 1: a rule-based tic-tac-toe agent.

Goal: implement RuleBasedAgent.choose_move so it never misses a forced win
and blocks a forced loss. See README.md for the definition of done.

Try changing:
- The priority order of the rules.
"""

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


class RuleBasedAgent:
    def __init__(self, seed=None):
        self.seed = seed

    def choose_move(self, board, player):
        opp = "O" if player == "X" else "X"
        moves = available_moves(board)
        # 1. Win now.
        for m in moves:
            board[m] = player
            if winner(board) == player:
                board[m] = " "
                return m
            board[m] = " "
        # 2. Block.
        for m in moves:
            board[m] = opp
            if winner(board) == opp:
                board[m] = " "
                return m
            board[m] = " "
        # 3. Centre.
        if 4 in moves:
            return 4
        # 4. Corners.
        for c in (0, 2, 6, 8):
            if c in moves:
                return c
        # 5. Sides.
        return moves[0] if moves else None


def play_game(agent_x, agent_o):
    board = [" "] * 9
    current = "X"
    while winner(board) is None and available_moves(board):
        agent = agent_x if current == "X" else agent_o
        move = agent.choose_move(list(board), current)
        if move is None or board[move] != " ":
            raise ValueError(f"Invalid move {move} by {current}")
        board[move] = current
        current = "O" if current == "X" else "X"
    return winner(board)
