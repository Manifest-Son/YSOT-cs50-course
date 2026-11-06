"""Tiny breakout (brick breaker) simulation.

Run: python demos/breakout.py

A ball bounces around a grid of bricks. The paddle at the bottom is
controlled by a simple rule-based AI: 'move toward the ball'. No learning,
no search - just a rule. That is the point of session 1.

Try changing:
- LIVES, WIDTH, BRICK_ROWS, or the paddle rule in ai_move().
"""

import random

WIDTH = 20
HEIGHT = 12
BRICK_ROWS = 3
LIVES = 3
MAX_TICKS = 1500
SEED = 7


def make_bricks():
    bricks = set()
    for r in range(1, 1 + BRICK_ROWS):
        for c in range(1, WIDTH - 1):
            bricks.add((r, c))
    return bricks


def ai_move(paddle_x, ball_x):
    # Rule: move one step toward the ball.
    if ball_x > paddle_x:
        return paddle_x + 1
    if ball_x < paddle_x:
        return paddle_x - 1
    return paddle_x


def run(seed=SEED):
    random.seed(seed)
    bricks = make_bricks()
    paddle_x = WIDTH // 2
    ball_x, ball_y = WIDTH // 2, HEIGHT - 2
    dx, dy = 1, -1
    lives = LIVES
    score = 0
    ticks = 0
    while ticks < MAX_TICKS and lives > 0 and bricks:
        ticks += 1
        # move paddle first (AI reacts)
        paddle_x = max(1, min(WIDTH - 2, ai_move(paddle_x, ball_x)))
        # move ball
        ball_x += dx
        ball_y += dy
        # side walls
        if ball_x <= 0 or ball_x >= WIDTH - 1:
            dx = -dx
            ball_x = max(1, min(WIDTH - 2, ball_x))
        # top wall
        if ball_y <= 0:
            dy = -dy
            ball_y = 1
        # bricks
        if (ball_y, ball_x) in bricks:
            bricks.discard((ball_y, ball_x))
            dy = -dy
            score += 1
        # paddle
        if ball_y == HEIGHT - 2 and paddle_x - 1 <= ball_x <= paddle_x + 1:
            dy = -1
            ball_y = HEIGHT - 3
        # bottom -> lose life
        if ball_y >= HEIGHT - 1:
            lives -= 1
            ball_x, ball_y = WIDTH // 2, HEIGHT - 2
            dx, dy = random.choice([-1, 1]), -1
    return score, lives, ticks, len(bricks)


def render_sample():
    score, lives, ticks, remaining = run()
    print("Breakout (rule-based AI paddle)")
    print(f"ticks={ticks} score={score} lives_left={lives} bricks_left={remaining}")
    # print a tiny final-state-ish board
    bricks = make_bricks()
    # remove 'score' bricks arbitrarily for a visual (not exact)
    print("Sample board (X=brick, -=empty, P=paddle, O=ball):")
    for r in range(HEIGHT):
        row = []
        for c in range(WIDTH):
            if r == 0 or r == HEIGHT - 1 or c == 0 or c == WIDTH - 1:
                row.append("#")
            elif (r, c) in bricks and r <= BRICK_ROWS:
                row.append("X")
            else:
                row.append(" ")
        print("".join(row))


if __name__ == "__main__":
    score, lives, ticks, remaining = run()
    print("Breakout (rule-based AI paddle)")
    print(f"ticks={ticks} score={score} lives_left={lives} bricks_left={remaining}")
