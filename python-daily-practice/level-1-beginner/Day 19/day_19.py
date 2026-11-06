"""Day 19: Loops and strings -- names starting with a letter, and vowel counts.

Run it from the python-daily-practice/ folder:

    python "level-1-beginner/Day 19/day_19.py"

The full instructions are in README.md (same folder).
"""

# Step 1 (done for you): one line of names separated by commas, and the chosen letter.
names_line = input("Enter student names, separated by commas: ")
letter = input("Show names starting with: ")

# Step 2: cut the line into names.
names = names_line.split(",")

# Step 3: print the names that start with the letter (ignore upper/lower case).
print(f"Names starting with {letter.upper()}:")
found_any = False
# for raw_name in names:
#     name = raw_name.strip()
#     TODO: if the name starts with the chosen letter, print it and set found_any = True
# TODO: if found_any is still False, print None

# Step 4: print every name with its number of vowels, e.g.  Alice Wanjiku: 6
print("Vowel counts:")
# for raw_name in names:
#     name = raw_name.strip()
#     vowels = 0
#     TODO: loop over the letters of name.lower() and count the vowels a e i o u
#     TODO: print the name and its vowel count
