"""Day 35: Capstone part 2 -- finish the Mavuno Mini School Management System.

Run it from the python-daily-practice/ folder:

    python "level-1-beginner/Day 35/day_35.py"

The full instructions are in README.md (same folder).

How to start:
  1. Copy your finished Day 34 code here (clean, search_student, add_student,
     view_students, delete_student).
  2. Copy your own calculate_average and get_grade (Day 29), calculate_fees (Day 30),
     class_statistics and get_top_students (Day 31), and generate_report_card (Day 32).
  3. Write enter_marks, the input helpers and main() below.
"""

PASS_MARK = 50

# ---------------------------------------------------------------------------
# Paste your Day 34 functions here: clean, search_student, add_student,
# view_students, delete_student.
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# Paste your earlier functions here: calculate_average, get_grade (Day 29),
# calculate_fees (Day 30), student_average, class_statistics, get_top_students (Day 31),
# generate_report_card (Day 32).
# ---------------------------------------------------------------------------


def enter_marks(students, name, subject, mark):
    """Store the mark under the subject in the student's marks.

    Return True on success. Return False if the student does not exist
    or the mark is not between 0 and 100.
    """
    # TODO
    raise NotImplementedError


def read_number(prompt, low, high):
    """Keep asking until the user types a number from low to high (inclusive); return it as a float.

    Hint: text.replace(".", "", 1).isdigit() is True for "78" and "55.5" but not for "abc".
    """
    # TODO
    raise NotImplementedError


def read_whole_number(prompt):
    """Keep asking until the user types a whole number (text.isdigit()); return it as an int."""
    # TODO
    raise NotImplementedError


def main():
    students = []

    while True:
        print()
        print("--- Mavuno School Management System ---")
        print("1. Add student")
        print("2. View all students")
        print("3. Search for a student")
        print("4. Delete a student")
        print("5. Enter marks")
        print("6. Print report card")
        print("7. Class statistics")
        print("8. Top 3 students")
        print("9. Fee calculator")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == "0":
            print("Goodbye!")
            break
        # TODO: elif choice == "1": ... one branch per menu option, each calling your functions
        #       and doing the printing. Build and test ONE option at a time.
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
