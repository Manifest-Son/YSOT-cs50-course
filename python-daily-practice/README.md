# Python Daily Practice

A small Python assignment every day, all set at **Mavuno School** (a school that needs a system to manage its students, teachers, parents, exams and reports; see [DOMAIN.md](DOMAIN.md)). Each day is its own folder (`Day 1`, `Day 2`, ...) with the same set of files, so you always know where to look and what to do.

## Levels

| Level | Days | Status |
| --- | --- | --- |
| [Level 1: Beginner](level-1-beginner/) | 35 | Ready. Ends with a Mini School Management System |
| [Level 2: Intermediate](level-2-intermediate/) | to be planned | Planned |

Each level has a `README.md` with the full list of days.

## What is in every day folder

```
Day N/
├── README.md     <- REQUIRED. The assignment and exactly how to do it
├── day_NN.py     <- starter code: you continue it and write your solution here
└── NOTES.md      <- your short reflection after finishing
```

`NN` is the day number padded to two digits (`day_01.py`, `day_12.py`). The day `README.md` always has these sections: **Goal**, **Concepts**, **Scenario**, **Task**, **Examples**, **How to do it**, **Run it**, **Done when**, **Stretch goals**.

The starter code gives you the scaffolding (comments, given data, function names). **You write the solution.** Your instructor reviews your work and gives feedback.

## What you need

Python 3.10 or newer, and a text editor. Nothing else to install. Day 1 shows you how to check your Python and run a file.

## Your daily routine

1. Pull the new day (see "For students" in the [main README](../README.md)).
2. Open the day's `README.md` and read it all the way through.
3. Work in `day_NN.py`, following the steps in **How to do it**. Run it as often as you like:
   ```bash
   python "level-1-beginner/Day 1/day_01.py"      # replace with today's level and day
   ```
4. Write a few lines in `NOTES.md`.
5. Commit and push to **your own branch** so your instructor can review it.

Folder names contain a space, so keep the quotes around them in commands. Run commands from this folder (`python-daily-practice/`).

## For instructors: adding a new day

```bash
python new_day.py --title "Loops and lists"                  # next Day N in the newest level
python new_day.py 7 --level 2 --title "Reading files"        # a specific day in level 2
python new_day.py --style functions --title "Fee functions"  # starter made of function stubs
```

This copies the files in `_template/` into a new `Day N` folder. Then:

1. Replace every `TODO(author)`: write the README and the starter code.
2. Add the day to the table in the level's `README.md`.
3. Run `python check_days.py`. It must say `OK`.

`check_days.py` (standard library only) enforces the rules: every day has a `README.md` with the required sections, a starter file that is valid Python, and a `NOTES.md`; day numbers have no gaps; the level README lists every day; and no `TODO(author)` is left behind.

Rules for a good day:

- It can be done in 30-60 minutes.
- The README explains what to build **and** how to approach it (hints, not the solution).
- The starter gives scaffolding and never the solution. Solutions are not stored in this repository.
- Everything is set at Mavuno School and follows the house rules in [DOMAIN.md](DOMAIN.md).
- The plan is organised by **day only**.
