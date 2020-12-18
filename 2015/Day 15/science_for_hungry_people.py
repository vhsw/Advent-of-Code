"Day 15 answers"
import re
from itertools import combinations_with_replacement

import numpy as np

INPUT = "2015/Day 15/input.txt"


def part1(data):
    "Part 1 answer"
    ingrs = {}
    for line in data:
        name, *props = re.match(
            r"(\w+): (\w+) (-?\d+), (\w+) (-?\d+), (\w+) (-?\d+), (\w+) (-?\d+)",
            line,
        ).groups()
        ingrs[name] = np.fromiter(map(int, props[1::2]), int)

    print(ingrs)
    s = []
    for c in combinations_with_replacement(ingrs, 100):
        tot = sum(ingrs[i] for i in c)
        tot = np.maximum(tot, 0)
        s.append(np.prod(tot))
    return max(s)


def part2(data):
    "Part 2 answer"
    ingrs = {}
    cals = {}
    for line in data:
        name, *props = re.match(
            r"(\w+): (\w+) (-?\d+), (\w+) (-?\d+), (\w+) (-?\d+), (\w+) (-?\d+), (\w+) (-?\d+)",
            line,
        ).groups()
        ingrs[name] = np.fromiter(map(int, props[1:9:2]), int)
        cals[name] = int(props[-1])
    print(ingrs)
    s = []
    for c in combinations_with_replacement(ingrs, 100):
        if sum(cals[i] for i in c) != 500:
            continue
        tot = sum(ingrs[i] for i in c)
        tot = np.maximum(tot, 0)
        s.append(np.prod(tot))
    return max(s)


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.readlines()
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
