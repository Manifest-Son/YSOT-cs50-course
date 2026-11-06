# Common errors

- Forgetting to activate venv -> "module not found". Fix: python -m venv .venv.
- Mutating board without undo in minimax -> wrong results. Fix: undo move.
- Off-by-one in epsilon comparison -> always explore. Fix: random.random() < epsilon.
- String-building prompts with user input -> injection. Fix: message dicts.
