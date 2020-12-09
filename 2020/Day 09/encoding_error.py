"Day 09 answers"
from itertools import combinations

INPUT = "2020/Day 09/input.txt"


def part1(data, preamble=25):
    "Part 1 answer"
    for i, v in enumerate(data[preamble:]):
        if v not in map(sum, combinations(data[i : i + preamble], 2)):
            return v


def part2(data, num):
    "Part 2 answer"
    for r in range(2, len(data)):
        for offset in range(len(data) - r):
            c = data[offset : offset + r]
            if sum(c) == num:
                return min(c) + max(c)


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = list(map(int, fp.readlines()))
    test = [
        35,
        20,
        15,
        25,
        47,
        40,
        62,
        55,
        65,
        95,
        102,
        117,
        150,
        182,
        127,
        219,
        299,
        277,
        309,
        576,
    ]
    assert part1(test, preamble=5) == 127
    assert part2(test, 127) == 62
    num = part1(DATA)
    print(f"Part 1: { num }")
    print(f"Part 2: { part2(DATA, num) }")
