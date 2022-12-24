"""Day 22: Monkey Map"""
import re
from collections import defaultdict

with open("2022/Day 22/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip("\n")


def part1(data: str):
    """Part 1 solution"""
    grid, instructions = parse(data, parse_grid)
    src = min(grid, key=lambda c: (c.real, c.imag))
    return move(grid, instructions, src)


def part2(data: str):
    """Part 2 solution"""
    grid, instructions = parse_2(data)
    rotations = {"R": -1j, "L": 1j}
    pos = min((p for p, i in grid.items() if i == "."), key=lambda c: (c.real, c.imag))
    direction = 0 + 1j

    for instr in instructions:
        if instr in rotations:
            direction *= rotations[instr]
            continue
        for _ in range(instr):
            p, d = pos + direction, direction
            if p not in grid:
                p, d = wrap(p, d)
            if grid[p] == ".":
                pos, direction = p, d

    return (
        1000 * (pos.real + 1) + 4 * (pos.imag + 1) + [1j, 1, -1j, -1].index(direction)
    )


# https://www.reddit.com/r/adventofcode/comments/zsct8w/comment/j17k7nn
def wrap(pos, direction):
    x, y = pos.real, pos.imag
    match direction, x // 50, y // 50:
        case 1j, 0, _:
            return complex(149 - x, 99), -1j
        case 1j, 1, _:
            return complex(49, x + 50), -1
        case 1j, 2, _:
            return complex(149 - x, 149), -1j
        case 1j, 3, _:
            return complex(149, x - 100), -1
        case -1j, 0, _:
            return complex(149 - x, 0), 1j
        case -1j, 1, _:
            return complex(100, x - 50), 1
        case -1j, 2, _:
            return complex(149 - x, 50), 1j
        case -1j, 3, _:
            return complex(0, x - 100), 1
        case 1, _, 0:
            return complex(0, y + 100), 1
        case 1, _, 1:
            return complex(100 + y, 49), -1j
        case 1, _, 2:
            return complex(-50 + y, 99), -1j
        case -1, _, 0:
            return complex(50 + y, 50), 1j
        case -1, _, 1:
            return complex(100 + y, 0), 1j
        case -1, _, 2:
            return complex(199, y - 100), -1


def parse(data: str, parse_fn):
    grid, instructions = data.split("\n\n")
    return parse_fn(grid), parse_instructions(instructions)


def parse_2(data: str):
    grid, instructions = data.split("\n\n")
    lines = grid.splitlines()
    return {
        complex(row, col): char
        for row, line in enumerate(lines)
        for col, char in enumerate(line)
        if char in ".#"
    }, parse_instructions(instructions)


def parse_instructions(instructions: str):
    matches = re.findall(r"\d+|\w", instructions)
    return [int(m) if m.isdigit() else m for m in matches]


def parse_grid(data: str):
    lines = data.splitlines()
    grid = defaultdict(dict)
    for row, line in enumerate(lines):
        min_col = min(i for i, c in enumerate(line) if c != " ")
        max_col = max(i for i, c in enumerate(line) if c != " ")
        for col, char in enumerate(line):
            if char != ".":
                continue
            src = complex(row, col)
            min_row = min(
                i for i, l in enumerate(lines) if col < len(l) and l[col] != " "
            )
            max_row = max(
                i for i, l in enumerate(lines) if col < len(l) and l[col] != " "
            )

            for d_pos in (1, -1, 1j, -1j):
                dst = src + d_pos
                dst_row = int(dst.real)
                dst_col = int(dst.imag)
                if dst_row > max_row:
                    dst_row = min_row
                elif dst_row < min_row:
                    dst_row = max_row
                if dst_col > max_col:
                    dst_col = min_col
                elif dst_col < min_col:
                    dst_col = max_col
                if lines[dst_row][dst_col] == ".":
                    grid[src][d_pos] = complex(dst_row, dst_col)

    return grid


def parse_cube(data: str):
    grid = defaultdict(dict)
    lines = data.splitlines()
    size = 50 if len(lines) > 50 else 4
    # example layout:
    #   1
    # 234
    #   56

    # input layout:
    #  12
    #  3
    # 45
    # 6
    # TODO: parse cube map as in part 1


def move(grid, instructions, src):
    rotations = {"R": -1j, "L": 1j}
    direction = 0 + 1j
    for instr in instructions:
        if instr in rotations:
            direction *= rotations[instr]
            continue
        for _ in range(instr):
            if direction not in grid[src]:
                break
            src = grid[src][direction]
    facing = {
        0 + 1j: 0,
        -1 + 0j: 1,
        0 - 1j: 2,
        1 + 0j: 3,
    }

    return int(1000 * (src.real + 1) + 4 * (src.imag + 1) + facing[direction])


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
