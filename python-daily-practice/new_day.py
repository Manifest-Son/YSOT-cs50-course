"""Create a new "Day N" practice folder inside a level, from the files in _template/.

Usage (run from python-daily-practice/):
    python new_day.py --title "Loops"                      # next day in the newest level
    python new_day.py 7 --level 2 --title "Dictionaries"   # a specific day in level 2
    python new_day.py --style functions --title "Fees"     # starter made of functions

Styles:
    script     (default) the student writes top-level code using input()/print()
    functions  the starter has function stubs for the student to fill in

Template files end in ".tmpl". Inside them, these placeholders are replaced:
    {{N}}      day number            -> 7
    {{NN}}     zero-padded number    -> 07
    {{TITLE}}  the title             -> Loops
    {{DATE}}   today's date          -> 2026-11-06
    {{LEVEL}}  the level folder      -> level-1-beginner
In file names, "_NN" becomes "_07" (day_NN.py.tmpl -> day_07.py).

Every new day contains "TODO(author)" markers. check_days.py reports them until
they are all replaced, so a day cannot be left half-written.
"""

import argparse
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TEMPLATE_DIR = ROOT / "_template"
STYLES = ("script", "functions")
LEVEL_DIR_RE = re.compile(r"^level-([1-9]\d*)-[a-z0-9]+(?:-[a-z0-9]+)*$")
DAY_DIR_RE = re.compile(r"^Day ([1-9]\d*)$")


def level_dirs():
    found = {}
    for path in ROOT.iterdir():
        match = LEVEL_DIR_RE.match(path.name)
        if path.is_dir() and match:
            found[int(match.group(1))] = path
    return found


def existing_day_numbers(level_dir):
    numbers = []
    for path in level_dir.iterdir():
        match = DAY_DIR_RE.match(path.name)
        if path.is_dir() and match:
            numbers.append(int(match.group(1)))
    return sorted(numbers)


def render(text, values):
    for key, value in values.items():
        text = text.replace("{{" + key + "}}", value)
    return text


def create_day(level_dir, number, title, style):
    target = level_dir / f"Day {number}"
    if target.exists():
        raise SystemExit(f"error: '{level_dir.name}/{target.name}' already exists; refusing to overwrite it.")

    templates = sorted((TEMPLATE_DIR / "common").glob("*.tmpl")) + sorted((TEMPLATE_DIR / style).glob("*.tmpl"))
    if not templates:
        raise SystemExit(f"error: no *.tmpl files found for style '{style}' in {TEMPLATE_DIR}")

    padded = f"{number:02d}"
    values = {
        "N": str(number),
        "NN": padded,
        "TITLE": title,
        "DATE": date.today().isoformat(),
        "LEVEL": level_dir.name,
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
    parser.add_argument("number", nargs="?", type=int, help="day number (default: next after the highest in the level)")
    parser.add_argument("--level", type=int, help="level number (default: the newest level)")
    parser.add_argument("--style", choices=STYLES, default="script", help="kind of starter file (default: script)")
    parser.add_argument("--title", default="TODO(author): title", help="short title for the day")
    args = parser.parse_args()

    levels = level_dirs()
    if not levels:
        raise SystemExit("error: no level folders found. Create one first, e.g. level-1-beginner/")
    level_number = args.level if args.level is not None else max(levels)
    if level_number not in levels:
        raise SystemExit(f"error: there is no folder for level {level_number}. Existing levels: {sorted(levels)}")
    level_dir = levels[level_number]

    days = existing_day_numbers(level_dir)
    number = args.number if args.number is not None else (days[-1] + 1 if days else 1)
    if number < 1:
        raise SystemExit("error: the day number must be 1 or higher.")

    target, created = create_day(level_dir, number, args.title, args.style)

    print(f"Created {level_dir.name}/{target.name}/")
    for name in created:
        print(f"  - {name}")
    print()
    print("Next steps:")
    print("  1. Write the task in README.md and replace every TODO(author).")
    print("  2. Fill in the starter code (scaffolding for the student, never the solution).")
    print(f"  3. Add the day to the table in {level_dir.name}/README.md.")
    print("  4. python check_days.py   (it must report OK)")


if __name__ == "__main__":
    main()
