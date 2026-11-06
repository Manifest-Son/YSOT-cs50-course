# Day 4: Variables, operators and input

> Estimated time: 30-45 minutes

## Goal

By the end of today you can ask the user for information with `input()`, turn the text they type into numbers, do arithmetic on it, and print the result.

## Concepts

- `input("question")` asks the user to type something and gives back **text** (a string), even when they type digits
- Converting text to numbers with `int()` (whole numbers) and `float()` (numbers with decimals)
- Storing values in variables and doing arithmetic with them
- `round(number, 2)` to show 2 decimal places

Useful docs: [input()](https://docs.python.org/3/library/functions.html#input) · [float()](https://docs.python.org/3/library/functions.html#float) · [round()](https://docs.python.org/3/library/functions.html#round)

## Scenario

At **Mavuno School** a teacher records each student's three assessments for the term: **CAT 1**, **CAT 2** and the **midsem exam**. Today you write the small program the teacher uses to enter those three scores and see the student's average.

## Task

In `day_04.py`, write a program that:

1. Asks the teacher for the **student's name** and stores it in a variable called `student_name`.
2. Asks for three scores, **CAT 1**, **CAT 2** and **Midsem**, one `input()` question each. Scores may have decimals, such as `55.5`.
3. Calculates the average of the three scores and stores it in a variable called `average`.
4. Prints the student's name and the average **rounded to 2 decimal places**.

## Examples

```text
Student name: Alice Wanjiku
CAT 1 score: 70
CAT 2 score: 80
Midsem score: 90
Alice Wanjiku's average score: 80.0
```

```text
Student name: Brian Otieno
CAT 1 score: 55.5
CAT 2 score: 60
Midsem score: 70
Brian Otieno's average score: 61.83
```

Your wording can differ, as long as the name and the average (rounded to 2 decimal places) are printed.

## How to do it

1. Open `day_04.py`. The first step is done for you as an example of how `input()` works. Read it, then do the other steps in the same way.
2. **Ask for the three scores.** Remember: `input()` always gives back text. If you add `"70" + "80"` you get `"7080"`, not `150`. Wrap each answer in `float(...)` to get a number: `cat1 = float(input("CAT 1 score: "))`.
3. **Calculate the average:** add the three scores and divide by 3. Put the addition in brackets, `(a + b + c) / 3`, because division happens before addition.
4. **Print the result.** `round(average, 2)` gives 2 decimal places. An f-string such as `f"{student_name}'s average score: {round(average, 2)}"` is a neat way to build the message.
5. **Try it on awkward input.** What happens if you type `55.5` and you used `int()`? Read the error message: it tells you what went wrong. (Fix it by using `float()`.)
6. Check your answers by hand with the two examples above, then fill in `NOTES.md`.

## Run it

Run this from the `python-daily-practice/` folder:

```bash
python "level-1-beginner/Day 4/day_04.py"
```

The quotes matter because the folder name contains a space.

## Done when

- [ ] Your program asks 4 questions: the name and three scores
- [ ] It prints the name and the average rounded to 2 decimal places
- [ ] The variables `student_name` and `average` exist
- [ ] `NOTES.md` is filled in
- [ ] Your work is committed and pushed to your own branch

## Stretch goals (optional)

- Also print the **total** of the three scores.
- Also print the percentage, assuming each score is out of 100 (the average of three scores out of 100 is already a percentage: why?).
