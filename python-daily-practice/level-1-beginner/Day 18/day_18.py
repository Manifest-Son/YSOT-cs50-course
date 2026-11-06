"""Day 18: Loops and conditionals -- the class grade distribution.

Run it from the python-daily-practice/ folder:

    python "level-1-beginner/Day 18/day_18.py"

The full instructions are in README.md (same folder).
"""

count_a = 0
count_b = 0
count_c = 0
count_fail = 0

for student_number in range(1, 11):
    mark = float(input(f"Mark for student {student_number}: "))

    # TODO: add 1 to the right counter:
    #   80 or more      -> count_a
    #   70 up to 80     -> count_b
    #   60 up to 70     -> count_c
    #   below 60        -> count_fail
    # Use if / elif / elif / else, from the highest mark down.

print("Grade summary")
# TODO: print the four counts with the labels A, B, C and Fail.
