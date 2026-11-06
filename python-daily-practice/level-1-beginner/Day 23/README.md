# Day 23: Tuples and sets

> Estimated time: 45 minutes

## Goal

By the end of today you can store fixed records in **tuples** and use **sets** to answer "who is in both groups?", "who is in only one?" and "who is in any group?".

## Concepts

- A **tuple** is a fixed group of values: `("Alice Wanjiku", 9)`. It cannot be changed after it is created. Unpack it into variables: `name, grade = record`
- A **set** holds unique items with no order: `{"Alice", "Brian"}`. Duplicates disappear
- Set operations: `a & b` (in both), `a | b` (in either), `a - b` (in `a` but not `b`), `a ^ b` (in exactly one)
- `sorted(a_set)` gives a sorted list so the output is in a steady order

Useful docs: [Tuples and sequences](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences) · [Sets](https://docs.python.org/3/tutorial/datastructures.html#sets)

## Scenario

**Mavuno School** needs to know who is studying which subjects and who belongs to which clubs. A student can take Mathematics and Physics, one of them, or neither, and can be in several clubs at once, but must only be counted once in the club registers.

## Task

`day_23.py` gives you the data. Write the code that does the following.

1. **Tuples.** The list `student_grades` holds `(student, grade_level)` tuples. Print each one as `<name> is in grade <grade_level>` by unpacking the tuple.
2. **Subjects.** `math_students` and `physics_students` are sets. Create:
   - `both`: students who take **both** Mathematics and Physics
   - `only_one`: students who take **exactly one** of the two
   Print each as a sorted list: `Both subjects: [...]` and `Only one subject: [...]`.
3. **Clubs.** `drama_club`, `chess_club` and `science_club` are sets. Create `all_club_members`: every student who is in **at least one** club, each student only once. Print `Club members (<count>): [...]` with the sorted list.

## Examples

```text
Alice Wanjiku is in grade 9
Brian Otieno is in grade 9
...
Both subjects: ['Brian Otieno', 'Grace Achieng']
Only one subject: ['Alice Wanjiku', 'Fatuma Hassan', 'Kevin Kiprop', 'Peter Mwangi']
Club members (7): ['Alice Wanjiku', 'Brian Otieno', 'Daniel Omondi', 'Esther Chebet', 'Grace Achieng', 'Kevin Kiprop', 'Mercy Njeri']
```

## How to do it

1. Open `day_23.py` and read the data that is given.
2. **Tuples:** `for name, grade in student_grades:` unpacks each tuple into two variables. Print an f-string.
3. **Both subjects:** `math_students & physics_students`. **Only one:** `math_students ^ physics_students`.
4. **All club members:** join the three sets with `|`. Notice that Alice and Kevin are in two clubs but appear once.
5. **Print sorted lists** with `sorted(...)`, because a set has no fixed order and the output would change from run to run.
6. **Check by hand:** who is in both subjects? Does your `both` match?

## Run it

Run this from the `python-daily-practice/` folder:

```bash
python "level-1-beginner/Day 23/day_23.py"
```

The quotes matter because the folder name contains a space.

## Done when

- [ ] Every tuple is printed as `<name> is in grade <grade_level>`
- [ ] `both`, `only_one` and `all_club_members` are sets with the right members
- [ ] The three result lines are printed as sorted lists
- [ ] `NOTES.md` is filled in
- [ ] Your work is committed and pushed to your own branch

## Stretch goals (optional)

- Find the students who take Mathematics but **not** Physics.
- Find the students who are in **no** club at all (compare with everyone in `student_grades`).
