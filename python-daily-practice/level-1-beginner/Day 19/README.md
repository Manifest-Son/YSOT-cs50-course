# Day 19: Loops and strings

> Estimated time: 45 minutes

## Goal

By the end of today you can loop over a list of words and over the letters of a word, filter names, and count characters.

## Concepts

- `text.split(",")` cuts a string at every comma and gives a list of pieces
- `for name in pieces:` takes the pieces one at a time (you can loop over the result of `.split()`; lists are covered properly on Day 22)
- `for letter in name:` takes the letters of a word one at a time
- `.strip()`, `.lower()`, `.startswith(...)` and `in` to test text
- A counter that goes up inside a loop (Day 18)

Useful docs: [String methods](https://docs.python.org/3/library/stdtypes.html#string-methods)

## Scenario

The **Mavuno School** drama club lists the students who signed up. The teacher wants to see only the names that start with a chosen letter, and the print shop wants to know how many vowels each name has (to size the name tags).

## Task

Write a program that:

1. Asks `Enter student names, separated by commas:` and reads **one line** of names, for example `Alice Wanjiku, Brian Otieno, Grace Achieng`.
2. Asks `Show names starting with:` and reads a **letter**.
3. Prints the heading `Names starting with <LETTER>:` (the letter in upper case) and then every name that starts with that letter, **ignoring upper/lower case**, one per line. If there are none, print `None`.
4. Prints the heading `Vowel counts:` and then **every** name with its number of vowels in the form `Alice Wanjiku: 6`. Vowels are `a e i o u`, upper or lower case.

Remove the spaces around each name before using it.

## Examples

```text
Enter student names, separated by commas: Alice Wanjiku, Brian Otieno, grace achieng, Amos Kiplagat
Show names starting with: a
Names starting with A:
Alice Wanjiku
Amos Kiplagat
Vowel counts:
Alice Wanjiku: 6
Brian Otieno: 6
grace achieng: 5
Amos Kiplagat: 5
```

## How to do it

1. Open `day_19.py`. The two questions are done for you.
2. **Cut the line into names:** `names = names_line.split(",")`. Loop with `for raw_name in names:` and clean each with `.strip()`.
3. **First part, filtering:** inside the loop, test `name.lower().startswith(letter.lower())`. Print the matching names. Use a variable (for example `found_any = False`) to know whether to print `None` afterwards.
4. **Second part, counting:** use a second loop over the names. For each name set `vowels = 0`, then `for letter_in_name in name.lower():` and add 1 when `letter_in_name in "aeiou"`.
5. **Test** a letter in upper case, a letter nobody has, and a list with extra spaces around the commas.

## Run it

Run this from the `python-daily-practice/` folder:

```bash
python "level-1-beginner/Day 19/day_19.py"
```

The quotes matter because the folder name contains a space.

## Done when

- [ ] Names starting with the chosen letter are printed, whatever the letter case
- [ ] `None` is printed when nobody matches
- [ ] Every name is listed with the right vowel count
- [ ] `NOTES.md` is filled in
- [ ] Your work is committed and pushed to your own branch

## Stretch goals (optional)

- Also print the name with the most vowels.
- Count consonants too (letters that are not vowels).
