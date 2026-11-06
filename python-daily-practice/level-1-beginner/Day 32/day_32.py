"""Day 32: Functions, dictionaries and conditionals -- generate_report_card.

Run it from the python-daily-practice/ folder:

    python "level-1-beginner/Day 32/day_32.py"

The full instructions are in README.md (same folder).
"""

PASS_MARK = 50


# Step 1: paste your own finished calculate_average and get_grade from Day 29 here.
def calculate_average(marks):
    """Return the average of a list of marks (0.0 for an empty list)."""
    raise NotImplementedError


def get_grade(score):
    """Return A (80+), B (70+), C (60+), D (50+) or F (below 50)."""
    raise NotImplementedError


# Step 2: write generate_report_card.
def generate_report_card(student):
    """Return the report card of one student as a single multi-line string.

    Lines, in order: the title, Name, Class, one line per subject "<Subject>: <mark> (<grade>)",
    "Average: <2 decimals> (<grade>)", and "Remark: ...".
    Return the text; do not print it.
    """
    # TODO: build a list of lines, then return "\n".join(lines)
    raise NotImplementedError


def main():
    alice = {"name": "Alice Wanjiku", "age": 15, "class": "Form 2A",
             "marks": {"Mathematics": 78, "English": 85, "Kiswahili": 72}}
    kevin = {"name": "Kevin Kiprop", "age": 15, "class": "Form 2A",
             "marks": {"Mathematics": 40, "English": 52, "Kiswahili": 47}}
    print(generate_report_card(alice))
    print()
    print(generate_report_card(kevin))


if __name__ == "__main__":
    main()
