"""Day 20: The teacher menu -- enter marks, view the average, exit.

Run it from the python-daily-practice/ folder:

    python "level-1-beginner/Day 20/day_20.py"

The full instructions are in README.md (same folder).

Until you write the Exit option, this menu never stops: press Ctrl+C to quit.
"""

total = 0
count = 0

while True:
    print()
    print("--- Teacher menu ---")
    print("1. Enter marks")
    print("2. View average")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        # TODO: ask for a mark; if it is below 0 or above 100 print "Invalid mark.";
        # otherwise add it to total, add 1 to count and print "Mark saved."
        pass
    elif choice == "2":
        # TODO: if count is 0 print "No marks entered yet." otherwise print the average (2 decimals)
        pass
    elif choice == "3":
        # TODO: print "Goodbye!" and stop the loop
        pass
    else:
        # TODO: print "Invalid choice."
        pass
