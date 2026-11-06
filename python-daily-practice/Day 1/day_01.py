"""Day 1: Functions and strings.

Implement the four functions below so that every test in test_day_01.py passes.
The full instructions are in README.md (same folder).

Replace each `raise NotImplementedError` with your own code.
"""


def greet(name):
    """Return a greeting for `name`.

    Leading/trailing spaces in `name` are ignored. If nothing is left after
    removing them, greet "friend" instead.

    Examples:
        >>> greet("Ada")
        'Hello, Ada!'
        >>> greet("  Grace  ")
        'Hello, Grace!'
        >>> greet("   ")
        'Hello, friend!'
    """
    raise NotImplementedError


def initials(full_name):
    """Return the initials of `full_name` as upper-case letters followed by dots.

    Words can be separated by any amount of whitespace. An empty or blank
    name gives an empty string.

    Examples:
        >>> initials("Ada Lovelace")
        'A.L.'
        >>> initials("  grace   brewster murray hopper ")
        'G.B.M.H.'
        >>> initials("")
        ''
    """
    raise NotImplementedError


def celsius_to_fahrenheit(celsius):
    """Convert a temperature from Celsius to Fahrenheit.

    Formula: fahrenheit = celsius * 9 / 5 + 32

    Examples:
        >>> celsius_to_fahrenheit(0)
        32.0
        >>> celsius_to_fahrenheit(100)
        212.0
        >>> celsius_to_fahrenheit(-40)
        -40.0
    """
    raise NotImplementedError


def count_vowels(text):
    """Count the vowels (a, e, i, o, u) in `text`, ignoring upper/lower case.

    The letter "y" is NOT counted as a vowel.

    Examples:
        >>> count_vowels("Python")
        1
        >>> count_vowels("YSOT")
        1
        >>> count_vowels("AEIOU aeiou")
        10
        >>> count_vowels("")
        0
    """
    raise NotImplementedError


def main():
    # Runs when you do:  python "Day 1/day_01.py"
    # It only works once your functions above are implemented.
    name = input("What is your name? ")
    print(greet(name))
    print("Your initials:", initials(name))
    print("Vowels in your name:", count_vowels(name))

    celsius = float(input("Temperature in Celsius? "))
    print(f"{celsius} C is {celsius_to_fahrenheit(celsius):.1f} F")


if __name__ == "__main__":
    main()
