# Day 29: Writing functions

> Estimated time: 30-45 minutes

## Goal

By the end of today you can package a piece of code into a **function** that takes values in and **returns** a result, so you can reuse it instead of copying it.

## Concepts

- Defining a function with `def name(parameters):`
- `return` sends a value back to whoever called the function; `print` only shows text on the screen
- Calling a function and using the value it returns
- Reusing earlier work: the average, the grade and the pass check you already wrote

Useful docs: [Defining functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

## Scenario

Every term, every teacher at **Mavuno School** works out the same three things for every student: the average mark, the letter grade and whether the student passed. Today you stop copying that code into every program and write it **once**, as three functions that the whole school system can reuse.

## Task

Open `day_29.py`. It has three functions that currently do nothing (`raise NotImplementedError`). Implement them:

| Function | What it must do |
| --- | --- |
| `calculate_average(marks)` | `marks` is a list of numbers. **Return** their average as a float. An empty list returns `0.0`. |
| `get_grade(score)` | **Return** the letter for a score: `"A"` 80-100, `"B"` 70-79, `"C"` 60-69, `"D"` 50-59, `"F"` below 50. A score below 0 or above 100 returns `"Invalid"`. |
| `is_passing(score)` | **Return** `True` if the score is at least the pass mark (`PASS_MARK`, which is 50), otherwise `False`. |

The functions must **return** their answer and must **not** print anything. `main()` at the bottom of the file does the printing for you.

## Examples

```python
>>> calculate_average([70, 80, 90])
80.0
>>> calculate_average([])
0.0

>>> get_grade(85)
'A'
>>> get_grade(50)
'D'
>>> get_grade(101)
'Invalid'

>>> is_passing(50)
True
>>> is_passing(49.5)
False
```

## How to do it

1. **Read the three docstrings** in `day_29.py`. They describe the exact behaviour, with examples.
2. **Do the functions in this order**, running the program after each one:
   1. `calculate_average`: use `sum(marks)` and `len(marks)`. Check for the empty list first, because dividing by zero is an error (you met it on Day 6).
   2. `is_passing`: one line. Compare `score` with `PASS_MARK`. A comparison already gives `True` or `False`, so you can `return` it directly.
   3. `get_grade`: reuse your Day 10 grade assigner. First handle the invalid scores, then go from the highest band down with `if` / `elif`.
3. **`return` is not `print`.** If your function shows `None` when you print its answer, you probably used `print(...)` instead of `return ...`.
4. **Check the boundaries** by hand in `main()`: try scores such as `0`, `49.9`, `50`, `79.5`, `80`, `100` and `101` and make sure each gives what the table above says.
5. Fill in `NOTES.md`.

## Run it

Run this from the `python-daily-practice/` folder:

```bash
python "level-1-beginner/Day 29/day_29.py"
```

The quotes matter because the folder name contains a space.

## Done when

- [ ] All three functions are written and return the values in the table above
- [ ] None of your three functions use `print()`
- [ ] You tried the boundary scores listed in step 4
- [ ] `NOTES.md` is filled in
- [ ] Your work is committed and pushed to your own branch

## Stretch goals (optional)

- Add a function `get_remark(score)` that returns `"Pass"` or `"Fail"`, reusing `is_passing`.
- Make `calculate_average` ignore `None` entries in the list (a student who missed the exam).
