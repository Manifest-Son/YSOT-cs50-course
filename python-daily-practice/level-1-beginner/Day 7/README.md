# Day 7: Mini project: Report Card v1

> Estimated time: 45-60 minutes

## Goal

By the end of today you have combined everything from Days 1-6 into one working program: a teacher enters a student's marks and the program prints a formatted report card.

## Concepts

- `print()`, variables, `input()`, `float()` (Days 1-4)
- Arithmetic and `round()` (Days 3-4)
- Aligned output with f-strings (Day 5)
- Reading error messages when something goes wrong (Day 6)

## Scenario

At the end of every term **Mavuno School** sends a **report card** home to parents. Today you write the first version: it takes a student's name and four marks and prints a card with the total, the average and the percentage.

## Task

Write a program that:

1. Asks for the **student's name**.
2. Asks for the mark in each of **4 subjects**, in this order: `Mathematics`, `English`, `Kiswahili`, `Science` (each out of 100; decimals allowed).
3. Calculates `total`, `average` and `percentage` (`total / 400 * 100`).
4. Prints a **report card** that shows the school name, the student's name, each subject with its mark, and the total, average and percentage (average and percentage rounded to 2 decimal places).

## Examples

```text
Student name: Brian Otieno
Mathematics: 68
English: 74
Kiswahili: 81
Science: 59

========= MAVUNO SCHOOL =========
         REPORT CARD
Student: Brian Otieno
---------------------------------
Mathematics            68.00
English                74.00
Kiswahili              81.00
Science                59.00
---------------------------------
Total                 282.00
Average                70.50
Percentage             70.50 %
=================================
```

The exact look is up to you, but every item above must appear and the numbers must be right.

## How to do it

1. **Plan on paper first.** List what you need to ask, what you need to calculate, and what the card looks like.
2. **Ask for the name and the four marks.** Use `float(input(...))` for the marks. Keep each mark in its own variable (`mathematics`, `english`, ...).
3. **Calculate** the total, average and percentage, one variable per line. Check against the example: 68 + 74 + 81 + 59 = 282.
4. **Print the card.** Start with the title lines, then one line per subject, then the results. Reuse the alignment trick from Day 5: `f"{'Mathematics':<15}{mathematics:>10.2f}"`.
5. **Test with different students**, including a student with decimal marks, and check the numbers with a calculator.
6. If you see an error, read the last line of the traceback first (Day 6).

## Run it

Run this from the `python-daily-practice/` folder:

```bash
python "level-1-beginner/Day 7/day_07.py"
```

The quotes matter because the folder name contains a space.

## Done when

- [ ] The program asks for the name and the four marks in the order given
- [ ] The card shows the school name, the student's name and every subject mark
- [ ] The total, average and percentage are correct and rounded to 2 decimal places
- [ ] `NOTES.md` is filled in
- [ ] Your work is committed and pushed to your own branch

## Stretch goals (optional)

- Print the highest and lowest marks too (compare them with `>` and `<`; you will do this properly with `if` on Day 10).
- Add a line with today's term name, such as `Term 2`, read with `input()`.
