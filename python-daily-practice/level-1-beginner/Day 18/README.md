# Day 18: Loops and conditionals

> Estimated time: 45 minutes

## Goal

By the end of today you can combine a loop with `if` / `elif` to **sort what you read into groups** and count each group.

## Concepts

- `for ... in range(...)` to repeat a fixed number of times (Day 15)
- `if` / `elif` / `else` inside a loop (Day 10)
- **Counters:** a variable that starts at 0 and goes up by 1 each time something happens: `count_a += 1`
- `+=` is short for "add to the variable"

Useful docs: [for statements](https://docs.python.org/3/tutorial/controlflow.html#for-statements)

## Scenario

After a **CAT** the **Mavuno School** academic office wants to know how the class did: how many students got an A, a B, a C, and how many failed. A class here has 10 students in the group being checked.

## Task

Write a program that:

1. Reads the marks of **10 students**, one `input()` per student, in a loop. Marks are between 0 and 100 and may have decimals. (You can assume the teacher types valid marks today.)
2. Counts them into four groups, in variables named exactly:
   - `count_a`: marks of 80 or more
   - `count_b`: 70 up to (not including) 80
   - `count_c`: 60 up to (not including) 70
   - `count_fail`: below 60 (this includes the D and F grades)
3. Prints a summary with the four counts, labelled `A`, `B`, `C` and `Fail`.

## Examples

```text
Mark for student 1: 85
Mark for student 2: 72
...
Mark for student 10: 41
Grade summary
A: 3
B: 2
C: 1
Fail: 4
```

(The four counts always add up to 10.)

## How to do it

1. Open `day_18.py`. The four counters and the loop header are given.
2. **Inside the loop,** read the mark with `float(input(...))`. Use `student_number` in the question so the teacher knows which student it is.
3. **Choose the group** with an `if` / `elif` / `elif` / `else` chain, going from the highest down: `>= 80`, `>= 70`, `>= 60`, else fail. In each branch add 1 to the matching counter.
4. **After the loop** (not indented) print the summary.
5. **Check your work:** do the four counters add up to 10? Run with all 10 marks the same (all `80`): the A count should be 10.
6. **Test the boundaries:** `80`, `79.9`, `70`, `69.9`, `60`, `59.9`.

## Run it

Run this from the `python-daily-practice/` folder:

```bash
python "level-1-beginner/Day 18/day_18.py"
```

The quotes matter because the folder name contains a space.

## Done when

- [ ] It reads exactly 10 marks
- [ ] The four counts are right at all the boundaries and always add up to 10
- [ ] The summary shows the labels `A`, `B`, `C` and `Fail`
- [ ] `NOTES.md` is filled in
- [ ] Your work is committed and pushed to your own branch

## Stretch goals (optional)

- Reject invalid marks (below 0 or above 100) by asking again.
- Print the percentage of the class that failed.
