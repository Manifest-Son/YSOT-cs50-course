"""Day 13: Admission checker -- admit, waitlist or reject an applicant.

Run it from the python-daily-practice/ folder:

    python "level-1-beginner/Day 13/day_13.py"

The full instructions are in README.md (same folder).
"""

# Step 1 (done for you): ask for the applicant's details.
applicant_name = input("Applicant name: ")
age = int(input("Age: "))
previous_average = float(input("Previous average mark (0-100): "))
entrance_score = float(input("Entrance exam score (0-100): "))

# Step 2: decide. Check the quick "no" answers first, then the rest.
if previous_average < 0 or previous_average > 100 or entrance_score < 0 or entrance_score > 100:
    # TODO: print Invalid input
    pass
# elif ... (the age is below 11 or above 18):
#     TODO: REJECTED because of the age
# elif ... (previous average >= 60 and entrance >= 50):
#     TODO: ADMITTED
# elif ... (the two WAITLISTED cases, each in brackets, joined with or):
#     TODO: WAITLISTED
# else:
#     TODO: REJECTED

# Every message should include applicant_name, built with an f-string,
# and the decision in capital letters: ADMITTED, WAITLISTED or REJECTED.
