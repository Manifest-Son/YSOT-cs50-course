# Day 17: break and continue

> Estimated time: 30-45 minutes

## Goal

By the end of today you can control a loop from the inside: `continue` skips the rest of one pass, and `break` stops the loop completely.

## Concepts

- `while True:` makes a loop that runs until something inside stops it
- `break` leaves the loop immediately
- `continue` jumps back to the start of the loop, skipping the rest of the block
- Order matters: the checks inside the loop run from top to bottom

Useful docs: [break and continue](https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops)

## Scenario

A **Mavuno School** teacher enters the marks from a pile of marked scripts, one after another. Sometimes a mark is mistyped (negative, or above 100), and the program must skip it. When the pile is finished, the teacher types **-1** to stop and sees the total and how many marks were counted.

## Task

Write a program that repeatedly asks `Enter mark (-1 to stop):` and:

1. If the teacher types **-1**, **stop** the loop (use `break`). Check this **first**, because -1 is also a negative number.
2. If the mark is **below 0 or above 100**, print `Invalid mark, skipped.` and **skip** it (use `continue`). It must not be added to the total or counted.
3. Otherwise add the mark to `total` and add 1 to `count`. Marks may have decimals.

After the loop print `Marks entered: <count>` and `Total: <total>`. Keep the results in variables called `total` and `count`.

## Examples

```text
Enter mark (-1 to stop): 70
Enter mark (-1 to stop): 105
Invalid mark, skipped.
Enter mark (-1 to stop): 85.5
Enter mark (-1 to stop): -1
Marks entered: 2
Total: 155.5
```

If the teacher types -1 straight away, the program prints `Marks entered: 0` and `Total: 0`.

## How to do it

1. Open `day_17.py`. The two counters and the start of the loop are given.
2. **First check inside the loop:** `if mark == -1: break`.
3. **Second check:** `if mark < 0 or mark > 100:` print the skipped message and `continue`.
4. **Everything below** runs only for valid marks: add to `total`, add 1 to `count`.
5. **Print the results after the loop** (not indented).
6. **Test:** all valid marks; a mix with invalid ones (-5, 101, 100.1); `0` and `100` (both valid); and -1 immediately.
7. Swap the order of the first two checks to see what goes wrong. Write what you notice in `NOTES.md`.

## Run it

Run this from the `python-daily-practice/` folder:

```bash
python "level-1-beginner/Day 17/day_17.py"
```

The quotes matter because the folder name contains a space.

## Done when

- [ ] -1 stops the loop and is not counted
- [ ] Invalid marks are skipped and not counted; 0 and 100 are valid
- [ ] The count and the total are printed after the loop
- [ ] `NOTES.md` is filled in
- [ ] Your work is committed and pushed to your own branch

## Stretch goals (optional)

- Print the average of the valid marks (only if at least one was entered).
- Print how many invalid marks were skipped.
