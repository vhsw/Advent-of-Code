"""Day 23: Unstable Diffusion"""
from collections import defaultdict, deque
from itertools import count

with open("2022/Day 23/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    grid = parse(data)
    _, grid = run(grid, range(10))
    return count_empty(grid)


def part2(data: str):
    """Part 2 solution"""
    grid = parse(data)
    round_, _ = run(grid, count(start=1))
    return round_


def parse(data: str) -> set[complex]:
    grid = set()
    for row, line in enumerate(data.splitlines()):
        for col, char in enumerate(line):
            if char == "#":
                grid.add(complex(row, col))
    return grid


MOVES = {
    "N": -1 + 0j,
    "E": +0 + 1j,
    "W": +0 - 1j,
    "S": +1 + 0j,
    "NE": -1 + 1j,
    "NW": -1 - 1j,
    "SE": +1 + 1j,
    "SW": +1 - 1j,
}


def run(grid, rounds):
    rules = deque(
        [
            ("N", lambda neigh: all(neigh[d] not in grid for d in ["N", "NE", "NW"])),
            ("S", lambda neigh: all(neigh[d] not in grid for d in ["S", "SE", "SW"])),
            ("W", lambda neigh: all(neigh[d] not in grid for d in ["W", "NW", "SW"])),
            ("E", lambda neigh: all(neigh[d] not in grid for d in ["E", "NE", "SE"])),
        ]
    )
    for round_ in rounds:
        targets = defaultdict(list)
        for src in grid:
            neigh = {k: v + src for k, v in MOVES.items()}
            if len(set(neigh.values()) & grid) == 0:
                targets[src].append(src)
                continue
            for direction, rule in rules:
                if rule(neigh):
                    targets[neigh[direction]].append(src)
                    break
            else:
                targets[src].append(src)
        new_grid: set[complex] = set()
        for dst, srcs in targets.items():
            if len(srcs) == 1:
                new_grid.add(dst)
            else:
                new_grid.update(srcs)
        if grid == new_grid:
            return round_, grid
        grid = new_grid
        rules.rotate(-1)
    return round_, grid


def count_empty(grid):
    min_row = min(g.real for g in grid)
    max_row = max(g.real for g in grid)
    min_col = min(g.imag for g in grid)
    max_col = max(g.imag for g in grid)
    return int((max_row - min_row + 1) * (max_col - min_col + 1) - len(grid))


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
