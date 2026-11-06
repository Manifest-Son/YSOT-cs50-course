# Day 3: Operators

> Estimated time: 30-45 minutes

## Goal

By the end of today you can use arithmetic operators to work out a student's total, average and percentage, and comparison operators to check whether they passed.

## Concepts

- Arithmetic operators: `+` `-` `*` `/` (and `//` `%` `**` for stretch work)
- Brackets control the order of operations: `(a + b) / 2`
- Comparison operators: `==` `!=` `>` `<` `>=` `<=`; they give `True` or `False`
- `round(number, 2)` to show 2 decimal places

Useful docs: [Numeric types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex)

## Scenario

At the end of the term a **Mavuno School** teacher has a student's marks in five subjects and needs the total, the average, the percentage, and a quick answer to "did this student pass?". The pass mark is **50** on the average.

## Task

`day_03.py` already contains the five marks (out of 100 each). Using those variables:

1. Calculate `total` (the sum of the five marks).
2. Calculate `average` (the total divided by 5).
3. Calculate `percentage` (the total as a percentage of the maximum possible, which is 5 × 100 = 500).
4. Calculate `passed`: a variable that is `True` when `average >= PASS_MARK` and `False` otherwise. Use a comparison operator, not an `if` (you will meet `if` on Day 10).
5. Print the total, the average and the percentage (each rounded to 2 decimal places), then print `Passed: True` or `Passed: False`.

## Examples

With the marks in the starter (78, 85, 72, 64, 90):

```text
Total: 389
Average: 77.8
Percentage: 77.8
Passed: True
```

Try changing the marks to low values (for example all `40`) and check that `Passed` becomes `False`.

## How to do it

1. Open `day_03.py` and read the marks and `PASS_MARK` that are given.
2. **Total:** add the five variables with `+`.
3. **Average:** divide the total by 5. `/` always gives a float.
4. **Percentage:** `total / 500 * 100`. Why is it the same number as the average here? Write your answer in `NOTES.md`.
5. **Passed:** a comparison is itself a value. `passed = average >= PASS_MARK` stores `True` or `False`.
6. **Print** with labels so the output is readable: `print("Total:", total)`. Use `round(value, 2)` for the average and percentage.
7. Change the marks, run again, and check by hand that the results make sense. Test the edge: marks that give an average of exactly `50`. Is it a pass?

## Run it

Run this from the `python-daily-practice/` folder:

```bash
python "level-1-beginner/Day 3/day_03.py"
```

The quotes matter because the folder name contains a space.

## Done when

- [ ] `total`, `average`, `percentage` and `passed` are calculated with operators
- [ ] The output shows all four values with labels
- [ ] An average of exactly 50 counts as a pass
- [ ] `NOTES.md` is filled in
- [ ] Your work is committed and pushed to your own branch

## Stretch goals (optional)

- Print how many marks the student needs in a sixth subject to bring the average up to 80.
- Use `//` and `%` to split the total into hundreds and the remainder.
