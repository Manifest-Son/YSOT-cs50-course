"""Day 10: if / elif / else -- the Mavuno School grade assigner.

Run it from the python-daily-practice/ folder:

    python "level-1-beginner/Day 10/day_10.py"

The full instructions are in README.md (same folder).
"""

# Step 1 (done for you): ask for the score as a number.
score = float(input("Score (0-100): "))

# Step 2: choose the grade. Complete the chain below. Remember that only the FIRST
# matching branch runs, so go from the invalid scores, then from the highest grade down.
if score < 0 or score > 100:
    # TODO: print a message that contains the word Invalid (and no grade)
    pass
# elif score >= 80:
#     TODO: the grade is A
# elif ...
# else:
#     TODO: the grade is F

# Step 3: print the result as   Grade: B   (use the letter you worked out).
# Hint: store the letter in a variable called grade inside each branch, then print it once at the end,
# but only for valid scores.
