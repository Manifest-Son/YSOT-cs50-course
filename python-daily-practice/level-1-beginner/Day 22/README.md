# Day 22: Lists

> Estimated time: 30-45 minutes

## Goal

By the end of today you can keep many values in one **list**, and add, remove, sort and slice them.

## Concepts

- A list holds several items in order: `names = ["Alice", "Brian"]`
- Items are numbered from 0: `names[0]`, and the last is `names[-1]`
- `.append(item)` adds to the end; `.remove(item)` removes the first match; `.sort()` sorts in place
- Slices: `names[:3]` is the first three, `names[-3:]` is the last three
- `len(names)` is how many items there are

Useful docs: [Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

## Scenario

The **Mavuno School** class teacher keeps the list of students in a class. During the term a new student joins, another one transfers to a different school, and the register must stay in alphabetical order.

## Task

`day_22.py` already has a list called `students` with **10** names. Using list methods:

1. **Add** a new student, `"Lucy Wambui"`, to the end of the list.
2. **Remove** the student who transferred: `"Kevin Kiprop"`.
3. **Sort** the list alphabetically.
4. Print `Number of students:` followed by how many students there are now (it should be 10 again).
5. Print `First three:` followed by the first three names of the sorted list, and `Last three:` followed by the last three.

## Examples

```text
Number of students: 10
First three: ['Alice Wanjiku', 'Brian Otieno', 'Daniel Omondi']
Last three: ['Mercy Njeri', 'Peter Mwangi', 'Samuel Kariuki']
```

The sorted list should be: Alice Wanjiku, Brian Otieno, Daniel Omondi, Esther Chebet, Fatuma Hassan, Grace Achieng, Lucy Wambui, Mercy Njeri, Peter Mwangi, Samuel Kariuki.

## How to do it

1. Open `day_22.py` and print the starting list once to see what you have.
2. **Add:** `students.append("Lucy Wambui")`. Print the list again. Where did she go?
3. **Remove:** `students.remove("Kevin Kiprop")`. Careful: spelling must match exactly, or you get a `ValueError` (Day 6).
4. **Sort:** `students.sort()`. This changes the list itself and returns nothing, so do not write `students = students.sort()`.
5. **Count and slice:** `len(students)`, `students[:3]` and `students[-3:]`.
6. **Compare** with the example. Check the count is 10 after one added and one removed.

## Run it

Run this from the `python-daily-practice/` folder:

```bash
python "level-1-beginner/Day 22/day_22.py"
```

The quotes matter because the folder name contains a space.

## Done when

- [ ] Lucy Wambui is in the list and Kevin Kiprop is not
- [ ] The list is in alphabetical order
- [ ] The count, the first three and the last three are printed as in the example
- [ ] `NOTES.md` is filled in
- [ ] Your work is committed and pushed to your own branch

## Stretch goals (optional)

- Print the list in reverse order without changing it.
- Insert a new student at the front of the list with `.insert(0, "Name")`.
