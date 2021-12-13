"""Day 13: Transparent Origami"""
import re

with open("2021/Day 13/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    dots, folds = data.split("\n\n")
    grid = parse_dots(dots)
    fold = next(parse_folds(folds))
    match fold:
        case ("x", line):
            grid = fold_x(grid, line)
        case ("y", line):
            grid = fold_y(grid, line)
    return len(grid)


def part2(data: str):
    """Part 2 solution"""
    dots, folds = data.split("\n\n")
    grid = parse_dots(dots)
    for fold in parse_folds(folds):
        match fold:
            case ("x", line):
                grid = fold_x(grid, line)
            case ("y", line):
                grid = fold_y(grid, line)
    return render(grid)


def parse_dots(data: str):
    return {complex(*map(int, line.split(","))) for line in data.splitlines()}


def parse_folds(data: str):
    for line in data.splitlines():
        match = re.match(r"fold along (x|y)=(\d+)", line)
        if not match:
            raise ValueError(line)
        coord, val = match.groups()
        yield coord, int(val)


def fold_x(grid: set[complex], line: int):
    return {
        complex(2 * line - pos.real, pos.imag) if pos.real > line else pos
        for pos in grid
    }


def fold_y(grid: set[complex], line: int):
    return {
        complex(pos.real, 2 * line - pos.imag) if pos.imag > line else pos
        for pos in grid
    }


def render(grid: set[complex]):
    max_col = int(max(v.real for v in grid) + 1)
    max_row = int(max(v.imag for v in grid) + 1)
    return "\n".join(
        "".join("#" if complex(col, row) in grid else "." for col in range(max_col))
        for row in range(max_row)
    )


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
