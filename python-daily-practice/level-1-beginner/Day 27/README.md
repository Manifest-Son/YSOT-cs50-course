# Day 27: Nested structures

> Estimated time: 45-60 minutes

## Goal

By the end of today you can combine lists and dictionaries into one data structure that stores whole **student records**, print them, and search them.

## Concepts

- A **list of dictionaries**: one dictionary per student, all in one list
- A dictionary **inside** a dictionary: each student's `"marks"` is itself a dictionary of subject: mark
- Reaching inside: `student["marks"]["English"]`
- Looping over the list to print or search
- Case-insensitive search with `.lower()` and `.strip()`

Useful docs: [Data structures](https://docs.python.org/3/tutorial/datastructures.html)

## Scenario

Until now each student was just a name and a mark. The real **Mavuno School** system needs to keep a student's name, age, class **and** all their marks together. Today you design that record and search a small school's students.

## Task

Every student is stored as a dictionary with these keys:

```python
{"name": "Alice Wanjiku", "age": 15, "class": "Form 2A",
 "marks": {"Mathematics": 78, "English": 85, "Kiswahili": 72}}
```

1. In `day_27.py`, build a list called `students` with these **four** students (the first is already written as a model):

| name | age | class | Mathematics | English | Kiswahili |
| --- | --- | --- | --- | --- | --- |
| Alice Wanjiku | 15 | Form 2A | 78 | 85 | 72 |
| Brian Otieno | 16 | Form 3B | 55 | 61 | 70 |
| Fatuma Hassan | 14 | Form 1C | 92 | 88 | 81 |
| Kevin Kiprop | 15 | Form 2A | 40 | 52 | 47 |

2. **Print all students**, one line each: `<name> | <class> | average <average>` with the average of their three marks rounded to 2 decimal places.
3. **Search.** Ask `Search for a student by name:`. Ignore capital letters and extra spaces around the typed name. If the student is found, print the name, age, class, each subject with its mark, and the average. If not, print `Student not found.`

## Examples

```text
Alice Wanjiku | Form 2A | average 78.33
Brian Otieno | Form 3B | average 62.0
Fatuma Hassan | Form 1C | average 87.0
Kevin Kiprop | Form 2A | average 46.33

Search for a student by name:   brian OTIENO
Name: Brian Otieno
Age: 16
Class: Form 3B
Mathematics: 55
English: 61
Kiswahili: 70
Average: 62.0
```

```text
Search for a student by name: Zawadi Mutua
Student not found.
```

## How to do it

1. Open `day_27.py`. Look at the first student: this is the shape of every record.
2. **Build the list:** write the other three dictionaries in the same shape inside `students = [ ... ]`. Mind the commas.
3. **Average of one student:** `sum(student["marks"].values()) / len(student["marks"])` (`.values()` gives the marks).
4. **Print all:** `for student in students:` and an f-string.
5. **Search:** read the name, clean it with `.strip().lower()`, then loop and compare with `student["name"].lower()`. Use a `found = False` variable, set it to `True` on a match, and print `Student not found.` after the loop if it is still `False`.
6. **Print the details of the match** with a second loop over `student["marks"].items()`.
7. **Test:** a name in capitals, a name with spaces around it, and a name that does not exist.

## Run it

Run this from the `python-daily-practice/` folder:

```bash
python "level-1-beginner/Day 27/day_27.py"
```

The quotes matter because the folder name contains a space.

## Done when

- [ ] `students` has the four records in the required shape
- [ ] All students are printed with the correct averages
- [ ] The search ignores capitals and extra spaces, and handles "not found"
- [ ] `NOTES.md` is filled in
- [ ] Your work is committed and pushed to your own branch

## Stretch goals (optional)

- Also print the number of students in each class (`Form 2A`: 2).
- Let the user search by class and print all the students in it.
