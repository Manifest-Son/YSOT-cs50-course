# Day 34: Capstone part 1

> Estimated time: 60-90 minutes

## Goal

By the end of today you have **planned** the Mini School Management System on paper and built its foundation: the data structure and the functions to add, view, search and delete students.

## Concepts

- **Planning before coding:** sketching the menu and listing the functions you need
- The data structure: a **list of student dictionaries** (Day 27)
- Functions that take the list as a parameter, so they do not rely on global variables
- Returning results instead of printing (Day 29), so the menu can decide what to show
- Testing each function by itself before connecting it to a menu

## Scenario

**Mavuno School** is ready for its first working system. Over the next two days you build a **Mini School Management System**. Today is the foundation: how a student is stored, and the four basic actions on the register. Tomorrow you add marks, report cards, statistics, fees and the menu.

## Task

### Part 1: the plan (in `NOTES.md`)

Fill in the **Plan** section of `NOTES.md` **before** you write any code:

1. **Menu sketch:** write the menu the finished system will show. Use the options from Day 35's README as a starting point, and change them if you have a better idea.
2. **Data structure:** write one example student record (the dictionary).
3. **Functions list:** for each function, write its name, its parameters and what it returns.

### Part 2: the foundation (in `day_34.py`)

Every student is a dictionary: `{"name": ..., "age": ..., "class": ..., "marks": {}}`. A new student starts with an empty `marks` dictionary. The register is a list of these dictionaries. Write four functions, each taking the register as its first parameter:

| Function | What it must do |
| --- | --- |
| `add_student(students, name, age, class_name)` | Add a new student record with an empty `marks` dictionary. Return `True` if added, or `False` (and add nothing) if a student with the same name already exists (ignore capitals and extra spaces). |
| `view_students(students)` | **Return** a list of text lines, one per student: `<name> | <class> | age <age>`. An empty register returns an empty list. |
| `search_student(students, name)` | **Return** the student's dictionary, or `None` if there is no such student. Ignore capitals and extra spaces. |
| `delete_student(students, name)` | Remove the student. Return `True` if deleted, `False` if not found. Same name matching. |

`main()` in the starter calls them so you can see them working.

## Examples

```python
>>> students = []
>>> add_student(students, "Alice Wanjiku", 15, "Form 2A")
True
>>> add_student(students, "  alice wanjiku ", 15, "Form 2A")
False
>>> view_students(students)
['Alice Wanjiku | Form 2A | age 15']
>>> search_student(students, "ALICE WANJIKU")["age"]
15
>>> delete_student(students, "Brian Otieno")
False
```

## How to do it

1. **Plan first.** Do Part 1 on paper or in `NOTES.md`. The plan will save you time tomorrow.
2. **Name matching is needed by three functions.** Write a small helper first (for example `clean(name)` that returns `name.strip().lower()`), and use it everywhere.
3. **`search_student`** is the easiest: loop and compare cleaned names. Return the dictionary on a match, and `None` after the loop.
4. **`add_student`** can call `search_student` to detect a duplicate. Build the dictionary and `append` it.
5. **`delete_student`** can also call `search_student`, then `students.remove(student)`.
6. **`view_students`** builds a list of f-strings and returns it. `main()` prints the lines.
7. **Test each function** in `main()` with the cases from the examples before moving on.

## Run it

Run this from the `python-daily-practice/` folder:

```bash
python "level-1-beginner/Day 34/day_34.py"
```

The quotes matter because the folder name contains a space.

## Done when

- [ ] The **Plan** in `NOTES.md` is written (menu, example record, functions list)
- [ ] The four functions work as in the table and as in the examples
- [ ] Duplicate names are refused, and name matching ignores capitals and extra spaces
- [ ] Your work is committed and pushed to your own branch

## Stretch goals (optional)

- Make `age` validation part of `add_student`: refuse ages below 3 or above 25 by returning `False`.
- Add a function `count_students(students)` and one that lists the students of a given class.
