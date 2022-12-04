"""Day 4: Camp Cleanup"""
with open("2022/Day 04/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    count = 0
    for pair in parse(data):
        (a_lo, a_hi), (b_lo, b_hi) = sorted(pair, key=lambda p: (p[0], -p[1]))
        if a_lo <= b_lo and b_hi <= a_hi:
            count += 1

    return count


def part2(data: str):
    """Part 2 solution"""
    count = 0
    for pair in parse(data):
        (a_lo, a_hi), (b_lo, _) = sorted(pair, key=lambda p: (p[0], -p[1]))
        if a_lo <= b_lo <= a_hi:
            count += 1

    return count


def parse(data: str):
    pairs = []
    for line in data.splitlines():
        range_a, range_b = line.split(",")
        a_lo, a_hi = map(int, range_a.split("-"))
        b_lo, b_hi = map(int, range_b.split("-"))
        pairs.append(((a_lo, a_hi), (b_lo, b_hi)))
    return pairs


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
