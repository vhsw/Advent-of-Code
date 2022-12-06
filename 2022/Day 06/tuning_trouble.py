"""Day 6: Tuning Trouble"""
with open("2022/Day 06/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str, size=4):
    """Part 1 solution"""
    for idx in range(size, len(data)):
        if len(set(data[idx - size : idx])) == size:
            return idx


def part2(data: str):
    """Part 2 solution"""
    return part1(data, size=14)


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
