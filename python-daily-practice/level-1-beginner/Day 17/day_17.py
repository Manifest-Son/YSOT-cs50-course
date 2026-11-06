"""Day 17: break and continue -- marks entry that skips invalid marks.

Run it from the python-daily-practice/ folder:

    python "level-1-beginner/Day 17/day_17.py"

The full instructions are in README.md (same folder).

Until you write the checks, this loop never stops: press Ctrl+C to quit.
"""

total = 0
count = 0

while True:
    mark = float(input("Enter mark (-1 to stop): "))

    # TODO 1: if the mark is -1, stop the loop (break). Do this check FIRST.

    # TODO 2: if the mark is below 0 or above 100, print "Invalid mark, skipped."
    # and go back to the start of the loop (continue).

    # TODO 3: otherwise add the mark to total and add 1 to count.
    pass

# TODO 4: print "Marks entered: ..." and "Total: ..."
