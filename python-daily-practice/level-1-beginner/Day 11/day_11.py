"""Day 11: Student portal login -- check the username and password.

Run it from the python-daily-practice/ folder:

    python "level-1-beginner/Day 11/day_11.py"

The full instructions are in README.md (same folder).
"""

# Step 1 (done for you): ask for the username and the password.
username = input("Username: ")
password = input("Password: ")

# Step 2: start by assuming everything is fine. A failed check will turn this to False.
is_valid = True

# Step 3: check 1 -- the username must not contain a space.
# if ...:
#     print("Username must not contain spaces.")
#     is_valid = False

# Step 4: check 2 -- the password must have at least 8 characters.

# Step 5: check 3 -- the password must contain at least one digit.
# Hint: loops are not taught yet, so test each digit:  "0" in password or "1" in password or ...
# has_digit = ...

# Step 6: if everything passed, print  Welcome, <username>!
