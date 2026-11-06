# Capstone Session 4 - LLM coach

## Goals
- Use an LLM to explain a move in plain English.
- Handle missing models gracefully.

## Predict before you run
1. What happens if the LLM hallucinates a rule?

## Definition of done
- [ ] `explain_move` returns a non-empty string.
- [ ] Falls back gracefully with no model.
- [ ] Tests pass.

## Explain it back
- Why must user input go through message fields, not string-built prompts?
