"""Day 14: Regolith Reservoir"""
from itertools import count
from math import copysign

with open("2022/Day 14/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    grid, lower_bound = parse(data)
    for num_particles in count():
        res = drop(grid, lower_bound)
        if res is None:
            return num_particles
        grid.add(res)


def part2(data: str):
    """Part 2 solution"""
    grid, lower_bound = parse(data)
    src = complex(500, 0)
    for num_particles in count():
        res = drop2(grid, lower_bound)
        if res == src:
            return num_particles + 1
        grid.add(res)


def parse(data: str):
    grid = set()
    lower_bound = 0.0
    for line in data.splitlines():
        points = [complex(*map(int, p.split(","))) for p in line.split(" -> ")]
        for a, b in zip(points, points[1:]):
            lower_bound = max(lower_bound, a.imag, b.imag)
            d_pos = complex(norm(a.real, b.real), norm(a.imag, b.imag))
            pos = a
            grid.add(pos)
            while pos != b:
                pos += d_pos
                grid.add(pos)
    return grid, lower_bound


def norm(a, b):
    delta = b - a
    value = min(1, abs(delta))
    return copysign(value, delta)


def drop(grid: set[complex], lower_bound: float, src=complex(500, 0)):
    pos = src
    while True:
        if pos.imag > lower_bound:
            return None
        dst = pos + 1j
        if dst not in grid:
            pos = dst
            continue
        dst = pos + (-1 + 1j)
        if dst not in grid:
            pos = dst
            continue
        dst = pos + (1 + 1j)
        if dst not in grid:
            pos = dst
            continue
        return pos


def drop2(grid: set[complex], lower_bound: float, src=complex(500, 0)):
    pos = src
    while True:
        dst = pos + 1j
        if dst not in grid and dst.imag < (lower_bound + 2):
            pos = dst
            continue
        dst = pos + (-1 + 1j)
        if dst not in grid and dst.imag < (lower_bound + 2):
            pos = dst
            continue
        dst = pos + (1 + 1j)
        if dst not in grid and dst.imag < (lower_bound + 2):
            pos = dst
            continue
        return pos


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
