# Decisions

- LLM access: both OpenAI-compatible and Ollama fallback; Ollama optional.
- Python 3.10+ target; pinned versions support 3.10 where possible (scikit-learn 1.5.2 etc).
- tictactoe minimax uses plain minimax (no alpha-beta) in capstone; alpha-beta is an exercise.
- Learning agent trains only as X against minimax.
- Tests import starter via importlib to avoid module-name collisions.
- No .env present in repo; students create from .env.example.
