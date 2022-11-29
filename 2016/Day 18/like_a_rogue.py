"""Day 18: Like a Rogue"""
with open("2016/Day 18/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str, size: int = 40):
    """Part 1 solution"""
    row = parse(data)
    counter = sum(not r for r in row)
    for _ in range(size - 1):
        row = get_next(row)
        counter += sum(not r for r in row)

    return counter


def part2(data: str):
    """Part 2 solution"""
    return part1(data, size=400000)


def parse(data: str):
    return [char == "^" for char in data]


def get_next(row: list[bool]):
    ext_row = [False] + row + [False]
    return [
        (
            (left and center and not right)
            or (center and right and not left)
            or (left and not center and not right)
            or (right and not center and not left)
        )
        for left, center, right in zip(ext_row, ext_row[1:], ext_row[2:])
    ]


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
