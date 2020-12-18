"Day 03 answers"
from typing import List, Tuple

INPUT = "2016/Day 03/input.txt"


def part1(data: List[Tuple[int, ...]]):
    "Part 1 answer"
    s = 0
    for sides in data:
        a, b, c = sorted(sides)
        if a + b > c:
            s += 1
    return s


def part2(data):
    "Part 2 answer"
    s = 0
    for i in range(0, len(data) - 2, 3):
        for sides in zip(*data[i : i + 3]):
            a, b, c = sorted(sides)
            if a + b > c:
                s += 1
    return s


if __name__ == "__main__":
    with open(INPUT) as fp:
        RAW = fp.read()
    DATA = [tuple(map(int, line.split())) for line in RAW.strip().split("\n")]
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
