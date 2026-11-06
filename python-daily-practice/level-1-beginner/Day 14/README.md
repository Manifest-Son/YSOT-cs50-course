# Day 14: Mini project: Report Card v2

> Estimated time: 60 minutes

## Goal

By the end of today you have upgraded your Day 7 report card with letter grades, a pass/fail remark and a personal teacher comment, using strings and `if` statements.

## Concepts

- Reusing your own earlier code (Day 7 for the card, Day 10 for the grades)
- `if` / `elif` / `else` for grades, remarks and comment bands
- Getting the first name from a full name (Day 8)
- f-strings for messages (Day 9)

## Scenario

Parents at **Mavuno School** want more than numbers on the **report card**: they want to see a grade for every subject, a clear pass or fail, and a personal comment from the class teacher.

## Task

**Start from your Day 7 code** (copy it into `day_14.py`). It already asks for the student's name and the marks in `Mathematics`, `English`, `Kiswahili` and `Science`, and prints the total, average and percentage. Upgrade it so the report card also shows:

1. **A letter grade for every subject**: `A` 80-100, `B` 70-79, `C` 60-69, `D` 50-59, `F` below 50.
2. **A remark for the whole card:** `Pass` if the average is at least 50, otherwise `Fail`.
3. **A teacher comment** that uses the student's **first name** and depends on the average:

| Average | Comment |
| --- | --- |
| 80 or more | `Excellent work, <first name>!` |
| 60 to below 80 | `Good effort, <first name>. Keep it up!` |
| 50 to below 60 | `<first name>, you passed. Aim higher next term.` |
| below 50 | `<first name>, please attend the remedial lessons.` |

## Examples

```text
========= MAVUNO SCHOOL =========
         REPORT CARD
Student: Brian Otieno
---------------------------------
Mathematics     68.00   C
English         74.00   B
Kiswahili       81.00   A
Science         59.00   D
---------------------------------
Total          282.00
Average         70.50
Remark: Pass
Teacher's comment: Good effort, Brian. Keep it up!
=================================
```

## How to do it

1. **Copy your Day 7 program** into `day_14.py` and run it to make sure it still works.
2. **Grades are repeated four times**, so write the `if` / `elif` chain for the first subject, run it, then copy it for the other three, changing only the variable names (on Day 29 you will learn a better way).
3. **Remark:** one `if` / `else` on the average.
4. **First name:** `student_name[:student_name.find(" ")]` (Day 8). What happens if the name has no space? Look at the stretch goal.
5. **Comment:** an `if` / `elif` chain on the average, going from the top band down. Build the message with an f-string that includes the first name.
6. **Add the grade and remark lines to the card.** Keep the layout tidy.
7. **Test** an excellent student, a failing student, and one exactly on each band edge (`50`, `60`, `80`).

## Run it

Run this from the `python-daily-practice/` folder:

```bash
python "level-1-beginner/Day 14/day_14.py"
```

The quotes matter because the folder name contains a space.

## Done when

- [ ] Each subject shows its mark and the right letter grade
- [ ] The card shows the total, the average, a `Pass` / `Fail` remark and the teacher's comment
- [ ] The comment uses the student's first name and matches the average band
- [ ] `NOTES.md` is filled in
- [ ] Your work is committed and pushed to your own branch

## Stretch goals (optional)

- Make the first-name code work when the student typed only one name (no space).
- Add a line that names the student's best subject (compare the four marks).
