"""Exercise B2: Q-value update rule."""


def update_q(q_table, state, action, reward, alpha=0.5):
    if state not in q_table:
        q_table[state] = [0.0] * 9
    old = q_table[state][action]
    q_table[state][action] = old + alpha * (reward - old)
    return q_table


# Try changing: modify this file and re-run the tests.
