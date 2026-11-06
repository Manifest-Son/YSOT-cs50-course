"""Day 34: Capstone part 1 -- the foundation of the Mavuno Mini School Management System.

Run it from the python-daily-practice/ folder:

    python "level-1-beginner/Day 34/day_34.py"

The full instructions are in README.md (same folder). Write your plan in NOTES.md first.

A student is a dictionary:
    {"name": "Alice Wanjiku", "age": 15, "class": "Form 2A", "marks": {}}
The register is a list of these dictionaries.
"""


def clean(name):
    """Return a name ready for comparing: no spaces at the ends, all lower case."""
    # TODO: use it in the functions below so "  ALICE wanjiku " matches "Alice Wanjiku"
    raise NotImplementedError


def search_student(students, name):
    """Return the student's dictionary, or None if there is no such student."""
    # TODO
    raise NotImplementedError


def add_student(students, name, age, class_name):
    """Add a student with an empty marks dictionary.

    Return True if added, or False (adding nothing) if a student with that name already exists.
    """
    # TODO
    raise NotImplementedError


def view_students(students):
    """Return a list of lines, one per student:  <name> | <class> | age <age>"""
    # TODO
    raise NotImplementedError


def delete_student(students, name):
    """Remove the student. Return True if deleted, False if not found."""
    # TODO
    raise NotImplementedError


def main():
    students = []
    # A small demo. Add your own checks here as you write each function.
    print(add_student(students, "Alice Wanjiku", 15, "Form 2A"))     # True
    print(add_student(students, "  alice wanjiku ", 15, "Form 2A"))  # False (duplicate)
    for line in view_students(students):
        print(line)
    print(search_student(students, "ALICE WANJIKU"))
    print(delete_student(students, "Brian Otieno"))                    # False (not found)


if __name__ == "__main__":
    main()
