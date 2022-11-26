"""Day 12 Answers"""
import re
from itertools import combinations
from dataclasses import dataclass
from typing import List
from copy import deepcopy
from math import gcd
import sys

from matplotlib import pyplot as plt
import matplotlib.animation

INPUT = "2019/Day 12/input"


def cmpf(a, b):
    if a > b:
        return -1
    if b > a:
        return 1
    return 0


@dataclass(frozen=True)
class Vector:
    x: int
    y: int
    z: int

    def compare(self, other):
        x = cmpf(self.x, other.x)
        y = cmpf(self.y, other.y)
        z = cmpf(self.z, other.z)
        return Vector(x, y, z)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector(x, y, z)

    def norm(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def tupl(self):
        return self.x, self.y, self.z


@dataclass(eq=True)
class Body:
    pos: Vector
    vel: Vector = Vector(0, 0, 0)

    def apply_gravity(self, other):
        if not isinstance(other, Body):
            return NotImplemented
        accel = self.pos.compare(other.pos)
        self.vel += accel

    @property
    def potential_energy(self):
        return self.pos.norm()

    @property
    def kinetic_energy(self):
        return self.vel.norm()

    @property
    def total_energy(self):
        return self.kinetic_energy * self.potential_energy


def step(bodies: List[Body]):
    for b1, b2 in combinations(bodies, 2):
        b1.apply_gravity(b2)
        b2.apply_gravity(b1)
    for b in bodies:
        b.pos += b.vel


def parse_input(data: str) -> List[Body]:
    bodies = []
    for line in data.splitlines():
        match = re.match(r"<x=(-?\d+), y=(-?\d+), z=(-?\d+)>", line)
        if not match:
            raise ValueError
        coords = [*map(int, match.group(1, 2, 3))]
        bodies.append(Body(Vector(*coords)))
    return bodies


def part1():
    """Part 1 answer"""
    with open(INPUT) as fptr:
        bodies = parse_input(fptr.read())
    for _ in range(1000):
        step(bodies)
    return sum(b.total_energy for b in bodies)


def find_period(init_bodies, ax):
    init_pos = deepcopy(init_bodies)
    bodies = deepcopy(init_bodies)
    count = 0
    while True:
        step(bodies)
        count += 1
        for cur, init in zip(bodies, init_pos):
            if (
                getattr(cur.pos, ax) != getattr(init.pos, ax)
                or getattr(cur.vel, ax) != 0
            ):
                break
        else:
            return count


def lcm(x, y, z):
    tmp = x * y // gcd(x, y)
    return tmp * z // gcd(tmp, z)


def period_all(bodies):
    x = find_period(bodies, "x")
    y = find_period(bodies, "y")
    z = find_period(bodies, "z")
    return lcm(x, y, z)


def part2():
    """Part 2 answer"""
    with open(INPUT) as fptr:
        bodies = parse_input(fptr.read())
    return period_all(bodies)


def animate():
    with open(INPUT) as fptr:
        bodies = parse_input(fptr.read())

    def get(bodies, attr):
        return [getattr(b.pos, attr) for b in bodies]

    def update_graph(_):
        step(bodies)
        X = get(bodies, "x")
        Y = get(bodies, "y")
        Z = [(z + 30) for z in get(bodies, "z")]
        graph.set_offsets(list(zip(X, Y)))
        graph.set_sizes(Z)
        return (graph,)

    fig = plt.figure()
    ax = fig.add_subplot()
    ax.set_xlim([-50, 50])
    ax.set_ylim([-50, 50])
    ax.set_facecolor((0, 0, 0))

    X = get(bodies, "x")
    Y = get(bodies, "y")
    Z = [(z + 30) for z in get(bodies, "z")]

    graph = ax.scatter(X, Y, s=Z, c="white")

    ani = matplotlib.animation.FuncAnimation(
        fig, update_graph, blit=True, interval=80, frames=range(100)
    )
    ani.save("2019/Day 12/animation.gif", writer="imagemagick", fps=24)
    plt.show()


if __name__ == "__main__":
    if sys.argv[1] == "anim":
        animate()
        sys.exit()
    ANSWER1 = part1()
    print(f"Part 1: {ANSWER1}")
    ANSWER2 = part2()
    print(f"Part 2: {ANSWER2}")
