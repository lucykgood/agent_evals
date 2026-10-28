"""Check parser behavior in bounded child processes."""

import json
import subprocess
import sys

import pytest

CASES = [
    ("1, 2, -3", [1, 2, -3]),
    (" 0 ", [0]),
    ("", []),
    (" \t\n", []),
    ("+4, -12, 0, 4", [4, -12, 0, 4]),
    ("7", [7]),
    ("1, nope, 3", None),
    ("1,,3", None),
    ("1,", None),
    (",1", None),
    (",", None),
    ("1,   ,3", None),
    ("1.5", None),
    ("1 2", None),
]


@pytest.mark.parametrize(("text", "expected"), CASES)
def test_parse_numbers(text, expected):
    program = """
import json
import sys
from parser import parse_numbers

try:
    result = parse_numbers(sys.argv[1])
except ValueError:
    print(json.dumps({"error": "ValueError"}))
else:
    assert isinstance(result, list)
    assert all(type(value) is int for value in result)
    print(json.dumps({"result": result}))
"""
    try:
        completed = subprocess.run(
            [sys.executable, "-c", program, text],
            cwd="/app/project",
            capture_output=True,
            text=True,
            timeout=1.0,
            check=False,
        )
    except subprocess.TimeoutExpired:
        pytest.fail(f"parse_numbers({text!r}) did not terminate within 1 second")
    assert completed.returncode == 0, completed.stderr
    actual = json.loads(completed.stdout)
    assert actual == ({"error": "ValueError"} if expected is None else {"result": expected})
