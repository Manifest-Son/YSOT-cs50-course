# Day 9: String methods and f-strings

> Estimated time: 30-45 minutes

## Goal

By the end of today you can clean up messy text with string methods and build new text from pieces with f-strings.

## Concepts

- `.strip()` removes spaces from both ends of a string
- `.title()` makes Each Word Start With A Capital; `.lower()` and `.upper()` change the case
- `.split()` with no argument cuts a string into words, ignoring any amount of spaces, and gives back a **list** of words
- `" ".join(words)` joins a list of words back into one string with single spaces
- Picking words from that list works like picking letters from a string: `words[0]` is the first word, `words[-1]` the last
- f-strings: `f"{first}.{last}@mavuno.ac.ke"`

Useful docs: [String methods](https://docs.python.org/3/library/stdtypes.html#string-methods) · [f-strings](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals)

## Scenario

When parents register a child at **Mavuno School**, the names arrive messy: extra spaces, odd capital letters. The office needs the name cleaned up and a school email address created for the student automatically.

## Task

Write a program that asks for a student's name exactly as typed, for example `"  aLICE   wanjiku "`, and prints:

1. `Clean name:` the name with no extra spaces and each word starting with a capital letter: `Alice Wanjiku`. Single spaces only between the words.
2. `Email:` the school email: `first.last@mavuno.ac.ke`, all in lower case, where *first* is the first word of the name and *last* is the last word. (If the name has three words, ignore the middle ones.)

## Examples

```text
Student name: "  aLICE   wanjiku "  ->  Clean name: Alice Wanjiku
                                       Email: alice.wanjiku@mavuno.ac.ke

Student name: mary  WANJIRU   kamau   ->  Clean name: Mary Wanjiru Kamau
                                          Email: mary.kamau@mavuno.ac.ke
```

(The quotes above only show the spaces. Do not type quotation marks when you run the program.)

## How to do it

1. Open `day_09.py`. The first line (asking for the messy name) is done for you.
2. **Cut it into words:** `words = raw_name.split()`. Notice that this already throws away the extra spaces at both ends and in the middle.
3. **Join the words with single spaces and fix the capitals:** `" ".join(words).title()`.
4. **Pick the first and last word:** `words[0]` and `words[-1]`. Make them lower case with `.lower()`.
5. **Build the email with an f-string:** `f"{first}.{last}@mavuno.ac.ke"`. Keep the school domain in a variable so it is easy to change.
6. **Test** with: all capitals, all lower case, lots of spaces, and a three-word name.
7. Run it and compare with the examples above.

## Run it

Run this from the `python-daily-practice/` folder:

```bash
python "level-1-beginner/Day 9/day_09.py"
```

The quotes matter because the folder name contains a space.

## Done when

- [ ] The clean name has single spaces and a capital letter on every word
- [ ] The email is in lower case and uses the first and last word
- [ ] It works for names with extra spaces and for three-word names
- [ ] `NOTES.md` is filled in
- [ ] Your work is committed and pushed to your own branch

## Stretch goals (optional)

- Also print the initials of the cleaned name.
- Add a number to the email (`alice.wanjiku2026@mavuno.ac.ke`) using a variable for the admission year.
