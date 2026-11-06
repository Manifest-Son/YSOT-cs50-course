# Day 13: Admission checker

> Estimated time: 45-60 minutes

## Goal

By the end of today you can put together strings, input, conditions and f-strings to build a program that makes a three-way decision and gives a personal message.

## Concepts

- Everything from Days 1-12: `input()`, conversions, comparisons, `and` / `or`, `if` / `elif` / `else`
- Three outcomes from one decision (admitted, waitlisted, rejected)
- Personalised messages with f-strings
- Checking the easy "no" answers first

## Scenario

New students apply to join **Mavuno School**, and the admissions office must decide quickly: admit, put on the **waiting list**, or **reject**. The deputy head has written the rules down and wants the **admission checker** to apply them and print a friendly, personal message.

## Task

Write a program that asks for the applicant's **name**, **age**, **previous average** mark (0-100) and **entrance exam score** (0-100), then decides:

1. **Invalid input:** if the previous average or the entrance score is below 0 or above 100, print `Invalid input` and stop (no decision).
2. **REJECTED** if the age is **below 11 or above 18** (the school takes ages 11 to 18 inclusive).
3. Otherwise:
   - **ADMITTED** if previous average `>= 60` **and** entrance score `>= 50`.
   - **WAITLISTED** if previous average `>= 60` and entrance score is from `40` up to (not including) `50`, **or** previous average is from `50` up to (not including) `60` and entrance score `>= 50`.
   - **REJECTED** for everything else.

Print a message with the applicant's **name** and the decision in capital letters: `ADMITTED`, `WAITLISTED` or `REJECTED`. Add a short reason or a kind sentence if you like.

## Examples

```text
Alice Wanjiku, 14, previous 72, entrance 65   ->  Congratulations Alice Wanjiku, you are ADMITTED to Mavuno School!
Brian Otieno, 13, previous 66, entrance 45    ->  Brian Otieno, you are WAITLISTED. We will contact you if a place opens.
Grace Achieng, 12, previous 55, entrance 70   ->  Grace Achieng, you are WAITLISTED. We will contact you if a place opens.
Peter Mwangi, 10, previous 90, entrance 90    ->  Peter Mwangi, you are REJECTED: the age must be 11 to 18.
Mercy Njeri, 15, previous 45, entrance 80     ->  Mercy Njeri, you are REJECTED.
```

## How to do it

1. Open `day_13.py`. The questions are done for you. Convert the numbers with `int()` / `float()`.
2. **Draw a decision table on paper** with the cases from the Task. Check that every applicant fits exactly one row.
3. **Check the invalid scores first**, then the **age**, because those are quick "no" answers.
4. **Write ADMITTED next** (`and`), then the two WAITLISTED cases joined with `or` (use brackets around each pair), and let `else` be REJECTED.
5. **Print with f-strings** that include `applicant_name`. Keep the three decision words in capital letters exactly as given.
6. **Test boundaries:** age `10`, `11`, `18`, `19`; previous average `49.9`, `50`, `59.9`, `60`; entrance `39.9`, `40`, `49.9`, `50`.

## Run it

Run this from the `python-daily-practice/` folder:

```bash
python "level-1-beginner/Day 13/day_13.py"
```

The quotes matter because the folder name contains a space.

## Done when

- [ ] Every applicant gets exactly one decision (or `Invalid input`)
- [ ] The messages include the applicant's name and the decision in capital letters
- [ ] The age and score boundaries behave as described
- [ ] `NOTES.md` is filled in
- [ ] Your work is committed and pushed to your own branch

## Stretch goals (optional)

- Add a scholarship note when the entrance score is `90` or more.
- Ask for the term of entry and mention it in the message.
