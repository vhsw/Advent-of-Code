"Day 03 answers"
from typing import Counter

import numpy as np

INPUT = "2015/Day 03/input.txt"


def part1(data):
    "Part 1 answer"
    c = Counter()
    pos = np.array([0, 0])
    c.update((tuple(pos),))
    for char in data:
        dpos = {"^": (1, 0), ">": (0, 1), "v": (-1, 0), "<": (0, -1)}[char]
        pos += dpos
        c.update((tuple(pos),))
    return len(c)


def part2(data):
    "Part 2 answer"
    c = Counter()
    santa = np.array([0, 0])
    robo_santa = np.array([0, 0])
    c.update((tuple(santa), tuple(robo_santa)))
    is_santa = True
    for char in data:
        if is_santa:
            pos = santa
        else:
            pos = robo_santa
        dpos = {"^": (1, 0), ">": (0, 1), "v": (-1, 0), "<": (0, -1)}[char]
        pos += dpos
        c.update((tuple(pos),))
        is_santa = not is_santa
    return len(c)


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.read()
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
