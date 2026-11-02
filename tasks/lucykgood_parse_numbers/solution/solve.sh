#!/bin/bash
set -euo pipefail

cat > /app/project/parser.py <<'PYTHON'
"""Parse comma-separated integers."""


def parse_numbers(text: str) -> list[int]:
    if not text.strip():
        return []
    return [int(token.strip()) for token in text.split(",")]
PYTHON
