"""Day 1: Calorie Counting"""
with open("2022/Day 01/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    elfs = parse(data)
    return max(map(sum, elfs))


def part2(data: str):
    """Part 2 solution"""
    elfs = parse(data)
    return sum(sorted(map(sum, elfs))[-3:])


def parse(data: str):
    return [[int(line) for line in group.splitlines()] for group in data.split("\n\n")]


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
