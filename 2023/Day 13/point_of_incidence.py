"""Day 13: Point of Incidence"""
with open("2023/Day 13/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str, max_smuges=0):
    """Part 1 solution"""
    patterns = parse(data)
    cols: list[int] = []
    rows: list[int] = []
    for pattern in patterns:
        if row := find_reflection_row(pattern, max_smuges):
            rows.append(row)
            continue
        if col := find_reflection_row(list(zip(*pattern)), max_smuges):
            cols.append(col)

    return sum(cols) + 100 * sum(rows)


def part2(data: str):
    """Part 2 solution"""
    return part1(data, max_smuges=1)


def parse(data: str):
    return [pattern.splitlines() for pattern in data.split("\n\n")]


def find_reflection_row(pattern: list[str], max_smuges: int):
    for row in range(1, len(pattern)):
        smuges = sum(strcmp(a, b) for a, b in zip(pattern[:row][::-1], pattern[row:]))
        if smuges == max_smuges:
            return row


def strcmp(a: str, b: str):
    return sum(char_a != char_b for char_a, char_b in zip(a, b))


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
