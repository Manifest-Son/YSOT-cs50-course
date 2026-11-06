# Day 21: Mini project: Class Results Calculator

> Estimated time: 60 minutes

## Goal

By the end of today you have used loops, input, arithmetic and conditions together to process a **whole class** of students and report the results.

## Concepts

- A `for` loop whose length depends on user input: `range(number_of_students)`
- Running totals and "best so far" variables, updated inside the loop
- Averages (Day 4), comparisons (Day 3), f-strings (Day 9)
- Breaking a bigger problem into steps you can check one at a time

## Scenario

After the **CATs** and the **midsem exam**, each **Mavuno School** class teacher needs the results for the class: every student's average, the class average, and the best student, so that the best student can be recognised at assembly.

## Task

Write a program that:

1. Asks `How many students are in the class?` (a whole number).
2. For **each student**, asks for the **name**, then three scores: `CAT 1`, `CAT 2` and `Midsem` (decimals allowed).
3. For each student prints a line with the name and that student's **average rounded to 2 decimal places**, for example `Alice Wanjiku: 80.0`.
4. After all the students, prints:
   - `Class average: <value>`: the average of the students' averages, rounded to 2 decimal places
   - `Best student: <name>`: the student with the highest average. If two students tie, the one entered **first** wins.

## Examples

```text
How many students are in the class? 3
Student 1 name: Alice Wanjiku
CAT 1: 70
CAT 2: 80
Midsem: 90
Alice Wanjiku: 80.0
Student 2 name: Brian Otieno
CAT 1: 60
CAT 2: 50
Midsem: 55
Brian Otieno: 55.0
Student 3 name: Grace Achieng
CAT 1: 90
CAT 2: 95
Midsem: 91
Grace Achieng: 92.0
Class average: 75.67
Best student: Grace Achieng
```

## How to do it

1. Open `day_21.py`. The number of students and the loop header are given, with the variables you will need.
2. **Do one student first.** Inside the loop, ask for the name and three scores and print the average (your Day 4 code).
3. **Add to a class total:** after each student, add their average to `class_total`.
4. **Track the best student:** start with `best_average = -1` and `best_name = ""`. If this student's average is **greater than** `best_average` (use `>`, not `>=`, so the first one wins a tie), save the average and the name.
5. **After the loop** (not indented), divide `class_total` by the number of students and print the two final lines.
6. **Test** a class of 1 student, a class of 3 (use the example), and a class where two students have the same average.

## Run it

Run this from the `python-daily-practice/` folder:

```bash
python "level-1-beginner/Day 21/day_21.py"
```

The quotes matter because the folder name contains a space.

## Done when

- [ ] It asks for the class size, then a name and three scores for each student
- [ ] Every student's average, the class average and the best student are printed correctly
- [ ] A tie is won by the student entered first
- [ ] `NOTES.md` is filled in
- [ ] Your work is committed and pushed to your own branch

## Stretch goals (optional)

- Also print the **lowest** student, and the number of students with an average below 50.
- Print the letter grade next to each student's average (reuse Day 10).
