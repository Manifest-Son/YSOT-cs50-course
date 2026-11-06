# Day 2: Variables and data types

> Estimated time: 30-45 minutes

## Goal

By the end of today you can store information in variables, tell the basic data types apart (`str`, `int`, `float`, `bool`) with `type()`, and change what a variable holds.

## Concepts

- A **variable** is a name that holds a value: `age = 15`
- The four basic data types: `str` (text), `int` (whole number), `float` (number with decimals), `bool` (`True` or `False`)
- `type(value)` tells you which type a value is
- A variable can be updated: `age = age + 1`

Useful docs: [Built-in types](https://docs.python.org/3/library/stdtypes.html)

## Scenario

When a student joins **Mavuno School**, the office records a few facts about them. Today you store one student's record in variables, check that each fact has the right type, and then promote the student to the next grade level at the end of the year.

## Task

In `day_02.py`, create these five variables with **exactly** these values:

| Variable | Value | Type |
| --- | --- | --- |
| `student_name` | `"Alice Wanjiku"` | `str` |
| `age` | `15` | `int` |
| `grade_level` | `9` | `int` |
| `gpa` | `3.6` | `float` |
| `is_enrolled` | `True` | `bool` |

Then:

1. Print each variable on its own line together with its type.
2. **Promote** the student: update `grade_level` so it goes up by one (to `10`).
3. Print the new `grade_level` with a message that says the student was promoted.

## Examples

```text
student_name: Alice Wanjiku (<class 'str'>)
age: 15 (<class 'int'>)
grade_level: 9 (<class 'int'>)
gpa: 3.6 (<class 'float'>)
is_enrolled: True (<class 'bool'>)
Alice Wanjiku was promoted. New grade_level: 10
```

## How to do it

1. Open `day_02.py`. The first variable and its `print` line are done for you: read them, then do the rest the same way.
2. **Create the other four variables.** Remember: text goes in quotes, numbers do not, and `True` has a capital `T` and no quotes.
3. **Print each one with its type.** `type(age)` gives the type. An f-string makes a tidy line: `f"age: {age} ({type(age)})"`.
4. **Promote the student.** To change a variable, assign it a new value that uses the old one: `grade_level = grade_level + 1`.
5. **Print the promotion message** using the new value of `grade_level`.
6. Compare your output with the example. If a type looks wrong (for example `<class 'str'>` for `age`), look at whether you put quotes around the number.

## Run it

Run this from the `python-daily-practice/` folder:

```bash
python "level-1-beginner/Day 2/day_02.py"
```

The quotes matter because the folder name contains a space.

## Done when

- [ ] All five variables exist with the exact values in the table
- [ ] The types printed are `str`, `int`, `int`, `float`, `bool`
- [ ] `grade_level` is `10` after the promotion
- [ ] `NOTES.md` is filled in
- [ ] Your work is committed and pushed to your own branch

## Stretch goals (optional)

- Add a variable `fees_paid = False` and print its type too.
- Print how old the student will be at the next promotion (`age + 1`).
