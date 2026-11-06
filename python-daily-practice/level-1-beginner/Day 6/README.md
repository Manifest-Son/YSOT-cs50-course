# Day 6: Reading errors

> Estimated time: 45-60 minutes

## Goal

By the end of today you are not afraid of error messages. You can read a **traceback**, say what kind of error it is, find the line that caused it, and fix it.

## Concepts

- An error is Python telling you what went wrong and where
- A **traceback** is read from the bottom: the last line names the error type and explains it; the lines above show where it happened
- Common errors: `ZeroDivisionError`, `TypeError`, `NameError`, `ValueError`, `SyntaxError`

Useful docs: [Errors and exceptions](https://docs.python.org/3/tutorial/errors.html)

## Scenario

Things go wrong in a real school system: a class with no students yet, a name typed where a mark was expected, a typo. The **Mavuno School** office wants staff who can read the message instead of panicking. Today you cause five errors on purpose, in school situations, and write down what each one means.

## Task

`day_06.py` has five numbered blocks, one for each error. For each block:

1. Read the scenario and uncomment the lines (remove the leading `#`).
2. Write the line that **causes** the error described.
3. Run the file and **read the traceback**. Find the error type on the last line.
4. Write the entry in the **Error log** table in `NOTES.md`: the error name, **what it means** in your own words, and **how to fix** it.
5. **Fix** the code so the block runs without error, then comment the block out again before starting the next one.

The five errors:

| # | Scenario | Error to cause |
| --- | --- | --- |
| 1 | Dividing the total marks by 0 students (a class with no students) | `ZeroDivisionError` |
| 2 | Adding a student's name to a score | `TypeError` |
| 3 | Misspelling a variable name | `NameError` |
| 4 | Turning a typed mark such as `"eighty five"` into a number with `int()` | `ValueError` |
| 5 | Forgetting to close a bracket in a `print(` line | `SyntaxError` |

## Examples

How to read a traceback:

```text
Traceback (most recent call last):
  File "day_06.py", line 12, in <module>
    average = total_marks / number_of_students
ZeroDivisionError: division by zero
```

- Last line: the **type** (`ZeroDivisionError`) and a short **explanation** (`division by zero`).
- The line above it shows the **code** that failed, and above that the **file and line number**.

## How to do it

1. **Do one block at a time.** Only one block should be uncommented when you run the file, because Python stops at the first error.
2. **Block 1:** the starter gives `total_marks = 450` and `number_of_students = 0`. Divide one by the other.
3. **Block 2:** try `"Alice" + 85`. What does Python say about the two types? What would make it work? (`str(85)` or an f-string.)
4. **Block 3:** create `average = 80`, then print the misspelled name `avrage`. Python tells you exactly which name it does not know.
5. **Block 4:** `int("eighty five")`. Which input would work? How could a program check first? (You will learn how on later days.)
6. **Block 5 last:** a `SyntaxError` stops the **whole** file from running, so do this one at the end, read the message, then fix it.
7. In `NOTES.md`, complete the Error log for all five errors. Be specific: say which line you wrote, what Python said, and the fix.

## Run it

Run this from the `python-daily-practice/` folder:

```bash
python "level-1-beginner/Day 6/day_06.py"
```

The quotes matter because the folder name contains a space.

## Done when

- [ ] You caused and read all five errors
- [ ] The Error log in `NOTES.md` has all five rows filled in (error name, meaning, fix)
- [ ] `day_06.py` ends with every block fixed, so the file runs without errors
- [ ] Your work is committed and pushed to your own branch

## Stretch goals (optional)

- Cause a sixth error: `IndexError` is coming later, so try `FileNotFoundError` with `open("marks.txt")`. What does it mean?
- Look up what `IndentationError` is and cause it.
