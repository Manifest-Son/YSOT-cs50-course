# Day 32: Functions, dictionaries and conditionals

> Estimated time: 45-60 minutes

## Goal

By the end of today you can write a function that takes a **student dictionary** and **returns a formatted report card** as text, using grades and remarks decided with conditionals.

## Concepts

- A function that receives a dictionary and reads from it: `student["name"]`, `student["marks"]`
- Building a multi-line string: collect the lines in a list, then `"\n".join(lines)`
- Reusing smaller functions inside a bigger one (`get_grade`, `calculate_average`)
- `if` / `else` for the remark
- Returning text for the caller to print or save

Useful docs: [str.join](https://docs.python.org/3/library/stdtypes.html#str.join)

## Scenario

At the end of the term **Mavuno School** produces a **report card** for every student, and parents also see it in the portal. The same card must look identical wherever it is shown, so you write **one function** that builds it from a student record.

## Task

In `day_32.py` you need three functions. Copy your finished `calculate_average` and `get_grade` from **Day 29** into the starter, then write the new one:

```python
def generate_report_card(student):
```

It takes a student dictionary (`name`, `age`, `class`, `marks`) and **returns** one string made of these lines, in this order, separated by newlines (no extra blank line at the end):

```text
MAVUNO SCHOOL REPORT CARD
Name: <name>
Class: <class>
<Subject>: <mark> (<grade>)        <- one line per subject, in the dictionary's order
Average: <average rounded to 2 decimals> (<grade of the average>)
Remark: <remark>
```

The remark is `Pass` if the average is **at least 50**. Otherwise it is `Fail - please attend remedial lessons`.

The function must **return** the card, not print it. `main()` prints it.

## Examples

```text
MAVUNO SCHOOL REPORT CARD
Name: Alice Wanjiku
Class: Form 2A
Mathematics: 78 (B)
English: 85 (A)
Kiswahili: 72 (B)
Average: 78.33 (B)
Remark: Pass
```

For Kevin Kiprop (marks 40, 52, 47), the last two lines are:

```text
Average: 46.33 (F)
Remark: Fail - please attend remedial lessons
```

## How to do it

1. Open `day_32.py`. Paste your `calculate_average` and `get_grade` from Day 29 where the starter says so, and check they still work.
2. **Start the list of lines:** `lines = ["MAVUNO SCHOOL REPORT CARD", f"Name: {student['name']}", ...]`.
3. **Subject lines:** `for subject, mark in student["marks"].items():` and append `f"{subject}: {mark} ({get_grade(mark)})"`.
4. **Average:** `calculate_average(list(student["marks"].values()))`. Use it for the grade as well. Handle a student with no marks sensibly (the average is `0.0`).
5. **Remark:** an `if` / `else` on the average.
6. **Return** `"\n".join(lines)`.
7. **Test** Alice and Kevin from `main()` and compare with the examples. Then make a student of your own with a failing average.

## Run it

Run this from the `python-daily-practice/` folder:

```bash
python "level-1-beginner/Day 32/day_32.py"
```

The quotes matter because the folder name contains a space.

## Done when

- [ ] `generate_report_card` returns the card as one string in the format above
- [ ] The grade of each subject and of the average are right, and the average has 2 decimals
- [ ] A failing student gets the `Fail - please attend remedial lessons` remark
- [ ] `NOTES.md` is filled in
- [ ] Your work is committed and pushed to your own branch

## Stretch goals (optional)

- Add a teacher comment line, using the bands from Day 14.
- Mention the student's strongest subject on the card.
