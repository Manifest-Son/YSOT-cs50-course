"""Day 29: Writing functions -- average, grade and pass check for Mavuno School.

Implement the three functions below. The full instructions are in README.md
(same folder).

Replace each `raise NotImplementedError` with your own code.
"""

PASS_MARK = 50


def calculate_average(marks):
    """Return the average of a list of marks as a float. An empty list gives 0.0.

    Examples:
        >>> calculate_average([70, 80, 90])
        80.0
        >>> calculate_average([])
        0.0
    """
    raise NotImplementedError


def get_grade(score):
    """Return the letter grade for a score: A 80-100, B 70-79, C 60-69, D 50-59, F below 50.

    A score below 0 or above 100 is not valid: return "Invalid".

    Examples:
        >>> get_grade(85)
        'A'
        >>> get_grade(50)
        'D'
        >>> get_grade(101)
        'Invalid'
    """
    raise NotImplementedError


def is_passing(score):
    """Return True if the score is at least PASS_MARK, otherwise False.

    Examples:
        >>> is_passing(50)
        True
        >>> is_passing(49.5)
        False
    """
    raise NotImplementedError


def main():
    # Runs when you do:  python "level-1-beginner/Day 29/day_29.py"
    # It only works once your three functions above are written.
    marks = [72, 85, 90]
    average = calculate_average(marks)
    print("Marks:", marks)
    print("Average:", round(average, 2))
    print("Grade:", get_grade(average))
    print("Passing:", is_passing(average))

    # TODO: try the boundary scores from the README (0, 49.9, 50, 79.5, 80, 100, 101)
    # and print get_grade(score) and is_passing(score) for each one.


if __name__ == "__main__":
    main()
