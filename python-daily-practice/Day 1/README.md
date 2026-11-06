# Day 1: Functions and strings

> Estimated time: 30-45 minutes

## Goal

By the end of today you can write small Python functions that take a value, work on a string or a number, and `return` a result, and you can check your work with automated tests.

## Concepts

- Defining a function with `def` and sending a value back with `return`
- String methods: `strip()`, `split()`, `upper()`, `lower()`
- Building text with f-strings: `f"Hello, {name}!"`
- Looping over the characters of a string, and the `in` operator
- Basic arithmetic with integers and floats

Useful docs: [Defining functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions) · [String methods](https://docs.python.org/3/library/stdtypes.html#string-methods) · [f-strings](https://docs.python.org/3/tutorial/inputoutput.html#formatted-string-literals)

## Task

Open `day_01.py`. It has four functions that currently do nothing (`raise NotImplementedError`). Implement each one:

| Function | What it must do |
| --- | --- |
| `greet(name)` | Return `"Hello, <name>!"`. Ignore spaces around the name. If the name is empty or only spaces, greet `"friend"` instead. |
| `initials(full_name)` | Return the upper-case first letter of each word, each followed by a dot: `"Ada Lovelace"` becomes `"A.L."`. Any amount of whitespace can separate the words. An empty or blank name gives `""`. |
| `celsius_to_fahrenheit(celsius)` | Convert using `celsius * 9 / 5 + 32` and return a float. |
| `count_vowels(text)` | Count `a`, `e`, `i`, `o`, `u` in the text, ignoring upper/lower case. `y` does not count. |

You only change the four function bodies. Leave `main()` and the tests alone.

## Examples

```python
>>> greet("Ada")
'Hello, Ada!'
>>> greet("   ")
'Hello, friend!'

>>> initials("grace   brewster murray hopper")
'G.B.M.H.'

>>> celsius_to_fahrenheit(100)
212.0

>>> count_vowels("YSOT")      # only the O counts
1
```

## How to do it

1. **Read first, code second.** Open `day_01.py` and read the docstring of each function. The examples in the docstrings are the exact behaviour the tests check.
2. **Start with the tests failing.** From the `python-daily-practice/` folder run `python -m pytest "Day 1" -q`. Every test fails with `NotImplementedError`. That is the starting point, not a problem.
3. **Do the functions in this order**, running the tests after each one so you see the number of passing tests go up:
   1. `celsius_to_fahrenheit`: one line. Apply the formula and return the result.
   2. `greet`: first remove the spaces around `name` with `.strip()`. Then use an `if` to handle the empty case. Finally build the result with an f-string.
   3. `count_vowels`: make the text lower case once, then loop over its characters and add 1 to a counter whenever the character is in `"aeiou"`.
   4. `initials`: `.split()` with no argument splits on any whitespace and drops empty pieces, which handles the extra-spaces cases for you. Take the first letter of each word, upper-case it, and add a dot.
4. **Read the failure messages.** When a test fails, pytest prints what it expected and what your function returned. Compare the two, change one thing, and run again.
5. **Run your program** with the command in the next section. It asks for your name and a temperature and uses your functions.
6. **Write your notes** in `NOTES.md` when everything passes.

If you are stuck for more than 10 minutes on one function, move on to the next one and come back.

## Run and test

Run these from the `python-daily-practice/` folder (see that folder's README for the one-time setup):

```bash
python "Day 1/day_01.py"          # run your program
python -m pytest "Day 1" -q       # run today's tests
```

Run the docstring examples as an extra check (optional):

```bash
python -m doctest "Day 1/day_01.py" -v
```

## Done when

- [ ] All tests in `test_day_01.py` pass
- [ ] `python "Day 1/day_01.py"` runs and prints sensible output for your own name
- [ ] `NOTES.md` is filled in

## Stretch goals (optional)

- Make `greet` capitalise the name nicely: `"  ada LOVELACE "` becomes `"Hello, Ada Lovelace!"` (hint: `str.title()`). Update the test to match.
- Add `fahrenheit_to_celsius` with its own tests.
- Make `count_vowels` also report how many times each vowel appears, as a dictionary such as `{"a": 0, "e": 1, ...}`.
