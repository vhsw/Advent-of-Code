"""Day 21: Fractal Art"""
from typing import Iterable

with open("2017/Day 21/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()

INIT = """
.#.
..#
###
""".strip()


def part1(data: str, steps=5):
    """Part 1 solution"""
    grid = to_coords(INIT.splitlines())
    rules = parse(data)
    size = 3
    for _ in range(steps):
        if size % 2 == 0:
            grid = apply_2(grid, size, rules)
            size = size // 2 * 3
        elif size % 3 == 0:
            grid = apply_3(grid, size, rules)
            size = size // 3 * 4

    return len(grid)


def part2(data: str):
    """Part 2 solution"""
    return part1(data, 18)


def parse(data: str):
    rules = {}
    for line in data.splitlines():
        src, dst = line.split(" => ")
        result = to_coords(dst.split("/"))
        rule = src.split("/")
        size = len(rule)
        for rotation in (rule, list(zip(*rule))):
            for flip in (rotation, rotation[::-1]):
                rules[(size, to_coords(flip))] = result
                rules[(size, to_coords([l[::-1] for l in flip]))] = result
    return rules


def to_coords(data: Iterable[Iterable[str]]):
    return frozenset(
        complex(col, row)
        for row, line in enumerate(data)
        for col, char in enumerate(line)
        if char == "#"
    )


def apply_2(grid, size, rules):
    dpos = [0 + 0j, 1 + 0j, 0 + 1j, 1 + 1j]
    new_grid = set()
    for row in range(0, size, 2):
        for col in range(0, size, 2):
            pattern = frozenset(pos for pos in dpos if pos + complex(col, row) in grid)
            replacement = rules[(2, pattern)]
            mapped_pos = complex(3 * col // 2, 3 * row // 2)
            new_grid |= {pos + mapped_pos for pos in replacement}

    return new_grid


def apply_3(grid, size, rules):
    dpos = [0 + 0j, 1 + 0j, 2 + 0j, 0 + 1j, 1 + 1j, 2 + 1j, 0 + 2j, 1 + 2j, 2 + 2j]
    new_grid = set()
    for row in range(0, size, 3):
        for col in range(0, size, 3):
            pattern = frozenset(pos for pos in dpos if pos + complex(col, row) in grid)
            replacement = rules[(3, pattern)]
            mapped_pos = complex(4 * col // 3, 4 * row // 3)
            new_grid |= {pos + mapped_pos for pos in replacement}

    return new_grid


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
