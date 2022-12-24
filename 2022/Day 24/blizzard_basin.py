"""Day 24: Blizzard Basin"""

import contextlib
from dataclasses import dataclass, field
from functools import cache
from queue import PriorityQueue

with open("2022/Day 24/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    state: tuple[int, complex] = field(compare=False)


def part1(data: str, start_step=0, reverse=False):
    """Part 1 solution"""
    size, start, end, blizzards, walls = parse(data)
    if reverse:
        end, start = start, end
    pq: PriorityQueue[PrioritizedItem] = PriorityQueue()
    pq.put(PrioritizedItem(0, (start_step, start)))
    seen = set()
    while not pq.empty():
        state = pq.get().state
        if state in seen:
            continue
        seen.add(state)
        step, pos = state
        if pos == end:
            return step
        if pos in walls or pos in get_blizzard_pos(step, size, blizzards):
            continue

        for d_pos in (0, 1, -1, -1j, 1j):
            dst = pos + d_pos
            if dst.real < 0:
                continue

            pq.put(
                PrioritizedItem(
                    manhattan_distance(end, dst) + step + 1, (step + 1, dst)
                )
            )


def part2(data: str):
    """Part 2 solution"""
    steps_front = part1(data)
    steps_back = part1(data, start_step=steps_front, reverse=True)
    return part1(data, start_step=steps_back)


DIRECTIONS = {
    "v": 1 + 0j,
    ">": 0 + 1j,
    "<": 0 - 1j,
    "^": -1 + 0j,
}


def parse(data: str):
    lines = data.splitlines()
    size = complex(len(lines), len(lines[0]))
    start = complex(0, lines[0].index("."))
    end = complex(len(lines) - 1, lines[-1].index("."))
    blizzards = []
    walls = set()
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            with contextlib.suppress(KeyError):
                direction = DIRECTIONS[char]
                blizzards.append((direction, complex(row, col)))
            if char == "#":
                walls.add(complex(row, col))
    return size, start, end, tuple(blizzards), walls


@cache
def get_blizzard_pos(step, size, blizzards):
    return {wrap(pos + direction * step, size) for direction, pos in blizzards}


def wrap(pos: complex, size: complex):
    x = pos.real - 1
    y = pos.imag - 1
    size_x = size.real - 2
    size_y = size.imag - 2
    return complex(x % size_x + 1, y % size_y + 1)


def manhattan_distance(x: complex, y: complex):
    diff = x - y
    return abs(diff.real) + abs(diff.imag)


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
