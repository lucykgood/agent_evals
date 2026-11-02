"""Check recovery output and preservation of the original inputs."""

import csv
import hashlib
import json
import subprocess
import sys
from pathlib import Path

APP = Path("/app")


def test_config() -> None:
    assert json.loads((APP / "config.json").read_text()) == {
        "delimiter": ";",
        "currency": "USD",
    }


def assert_report() -> None:
    with (APP / "report.csv").open(newline="") as report:
        assert list(csv.reader(report)) == [
            ["customer", "total"],
            ["Linus", "0.10"],
            ["Lucy", "15.90"],
            ["Sally", "10.00"],
        ]


def test_generated_report() -> None:
    assert_report()


def test_input_unchanged() -> None:
    assert (APP / "data/orders.csv").read_bytes() == (
        b"customer;amount\nLucy;12.50\nSally;7.25\nLucy;3.40\nLinus;0.10\nSally;2.75\n"
    )


def test_exporter_unchanged() -> None:
    source = (APP / "tools/export_report.py").read_bytes()
    assert (
        hashlib.sha256(source).hexdigest()
        == "aab4544ca934831453616f1f852b570cf65e81d9e946f0f0a8d8bc361c4b117e"
    )


def test_export_can_be_repeated() -> None:
    result = subprocess.run(
        [sys.executable, str(APP / "tools/export_report.py")],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert_report()
