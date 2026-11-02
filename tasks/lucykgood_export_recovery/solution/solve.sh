#!/bin/bash
set -euo pipefail

python - <<'PYTHON'
import json
from pathlib import Path

path = Path("/app/config.json")
config = json.loads(path.read_text())
config["delimiter"] = ";"
path.write_text(json.dumps(config, indent=2) + "\n")
PYTHON
python /app/tools/export_report.py
