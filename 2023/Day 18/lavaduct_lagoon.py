"""Day 18: Lavaduct Lagoon"""
from typing import NamedTuple

with open("2023/Day 18/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str, swap=False):
    """Part 1 solution"""
    pos = 0j
    poly: list[complex] = []
    for instr in parse(data, swap):
        poly.append(pos)
        pos += instr.direction * instr.distance
    assert pos == 0j

    offsets = {
        1 + 1j: 0,
        1 - 1j: 1,
        -1 + 1j: -1j,
        -1 - 1j: 1 - 1j,
    }

    edges = []

    for prv, cur, nxt in zip([poly[-1]] + poly, poly, poly[1:] + [poly[0]]):
        a = prv - cur
        a /= abs(a)
        b = nxt - cur
        b /= abs(b)
        edges.append(cur + offsets[b - a])

    return int(area(edges))


def part2(data: str):
    """Part 2 solution"""
    return part1(data, swap=True)


def area(poly: list[complex]):
    return 0.5 * abs(
        sum(a.real * b.imag - b.real * a.imag for (a, b) in zip(poly, poly[1:]))
    )


class Instruction(NamedTuple):
    direction: complex
    distance: int


def parse(data: str, swap=False):
    dirs = {
        "R": 1,
        "0": 1,
        "D": -1j,
        "1": -1j,
        "L": -1,
        "2": -1,
        "U": 1j,
        "3": 1j,
    }
    for line in data.splitlines():
        direction, distance, color = line.split()
        base = 10
        if swap:
            color = color.strip("(#)")
            distance = color[:5]
            direction = color[5]
            base = 16

        yield Instruction(dirs[direction], int(distance, base))


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
