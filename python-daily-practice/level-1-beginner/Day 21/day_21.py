"""Day 21: Mini project -- Class Results Calculator for Mavuno School.

Run it from the python-daily-practice/ folder:

    python "level-1-beginner/Day 21/day_21.py"

The full instructions are in README.md (same folder).
"""

# Step 1 (done for you): how many students are in the class?
number_of_students = int(input("How many students are in the class? "))

class_total = 0       # the sum of every student's average
best_average = -1     # the highest average seen so far
best_name = ""        # who has it

for student_number in range(1, number_of_students + 1):
    # Step 2: ask for the name and the three scores of this student.
    name = input(f"Student {student_number} name: ")
    # cat1 = float(input("CAT 1: "))
    # ...

    # Step 3: work out this student's average and print  <name>: <average>  (2 decimals).

    # Step 4: add the average to class_total.

    # Step 5: if this average is HIGHER than best_average, remember it and the name.
    pass

# Step 6: after the loop, print the class average and the best student.
