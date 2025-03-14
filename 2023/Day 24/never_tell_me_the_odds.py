"""Day 24: Never Tell Me The Odds"""

from dataclasses import dataclass
from itertools import combinations
from math import isclose
from typing import Self

with open("2023/Day 24/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str, bounds=(200000000000000, 400000000000000)):
    """Part 1 solution"""
    hailstones = parse_input(data)
    count = 0
    for a, b in combinations(hailstones, 2):
        if is_2d_collision(a, b, bounds):
            count += 1
    return count


def part2(data: str):
    """Part 2 solution"""
    return


def parse_input(data: str):
    return [Hailstone.from_str(line) for line in data.splitlines()]


@dataclass
class Vec3d:
    x: float
    y: float
    z: float

    @classmethod
    def from_str(cls, s: str) -> Self:
        x, y, z = map(float, s.split(", "))
        return cls(x, y, z)

    def dot(self, other: Self) -> float:
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other: Self) -> Self:
        return self.__class__(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x,
        )

    def __add__(self, other: Self) -> Self:
        return self.__class__(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: Self) -> Self:
        return self.__class__(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other: float) -> Self:
        return self.__class__(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, other: float) -> Self:
        return self.__class__(self.x / other, self.y / other, self.z / other)


@dataclass
class Hailstone:
    pos: Vec3d
    vel: Vec3d

    @classmethod
    def from_str(cls, s: str) -> Self:
        pos, vel = s.split(" @ ")
        return cls(Vec3d.from_str(pos), Vec3d.from_str(vel))


def is_2d_collision(a: Hailstone, b: Hailstone, bounds: tuple[int, int]):
    det = a.vel.y * b.vel.x - a.vel.x * b.vel.y
    if isclose(det, 0):
        return False
    diff = a.pos - b.pos
    t = (b.vel.y * diff.x - b.vel.x * diff.y) / det
    s = (a.vel.y * diff.x - a.vel.x * diff.y) / det
    if t < 0 or s < 0:
        return False
    coll = a.pos + a.vel * t
    return bounds[0] <= coll.x <= bounds[1] and bounds[0] <= coll.y <= bounds[1]


if __name__ == "__main__":
    print(f"Part 1: {part1(DATA)}")
    print(f"Part 2: {part2(DATA)}")
