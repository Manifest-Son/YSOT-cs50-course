"""Multi-armed bandit: explore vs exploit.

Run: python demos/bandit.py

Three slot machines with different (hidden) win rates. An epsilon-greedy
agent picks the best-known machine most of the time and explores randomly
the rest. Watch how epsilon changes total reward.

Try changing:
- N_ARMS, TRUE_REWARDS, N_PULLS, or the list of epsilons.
- Set seed to a different number for a different "luck".
"""

import argparse
import random

N_ARMS = 3
TRUE_REWARDS = [0.2, 0.5, 0.8]   # hidden win probabilities
N_PULLS = 2000
EPSILONS = [0.0, 0.01, 0.1, 0.3, 0.5]
SEED = 42


def run_bandit(epsilon, seed=SEED, n_pulls=N_PULLS):
    random.seed(seed)
    counts = [0] * N_ARMS
    values = [0.0] * N_ARMS
    total_reward = 0.0
    for _ in range(n_pulls):
        if random.random() < epsilon:
            arm = random.randrange(N_ARMS)
        else:
            # exploit: pick arm with highest estimated value (ties -> first)
            arm = max(range(N_ARMS), key=lambda i: values[i])
        reward = 1.0 if random.random() < TRUE_REWARDS[arm] else 0.0
        counts[arm] += 1
        # incremental mean
        values[arm] += (reward - values[arm]) / counts[arm]
        total_reward += reward
    return total_reward / n_pulls, counts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seed", type=int, default=SEED)
    args = parser.parse_args()
    print(f"Bandit experiment (seed={args.seed}, pulls={N_PULLS})")
    print(f"True rewards: {TRUE_REWARDS}")
    print(f"{'epsilon':>8} {'avg_reward':>12} {'counts':>20}")
    for eps in EPSILONS:
        avg, counts = run_bandit(eps, seed=args.seed)
        print(f"{eps:>8.2f} {avg:>12.4f} {str(counts):>20}")


if __name__ == "__main__":
    main()
