# Capstone Session 1 - Rule-based agent

## Goals
- Understand the difference between rules, search, and learning.
- Implement a tic-tac-toe agent that follows priority rules.

## Predict before you run
1. If a rule-based agent always takes the centre first, can it ever lose to a perfect player?
2. What is the smallest set of rules that never loses at tic-tac-toe?

## Definition of done
- [ ] `choose_move` returns a valid empty square index.
- [ ] Agent takes an immediate win.
- [ ] Agent blocks an immediate loss.
- [ ] Tests pass: `python -m pytest capstone/session1_rules/tests -q`

## Explain it back
- Why is this agent not "learning"?
- Which rule matters most and why?
