"""Day 3: Rucksack Reorganization"""

with open("2022/Day 03/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    score = 0
    for line in data.splitlines():
        l = len(line)
        diff = set(line[: l // 2]) & set(line[l // 2 :])
        d = diff.pop()
        score += priority(d)
    return score


def part2(data: str):
    """Part 2 solution"""
    lines = data.splitlines()
    score = 0
    for i in range(0, len(lines), 3):
        diff = set(lines[i]) & set(lines[i + 1]) & set(lines[i + 2])
        d = diff.pop()
        score += priority(d)

    return score


def priority(d: str):
    if "a" <= d <= "z":
        return ord(d) - ord("a") + 1
    else:
        return ord(d) - ord("A") + 27


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
