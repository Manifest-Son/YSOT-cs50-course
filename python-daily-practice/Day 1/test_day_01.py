"""Tests for Day 1. Run from python-daily-practice/:

    python -m pytest "Day 1" -q
"""

import pytest

import day_01


@pytest.mark.parametrize(
    "name, expected",
    [
        ("Ada", "Hello, Ada!"),
        ("  Grace  ", "Hello, Grace!"),
        ("Linus Torvalds", "Hello, Linus Torvalds!"),
        ("", "Hello, friend!"),
        ("   ", "Hello, friend!"),
    ],
)
def test_greet(name, expected):
    assert day_01.greet(name) == expected


@pytest.mark.parametrize(
    "full_name, expected",
    [
        ("Ada Lovelace", "A.L."),
        ("grace brewster murray hopper", "G.B.M.H."),
        ("  alan    turing ", "A.T."),
        ("Madonna", "M."),
        ("", ""),
        ("   ", ""),
    ],
)
def test_initials(full_name, expected):
    assert day_01.initials(full_name) == expected


@pytest.mark.parametrize(
    "celsius, expected",
    [
        (0, 32.0),
        (100, 212.0),
        (-40, -40.0),
        (37, 98.6),
        (21.5, 70.7),
    ],
)
def test_celsius_to_fahrenheit(celsius, expected):
    assert day_01.celsius_to_fahrenheit(celsius) == pytest.approx(expected)


def test_celsius_to_fahrenheit_returns_a_float():
    assert isinstance(day_01.celsius_to_fahrenheit(0), float)


@pytest.mark.parametrize(
    "text, expected",
    [
        ("Python", 1),
        ("YSOT", 1),
        ("AEIOU aeiou", 10),
        ("rhythm", 0),
        ("Programming is fun!", 5),
        ("", 0),
    ],
)
def test_count_vowels(text, expected):
    assert day_01.count_vowels(text) == expected
