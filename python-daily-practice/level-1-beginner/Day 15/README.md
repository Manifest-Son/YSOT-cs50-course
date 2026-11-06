# Day 15: for loops and range()

> Estimated time: 30-45 minutes

## Goal

By the end of today you can repeat an action a set number of times with a `for` loop and control the numbers with `range()`.

## Concepts

- `for variable in range(...):` repeats the indented block once for each number
- `range(stop)` counts from 0 up to `stop - 1`; `range(start, stop)` starts at `start`; `range(start, stop, step)` jumps by `step`
- The stop number is **not included**: `range(1, 4)` gives 1, 2, 3
- The loop variable holds the current number and can be used in the block

Useful docs: [for statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements) · [range()](https://docs.python.org/3/library/stdtypes.html#range)

## Scenario

Every morning the class teacher at **Mavuno School** calls the **roll**. Form 2A has **30 seats**, numbered 1 to 30. Today you print the roll call, and then only the **even-numbered seats**, which are the ones seated by the window.

## Task

Write a program with two parts, using `for` loops:

1. **Roll call.** Print the heading `Roll call: Form 2A`, then one line per seat from 1 to 30 in the form `Seat 1`, `Seat 2`, ..., `Seat 30`.
2. **Even seats.** Print the heading `Even-numbered seats:` and then only the even seats, in the same form: `Seat 2`, `Seat 4`, ..., `Seat 30`.

## Examples

```text
Roll call: Form 2A
Seat 1
Seat 2
Seat 3
...
Seat 30
Even-numbered seats:
Seat 2
Seat 4
...
Seat 30
```

## How to do it

1. Open `day_15.py`. The two headings are printed for you.
2. **Roll call:** `for seat in range(1, 31):` runs for 1 to 30 (remember that 31 is not included). Inside the loop print `f"Seat {seat}"`. Indent the print line by 4 spaces.
3. **Even seats:** the easy way is `range(2, 31, 2)`: start at 2, stop before 31, step 2. Print them in the same way.
4. **Check the ends:** the first and last line of each part. Does the roll call end at `Seat 30`? Does the even list start at `Seat 2`?
5. **Experiment:** what does `range(5)` print? What does `range(10, 0, -1)` print? Write what you find in `NOTES.md`.

## Run it

Run this from the `python-daily-practice/` folder:

```bash
python "level-1-beginner/Day 15/day_15.py"
```

The quotes matter because the folder name contains a space.

## Done when

- [ ] The roll call prints exactly 30 lines, `Seat 1` to `Seat 30`
- [ ] The even-seat part prints exactly 15 lines, `Seat 2` to `Seat 30`
- [ ] `NOTES.md` is filled in
- [ ] Your work is committed and pushed to your own branch

## Stretch goals (optional)

- Print the odd-numbered seats too, with their own heading.
- Print the seats counting down from 30 to 1.
