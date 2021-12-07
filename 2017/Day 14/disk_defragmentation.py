"""Day 14: Disk Defragmentation"""
from typing import Counter

from knot_hash import knot_hash

with open("2017/Day 14/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    grid = (to_bin(knot_hash(f"{data}-{i}")) for i in range(128))
    return "".join(grid).count("1")


def part2(data: str):
    """Part 2 solution"""
    grid = {
        complex(row, col)
        for row in range(128)
        for col, val in enumerate(to_bin(knot_hash(f"{data}-{row}")))
        if val == "1"
    }
    regions: dict[complex, int] = {}
    current_region = 0
    while grid:
        todo = [next(iter(grid))]
        current_region += 1
        while todo:
            pos = todo.pop()
            if pos not in grid:
                continue
            regions[pos] = current_region
            grid.remove(pos)
            for n_pos in neighbors(pos):
                if n_pos in grid:
                    todo.append(n_pos)

    return len(Counter(regions.values()))


def to_bin(hex_str: str):
    return (bin(int(hex_str, 16))[2:]).rjust(128, "0")


def neighbors(pos: complex):
    for d_pos in (1, 1j, -1j, -1):
        yield pos + d_pos


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
