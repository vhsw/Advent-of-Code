"""Day 15: Chiton"""
from dataclasses import dataclass, field
from heapq import heappop, heappush
from typing import Optional

with open("2021/Day 15/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


@dataclass(order=True)
class PrioritizedItem:
    priority: int
    pos: complex = field(compare=False)


def part1(data: str):
    """Part 1 solution"""
    grid = parse(data)
    src = 0
    dst = complex(max(key.real for key in grid), max(key.imag for key in grid))
    path = a_star(src, dst, grid)
    return sum(grid[pos] for pos in path[1:])


def part2(data: str):
    """Part 2 solution"""
    small_grid = parse(data)
    src = 0
    max_c = int(max(key.real for key in small_grid)) + 1
    max_r = int(max(key.imag for key in small_grid)) + 1
    grid = {}
    for col in range(max_c):
        for row in range(max_r):
            for m_col in range(5):
                for m_row in range(5):
                    pos = complex(max_c * m_col + col, m_row * max_r + row)
                    grid[pos] = (
                        small_grid[complex(col, row)] + m_col + m_row - 1
                    ) % 9 + 1
    dst = complex(max_c * 5 - 1, max_r * 5 - 1)
    path = a_star(src, dst, grid)
    return sum(grid[pos] for pos in path[1:])


def a_star(src: complex, dst: complex, grid: dict[complex, int]):
    todo: list[PrioritizedItem] = []
    heappush(todo, PrioritizedItem(0, src))
    todo_lookup = {src}
    distances = {src: 0}
    parents: dict[complex, complex] = {}
    while todo:
        pos = heappop(todo).pos
        todo_lookup.remove(pos)
        if pos == dst:
            return get_path(pos, parents)

        for n_pos in neighbors(pos):
            if n_pos not in grid:
                continue
            distance = distances[pos] + grid[n_pos]
            if n_pos in distances and distance >= distances[n_pos]:
                continue
            distances[n_pos] = distance
            parents[n_pos] = pos
            if n_pos not in todo_lookup:
                todo_lookup.add(n_pos)
                heappush(todo, PrioritizedItem(-heuristic(n_pos, dst), n_pos))
    raise ValueError(f"{dst=} is unreachable")


def get_path(start: complex, parents: dict[complex, complex]):
    path = []
    pos: Optional[complex] = start
    while pos is not None:
        path.append(pos)
        pos = parents.get(pos)
    return path[::-1]


def neighbors(pos: complex):
    for d_pos in (1, 1j, -1j, -1):
        yield pos + d_pos


def heuristic(src: complex, dst: complex):
    diff = dst - src
    return abs(diff.real) + abs(diff.imag)


def parse(data: str):
    return {
        complex(col, row): int(char)
        for row, line in enumerate(data.splitlines())
        for col, char in enumerate(line)
    }


def display(path, grid: dict[complex, str], dst):
    print()
    for row in range(int(dst.imag) + 1):
        for col in range(int(dst.real) + 1):
            pos = complex(col, row)
            if pos in path:
                print(f"\033[1m{grid[pos]}\033[0m", end="")
            else:
                print(grid[pos], end="")
        print()
    print()


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
