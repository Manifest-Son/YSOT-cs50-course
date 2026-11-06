"""Tiny task runner (like make). Usage: python tasks.py <task> [args].

Tasks: setup, check, test, demo <name>
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def run(cmd):
    print("$ " + " ".join(cmd))
    return subprocess.run(cmd, cwd=ROOT)


def setup():
    run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    env = ROOT / ".env"
    example = ROOT / ".env.example"
    if not env.exists() and example.exists():
        env.write_text(example.read_text())
        print("Created .env from .env.example (fill in your keys).")


def check():
    run([sys.executable, "check_setup.py"])


def test():
    run([sys.executable, "-m", "pytest", "-q"])


def demo(name):
    if not name:
        print("Usage: python tasks.py demo <name>")
        sys.exit(1)
    path = ROOT / "demos" / f"{name}.py"
    if not path.exists():
        print(f"Demo not found: {path}")
        sys.exit(1)
    run([sys.executable, str(path)])


def main():
    if len(sys.argv) < 2:
        print("Usage: python tasks.py {setup|check|test|demo <name>}")
        sys.exit(1)
    task = sys.argv[1]
    if task == "setup":
        setup()
    elif task == "check":
        check()
    elif task == "test":
        test()
    elif task == "demo":
        demo(sys.argv[2] if len(sys.argv) > 2 else "")
    else:
        print(f"Unknown task: {task}")
        sys.exit(1)


if __name__ == "__main__":
    main()


# Try changing: modify this file and re-run the tests.
