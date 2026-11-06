# Day 35: Capstone part 2

> Estimated time: 90-120 minutes

## Goal

By the end of today you have finished the **Mavuno Mini School Management System**: a menu-driven program that manages students, marks, report cards, class statistics and fees, using every Level 1 concept.

## Concepts

Everything from Level 1 (see the checklist in the [level plan](../README.md)):

- Variables, data types, operators, `input()`, formatted output
- Strings, f-strings, string cleaning
- `if` / `elif` / `else`, `and` / `or`
- `for` and `while` loops, `break` and `continue`
- Lists, dictionaries (and the nested student records)
- Functions with parameters, defaults and return values
- Input validation, so that bad input never crashes the program

## Scenario

**Mavuno School** is going live with its first system. The office will use it to register students, teachers will enter **CAT** and exam marks, the head teacher will see the **top students** and the class statistics, parents' fees will be calculated, and **report cards** will be printed. It is small and lives in memory only (saving to files comes in Level 2), but it is a real system.

## Task

**Start from your Day 34 code.** Copy it into `day_35.py` (the starter lists what to add). Keep the student record shape and the four functions from Day 34, and add:

| Function | What it must do |
| --- | --- |
| `enter_marks(students, name, subject, mark)` | Store `mark` under `subject` in the student's `marks`. Return `True` on success; return `False` if the student does not exist or the mark is not between 0 and 100. |
| `calculate_average(marks)` and `get_grade(score)` | From Day 29 (copy your own). |
| `generate_report_card(student)` | From Day 32 (copy your own). |
| `class_statistics(students)` and `get_top_students(students, n)` | From Day 31 (copy your own). Today the menu uses `n = 3`. |
| `calculate_fees(tuition, transport=0, discount=0)` | From Day 30 (copy your own). |

Then write `main()`: a **clean, looping menu** with **input validation**:

```text
--- Mavuno School Management System ---
1. Add student
2. View all students
3. Search for a student
4. Delete a student
5. Enter marks
6. Print report card
7. Class statistics
8. Top 3 students
9. Fee calculator
0. Exit
```

The menu must:

- **Repeat** until the user chooses `0`, then print `Goodbye!`
- Print `Invalid choice.` for anything that is not on the menu
- **Validate every number typed**: age must be a whole number; marks must be numbers between 0 and 100; fees must be numbers. If the input is not valid, say so and **ask again**. The program must never crash on bad input.
- Handle **empty cases** without crashing (no students yet, a student with no marks, an unknown name)

## Examples

```text
Choose an option: 5
Student name: Alice Wanjiku
Subject: Mathematics
Mark (0-100): abc
Please enter a number between 0 and 100.
Mark (0-100): 78
Marks saved.
...
Choose an option: 6
Student name: Alice Wanjiku
MAVUNO SCHOOL REPORT CARD
Name: Alice Wanjiku
Class: Form 2A
Mathematics: 78 (B)
Average: 78.0 (B)
Remark: Pass
```

## How to do it

1. **Copy your Day 34 code first** and check that it still runs. Then add the other functions one at a time, copying your earlier work from Days 29-32.
2. **Write a helper for validated input** before the menu. For example `read_number(prompt, low, high)`: it asks again in a `while` loop until the text is a number in range. To check that typed text is a number without crashing: `text.replace(".", "", 1).isdigit()` is `True` for `"78"` and `"55.5"` but not for `"abc"`. Write a second helper `read_whole_number` for ages (`text.isdigit()`).
3. **Build the menu one option at a time** and run after each: first `0` and the invalid choice, then 1 and 2, and so on. Do not write the whole menu and then test.
4. **Menu options call your functions and do the printing;** the functions return values. Option 5 prints `Marks saved.` or a clear problem message depending on what `enter_marks` returns.
5. **Test the edge cases on purpose:** an empty register in every option, a student with no marks on the report card, a mark of `0` and `100`, a mark of `101`, a name with the wrong capitals, a letter instead of a number.
6. **Read your own code as a stranger would.** Add comments, give variables clear names, remove leftover test code.
7. Finish `NOTES.md` with what you would add in Level 2.

## Run it

Run this from the `python-daily-practice/` folder:

```bash
python "level-1-beginner/Day 35/day_35.py"
```

The quotes matter because the folder name contains a space.

## Done when

- [ ] All ten menu options work, and the menu repeats until `0`
- [ ] Bad input (letters, out-of-range marks, unknown names, empty register) never crashes the program
- [ ] The report card, class statistics, top 3 and fee calculator give correct results
- [ ] The code is readable and commented, and uses every concept in the Level 1 checklist
- [ ] `NOTES.md` is filled in
- [ ] Your work is committed and pushed to your own branch

## Stretch goals (optional)

- Add an attendance option: record a present/absent mark for a student on a date and show their attendance percentage.
- Add a **remedial** list: students with an average below 50.
- Add a short **clinic** note per student: one line each for academic, sport and life skills.
