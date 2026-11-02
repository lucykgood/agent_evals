"""Parse comma-separated integers."""


def parse_numbers(text: str) -> list[int]:
    if not text.strip():
        return []

    tokens = text.split(",")
    numbers = []
    index = 0
    while index < len(tokens):
        try:
            number = int(tokens[index].strip())
        except ValueError:
            continue
        numbers.append(number)
        index += 1
    return numbers
