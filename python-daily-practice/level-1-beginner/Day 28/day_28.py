"""Day 28: Mini project -- the Mavuno School Student Database (in memory).

Run it from the python-daily-practice/ folder:

    python "level-1-beginner/Day 28/day_28.py"

The full instructions are in README.md (same folder).

Until you write the Exit option, this menu never stops: press Ctrl+C to quit.
"""

students = []   # each student is a dictionary: name, age, class, marks

while True:
    print()
    print("--- Mavuno Student Database ---")
    print("1. Add student")
    print("2. View all students")
    print("3. Search by name")
    print("4. Delete a student")
    print("5. Show class topper")
    print("6. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        # TODO: ask for name, age, class and the three marks; build the dictionary;
        # append it to students; print "Student added."
        pass
    elif choice == "2":
        # TODO: print "No students yet." or one line per student
        pass
    elif choice == "3":
        # TODO: ask for a name, find the student (ignore capitals and spaces), print details
        pass
    elif choice == "4":
        # TODO: ask for a name, remove the student if found
        pass
    elif choice == "5":
        # TODO: find and print the class topper (highest average; the first added wins a tie)
        pass
    elif choice == "6":
        # TODO: print "Goodbye!" and stop the loop
        pass
    else:
        # TODO: print "Invalid choice."
        pass
