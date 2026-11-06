# AI Practical: Introduction to Artificial Intelligence

A beginner-friendly, 6-session hands-on course. Python 3.10+.

## What this is
Six 90-minute sessions in pairs (driver/navigator, swap every 15 min).
Capstone: "Game Night" tic-tac-toe bot that grows across the course.

## Setup
See SETUP.md. Quick version:
```
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python check_setup.py
```

## How sessions work
Each session README has "Predict before you run" and "Explain it back".
Run demos:
```
python demos/breakout.py
python demos/tictactoe.py
python demos/bandit.py
python demos/chat.py --system "You are a tutor."
```

## Sample outputs
breakout.py:
```
Breakout (rule-based AI paddle)
ticks=386 score=54 lives_left=3 bricks_left=0
```
bandit.py (seed=42):
```
 epsilon   avg_reward               counts
    0.00       0.1955         [2000, 0, 0]
    0.10       0.7485      [129, 72, 1799]
```

## Tasks
```
python tasks.py setup
python tasks.py check
python tasks.py test
python tasks.py demo tictactoe
```
