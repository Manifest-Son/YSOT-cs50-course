"""Plot bandit / epsilon experiment CSVs produced by the course.

Usage:
    python tools/plot_results.py path/to/results.csv

The CSV is expected to have columns: epsilon,avg_reward (or similar).
The script tries to be forgiving about column names.

Try changing:
- FIGSIZE: size of the output figure.
- OUTPUT: where the PNG is saved.
"""

import csv
import sys
from pathlib import Path

import matplotlib.pyplot as plt

FIGSIZE = (8, 5)
OUTPUT = "experiment_plot.png"


def _find_col(headers, candidates):
    low = [h.strip().lower() for h in headers]
    for c in candidates:
        if c in low:
            return headers[low.index(c)]
    return None


def plot(csv_path):
    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    if not rows:
        raise ValueError("CSV is empty")
    headers = list(rows[0].keys())
    xcol = _find_col(headers, ["epsilon", "eps", "x"])
    ycol = _find_col(headers, ["avg_reward", "average_reward", "reward", "y", "win_rate"])
    if xcol is None or ycol is None:
        raise ValueError(f"Could not find x/y columns in {headers}")

    xs = [float(r[xcol]) for r in rows]
    ys = [float(r[ycol]) for r in rows]

    plt.figure(figsize=FIGSIZE)
    plt.plot(xs, ys, marker="o")
    plt.xlabel(xcol)
    plt.ylabel(ycol)
    plt.title("Experiment results")
    plt.grid(True, alpha=0.3)
    out = Path(csv_path).with_suffix(".png")
    plt.savefig(out)
    print(f"Saved plot to {out}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python tools/plot_results.py <csv_file>")
        sys.exit(1)
    plot(sys.argv[1])


if __name__ == "__main__":
    main()
