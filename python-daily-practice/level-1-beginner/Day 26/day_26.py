"""Day 26: Dictionaries, loops and strings -- subject-wise marks for one student.

Run it from the python-daily-practice/ folder:

    python "level-1-beginner/Day 26/day_26.py"

The full instructions are in README.md (same folder).
"""

marks = {
    "Mathematics": 78,
    "English": 85,
    "Kiswahili": 72,
    "Biology": 59,
    "Chemistry": 66,
    "Physics": 91,
}

# Start with the first subject as both the best and the weakest, then improve as you loop.
best_subject = list(marks)[0]
weakest_subject = list(marks)[0]

for subject, mark in marks.items():
    # TODO 1: work out the grade for this mark (A 80+, B 70+, C 60+, D 50+, F below 50).

    # TODO 2: print the subject in CAPITALS, its mark and its grade on one line.

    # TODO 3: if this mark is higher than the best so far, update best_subject.
    #         if it is lower than the weakest so far, update weakest_subject.
    pass

# TODO 4: print "Best subject: ..." and "Weakest subject: ..."
