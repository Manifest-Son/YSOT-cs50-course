# Day 25: Lists, loops and conditionals

> Estimated time: 45 minutes

## Goal

By the end of today you can walk through a list with a loop, use `if` inside it, and work out the statistics of a set of scores.

## Concepts

- `for score in scores:` visits every item of a list
- Running totals, "highest so far" and "lowest so far" variables
- `if` inside a loop to count or collect only some items
- Building a new list: `failing_scores = []` then `.append(...)`
- The shortcuts `sum()`, `len()`, `max()` and `min()` (try the loop way first, then check yourself with the shortcuts)

Useful docs: [Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) · [Built-in functions](https://docs.python.org/3/library/functions.html)

## Scenario

After the **midsem exam**, the **Mavuno School** head of department wants a quick summary of the scores in a subject: the average, the highest and lowest score, how many students are above average, and the list of failing scores so that those students can be offered **remedial lessons**.

## Task

`day_25.py` gives you a list called `scores` with 12 scores. Create these variables and print them:

| Variable | Meaning |
| --- | --- |
| `average` | the average of all the scores |
| `highest` | the highest score |
| `lowest` | the lowest score |
| `above_average_count` | how many scores are **above** the average (strictly greater) |
| `failing_scores` | a **list** of the scores below the pass mark (`PASS_MARK`, 50), in the original order |

Print each on its own line with a label. Print `average` rounded to 2 decimal places.

Your code must work for **any** list of scores: someone may change the numbers in `scores` and run it again.

## Examples

For the scores in the starter:

```text
Average: 68.25
Highest: 95
Lowest: 39
Above average: 6
Failing scores: [45, 39, 49]
```

## How to do it

1. Open `day_25.py` and look at `scores` and `PASS_MARK`.
2. **Average:** loop through the scores adding each to a `total`, then divide by `len(scores)`.
3. **Highest and lowest:** start with the first score (`scores[0]`) and update when you meet a bigger or smaller one.
4. **Above average:** you need the average first. Loop a second time and count the scores `> average`.
5. **Failing scores:** start with an empty list and append each score `< PASS_MARK`.
6. **Check yourself:** compare with `sum(scores) / len(scores)`, `max(scores)` and `min(scores)`.
7. **Change the numbers** in `scores` (add a score, remove one) and make sure the output still makes sense.

## Run it

Run this from the `python-daily-practice/` folder:

```bash
python "level-1-beginner/Day 25/day_25.py"
```

The quotes matter because the folder name contains a space.

## Done when

- [ ] The five variables exist and are printed with labels
- [ ] The results match the example for the given scores
- [ ] It still works after you change the numbers in `scores`
- [ ] `NOTES.md` is filled in
- [ ] Your work is committed and pushed to your own branch

## Stretch goals (optional)

- Also print the **median** score (sort a copy of the list first).
- Print the scores that are within 5 marks of the pass mark: students who may need support.
