"""Exercise B3: one training game for a Q-learning agent."""

import random

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


class SimpleQAgent:
    def __init__(self, epsilon=0.2, alpha=0.5, seed=None):
        self.epsilon = epsilon
        self.alpha = alpha
        self.q = {}
        if seed is not None:
            random.seed(seed)

    def _qvalues(self, state):
        if state not in self.q:
            self.q[state] = [0.0] * 9
        return self.q[state]

    def choose_move(self, board, player, training=False):
        moves = available_moves(board)
        if not moves:
            return None
        qs = self._qvalues(tuple(board))
        if training and random.random() < self.epsilon:
            return random.choice(moves)
        return max(moves, key=lambda m: qs[m])

    def train_one(self, opponent, agent_player="X"):
        opp_player = "O" if agent_player == "X" else "X"
        board = [" "] * 9
        history = []
        current = "X"
        if agent_player == "O":
            mv = opponent.choose_move(list(board), "X") if hasattr(opponent, "choose_move") else None
            if mv is None:
                mv = available_moves(board)[0]
            board[mv] = "X"
            current = "O"
        while winner(board) is None and available_moves(board):
            if current == agent_player:
                state = tuple(board)
                action = self.choose_move(board, agent_player, training=True)
                history.append((state, action))
                board[action] = agent_player
            else:
                if hasattr(opponent, "choose_move"):
                    mv = opponent.choose_move(list(board), opp_player)
                else:
                    mv = available_moves(board)[0]
                board[mv] = opp_player
            current = "O" if current == "X" else "X"
        result = winner(board)
        if result == agent_player:
            reward = 1.0
        elif result == "draw":
            reward = 0.0
        else:
            reward = -1.0
        for state, action in history:
            qs = self._qvalues(state)
            qs[action] += self.alpha * (reward - qs[action])
        return reward


# Try changing: modify this file and re-run the tests.
