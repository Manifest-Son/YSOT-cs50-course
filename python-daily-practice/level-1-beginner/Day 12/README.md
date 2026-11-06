# Day 12: Logical operators and nesting

> Estimated time: 45-60 minutes

## Goal

By the end of today you can combine conditions with `and`, `or` and `not`, and place one `if` inside another to check input first and decide second.

## Concepts

- `and`: both conditions must be true. `or`: at least one must be true. `not`: flips true and false
- Brackets group conditions: `(a and b) or c`
- **Nesting:** an `if` inside another `if`. The inner one only runs when the outer one is true
- Validating input before using it

Useful docs: [Boolean operations](https://docs.python.org/3/reference/expressions.html#boolean-operations)

## Scenario

**Mavuno School** gives a scholarship to students who do very well. A student **qualifies** if they have a high average and good attendance, **or** if they are in the top three of the class. Marks and attendance must make sense, or the application is rejected.

## Task

Write a program that asks for:

1. The student's **average** mark (0-100, decimals allowed)
2. The student's **attendance** in percent (0-100, decimals allowed)
3. The student's **position** in the class (1 for first, 2 for second, ...)

Then:

- **Validate first.** The input is invalid if the average or the attendance is below 0 or above 100, or if the position is less than 1. Print `Invalid input` followed by the reason, and print **no** decision.
- **Otherwise decide.** The student qualifies if `(average >= 80 and attendance >= 90)` **or** `position <= 3`.
  - If the student qualifies, print `QUALIFIES for the Mavuno scholarship`.
  - Otherwise, print `DOES NOT QUALIFY for the Mavuno scholarship`.

## Examples

```text
Average: 85, Attendance: 92, Position: 8   ->  QUALIFIES for the Mavuno scholarship
Average: 85, Attendance: 89.9, Position: 8 ->  DOES NOT QUALIFY for the Mavuno scholarship
Average: 60, Attendance: 70, Position: 3   ->  QUALIFIES for the Mavuno scholarship
Average: 60, Attendance: 70, Position: 4   ->  DOES NOT QUALIFY for the Mavuno scholarship
Average: 105, Attendance: 90, Position: 1  ->  Invalid input: the average must be between 0 and 100
```

## How to do it

1. Open `day_12.py`. The three questions are done for you.
2. **Outer `if` (validation):** `if average < 0 or average > 100:` ... then `elif` for attendance, then `elif` for position. Each prints its own `Invalid input: ...` message.
3. **`else` (decision):** when all input is valid, put the second `if` **inside** this `else`.
4. **Inner `if`:** write the qualifying rule with brackets exactly as in the Task: `(average >= 80 and attendance >= 90) or position <= 3`.
5. **Test the boundaries:** average `80` and `79.9`; attendance `90` and `89.9`; position `3` and `4`; and an invalid value for each of the three inputs.
6. Draw the logic as a small tree on paper if the nesting confuses you.

## Run it

Run this from the `python-daily-practice/` folder:

```bash
python "level-1-beginner/Day 12/day_12.py"
```

The quotes matter because the folder name contains a space.

## Done when

- [ ] Invalid input prints `Invalid input` with a reason and no decision
- [ ] Valid input prints exactly one of the two decisions
- [ ] The boundaries (80, 90 and position 3) behave as in the examples
- [ ] `NOTES.md` is filled in
- [ ] Your work is committed and pushed to your own branch

## Stretch goals (optional)

- Print the **reason** a student qualified (good marks, or top three, or both).
- Add a third route: a student with 100% attendance and an average of at least 70 also qualifies.
