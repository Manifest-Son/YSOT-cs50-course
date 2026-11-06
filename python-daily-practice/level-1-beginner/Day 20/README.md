# Day 20: The teacher menu

> Estimated time: 45-60 minutes

## Goal

By the end of today you can build a **menu-driven program**: it shows options, does what the user picks, and repeats until the user chooses to leave.

## Concepts

- `while True:` with a `break` to leave (Day 17)
- `if` / `elif` / `else` to act on the menu choice (Day 10)
- Keeping a **running total and count** between menu choices
- Validating input before using it
- Dividing safely: never divide by a count that might be 0

Useful docs: [while statement](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement)

## Scenario

Teachers at **Mavuno School** use a small program on the staff computer to enter the marks from a CAT and check the average so far. It shows a menu, again and again, until the teacher is done.

## Task

Write a program that repeatedly shows this menu:

```text
--- Teacher menu ---
1. Enter marks
2. View average
3. Exit
```

and asks `Choose an option:`. Then:

| Choice | What to do |
| --- | --- |
| `1` | Ask `Enter a mark (0-100):`. If the mark is below 0 or above 100, print `Invalid mark.` and do not store it. Otherwise add it to the running `total` and add 1 to `count`, and print `Mark saved.` |
| `2` | If no marks have been entered yet, print `No marks entered yet.` Otherwise print `Average: <average>` rounded to 2 decimal places. |
| `3` | Print `Goodbye!` and **stop** the program. |
| anything else | Print `Invalid choice.` and show the menu again. |

The marks entered with option 1 are remembered between menu choices.

## Examples

```text
--- Teacher menu ---
1. Enter marks
2. View average
3. Exit
Choose an option: 1
Enter a mark (0-100): 70
Mark saved.
...
Choose an option: 1
Enter a mark (0-100): 85
Mark saved.
...
Choose an option: 2
Average: 77.5
...
Choose an option: 3
Goodbye!
```

## How to do it

1. Open `day_20.py`. The running totals and the loop are given, with the menu printed for you.
2. **Read the choice** with `input` and compare it as **text**: `if choice == "1":`.
3. **Option 1:** read the mark as a `float`, check it is in range, and update `total` and `count`.
4. **Option 2:** check `count == 0` **before** dividing, otherwise you get `ZeroDivisionError` (Day 6).
5. **Option 3:** print the goodbye message and `break`.
6. **`else`:** print `Invalid choice.`
7. **Test a whole session:** view the average first (no marks yet), enter two marks, enter an invalid mark, view the average, type `9`, then exit.

## Run it

Run this from the `python-daily-practice/` folder:

```bash
python "level-1-beginner/Day 20/day_20.py"
```

The quotes matter because the folder name contains a space.

## Done when

- [ ] The menu appears again after every choice until the user exits
- [ ] Marks are validated and remembered; the average is correct and rounded to 2 decimals
- [ ] Viewing the average with no marks does not crash
- [ ] `NOTES.md` is filled in
- [ ] Your work is committed and pushed to your own branch

## Stretch goals (optional)

- Add an option to show the highest mark entered.
- Add an option to reset the marks and start again.
