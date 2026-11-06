"""Exercise B1: multi-armed bandit epsilon-greedy."""

import random

TRUE_REWARDS = [0.2, 0.5, 0.8]
N_ARMS = 3


def run_bandit(epsilon, seed=0, n_pulls=1000):
    random.seed(seed)
    counts = [0] * N_ARMS
    values = [0.0] * N_ARMS
    total = 0.0
    for _ in range(n_pulls):
        if random.random() < epsilon:
            arm = random.randrange(N_ARMS)
        else:
            arm = max(range(N_ARMS), key=lambda i: values[i])
        reward = 1.0 if random.random() < TRUE_REWARDS[arm] else 0.0
        counts[arm] += 1
        values[arm] += (reward - values[arm]) / counts[arm]
        total += reward
    return total / n_pulls, counts


# Try changing: modify this file and re-run the tests.
