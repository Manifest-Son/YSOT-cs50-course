"""Day 27: Nested structures -- a list of student records.

Run it from the python-daily-practice/ folder:

    python "level-1-beginner/Day 27/day_27.py"

The full instructions are in README.md (same folder).
"""

# Step 1: build the list of four students. The first one is done for you as a model.
students = [
    {
        "name": "Alice Wanjiku",
        "age": 15,
        "class": "Form 2A",
        "marks": {"Mathematics": 78, "English": 85, "Kiswahili": 72},
    },
    # TODO: add Brian Otieno, Fatuma Hassan and Kevin Kiprop (see the table in the README)
]

# Step 2: print every student as   <name> | <class> | average <average>   (2 decimals).
# for student in students:
#     ...

# Step 3: ask for a name and search for it, ignoring capitals and extra spaces.
search_name = input("Search for a student by name: ")
# TODO: loop through students; if the names match, print the details (name, age, class,
# every subject with its mark, and the average) and remember that you found it.
# TODO: if nobody matched, print "Student not found."
