"""Day 33: Debugging day -- this program has FIVE bugs. Find them and fix them.

Run it from the python-daily-practice/ folder:

    python "level-1-beginner/Day 33/day_33.py"

When it is fixed it must print exactly the expected output shown in README.md.
Do not rewrite the program: find the bugs and correct them, one at a time,
and record each one in NOTES.md.
"""

names = ["Alice", "Brian", "Fatuma", "Kevin", "Grace"]
marks = [72, 45, 88, 91, 39]
PASS_MARK = 50

total = 0
passed = 0
highest = marks[0]
top_student = names[0]

for i in range(len(marks) + 1):
    mark = marks[i]
    total = mark
    if mark >= PASS_MARK:
        passed += 1
    if mark > highest:
        highest = mark
        top_student = names[i]

    if mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    elif mark >= 5:
        grade = "D"
    else:
        grade = "F"
    print(f"{names[i]}: {mark} ({grade})")

average = total / len(marks)
print("Total: " + total)
print(f"Average: {round(average, 2)}")
print(f"Top student: {top_studnet} with {highest}")
print(f"Passed: {passed} of {len(marks)}")
