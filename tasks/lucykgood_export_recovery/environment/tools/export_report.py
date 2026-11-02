"""Export customer totals using the configured input delimiter."""

import csv
import json
from decimal import Decimal
from pathlib import Path


def main() -> None:
    app = Path(__file__).resolve().parents[1]
    config = json.loads((app / "config.json").read_text())
    totals: dict[str, Decimal] = {}
    with (app / "data/orders.csv").open(newline="") as source:
        reader = csv.DictReader(source, delimiter=config["delimiter"])
        if reader.fieldnames != ["customer", "amount"]:
            raise SystemExit(
                f"Expected columns ['customer', 'amount']; found {reader.fieldnames!r}. "
                "Check the input delimiter in config.json."
            )
        for row in reader:
            customer = row["customer"]
            totals[customer] = totals.get(customer, Decimal("0")) + Decimal(row["amount"])
    with (app / "report.csv").open("w", newline="") as output:
        writer = csv.writer(output)
        writer.writerow(["customer", "total"])
        for customer, total in sorted(totals.items()):
            writer.writerow([customer, f"{total:.2f}"])


if __name__ == "__main__":
    main()
