"""Exercise C4: safe prompt construction (no string-building with user input)."""


def make_messages(user_input, system_prompt="You are a helpful tutor."):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input},
    ]


# Try changing: modify this file and re-run the tests.
