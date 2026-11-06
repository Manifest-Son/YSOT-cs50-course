"""Capstone session 2: minimax tic-tac-toe agent.

Goal: implement minimax so the agent never loses.

Try changing:
- Add alpha-beta pruning and compare positions_evaluated.
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


class MinimaxAgent:
    def __init__(self):
        self.positions_evaluated = 0

    def choose_move(self, board, player):
        self.positions_evaluated = 0
        opp = "O" if player == "X" else "X"
        _score, move = self._minimax(list(board), True, player, opp)
        return move

    def _minimax(self, board, is_maximizing, ai_player, human_player):
        self.positions_evaluated += 1
        # winner check on board
        res = None
        for a, b, c in WINS:
            if board[a] == board[b] == board[c] != " ":
                res = board[a]
                break
        if res == ai_player:
            return 1, None
        if res == human_player:
            return -1, None
        if " " not in board:
            return 0, None
        best_score = None
        best_move = None
        current = ai_player if is_maximizing else human_player
        for m in [i for i, v in enumerate(board) if v == " "]:
            board[m] = current
            score, _ = self._minimax(board, not is_maximizing, ai_player, human_player)
            board[m] = " "
            if best_score is None or (is_maximizing and score > best_score) or (not is_maximizing and score < best_score):
                best_score = score
                best_move = m
                if is_maximizing and best_score == 1:
                    break
                if not is_maximizing and best_score == -1:
                    break
        return best_score, best_move


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
