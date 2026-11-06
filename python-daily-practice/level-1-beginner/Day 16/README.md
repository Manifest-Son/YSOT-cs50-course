# Day 16: while loops

> Estimated time: 30-45 minutes

## Goal

By the end of today you can repeat an action **until a condition changes** with a `while` loop, and count down with one.

## Concepts

- `while condition:` repeats the block as long as the condition is true
- Something inside the loop must eventually make the condition false, or the loop runs forever (press **Ctrl+C** to stop a runaway program)
- A counter variable that changes on every pass: `countdown = countdown - 1`
- Comparing text with `!=` and `==`

Useful docs: [while statement](https://docs.python.org/3/reference/compound_stmts.html#the-while-statement)

## Scenario

Teachers at **Mavuno School** must log in to the staff computer before they can enter marks, and it keeps asking until the password is right. When the lesson ends, the bell countdown starts. Today you build both.

## Task

Write a program in two parts. The correct password is the constant `TEACHER_PASSWORD` (given in the starter).

1. **Password prompt.** Keep asking `Teacher password:` until the teacher types the correct password. After each wrong attempt print `Wrong password. Try again.` When it is right, print `Access granted.`
2. **Bell countdown.** Then print a countdown from **10 down to 0**, one number per line (`10`, `9`, ..., `1`, `0`), and finally print `The bell rings. Class ends!`

## Examples

```text
Teacher password: abc
Wrong password. Try again.
Teacher password: mavuno2026
Access granted.
10
9
8
...
1
0
The bell rings. Class ends!
```

## How to do it

1. Open `day_16.py`. `TEACHER_PASSWORD` is given, and the first question is asked once for you.
2. **Password loop:** after asking once, `while password != TEACHER_PASSWORD:` print the wrong-password message and ask again (put the `input` inside the loop and **assign** the answer to `password`). When the loop ends, the password is correct.
3. **Countdown:** `countdown = 10`, then `while countdown >= 0:` print it and then **subtract 1**. If you forget the subtraction, the loop never ends: press Ctrl+C and fix it.
4. **After the loop** print the bell message. It is not indented, so it runs once.
5. **Test** a correct password on the first try (no "Wrong password" message), then two wrong ones followed by the right one.

## Run it

Run this from the `python-daily-practice/` folder:

```bash
python "level-1-beginner/Day 16/day_16.py"
```

The quotes matter because the folder name contains a space.

## Done when

- [ ] It keeps asking until the right password is typed, with the wrong-password message after each failure
- [ ] The countdown prints 10 down to 0 and then the bell message
- [ ] `NOTES.md` is filled in
- [ ] Your work is committed and pushed to your own branch

## Stretch goals (optional)

- Stop after 3 wrong attempts and print `Account locked`.
- Pause one second between the countdown numbers with `import time` and `time.sleep(1)`.
