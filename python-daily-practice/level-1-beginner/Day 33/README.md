# Day 33: Debugging day

> Estimated time: 60 minutes

## Goal

By the end of today you can find and fix bugs on purpose: by reading error messages carefully, by checking values with `print()`, and by comparing what the program does with what it should do.

## Concepts

- A **bug** is a mistake in a program. Some **crash** it (an error message), others make it quietly give the **wrong answer**
- Read the **last line** of a traceback first, then the line number above it (Day 6)
- **`print()` debugging:** print a variable inside the loop to see what it really holds
- Compare the actual output with the **expected output**, line by line
- Fix **one bug at a time** and run again

Useful docs: [Errors and exceptions](https://docs.python.org/3/tutorial/errors.html)

## Scenario

A teacher at **Mavuno School** wrote a little program to summarise a CAT for five students, but it does not work, and the teacher has gone home. You are the school's debugger for the day.

## Task

### Part A: fix the broken program

`day_33.py` contains a program with **exactly five bugs**: one crashes with an `IndexError`, one with a `TypeError`, one with a `NameError`, and **two** give the wrong answer without crashing. When it is fixed, it must print exactly:

```text
Alice: 72 (B)
Brian: 45 (F)
Fatuma: 88 (A)
Kevin: 91 (A)
Grace: 39 (F)
Total: 335
Average: 67.0
Top student: Kevin with 91
Passed: 3 of 5
```

For every bug write down, in the **Bug log (Part A)** table in `NOTES.md`: where it was, what was wrong, how you found it, and how you fixed it.

### Part B: break your own project

Take your finished **Day 28** program (the Student Database). Copy it into a new file called `day_33_break.py` in this folder, then:

1. **Deliberately break it in 5 different ways** (for example: a misspelled variable, `+` between text and a number, a wrong comparison, an off-by-one in a loop, a missing `break`).
2. Run it after each break and note the error or wrong behaviour.
3. **Fix** each break and confirm the program works again.
4. Record each one in the **Bug log (Part B)** table in `NOTES.md`.

## Examples

How the debugging loop works:

1. Run the program. It stops with `IndexError: list index out of range` on line N.
2. Read line N and the line above. What is the loop doing? What is the biggest index it uses?
3. Fix it, run again. The next problem appears. Repeat.

## How to do it

1. **Run the program as it is** and read the first error message. Do not change anything yet.
2. **Fix the crash**, run again, and read the next message. Fix the bugs that crash first: that is what the traceback is for.
3. **When the program runs to the end,** compare its output with the expected output above, line by line. Where is the first line that differs? Add a `print()` of the variable just before it (for example `print("total is", total)` inside the loop).
4. **Fix the wrong-answer bugs.** One of them only shows up for two of the five students: which marks sit on the wrong side of a boundary?
5. **After each fix, write the log row** straight away, while it is fresh.
6. **Part B:** write down your plan before you start breaking things. Break **one thing at a time**.
7. Remove the debugging `print()` lines you added once everything works.

## Run it

Run this from the `python-daily-practice/` folder:

```bash
python "level-1-beginner/Day 33/day_33.py"
```

The quotes matter because the folder name contains a space.

## Done when

- [ ] `day_33.py` prints exactly the expected output above
- [ ] Both bug logs in `NOTES.md` are filled in (5 rows each)
- [ ] `day_33_break.py` exists and works again after your fixes
- [ ] Your work is committed and pushed to your own branch

## Stretch goals (optional)

- Add a sixth student with a mark of exactly 50 and check the program handles the boundary correctly.
- Swap files with a classmate: break each other's `day_33_break.py` and find the bugs.
