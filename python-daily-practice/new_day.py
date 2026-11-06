"""Create a new "Day N" practice folder from the files in _template/.

Usage (run from python-daily-practice/):
    python new_day.py                       # next day number after the highest existing one
    python new_day.py 7                     # a specific day number
    python new_day.py --title "Loops"       # also fill in the title

Template files end in ".tmpl". Inside them, these placeholders are replaced:
    {{N}}      day number            -> 7
    {{NN}}     zero-padded number    -> 07
    {{TITLE}}  the title             -> Loops
    {{DATE}}   today's date          -> 2026-11-06
In file names, "_NN" becomes "_07" (day_NN.py.tmpl -> day_07.py).

Every new day contains "TODO(author)" markers. tests/test_structure.py fails
until they are all replaced, so a day cannot be left half-written.
"""

import argparse
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TEMPLATE_DIR = ROOT / "_template"
DAY_DIR_RE = re.compile(r"^Day ([1-9]\d*)$")


def existing_day_numbers():
    numbers = []
    for path in ROOT.iterdir():
        match = DAY_DIR_RE.match(path.name)
        if path.is_dir() and match:
            numbers.append(int(match.group(1)))
    return sorted(numbers)


def render(text, values):
    for key, value in values.items():
        text = text.replace("{{" + key + "}}", value)
    return text


def create_day(number, title):
    target = ROOT / f"Day {number}"
    if target.exists():
        raise SystemExit(f"error: '{target.name}' already exists; refusing to overwrite it.")

    templates = sorted(TEMPLATE_DIR.glob("*.tmpl"))
    if not templates:
        raise SystemExit(f"error: no *.tmpl files found in {TEMPLATE_DIR}")

    padded = f"{number:02d}"
    values = {
        "N": str(number),
        "NN": padded,
        "TITLE": title,
        "DATE": date.today().isoformat(),
    }

    target.mkdir()
    created = []
    for template in templates:
        file_name = template.name[: -len(".tmpl")].replace("_NN", "_" + padded)
        content = render(template.read_text(encoding="utf-8"), values)
        (target / file_name).write_text(content, encoding="utf-8", newline="\n")
        created.append(file_name)
    return target, created


def main():
    parser = argparse.ArgumentParser(description="Create a new 'Day N' practice folder.")
    parser.add_argument("number", nargs="?", type=int, help="day number (default: next after the highest existing)")
    parser.add_argument("--title", default="TODO(author): title", help="short title for the day")
    args = parser.parse_args()

    days = existing_day_numbers()
    number = args.number if args.number is not None else (days[-1] + 1 if days else 1)
    if number < 1:
        raise SystemExit("error: the day number must be 1 or higher.")

    target, created = create_day(number, args.title)

    print(f"Created {target.name}/")
    for name in created:
        print(f"  - {name}")
    print()
    print("Next steps:")
    print(f"  1. Write the task in '{target.name}/README.md' and replace every TODO(author).")
    print(f"  2. Fill in the starter and the tests in '{target.name}/'.")
    print("  3. Add a row for the day to the table in this module's README.md.")
    print("  4. python -m pytest tests -q   (the structure check must pass)")


if __name__ == "__main__":
    main()
