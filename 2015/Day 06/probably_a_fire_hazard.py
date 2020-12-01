"Day 06 answers"
import re

import numpy as np
import pylab as plt

INPUT = "2015/Day 06/input.txt"


def parse(line):
    match = re.match(r"(.+) (\d+),(\d+) through (\d+),(\d+)", line)
    command, x0, y0, x1, y1 = match.groups()
    return command, int(x0), int(y0), int(x1), int(y1)


def part1(data):
    "Part 1 answer"
    grid: np.ndarray = np.zeros((1000, 1000), dtype=bool)
    for command, x0, y0, x1, y1 in map(parse, data):
        size_x = x1 - x0 + 1
        size_y = y1 - y0 + 1
        mask = np.ones((size_x, size_y), dtype=bool)
        mask = np.pad(mask, ((x0, 1000 - x1 - 1), (y0, 1000 - y1 - 1)))
        if command == "turn on":
            grid = grid | mask
        elif command == "turn off":
            grid = grid & np.invert(mask)
        elif command == "toggle":
            grid = grid ^ mask
        else:
            raise ValueError(f"unknown command: {command}")

    plt.imshow(grid, interpolation="none", vmin=0, vmax=1)
    plt.show()
    return np.sum(grid)


def part2(data):
    "Part 2 answer"
    grid: np.ndarray = np.zeros((1000, 1000), dtype=int)
    for command, x0, y0, x1, y1 in map(parse, data):
        size_x = x1 - x0 + 1
        size_y = y1 - y0 + 1
        mask = np.ones((size_x, size_y), dtype=int)
        mask = np.pad(mask, ((x0, 1000 - x1 - 1), (y0, 1000 - y1 - 1)))
        if command == "turn on":
            grid = grid + mask
        elif command == "turn off":
            grid = np.maximum(grid - mask, 0)
        elif command == "toggle":
            grid = grid + (2 * mask)
        else:
            raise ValueError(f"unknown command: {command}")
    plt.imshow(grid, interpolation="none", vmin=0)
    plt.show()
    return np.sum(grid)


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.readlines()

    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
