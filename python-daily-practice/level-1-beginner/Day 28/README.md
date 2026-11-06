# Day 28: Mini project: Student Database

> Estimated time: 60-90 minutes

## Goal

By the end of today you have built a complete, menu-driven program that stores student records in memory, and lets the user add, view, search and delete them.

## Concepts

- A `while True` menu loop with `break` (Day 20)
- A list of student dictionaries (Day 27)
- Searching and deleting inside a list
- Averages and comparisons to find the best student
- Splitting a bigger program into clearly commented parts

## Scenario

The **Mavuno School** office needs a first version of its student register: add a new student when a parent registers them, look students up, remove them if they leave, and see who is at the top of the class. The data only lives while the program runs for now (saving to files comes in a later level).

## Task

Write a program that starts with an **empty** list `students` and repeatedly shows this menu:

```text
--- Mavuno Student Database ---
1. Add student
2. View all students
3. Search by name
4. Delete a student
5. Show class topper
6. Exit
```

and asks `Choose an option:`. Every student is a dictionary in the shape from Day 27:
`{"name": ..., "age": ..., "class": ..., "marks": {"Mathematics": ..., "English": ..., "Kiswahili": ...}}`.

| Choice | What to do |
| --- | --- |
| `1` | Ask for the name, the age (whole number), the class, and the three marks (decimals allowed). Add the record to the list and print `Student added.` |
| `2` | If the list is empty print `No students yet.` Otherwise print one line per student: `<name> | <class> | average <average>` (2 decimals). |
| `3` | Ask for a name (ignore capitals and extra spaces). Print the student's name, age, class, marks and average, or `Student not found.` |
| `4` | Ask for a name (same matching). If found, remove the student and print `Student deleted.`; otherwise print `Student not found.` |
| `5` | If the list is empty print `No students yet.` Otherwise print `Class topper: <name> (average <average>)` for the student with the **highest** average. On a tie the student added **first** wins. |
| `6` | Print `Goodbye!` and stop. |
| anything else | Print `Invalid choice.` |

## Examples

```text
--- Mavuno Student Database ---
...
Choose an option: 1
Name: Alice Wanjiku
Age: 15
Class: Form 2A
Mathematics: 78
English: 85
Kiswahili: 72
Student added.
...
Choose an option: 5
Class topper: Alice Wanjiku (average 78.33)
...
Choose an option: 6
Goodbye!
```

## How to do it

1. **Plan before you code.** On paper, write the menu and, for each option, the 2-3 steps it needs.
2. **Start with the skeleton:** the loop, the menu, and option `6` and the `else` branch. Run it. Add one option at a time and run after each.
3. **Build the record** for option 1 as a dictionary and `append` it to `students`.
4. **Print all** with a `for` loop and an f-string. Test option 2 on an empty list first.
5. **Search and delete** share the same matching: loop through the list and compare `student["name"].strip().lower()` with the cleaned typed name. For delete, remove the matching dictionary with `students.remove(student)` once found, and then `break` out of that loop.
6. **Topper:** a "best so far" variable like Day 21. Use `>` so the first student wins a tie.
7. **Test a whole session:** view on empty, add three students, search (in capitals), delete one, topper, an invalid option, exit.

## Run it

Run this from the `python-daily-practice/` folder:

```bash
python "level-1-beginner/Day 28/day_28.py"
```

The quotes matter because the folder name contains a space.

## Done when

- [ ] All six menu options work as in the table, and the menu repeats until Exit
- [ ] Empty-list cases print `No students yet.` and do not crash
- [ ] Search and delete ignore capitals and extra spaces and report `Student not found.`
- [ ] `NOTES.md` is filled in
- [ ] Your work is committed and pushed to your own branch

## Stretch goals (optional)

- Reject a second student with the same name.
- Add option 7 to update one of a student's marks.
