"""Day 23: Tuples and sets -- subject enrolment and clubs.

Run it from the python-daily-practice/ folder:

    python "level-1-beginner/Day 23/day_23.py"

The full instructions are in README.md (same folder).
"""

# Tuples: (student, grade_level)
student_grades = [
    ("Alice Wanjiku", 9),
    ("Brian Otieno", 9),
    ("Fatuma Hassan", 10),
    ("Kevin Kiprop", 10),
    ("Grace Achieng", 11),
]

# Sets: who studies which subject
math_students = {"Alice Wanjiku", "Brian Otieno", "Fatuma Hassan", "Grace Achieng"}
physics_students = {"Brian Otieno", "Grace Achieng", "Kevin Kiprop", "Peter Mwangi"}

# Sets: who is in which club
drama_club = {"Alice Wanjiku", "Mercy Njeri", "Kevin Kiprop"}
chess_club = {"Brian Otieno", "Kevin Kiprop", "Daniel Omondi"}
science_club = {"Grace Achieng", "Alice Wanjiku", "Esther Chebet"}

# Step 1: print each tuple as  <name> is in grade <grade_level>  (unpack it in a for loop).

# Step 2: both = students taking Mathematics AND Physics;
#         only_one = students taking exactly one of them. Print each as a sorted list.

# Step 3: all_club_members = everyone in at least one club, each only once.
#         Print  Club members (<count>): [...]  with the sorted list.
