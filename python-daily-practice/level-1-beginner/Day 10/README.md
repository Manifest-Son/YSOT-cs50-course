# Day 10: if / elif / else

> Estimated time: 30-45 minutes

## Goal

By the end of today you can make a program choose between several actions using `if`, `elif` and `else`.

## Concepts

- `if condition:` runs the indented block only when the condition is `True`
- `elif` ("else if") tries the next condition; `else` runs when none matched
- Only the **first** matching branch runs, so the order of conditions matters
- Comparison operators `>=`, `<`, `==` and so on (Day 3)
- Indentation (4 spaces) is part of the syntax

Useful docs: [if statements](https://docs.python.org/3/tutorial/controlflow.html#if-statements)

## Scenario

At the end of the term **Mavuno School** turns every score into a letter grade. Today you build the **grade assigner** that teachers use.

## Task

Write a program that asks for a score (a number that may have decimals) and prints the letter grade:

| Score | Grade |
| --- | --- |
| 80 to 100 | `A` |
| 70 up to (but not including) 80 | `B` |
| 60 up to 70 | `C` |
| 50 up to 60 | `D` |
| 0 up to 50 | `F` |

If the score is below 0 or above 100, print a message that contains the word `Invalid` and **do not** print a grade.

Print the result as `Grade: B` (with the letter you worked out).

## Examples

```text
Score (0-100): 85    ->  Grade: A
Score (0-100): 79.5  ->  Grade: B
Score (0-100): 50    ->  Grade: D
Score (0-100): 49.9  ->  Grade: F
Score (0-100): 101   ->  Invalid score: it must be between 0 and 100
```

## How to do it

1. Open `day_10.py`. Asking for the score is done for you.
2. **Handle invalid scores first:** `if score < 0 or score > 100:`. Anything that gets past this check is a valid score.
3. **Then go from the top grade down:** `elif score >= 80:` is `A`, `elif score >= 70:` is `B`, and so on. You do not need to write "and below 80" for B, because an `A` already stopped earlier.
4. **The last branch is `else`:** whatever is left is below 50, so `F`.
5. **Test the boundaries** by running the program several times: `0`, `49.9`, `50`, `59.9`, `60`, `69.9`, `70`, `79.9`, `80`, `100`, `-1`, `101`. Each must give the grade in the table.
6. If a boundary gives the wrong grade, check `>=` versus `>`.

## Run it

Run this from the `python-daily-practice/` folder:

```bash
python "level-1-beginner/Day 10/day_10.py"
```

The quotes matter because the folder name contains a space.

## Done when

- [ ] Every score from 0 to 100 gives the right grade, including all the boundaries
- [ ] Scores below 0 or above 100 print a message with `Invalid` and no grade
- [ ] `NOTES.md` is filled in
- [ ] Your work is committed and pushed to your own branch

## Stretch goals (optional)

- Also print `Pass` or `Fail` (pass mark 50).
- Add the remark `Distinction` for scores of 90 and above.
