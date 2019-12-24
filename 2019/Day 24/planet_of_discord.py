"""Day 24 Answers"""

from typing import NamedTuple, Iterator
from collections import defaultdict

INPUT = "2019/Day 24/input"


class Vec(NamedTuple):
    """2D Vec"""

    line: int
    col: int

    def __add__(self, other):
        return Vec(self.line + other.line, self.col + other.col)


def parse(data):
    grid = set()
    lines = data.splitlines()
    for line, row in enumerate(lines):
        for col, char in enumerate(row):
            if char == "#":
                grid.add(Vec(line, col))
    ml = len(lines)
    mc = len(lines[0])
    return grid, ml, mc


def neighbors(p: Vec) -> Iterator[Vec]:
    """yield points near p"""
    for dp in [
        Vec(0, 1),
        Vec(0, -1),
        Vec(1, 0),
        Vec(-1, 0),
    ]:
        yield p + dp


def step(grid: set, ml=5, mc=5):
    temp = grid.copy()
    for line in range(ml):
        for col in range(mc):
            point = Vec(line, col)
            num = sum(p in grid for p in neighbors(point))
            if num != 1 and point in grid:
                temp.remove(point)
                continue
            if 1 <= num <= 2 and point not in grid:
                temp.add(point)
    return temp


def biodiversity(grid, ml, mc):
    bd = 0
    for line in range(ml):
        for col in range(mc):
            point = Vec(line, col)
            if point in grid:
                bd += pow(2, line * ml + col)
    return bd


def print_grid(grid, ml=5, mc=5):
    for line in range(ml):
        for col in range(mc):
            point = Vec(line, col)
            if point == Vec(ml // 2, mc // 2):
                print("?", end="")
            elif point in grid:
                print("#", end="")
            else:
                print(".", end="")
        print()
    print()


def part1():
    """Part 1 answer"""
    with open(INPUT) as fp:
        data = fp.read()
    grid, ml, mc = parse(data)
    seen = set()
    while True:
        grid = step(grid, ml, mc)
        bd = biodiversity(grid, ml, mc)
        if bd in seen:
            return bd
        seen.add(bd)


def step_recur(grids, lvl, ml=5, mc=5):
    grid = grids[lvl]
    temp = grid.copy()

    for line in range(ml):
        for col in range(mc):
            point = Vec(line, col)
            if point == Vec(2, 2):
                continue
            num = 0
            for np in neighbors(point):
                if np.line == -1:
                    num += Vec(1, 2) in grids[lvl - 1]
                elif np.line == ml:
                    num += Vec(3, 2) in grids[lvl - 1]
                elif np.col == -1:
                    num += Vec(2, 1) in grids[lvl - 1]
                elif np.col == mc:
                    num += Vec(2, 3) in grids[lvl - 1]
                elif np == Vec(2, 2):
                    if point == (1, 2):
                        num += sum(Vec(0, i) in grids[lvl + 1] for i in range(mc))
                    if point == (3, 2):
                        num += sum(Vec(ml - 1, i) in grids[lvl + 1] for i in range(mc))
                    if point == (2, 1):
                        num += sum(Vec(i, 0) in grids[lvl + 1] for i in range(ml))
                    if point == (2, 3):
                        num += sum(Vec(i, mc - 1) in grids[lvl + 1] for i in range(ml))
                else:
                    num += np in grid

            if num != 1 and point in grid:
                temp.remove(point)
                continue
            if 1 <= num <= 2 and point not in grid:
                temp.add(point)
    return temp


def part2():
    """Part 2 answer"""
    with open(INPUT) as fp:
        data = fp.read()
    grid, ml, mc = parse(data)
    grids = defaultdict(set)
    tmp = defaultdict(set)
    grids[0] = grid
    for i in range(200):
        for lvl in range(-i - 1, i + 2):
            tmp[lvl] = step_recur(grids, lvl, ml, mc)
        grids = tmp.copy()
    return sum(len(g) for g in grids.values())


if __name__ == "__main__":
    ANSWER1 = part1()
    print(f"Part 1: {ANSWER1}")
    ANSWER2 = part2()
    print(f"Part 2: {ANSWER2}")
