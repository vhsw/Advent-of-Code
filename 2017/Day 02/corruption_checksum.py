"Day 02 answers"
from itertools import combinations

INPUT = "2017/Day 02/input.txt"


def part1(data):
    "Part 1 answer"
    return sum(max(row) - min(row) for row in data)


def part2(data):
    "Part 2 answer"
    s = 0
    for line in data:
        for a, b in combinations(line, 2):
            a, b = max(a, b), min(a, b)
            d, m = divmod(a, b)
            if m == 0:
                s += d
                break
    return s


if __name__ == "__main__":
    with open(INPUT) as fp:
        RAW = fp.read()
    DATA = [[int(i) for i in line.split()] for line in RAW.splitlines()]
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
