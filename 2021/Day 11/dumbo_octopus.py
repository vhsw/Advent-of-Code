"""Day 11: Dumbo Octopus"""
with open("2021/Day 11/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    grid = parse(data)
    return sum(evaluate(grid) for _ in range(100))


def part2(data: str):
    """Part 2 solution"""
    grid = parse(data)
    step = 1
    while evaluate(grid) != 100:
        step += 1
    return step


def parse(data: str):
    return {
        complex(row, col): int(char)
        for row, line in enumerate(data.splitlines())
        for col, char in enumerate(line)
    }


def evaluate(grid):
    flashed = set()
    for pos in grid:
        grid[pos] += 1

    is_flash = True
    while is_flash:
        is_flash = False
        for pos in grid:
            if pos in flashed or grid[pos] <= 9:
                continue
            is_flash = True
            flashed.add(pos)
            for n_pos in neighbors(pos):
                try:
                    grid[n_pos] += 1
                except KeyError:
                    pass

    for pos in flashed:
        grid[pos] = 0
    return len(flashed)


def neighbors(pos: complex):
    for d_pos in (1, 1j, -1, -1j, 1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j):
        yield pos + d_pos


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
