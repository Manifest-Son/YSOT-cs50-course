# Day 31: Functions, lists and loops

> Estimated time: 45-60 minutes

## Goal

By the end of today you can write functions that take a **list of student records**, loop through it, and return a useful answer: the top students and the class statistics.

## Concepts

- Passing a list to a function: `def get_top_students(students, n):`
- Looping inside a function and returning the result
- Sorting records by a calculated value: `sorted(students, key=student_average, reverse=True)` (a function can be used as the `key`)
- Returning a **dictionary** with several results
- Reusing a function from another function

Useful docs: [Sorting HOW TO](https://docs.python.org/3/howto/sorting.html)

## Scenario

The **Mavuno School** head teacher wants two things from the exam results: the **top students** (for the prize-giving list) and the **class statistics** (average, highest and lowest) for the termly report. Both functions will later become part of the school system.

## Task

`day_31.py` gives you a list `students` of five student records (each with `name`, `age`, `class` and a `marks` dictionary, as on Day 27). Write three functions:

| Function | What it must do |
| --- | --- |
| `student_average(student)` | **Return** the average of the student's marks (the values in `student["marks"]`) as a float. A student with no marks gets `0.0`. |
| `get_top_students(students, n)` | **Return** a list of the `n` students with the highest averages, **best first**. If two students have the same average, keep their original order. If `n` is bigger than the number of students, return all of them. |
| `class_statistics(students)` | **Return** a dictionary with three keys: `"average"` (the average of the students' averages), `"highest"` (the highest student average) and `"lowest"` (the lowest). For an empty list return `0.0` for all three. |

The functions must **return** their answers and not print. `main()` prints for you.

## Examples

For the five students in the starter (averages 78.33, 62.0, 87.0, 46.33 and 92.0):

```text
Top 3 students:
1. Grace Achieng (92.0)
2. Fatuma Hassan (87.0)
3. Alice Wanjiku (78.33)
Class average: 73.13
Highest: 92.0
Lowest: 46.33
```

## How to do it

1. Open `day_31.py`. Read the data and the three function stubs.
2. **Start with `student_average`:** it is Day 29's `calculate_average` applied to `student["marks"].values()`. Check for an empty `marks` dictionary first.
3. **`get_top_students`:** `sorted(students, key=student_average, reverse=True)` gives all the students best first (ties keep their original order). Then slice with `[:n]`.
4. **`class_statistics`:** build a list of the averages with a loop (call `student_average` for each student), then use `sum`, `len`, `max` and `min`. Handle the empty list **first**.
5. **Use `main()`** to print the results and compare with the example.
6. **Test other cases** by changing the data: only one student, `n` larger than the list, two students with the same average.

## Run it

Run this from the `python-daily-practice/` folder:

```bash
python "level-1-beginner/Day 31/day_31.py"
```

The quotes matter because the folder name contains a space.

## Done when

- [ ] All three functions return (and do not print) the values described
- [ ] The output for the starter data matches the example
- [ ] Empty lists and `n` larger than the list do not crash
- [ ] `NOTES.md` is filled in
- [ ] Your work is committed and pushed to your own branch

## Stretch goals (optional)

- Add `get_failing_students(students)` that returns the students whose average is below 50 (candidates for **remedial** lessons).
- Add a `"median"` key to `class_statistics`.
