"""Day 20: Trench Map"""
with open("2021/Day 20/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    rules, grid = parse(data)
    defalut = False
    for _ in range(2):
        grid = step(rules, grid, defalut)
        if 0 in rules:
            defalut = not defalut

    return sum(grid.values())


def part2(data: str):
    """Part 2 solution"""
    rules, grid = parse(data)
    defalut = False
    for _ in range(50):
        grid = step(rules, grid, defalut)
        if 0 in rules:
            defalut = not defalut

    return sum(grid.values())


def step(rules: set[int], grid: dict[complex, bool], defalut):
    new_grid: dict[complex, bool] = {}
    for pos in grid:
        for npos in neighbors(pos):
            if npos in new_grid:
                continue
            new_grid[npos] = encode(npos, grid, defalut) in rules
    return new_grid


def encode(pos: complex, grid: dict[complex, bool], defalut):
    return sum(
        2 ** idx for idx, val in enumerate(neighbors(pos)) if grid.get(val, defalut)
    )


def neighbors(pos: complex):
    return [
        pos + complex(col, row) for row in range(1, -2, -1) for col in range(1, -2, -1)
    ]


def parse(data: str):
    lines = data.splitlines()

    rules = {idx for idx, char in enumerate(lines[0]) if char == "#"}
    grid = {
        complex(col, row): True
        for row, line in enumerate(lines[2:])
        for col, char in enumerate(line)
        if char == "#"
    }
    return rules, grid


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
