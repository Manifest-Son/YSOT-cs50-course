# Python Daily Practice

A small Python exercise every day. Each day lives in its own folder (`Day 1`, `Day 2`, ...) with the same set of starter files, so you always know where to look and what to do.

## The days

| Day | Topic | Status |
| --- | --- | --- |
| [Day 1](Day%201/) | Functions and strings | Ready |

## What is in every day folder

```
Day N/
├── README.md        <- REQUIRED. Explains the task and exactly how to do it
├── day_NN.py        <- starter code with TODO stubs: you write your solution here
├── test_day_NN.py   <- tests that tell you when you are done
└── NOTES.md         <- your short reflection after finishing
```

`NN` is the day number padded to two digits (`day_01.py`, `day_12.py`), so each day's files have a unique name and all days can be tested together.

The day `README.md` always has these sections: **Goal**, **Concepts**, **Task**, **Examples**, **How to do it**, **Run and test**, **Done when**, **Stretch goals**. `tests/test_structure.py` fails if a day has no README or if Goal, Task, How to do it, Run and test or Done when is missing or empty.

## One-time setup

You need Python 3.10 or newer. From this folder (`python-daily-practice/`):

```bash
python -m venv .venv
# Windows:      .venv\Scripts\activate
# macOS/Linux:  source .venv/bin/activate
pip install -r requirements.txt
```

## Your daily routine

1. Open the day's `README.md` and read it all the way through.
2. Work in `day_NN.py`. Follow the steps in the README's **How to do it** section.
3. Check your work as you go:
   ```bash
   python -m pytest "Day 1" -q        # replace 1 with today's number
   ```
4. Run your program:
   ```bash
   python "Day 1/day_01.py"
   ```
5. When all the tests pass, write a few lines in `NOTES.md`.

Folder names contain a space, so keep the quotes around them in commands.

## Adding a new day

```bash
python new_day.py --title "Loops and lists"     # creates the next Day N
python new_day.py 7 --title "Dictionaries"      # or a specific number
```

This copies the files in `_template/` into a new `Day N` folder. Then:

1. Replace every `TODO(author)` in the new folder: write the README, the starter code and the tests. `tests/test_structure.py` will not pass until you do.
2. Add the day to the table at the top of this file.
3. Check the structure: `python -m pytest tests -q`

Rules for a good day:

- It can be done in 30-45 minutes.
- The README explains what to build **and** how to approach it (hints, not the solution).
- Tests cover the normal cases and the edge cases, and each test failure message tells the learner what went wrong.

## Useful commands

```bash
python -m pytest tests -q          # check every day has a complete README and starter files
python -m pytest "Day 1" -q        # test a single day
python -m pytest -q                # everything (days you have not solved yet will fail: that is expected)
```

Solutions are not stored in this repo. Keep your own solution in `day_NN.py` and commit it when you are done.
