"""Day 22: Reactor Reboot"""
# pylint: disable=invalid-name
import re
from collections import Counter
from dataclasses import dataclass
from itertools import product
from math import prod

with open("2021/Day 22/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


@dataclass(unsafe_hash=True)
class Cube:
    lo: tuple[int, int, int]
    hi: tuple[int, int, int]

    def __and__(self, other):
        if not isinstance(other, Cube):
            return NotImplemented
        lo = tuple(map(max, zip(self.lo, other.lo)))
        hi = tuple(map(min, zip(self.hi, other.hi)))
        return Cube(lo, hi)

    def __bool__(self):
        return all(l <= h for l, h in zip(self.lo, self.hi))

    def volume(self):
        return prod(h - l + 1 for l, h in zip(self.lo, self.hi))

    def __iter__(self):
        return product(*(range(l, h + 1) for l, h in zip(self.lo, self.hi)))


def part1(data: str):
    """Part 1 solution"""
    limit = Cube((-50, -50, -50), (50, 50, 50))
    voxels = set()
    for sign, cube in parse(data):
        cube = cube & limit
        if sign > 0:
            voxels |= set(cube)
        else:
            voxels -= set(cube)
    return len(voxels)


def part2(data: str):
    """Part 2 solution"""
    cubes: Counter[Cube] = Counter()
    for n_sign, n_cube in parse(data):
        update: Counter[Cube] = Counter()
        for cube, sign in cubes.items():
            intersection = cube & n_cube
            if intersection:
                update[intersection] -= sign
        if n_sign > 0:
            update[n_cube] += n_sign
        cubes.update(update)
    return sum(cube.volume() * sign for cube, sign in cubes.items())


def parse(data: str):
    regex = r"(\w+) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)"
    for line in data.splitlines():
        match = re.match(regex, line)
        if not match:
            raise ValueError(line)
        cmd, *groups = match.groups()
        xl, xh, yl, yh, zl, zh = map(int, groups)
        yield 1 if cmd == "on" else -1, Cube((xl, yl, zl), (xh, yh, zh))


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
