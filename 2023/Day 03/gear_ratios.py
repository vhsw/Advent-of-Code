"""Day 3: Gear Ratios"""
import re
from itertools import groupby
from typing import NamedTuple

with open("2023/Day 03/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    return sum(part.no for part in iter_parts(data))


def part2(data: str):
    """Part 2 solution"""

    return sum(iter_gears(data))


class Part(NamedTuple):
    row: int
    col: int
    no: int
    type: str


def iter_parts(data: str):
    lines = data.splitlines()
    for line_no, line in enumerate(lines):
        for match in re.finditer(r"\d+", line):
            start, end = match.span()
            for row, col in neighbors(line_no, start, end - 1, len(lines), len(line)):
                if (part_type := lines[row][col]) != ".":
                    yield Part(row, col, int(match.group()), part_type)
                    break


def iter_gears(data: str):
    parts = list(iter_parts(data))
    gears = [part for part in parts if part.type == "*"]
    for _, it in groupby(sorted(gears), lambda part: (part.row, part.col)):
        group = list(it)
        if len(group) == 2:
            yield group[0].no * group[1].no


def neighbors(line_no, start, end, n_rows, n_cols):
    if (start - 1) >= 0:
        yield (line_no, start - 1)
    if (end + 1) < n_cols:
        yield (line_no, end + 1)

    start = max(start - 1, 0)
    end = min(end + 2, n_cols)
    if (line_no - 1) >= 0:
        yield from ((line_no - 1, col) for col in range(start, end))
    if (line_no + 1) < n_rows:
        yield from ((line_no + 1, col) for col in range(start, end))


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
