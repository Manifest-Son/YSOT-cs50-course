"""Day 12: Logical operators and nesting -- scholarship eligibility.

Run it from the python-daily-practice/ folder:

    python "level-1-beginner/Day 12/day_12.py"

The full instructions are in README.md (same folder).
"""

# Step 1 (done for you): ask for the three values.
average = float(input("Average mark (0-100): "))
attendance = float(input("Attendance % (0-100): "))
position = int(input("Class position (1 = first): "))

# Step 2: validate first. Print "Invalid input: ..." with a reason for each problem
# (average out of range, attendance out of range, position below 1).
if average < 0 or average > 100:
    # TODO: print Invalid input and the reason
    pass
# elif ... (attendance)
# elif ... (position)

# Step 3: when the input is valid, decide. This inner if goes INSIDE the final else.
# else:
#     if (average >= 80 and attendance >= 90) or position <= 3:
#         TODO: print QUALIFIES for the Mavuno scholarship
#     else:
#         TODO: print DOES NOT QUALIFY for the Mavuno scholarship
