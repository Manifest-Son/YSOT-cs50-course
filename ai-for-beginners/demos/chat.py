"""Chat with a language model from the terminal.

Run: python demos/chat.py
     python demos/chat.py --system "You are a pirate."

Type 'quit' to exit. Reads config from .env.

Try changing:
- The default system prompt below.
- Temperature in llm_client.chat().
"""

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from tools.llm_client import chat, NoModelAvailableError

# System prompt
DEFAULT_SYSTEM = "You are Lenny AI, a CS50 computer scientist"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--system", default=DEFAULT_SYSTEM, help="system prompt")
    args = parser.parse_args()

    print("Chat (type 'quit' to exit)")
    print(f"System: {args.system}")
    while True:
        try:
            user = input("you> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if user.lower() in {"quit", "exit", "q"}:
            break
        if not user:
            continue
        try:
            reply = chat(args.system, user)
        except NoModelAvailableError as exc:
            print(f"error> {exc}")
            break
        except Exception as exc:  # pragma: no cover - network errors
            print(f"error> {exc}")
            continue
        print(f"ai> {reply}")


if __name__ == "__main__":
    main()
