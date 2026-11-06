#!/usr/bin/env python3
"""Check that every level and every "Day N" folder is complete and well formed.

Usage (run from python-daily-practice/):

    python check_days.py

Uses only the standard library. Exit status is 0 when everything is fine and 1
otherwise, with a list of what to fix.

The main rule: every day MUST have a README.md that explains how the task is to
be done. This script fails if a README is missing, empty, missing a key section,
points at the wrong folder, or still contains an unfinished TODO(author) marker.
It also checks that the starter file is valid Python, so a day never ships a
starter that cannot even be opened and run.

Layout being checked:

    python-daily-practice/
        level-1-beginner/
            README.md          (the plan: a table linking to every day)
            Day 1/ ... Day 35/ (each: README.md, day_NN.py, NOTES.md)
        level-2-intermediate/
            README.md
"""

import ast
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LEVEL_DIR_RE = re.compile(r"^level-([1-9]\d*)-[a-z0-9]+(?:-[a-z0-9]+)*$")
DAY_DIR_RE = re.compile(r"^Day ([1-9]\d*)$")  # no leading zeros: "Day 3", not "Day 03"

# Sections every day README must have, each with some text under it.
REQUIRED_SECTIONS = ["Goal", "Scenario", "Task", "How to do it", "Run it", "Done when"]


def visible_dirs(path):
    return sorted(p for p in path.iterdir() if p.is_dir() and not p.name.startswith(".") and p.name != "__pycache__")


def day_number(path):
    return int(DAY_DIR_RE.match(path.name).group(1))


def section_body(text, heading):
    """Return the text under '## heading' up to the next '## ' heading, or None."""
    pattern = r"^## " + re.escape(heading) + r"[ \t]*\n(.*?)(?=^## |\Z)"
    match = re.search(pattern, text, flags=re.MULTILINE | re.DOTALL)
    return match.group(1) if match else None


def check_names(problems):
    """Catch typos like 'Level1', 'day 1', 'Day3', 'Day 03', or a Day folder outside a level."""
    for path in visible_dirs(ROOT):
        name = path.name
        if name.lower().startswith("level") and not LEVEL_DIR_RE.match(name):
            problems.append(f"'{name}': level folders must be named like 'level-1-beginner'")
        if name.lower().replace(" ", "").startswith("day"):
            problems.append(f"'{name}': Day folders belong inside a level folder, e.g. level-1-beginner/Day 1")
    for level in levels():
        for path in visible_dirs(level):
            if path.name.lower().replace(" ", "").startswith("day") and not DAY_DIR_RE.match(path.name):
                problems.append(f"'{level.name}/{path.name}': folders must be named exactly 'Day <number>', e.g. 'Day 1'")


def levels():
    return sorted(
        (p for p in visible_dirs(ROOT) if LEVEL_DIR_RE.match(p.name)),
        key=lambda p: int(LEVEL_DIR_RE.match(p.name).group(1)),
    )


def days_of(level):
    return sorted((d for d in visible_dirs(level) if DAY_DIR_RE.match(d.name)), key=day_number)


def check_level(level, problems):
    readme = level / "README.md"
    if not readme.is_file() or not readme.read_text(encoding="utf-8").strip():
        problems.append(f"{level.name}: missing or empty README.md (the plan for the level)")
        return
    text = readme.read_text(encoding="utf-8")

    if re.search(r"^#+\s*Week\b", text, flags=re.MULTILINE | re.IGNORECASE):
        problems.append(f"{level.name}/README.md: the plan is organised by day only, so remove the 'Week' headings")

    numbers = [day_number(d) for d in days_of(level)]
    if numbers != list(range(1, len(numbers) + 1)):
        problems.append(f"{level.name}: day numbers have gaps or do not start at 1: {numbers}")

    linked = sorted({int(n) for n in re.findall(r"\(Day%20(\d+)/\)", text)})
    for n in linked:
        if not (level / f"Day {n}").is_dir():
            problems.append(f"{level.name}/README.md links to Day {n}, which does not exist yet")
    for n in numbers:
        if n not in linked:
            problems.append(f"{level.name}/README.md does not list Day {n}")


def check_day(level, day, problems):
    label = f"{level.name}/{day.name}"
    number = day_number(day)

    for name in ("README.md", f"day_{number:02d}.py", "NOTES.md"):
        if not (day / name).is_file():
            problems.append(f"{label}: missing {name}")

    readme = day / "README.md"
    if readme.is_file():
        text = readme.read_text(encoding="utf-8")
        if not text.strip():
            problems.append(f"{label}/README.md is empty")
        else:
            first_line = text.lstrip().splitlines()[0]
            if not first_line.startswith(f"# Day {number}:"):
                problems.append(f"{label}/README.md must start with '# Day {number}: <title>' (found: {first_line!r})")
            for section in REQUIRED_SECTIONS:
                body = section_body(text, section)
                if body is None:
                    problems.append(f"{label}/README.md is missing a '## {section}' section")
                elif not body.strip():
                    problems.append(f"{label}/README.md has an empty '## {section}' section")
            run_body = section_body(text, "Run it") or ""
            if f"{level.name}/{day.name}" not in run_body:
                problems.append(f'{label}/README.md: the "Run it" command should use the path "{level.name}/{day.name}"')

    starter = day / f"day_{number:02d}.py"
    if starter.is_file():
        try:
            ast.parse(starter.read_text(encoding="utf-8"), filename=str(starter))
        except SyntaxError as error:
            problems.append(f"{label}/{starter.name}: the starter is not valid Python (line {error.lineno}: {error.msg})")

    for path in sorted(day.rglob("*")):
        if not path.is_file() or "__pycache__" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if "TODO(author)" in text:
            problems.append(f"{label}/{path.name}: contains TODO(author); finish writing it")
        if re.search(r"\{\{(N|NN|TITLE|DATE|LEVEL)\}\}", text):
            problems.append(f"{label}/{path.name}: unreplaced template placeholder")


def main():
    problems = []
    check_names(problems)
    level_list = levels()
    if not level_list:
        problems.append("no level folders found, e.g. level-1-beginner/")
    day_count = 0
    for level in level_list:
        check_level(level, problems)
        for day in days_of(level):
            day_count += 1
            check_day(level, day, problems)

    if problems:
        print(f"Found {len(problems)} problem(s):\n")
        for problem in problems:
            print(f"  - {problem}")
        sys.exit(1)
    print(f"OK: {len(level_list)} level(s) and {day_count} day(s) checked, all complete.")


if __name__ == "__main__":
    main()
