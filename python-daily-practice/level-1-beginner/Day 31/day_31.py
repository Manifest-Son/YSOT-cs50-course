"""Day 31: Functions, lists and loops -- top students and class statistics.

Run it from the python-daily-practice/ folder:

    python "level-1-beginner/Day 31/day_31.py"

The full instructions are in README.md (same folder).
"""

students = [
    {"name": "Alice Wanjiku", "age": 15, "class": "Form 2A",
     "marks": {"Mathematics": 78, "English": 85, "Kiswahili": 72}},
    {"name": "Brian Otieno", "age": 16, "class": "Form 3B",
     "marks": {"Mathematics": 55, "English": 61, "Kiswahili": 70}},
    {"name": "Fatuma Hassan", "age": 14, "class": "Form 1C",
     "marks": {"Mathematics": 92, "English": 88, "Kiswahili": 81}},
    {"name": "Kevin Kiprop", "age": 15, "class": "Form 2A",
     "marks": {"Mathematics": 40, "English": 52, "Kiswahili": 47}},
    {"name": "Grace Achieng", "age": 16, "class": "Form 3B",
     "marks": {"Mathematics": 90, "English": 95, "Kiswahili": 91}},
]


def student_average(student):
    """Return the average of the student's marks as a float (0.0 if there are no marks)."""
    # TODO
    raise NotImplementedError


def get_top_students(students, n):
    """Return the n students with the highest averages, best first.

    Ties keep their original order. If n is bigger than the number of students,
    return all of them.
    """
    # TODO
    raise NotImplementedError


def class_statistics(students):
    """Return {"average": ..., "highest": ..., "lowest": ...} of the students' averages.

    For an empty list return 0.0 for all three.
    """
    # TODO
    raise NotImplementedError


def main():
    print("Top 3 students:")
    for position, student in enumerate(get_top_students(students, 3), start=1):
        print(f"{position}. {student['name']} ({round(student_average(student), 2)})")

    stats = class_statistics(students)
    print("Class average:", round(stats["average"], 2))
    print("Highest:", round(stats["highest"], 2))
    print("Lowest:", round(stats["lowest"], 2))


if __name__ == "__main__":
    main()
