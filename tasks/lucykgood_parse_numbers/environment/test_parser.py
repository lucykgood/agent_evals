"""Tests for the parser."""

import pytest
from parser import parse_numbers


@pytest.mark.parametrize(
    ("text", "expected"),
    [("1, 2, -3", [1, 2, -3]), (" 0 ", [0]), ("", []), ("  ", [])],
)
def test_valid_numbers(text, expected):
    assert parse_numbers(text) == expected


@pytest.mark.parametrize("text", ["1, nope, 3", "1,,3", "1,"])
def test_invalid_numbers(text):
    with pytest.raises(ValueError):
        parse_numbers(text)
