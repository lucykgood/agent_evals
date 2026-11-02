Run `python /app/tools/export_report.py` to generate `/app/report.csv` from
`/app/data/orders.csv`. The report must contain each customer's total order
amount, sorted by customer name, with columns `customer,total` and amounts
formatted to two decimal places.

Use `/app/HANDOFF.md` as background from the previous investigation.

If the export fails, diagnose and fix the configuration problem, then rerun it.
Preserve the input data, exporter source, and unrelated configuration values.
