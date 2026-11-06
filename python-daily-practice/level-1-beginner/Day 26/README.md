# Day 26: Dictionaries, loops and strings

> Estimated time: 45 minutes

## Goal

By the end of today you can loop through a dictionary, build neat output from its keys and values, and find the biggest and smallest value together with its key.

## Concepts

- `for subject, mark in marks.items():` gives the key and the value in each pass
- `.upper()` and padded f-strings such as `f"{subject.upper():<12}"` for a tidy table
- Tracking the **key** of the best and weakest value, not only the value itself
- Grade bands from Day 10: `A` 80+, `B` 70+, `C` 60+, `D` 50+, `F` below 50

Useful docs: [Looping through dictionaries](https://docs.python.org/3/tutorial/datastructures.html#looping-techniques)

## Scenario

On the **Mavuno School** report card, a student's marks are shown subject by subject, with a grade for each. The **students clinic** also wants to know each learner's **strongest** and **weakest** subject, so that they can guide the learner on where to improve.

## Task

`day_26.py` gives you a dictionary called `marks` with one student's marks in six subjects. Write the code that:

1. Loops through the dictionary and prints one line per subject with the subject name in **capital letters**, its mark and its grade: for example `MATHEMATICS   78   B`.
2. Finds the **best** subject and the **weakest** subject. Keep them in variables called `best_subject` and `weakest_subject` (the subject **names**, not the marks).
3. Prints `Best subject: <name>` and `Weakest subject: <name>` using the normal capitalisation of the name.

Your code must work for **any** marks dictionary, not just this one.

## Examples

```text
MATHEMATICS   78   B
ENGLISH       85   A
KISWAHILI     72   B
BIOLOGY       59   D
CHEMISTRY     66   C
PHYSICS       91   A
Best subject: Physics
Weakest subject: Biology
```

## How to do it

1. Open `day_26.py` and read the dictionary.
2. **Print the table.** In a `for subject, mark in marks.items():` loop, work out `grade` with an `if` / `elif` chain, then print an f-string that pads the subject name: `f"{subject.upper():<12}{mark:>4}   {grade}"`.
3. **Best and weakest:** before the loop, set `best_subject` and `weakest_subject` to the first key (hint: `list(marks)[0]` gives the first key). Inside the loop, compare `mark` with `marks[best_subject]` and `marks[weakest_subject]` and update the names.
4. **Print the two final lines** after the loop.
5. **Try a different dictionary:** change a mark so another subject is best, run again, and check it follows.

## Run it

Run this from the `python-daily-practice/` folder:

```bash
python "level-1-beginner/Day 26/day_26.py"
```

The quotes matter because the folder name contains a space.

## Done when

- [ ] Every subject is printed in capitals with its mark and grade
- [ ] `best_subject` and `weakest_subject` hold the right subject names
- [ ] It still works after you change the marks
- [ ] `NOTES.md` is filled in
- [ ] Your work is committed and pushed to your own branch

## Stretch goals (optional)

- Print the student's average and overall grade after the table.
- If two subjects tie for best, print both.
