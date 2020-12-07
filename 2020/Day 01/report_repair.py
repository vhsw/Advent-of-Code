"Day 01 answers"
from itertools import combinations

INPUT = "2020/Day 01/input.txt"


def part1(data):
    "Part 1 answer"
    for i in data:
        if (n := 2020 - i) in data:
            return i * n


def part2(data):
    "Part 2 answer"
    for i, j in combinations(data, 2):
        if (n := 2020 - i - j) in data:
            return i * j * n


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = set(map(int, fp.readlines()))
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
