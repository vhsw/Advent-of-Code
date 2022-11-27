"""Day 11: Radioisotope Thermoelectric Generators"""
from collections import deque
import re
from functools import cache
from itertools import chain, combinations
from typing import NamedTuple, FrozenSet

with open("2016/Day 11/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


class Facility(NamedTuple):
    elevator: int
    floors: tuple[FrozenSet[str], ...]

    def __str__(self) -> str:
        lines = []
        for f in range(4):
            el = "E" if f == self.elevator else "."
            lines.append(f"F{f+1} {el} {' '.join(self.floors[f])}")
        return "\n".join(reversed(lines)) + "\n"


def part1(data: str):
    """Part 1 solution"""
    fac = parse(data)
    print(fac)
    seen = set()
    todo = deque([(0, fac)])
    while todo:
        steps, fac = todo.popleft()
        if not any(fac.floors[:-1]):
            return steps
        seen.add(fac)
        for new_fac in possible_moves(fac):
            if new_fac in seen:
                continue
            todo.append((steps + 1, new_fac))


DIRS = ((1,), (1, -1), (1, -1), (-1,))


def possible_moves(fac: Facility):
    src = fac.elevator
    for d_pos in DIRS[src]:
        dst = src + d_pos
        for old, new in move(src, dst, fac):
            floors = list(fac.floors)
            floors[src] = old
            floors[dst] = new
            yield Facility(dst, tuple(floors))


@cache
def move(src: int, dst: int, fac: Facility):
    if src < dst:
        singles = ((pl,) for pl in fac.floors[src])
        possible_items = chain(combinations(fac.floors[src], 2), singles)
    else:
        possible_items = ((pl,) for pl in fac.floors[src])
    for items in possible_items:
        diff = set(items)
        old_floor = fac.floors[src] - diff
        if not check(old_floor):
            continue
        new_floor = fac.floors[dst] | diff
        if not check(new_floor):
            continue
        yield old_floor, new_floor


@cache
def check(floor: tuple[str, ...]):
    gens = set()
    mods = set()
    for item in floor:
        if item[1] == "G":
            gens.add(item[0])
        else:
            mods.add(item[0])
    return gens >= mods if gens else True


def part2(data: str):
    """Part 2 solution"""
    extra = """
    An elerium generator.
    An elerium-compatible microchip.
    A dilithium generator.
    A dilithium-compatible microchip.
    """.replace(
        "\n", " "
    )
    head, tail = data.split("\n", 1)
    head += extra
    return part1(head + "\n" + tail)


def parse(data: str) -> Facility:
    floors: list[frozenset[str]] = []
    for line in data.splitlines():
        floor = set()
        for item, type_ in re.findall(r"(\w+)(-compatible microchip| generator)", line):
            if type_.endswith("generator"):
                floor.add(f"{item[0].upper()}G")
            else:
                floor.add(f"{item[0].upper()}M")
        floors.append(frozenset(floor))
    return Facility(elevator=0, floors=tuple(floors))


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
