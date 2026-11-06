# Day 24: Dictionaries

> Estimated time: 45 minutes

## Goal

By the end of today you can store information as **key: value** pairs in a dictionary, and add, update, delete and print entries.

## Concepts

- A dictionary maps keys to values: `marks = {"Alice Wanjiku": 78}`
- Read a value with its key: `marks["Alice Wanjiku"]`
- Add or update with assignment: `marks["Peter Mwangi"] = 70`
- Delete with `del marks["Brian Otieno"]`
- Loop over keys and values together: `for name, mark in marks.items():`

Useful docs: [Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)

## Scenario

The **Mavuno School** marks book records one CAT mark per student. During the term a new student joins and gets a mark, a student's mark is corrected after **remedial** lessons, and a student who transfers is removed.

## Task

`day_24.py` already has a dictionary called `marks` with 5 students. Change it in this order:

1. **Add** `"Peter Mwangi"` with the mark `70`.
2. **Update** `"Kevin Kiprop"` to `58` (he improved after remedial lessons).
3. **Delete** `"Brian Otieno"` (he transferred).
4. Print every entry, one per line, in the form `name: mark`.

## Examples

```text
Alice Wanjiku: 78
Fatuma Hassan: 82
Kevin Kiprop: 58
Grace Achieng: 91
Peter Mwangi: 70
```

## How to do it

1. Open `day_24.py` and print the starting dictionary once.
2. **Add:** assign to a key that does not exist yet: `marks["Peter Mwangi"] = 70`.
3. **Update:** assign to a key that already exists. The old value is replaced.
4. **Delete:** `del marks["Brian Otieno"]`. A key that is not there gives a `KeyError`: read the message (Day 6).
5. **Print each entry:** `for name, mark in marks.items():` and an f-string `f"{name}: {mark}"`.
6. **Compare** with the example: 5 lines, Kevin at 58, no Brian.

## Run it

Run this from the `python-daily-practice/` folder:

```bash
python "level-1-beginner/Day 24/day_24.py"
```

The quotes matter because the folder name contains a space.

## Done when

- [ ] Peter Mwangi is added with 70, Kevin Kiprop is 58, and Brian Otieno is gone
- [ ] Each entry is printed as `name: mark`
- [ ] `NOTES.md` is filled in
- [ ] Your work is committed and pushed to your own branch

## Stretch goals (optional)

- Print the student with the highest mark.
- Use `marks.get("Unknown Student", "no mark yet")` to look up a name that may not exist.
