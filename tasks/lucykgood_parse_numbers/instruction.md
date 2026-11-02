# Fix `parse_numbers(text)` in `/app/project/parser.py`.

The function must parse a comma-separated string of integers and return them as a list, preserving their order.

Required behaviors:
- Accept positive integers, negative integers, and zero.
- Allow whitespace around each integer.
- Return an empty list for an empty or whitespace-only string.
- Raise `ValueError` for invalid integers or empty fields, including leading, trailing, or repeated commas. 
- Terminate promptly for both valid and invalid inputs.

Examples:
- `"1, 2, -3"` -> `[1, 2, -3]`
- `" 0 "` -> `[0]`
- `""` -> `[]`
- `"1, nope, 3"` -> raises `ValueError`
- `"1,,3"` -> raises `ValueError`
- `"1,"` -> raises `ValueError`

Preserve the function name and signature. Do not modify the supplied tests. 
