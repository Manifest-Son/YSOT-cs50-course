# Day 1: Setup and print()

> Estimated time: 30-45 minutes

## Goal

By the end of today you have Python working on your computer, you can run a Python file from the terminal, and you can use `print()` to produce neat, formatted text.

## Concepts

- Running a Python script from the terminal: `python file.py`
- `print()` shows text on the screen
- Text (a *string*) goes inside quotes: `"like this"`
- A string can be repeated with `*`: `"-" * 10` gives `----------`

Useful docs: [Using the Python interpreter](https://docs.python.org/3/tutorial/interpreter.html) · [print()](https://docs.python.org/3/library/functions.html#print)

## Scenario

On admission day every new student at **Mavuno School** receives an ID card. Today you make Mavuno's very first ID-card printer: a Python program that prints a student's card.

## Task

Open `day_01.py` and write a program that prints a **student ID card** like this:

```text
******************************
        MAVUNO SCHOOL
******************************
Name:  Alice Wanjiku
Class: Form 2A
ID:    MAV-2026-014
******************************
```

The rules:

1. The **first** and the **last** line of the card are border lines made only of `*` (or only of `-`). They must be at least 20 characters long and **the same length**.
2. The card shows the school name, **Mavuno School** (capital letters are fine).
3. The card has three labelled lines: `Name:`, `Class:` and `ID:`, each followed by a value. Use your own details or make up a student.

Everything else (spacing, extra decoration, a border in the middle) is up to you.

## Examples

Another valid card:

```text
------------------------------
Mavuno School - Student Card
------------------------------
Name: Brian Otieno
Class: Form 3B
ID: MAV-2025-102
------------------------------
```

## How to do it

1. **Check that Python is installed.** Open a terminal (on Windows: PowerShell) and run:
   ```bash
   python --version        # on macOS/Linux this may be: python3 --version
   ```
   You need **3.10 or newer**. If the command is not found, install Python from <https://www.python.org/downloads/>. On Windows, tick **"Add python.exe to PATH"** in the installer, then open a new terminal.
2. **Go to the practice folder** in the terminal. From the folder where you cloned the repository:
   ```bash
   cd python-daily-practice
   ```
3. **Open `day_01.py`** in your editor. It only has comments that list the steps.
4. **Write the card, one `print()` per line.** Start with the border. To avoid typing 30 stars, use repetition: `print("*" * 30)`.
5. **Run your program** and look at the card. Change it until you like it.
6. **Check your card against the rules** in the Task section: same border at the top and the bottom, the school name, and the three labelled lines.
7. **Write your notes** in `NOTES.md`.

## Run it

Run this from the `python-daily-practice/` folder:

```bash
python "level-1-beginner/Day 1/day_01.py"
```

The quotes matter because the folder name contains a space.

## Done when

- [ ] The program prints a card that follows all three rules
- [ ] `NOTES.md` is filled in
- [ ] Your work is committed and pushed to your own branch

## Stretch goals (optional)

- Centre the school name inside the border using spaces (or the string method `.center(30)`).
- Print a second card for a different student below the first.
