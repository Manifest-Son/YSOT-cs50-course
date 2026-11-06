"""Capstone session 3: epsilon-greedy learning agent.

Goal: implement a Q-learning agent that trains against the minimax agent.

Try changing:
- epsilon, alpha, number of training games.
"""

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


class EpsilonGreedyAgent:
    def __init__(self, epsilon=0.1, alpha=0.5, seed=None):
        self.epsilon = epsilon
        self.alpha = alpha
        self.q = {}  # state tuple -> list of 9 floats
        self.rng = random.Random(seed) if seed is not None else random

    def _q_values(self, state):
        if state not in self.q:
            self.q[state] = [0.0] * 9
        return self.q[state]

    def choose_move(self, board, player, training=False):
        moves = available_moves(board)
        if not moves:
            return None
        state = tuple(board)
        qs = self._q_values(state)
        if training and self.rng.random() < self.epsilon:
            return self.rng.choice(moves)
        return max(moves, key=lambda m: qs[m])

    def train(self, opponent, games=200, agent_player="X"):
        opp_player = "O" if agent_player == "X" else "X"
        for _ in range(games):
            board = [" "] * 9
            history = []
            current = "X"
            if agent_player == "O":
                mv = opponent.choose_move(list(board), "X")
                board[mv] = "X"
                current = "O"
            while winner(board) is None and available_moves(board):
                if current == agent_player:
                    state = tuple(board)
                    action = self.choose_move(board, agent_player, training=True)
                    history.append((state, action))
                    board[action] = agent_player
                else:
                    mv = opponent.choose_move(list(board), opp_player)
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
                qs = self._q_values(state)
                qs[action] += self.alpha * (reward - qs[action])


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
