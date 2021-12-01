"""Day 01: Sonar Sweep"""
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view

INPUT = "2021/Day 01/input.txt"


def part1(data):
    """Part 1 answer"""
    depth = list(map(int, data))
    return sum(d2 > d1 for d1, d2 in zip(depth, depth[1:]))


def part2(data):
    """Part 2 answer"""
    depth = np.fromiter(map(int, data), dtype=int)
    window = np.sum(sliding_window_view(depth, 3), axis=1)
    return sum(d2 > d1 for d1, d2 in zip(window, window[1:]))


if __name__ == "__main__":
    with open(INPUT, encoding="utf-8") as fp:
        DATA = fp.read().strip().split()

    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
