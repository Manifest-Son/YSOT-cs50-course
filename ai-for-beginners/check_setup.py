"""Verify that this machine can run the course materials.

Run with: python check_setup.py
"""

import sys

MIN_PYTHON = (3, 10)
REQUIRED = [
    ("openai", "openai"),
    ("dotenv", "python-dotenv"),
    ("sklearn", "scikit-learn"),
    ("matplotlib", "matplotlib"),
    ("numpy", "numpy"),
    ("pytest", "pytest"),
]

errors = []
warnings = []

# 1. Python version
if sys.version_info < MIN_PYTHON:
    errors.append(
        f"Python {MIN_PYTHON[0]}.{MIN_PYTHON[1]}+ is required, "
        f"you have {sys.version.split()[0]}. Install from https://www.python.org/downloads/"
    )
else:
    print(f"[OK] Python {sys.version.split()[0]}")

# 2. Packages
for module, pkg in REQUIRED:
    try:
        __import__(module)
        print(f"[OK] {pkg}")
    except ImportError:
        errors.append(f"Missing package '{pkg}'. Run: pip install -r requirements.txt")

# 3. .env
from pathlib import Path
root = Path(__file__).resolve().parent
env_file = root / ".env"
if not env_file.exists():
    warnings.append("No .env file found. Copy .env.example to .env and fill in keys.")
else:
    print("[OK] .env present")

# 4. Model access
try:
    sys.path.insert(0, str(root))
    from tools.llm_client import get_client

    try:
        client, model, source = get_client()
        print(f"[OK] Model reachable: {model} via {source}")
    except Exception as exc:
        warnings.append(f"Model not reachable: {exc}")
except Exception as exc:
    warnings.append(f"Could not check model: {exc}")

# 5. Ollama hint
import shutil

if shutil.which("ollama") is None:
    warnings.append("Ollama not found on PATH (optional, used as fallback).")

print()
if errors:
    print("SETUP INCOMPLETE. Fix these:")
    for e in errors:
        print("  - " + e)
    sys.exit(1)
if warnings:
    print("SETUP OK with warnings:")
    for w in warnings:
        print("  - " + w)
else:
    print("SETUP COMPLETE. You are ready.")


# Try changing: modify this file and re-run the tests.
