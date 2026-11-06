# Day 8: Indexing and slicing

> Estimated time: 30-45 minutes

## Goal

By the end of today you can pick single characters and pieces out of a string using indexes and slices, and measure a string with `len()`.

## Concepts

- A string is a row of characters; each has a position (index) starting at **0**: `name[0]` is the first letter
- Negative indexes count from the end: `name[-1]` is the last letter
- Slices take a piece: `name[0:5]` (from 0 up to, but not including, 5), `name[:5]`, `name[6:]`
- `name[::-1]` reverses a string
- `len(name)` is the number of characters (spaces count)
- `name.find(" ")` gives the index of the first space

Useful docs: [Strings](https://docs.python.org/3/tutorial/introduction.html#strings)

## Scenario

**Mavuno School** prints names in different ways: initials on exercise-book labels, first names on the class register, and so on. Today you write the small tool that takes a student's full name and produces each version.

## Task

Write a program that asks for a student's **full name** (always two words separated by one space, for example `Alice Wanjiku`) and prints four lines:

1. `Initials:` the first letter of each name, upper case, each followed by a dot: `A.W.`
2. `First name:` the first name only: `Alice`
3. `Reversed:` the whole name written backwards: `ukijnaW ecilA`
4. `Length:` the number of characters in the name, **including the space**: `13`

## Examples

```text
Full name (first and last name): Alice Wanjiku
Initials: A.W.
First name: Alice
Reversed: ukijnaW ecilA
Length: 13
```

```text
Full name (first and last name): Kevin Kiprop
Initials: K.K.
First name: Kevin
Reversed: porpiK niveK
Length: 12
```

## How to do it

1. Open `day_08.py`. The first line (asking for the name) is done for you.
2. **Length** is the easiest: `len(full_name)`. Start there so you see your first correct output.
3. **Reversed:** a slice with a step of `-1`: `full_name[::-1]`.
4. **First name:** find where the space is with `full_name.find(" ")`, then slice from the start up to that position: `full_name[:space_position]`.
5. **Initials:** the first initial is `full_name[0]`. The second initial is the letter right after the space: its index is `space_position + 1`. Join them with dots in an f-string: `f"{first}.{last}."`. Use `.upper()` so lower-case names also work.
6. **Test** with a name typed in lower case (`brian otieno`), then with a short name (`Li Wu`).
7. Draw the name on paper with its indexes written under each letter if a slice does not give what you expect.

## Run it

Run this from the `python-daily-practice/` folder:

```bash
python "level-1-beginner/Day 8/day_08.py"
```

The quotes matter because the folder name contains a space.

## Done when

- [ ] All four lines are printed with the labels given in the Task
- [ ] It works for names of different lengths and for lower-case names
- [ ] `NOTES.md` is filled in
- [ ] Your work is committed and pushed to your own branch

## Stretch goals (optional)

- Print the last name only.
- Print every second letter of the name with a slice step: `full_name[::2]`.
