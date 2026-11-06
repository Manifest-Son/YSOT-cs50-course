"""Structure checks: every "Day N" folder must be complete and well formed.

Run with:  python -m pytest tests -q

The main rule: every day MUST have a README.md that explains how the task is
to be done. This file fails if a README is missing, empty, missing a key
section, or still contains an unfinished TODO(author) marker.
"""

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
DAY_DIR_RE = re.compile(r"^Day ([1-9]\d*)$")  # no leading zeros: "Day 3", not "Day 03"

# Sections every day README must have, each with some text under it.
REQUIRED_SECTIONS = [
    "Goal",
    "Task",
    "How to do it",
    "Run and test",
    "Done when",
]


def _day_number(path):
    return int(DAY_DIR_RE.match(path.name).group(1))


DAY_DIRS = sorted(
    (p for p in ROOT.iterdir() if p.is_dir() and DAY_DIR_RE.match(p.name)),
    key=_day_number,
)

day_param = pytest.mark.parametrize("day", DAY_DIRS, ids=lambda p: p.name)


def _section_body(text, heading):
    """Return the text under '## heading' up to the next '## ' heading, or None."""
    pattern = r"^## " + re.escape(heading) + r"[ \t]*\n(.*?)(?=^## |\Z)"
    match = re.search(pattern, text, flags=re.MULTILINE | re.DOTALL)
    return match.group(1) if match else None


def test_there_is_at_least_one_day():
    assert DAY_DIRS, "No 'Day N' folders found. Create one with: python new_day.py"


def test_day_folder_names_are_exact():
    """Catch typos like 'day 1', 'Day1' or 'Day 01' that the other checks would skip."""
    bad = [
        p.name
        for p in ROOT.iterdir()
        if p.is_dir()
        and p.name.lower().replace(" ", "").startswith("day")
        and not DAY_DIR_RE.match(p.name)
    ]
    assert not bad, f"Folders must be named exactly 'Day <number>' (e.g. 'Day 1'): {bad}"


@day_param
def test_readme_exists_and_is_not_empty(day):
    readme = day / "README.md"
    assert readme.is_file(), f"{day.name} is missing README.md (required)"
    assert readme.read_text(encoding="utf-8").strip(), f"{day.name}/README.md is empty"


@day_param
def test_readme_title_matches_the_day(day):
    text = (day / "README.md").read_text(encoding="utf-8")
    first_line = text.lstrip().splitlines()[0] if text.strip() else ""
    expected = f"# Day {_day_number(day)}:"
    assert first_line.startswith(expected), (
        f"{day.name}/README.md must start with '{expected} <title>' (found: {first_line!r})"
    )


@day_param
@pytest.mark.parametrize("section", REQUIRED_SECTIONS)
def test_readme_has_required_section(day, section):
    text = (day / "README.md").read_text(encoding="utf-8")
    body = _section_body(text, section)
    assert body is not None, f"{day.name}/README.md is missing a '## {section}' section"
    assert body.strip(), f"{day.name}/README.md has an empty '## {section}' section"


@day_param
def test_starter_files_exist(day):
    number = _day_number(day)
    expected = [
        "README.md",
        f"day_{number:02d}.py",
        f"test_day_{number:02d}.py",
        "NOTES.md",
    ]
    missing = [name for name in expected if not (day / name).is_file()]
    assert not missing, f"{day.name} is missing: {missing}"


@day_param
def test_no_unfinished_template_markers(day):
    problems = []
    for path in sorted(day.rglob("*")):
        if not path.is_file() or "__pycache__" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if "TODO(author)" in text:
            problems.append(f"{path.relative_to(ROOT)}: contains TODO(author)")
        if re.search(r"\{\{(N|NN|TITLE|DATE)\}\}", text):
            problems.append(f"{path.relative_to(ROOT)}: unreplaced template placeholder")
    assert not problems, "Finish the day before committing:\n  " + "\n  ".join(problems)
