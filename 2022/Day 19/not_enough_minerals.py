"""Day 19: Not Enough Minerals"""
import re
from collections import defaultdict, deque
from functools import cache, partial
from math import prod
from multiprocessing import Pool
from typing import Any, NamedTuple

with open("2022/Day 19/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


class Materials(NamedTuple):
    ore: int = 0
    clay: int = 0
    obsidian: int = 0
    geode: int = 0

    def __le__(self, other: Any) -> bool:
        return all(s <= o for s, o in zip(self, other))

    def __add__(self, other: Any):
        return Materials(*(s + o for s, o in zip(self, other)))

    def __sub__(self, other: Any):
        return Materials(*(s - o for s, o in zip(self, other)))


class Blueprint(NamedTuple):
    ore: Materials
    clay: Materials
    obsidian: Materials
    geode: Materials


class Robots(NamedTuple):
    ore: int = 0
    clay: int = 0
    obsidian: int = 0
    geode: int = 0

    def produce(self):
        return Materials(*self)

    def __add__(self, other: Any):
        return Robots(*(s + o for s, o in zip(self, other)))


def part1(data: str):
    """Part 1 solution"""
    blueprints = parse(data)
    func = partial(run_blueprint, robots=Robots(ore=1), limit=24)
    with Pool() as pool:
        max_geodes = pool.map(func, blueprints)
    return sum(idx * geodes for idx, geodes in enumerate(max_geodes, start=1))


def part2(data: str):
    """Part 2 solution"""
    blueprints = parse(data)[:3]
    func = partial(run_blueprint, robots=Robots(ore=1), limit=32)
    with Pool() as pool:
        max_geodes = pool.map(func, blueprints)
    return prod(max_geodes)


def parse(data: str):
    regex = (
        r"Blueprint \d+: Each ore robot costs (\d+) ore\. "
        r"Each clay robot costs (\d+) ore\. "
        r"Each obsidian robot costs (\d+) ore and (\d+) clay\. "
        r"Each geode robot costs (\d+) ore and (\d+) obsidian\."
    )
    blueprints = []
    for line in data.splitlines():
        match = re.match(regex, line)
        if not match:
            raise ValueError(line)
        materials = tuple(map(int, match.groups()))
        bp = Blueprint(
            ore=Materials(ore=materials[0]),
            clay=Materials(ore=materials[1]),
            obsidian=Materials(ore=materials[2], clay=materials[3]),
            geode=Materials(ore=materials[4], obsidian=materials[5]),
        )
        blueprints.append(bp)
    return blueprints


def run_blueprint(bp: Blueprint, robots: Robots, limit: int):
    max_geodes = 0

    @cache
    def dfs(time: int, materials: Materials, robots: Robots):
        nonlocal max_geodes
        upper_geode_bound = materials.geode + robots.geode * time + triangular(time)
        if time <= 1 or upper_geode_bound <= max_geodes:
            return 0

        time -= 1
        new_materials = materials + robots.produce()
        geodes = dfs(time, new_materials, robots)

        if bp.geode <= materials:
            new_robots = robots + Robots(geode=1)
            geodes = max(geodes, dfs(time, new_materials - bp.geode, new_robots) + time)

        if bp.obsidian <= materials and robots.obsidian < bp.geode.obsidian:
            new_robots = robots + Robots(obsidian=1)
            geodes = max(geodes, dfs(time, new_materials - bp.obsidian, new_robots))

        if bp.clay <= materials and robots.clay < bp.obsidian.clay:
            new_robots = robots + Robots(clay=1)
            geodes = max(geodes, dfs(time, new_materials - bp.clay, new_robots))

        if bp.ore <= materials and robots.ore < max(materials.ore for materials in bp):
            new_robots = robots + Robots(ore=1)
            geodes = max(geodes, dfs(time, new_materials - bp.ore, new_robots))
        max_geodes = max(max_geodes, geodes)
        return geodes

    return dfs(limit, Materials(), robots)


@cache
def triangular(n):
    return (n - 1) * n // 2


# I don't have enough RAM
def run_blueprint_bfs(bp: Blueprint, robots: Robots, limit: int):
    todo = deque([(0, Materials(), robots)])
    seen: set[tuple[int, Materials, Robots]] = set()
    max_geodes: dict[int, int] = defaultdict(int)
    while todo:
        state = todo.popleft()
        if state in seen:
            continue
        time, materials, robots = state
        if time >= limit:
            continue
        geodes = materials.geode + robots.geode
        if geodes < max_geodes[time]:
            continue
        max_geodes[time] = geodes
        time += 1

        if bp.geode <= materials:
            new_materials = materials - bp.geode + robots.produce()
            new_robots = robots + Robots(geode=1)
            todo.append((time, new_materials, new_robots))
            continue

        if bp.obsidian <= materials and robots.obsidian < bp.geode.obsidian:
            new_materials = materials - bp.obsidian + robots.produce()
            new_robots = robots + Robots(obsidian=1)
            todo.append((time, new_materials, new_robots))
        if bp.clay <= materials and robots.clay < bp.obsidian.clay:
            new_materials = materials - bp.clay + robots.produce()
            new_robots = robots + Robots(clay=1)
            todo.append((time, new_materials, new_robots))
        if bp.ore <= materials and robots.ore < max(materials.ore for materials in bp):
            new_materials = materials - bp.ore + robots.produce()
            new_robots = robots + Robots(ore=1)
            todo.append((time, new_materials, new_robots))

        todo.append((time, materials + robots.produce(), robots))
    return max_geodes[limit - 1]


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
