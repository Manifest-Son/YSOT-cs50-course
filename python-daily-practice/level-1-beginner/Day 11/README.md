# Day 11: Student portal login

> Estimated time: 45-60 minutes

## Goal

By the end of today you can combine string checks, `if` statements and `input()` to validate what a user types and give a specific message for every problem.

## Concepts

- Checking text: `" " in username` (is there a space?), `len(password)` (how long is it?)
- Checking for a digit: `"0" in password`, `"1" in password`, ... joined with `or`
- Several independent `if` statements (not `elif`) when more than one problem can happen at once
- A flag variable such as `is_valid = True` that you turn to `False` when a check fails
- f-strings for messages

Useful docs: [Boolean operations](https://docs.python.org/3/reference/expressions.html#boolean-operations)

## Scenario

Every student at **Mavuno School** gets a login for the **student portal**, where parents also see fees and report cards. The portal must reject bad usernames and weak passwords and tell the user exactly what is wrong.

## Task

Write a program that asks for a **username** and a **password** and checks:

1. The username has **no spaces**. If it has: print `Username must not contain spaces.`
2. The password has **at least 8 characters**. If not: print `Password must be at least 8 characters.`
3. The password contains **at least one digit** (0-9). If not: print `Password must contain at least one digit.`

Rules:

- Every failed check prints its own message. If three things are wrong, print all three messages.
- If **all** checks pass, print `Welcome, <username>!`
- Use these exact messages (the words `spaces`, `8 characters` and `digit` must be in the right messages).

## Examples

```text
Username: alice wanjiku
Password: abc
Username must not contain spaces.
Password must be at least 8 characters.
Password must contain at least one digit.
```

```text
Username: alice.wanjiku
Password: mavuno2026
Welcome, alice.wanjiku!
```

## How to do it

1. Open `day_11.py`. Asking for the username and the password is done for you.
2. **Start with a flag:** `is_valid = True`. Each failed check prints its message and sets `is_valid = False`.
3. **Username check:** `if " " in username:` ...
4. **Length check:** `if len(password) < 8:` ...
5. **Digit check:** loops come on Day 15, so for now test each digit: `"0" in password or "1" in password or ...` up to `"9"`. Store the answer in a variable such as `has_digit`, then `if not has_digit:` ...
6. **Final step:** after the three checks, `if is_valid:` print the welcome message.
7. **Test** all eight combinations: everything wrong, each single problem, and everything right.

## Run it

Run this from the `python-daily-practice/` folder:

```bash
python "level-1-beginner/Day 11/day_11.py"
```

The quotes matter because the folder name contains a space.

## Done when

- [ ] Each of the three problems gives its own message, and several can appear together
- [ ] A good username and password print the welcome message and nothing else
- [ ] `NOTES.md` is filled in
- [ ] Your work is committed and pushed to your own branch

## Stretch goals (optional)

- Also require at least one upper-case letter (look up `.lower()`: how can you tell if the password changes when you lower-case it?).
- Reject a password that is the same as the username.
