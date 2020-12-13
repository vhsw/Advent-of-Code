"Day 24 answers"
from itertools import combinations
from math import prod

INPUT = "2015/Day 24/input.txt"


def part1(data):
    "Part 1 answer"
    g1 = set()
    i = 0
    while not g1:
        i += 1
        for c in combinations(data, i):
            if sum(data - set(c)) == sum(c) * 2:
                g1.add(c)
    return prod(min(g1, key=prod))


def part2(data):
    "Part 2 answer"
    g1 = set()
    i = 0
    while not g1:
        i += 1
        for c in combinations(data, i):
            if sum(data - set(c)) == sum(c) * 3:
                g1.add(c)
    return prod(min(g1, key=prod))


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = {int(i) for i in fp.readlines()}
    # DATA = set(range(1, 6)) | set(range(7, 12))
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
