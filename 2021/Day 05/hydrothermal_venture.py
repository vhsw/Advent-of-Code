"""Day 5: Hydrothermal Venture"""
import re
from collections import defaultdict
from typing import DefaultDict

with open("2021/Day 05/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    grid = create_grid(data)
    return sum(v > 1 for v in grid.values())


def create_grid(data: str):
    grid: DefaultDict[str, int] = defaultdict(int)
    for src, dst in parse(data):
        vec = dst - src
        if vec.real == 0 or vec.imag == 0:
            for pos in complex_range(src, dst):
                grid[pos] += 1
    return grid


def create_diag_grid(data: str):
    grid: DefaultDict[str, int] = defaultdict(int)
    for src, dst in parse(data):
        vec = dst - src
        if vec.real == 0 or vec.imag == 0 or abs(vec.real) == abs(vec.imag):
            for pos in complex_range(src, dst):
                grid[pos] += 1
    return grid


def part2(data: str):
    """Part 2 solution"""
    grid = create_diag_grid(data)
    return sum(v > 1 for v in grid.values())


def parse(data: str):
    return map(parse_line, data.splitlines())


def parse_line(line: str):
    match = re.match(r"(\d+),(\d+) -> (\d+),(\d+)", line)
    if not match:
        raise ValueError(line)
    c0, r0, c1, r1 = map(int, match.groups())  # pylint: disable="invalid-name"
    src = complex(c0, r0)
    dst = complex(c1, r1)
    return src, dst


def complex_range(start: complex, stop: complex):
    direction = stop - start
    if direction.real <= 0 and direction.imag <= 0:
        start, stop = stop, start
        direction = -direction
    steps = int(max(abs(direction.real), abs(direction.imag)))
    d_pos = direction / steps
    for step in range(steps + 1):
        yield start + d_pos * step


def draw(grid: dict[complex, int]):
    max_c = int(max(k.real for k in grid))
    max_r = int(max(k.imag for k in grid))
    return "\n".join(
        "".join(str(grid.get(complex(col, row), ".")) for col in range(max_c + 1))
        for row in range(max_r + 1)
    )


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
