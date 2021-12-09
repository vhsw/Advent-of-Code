"""Day 9: Smoke Basin"""
from math import prod

with open("2021/Day 09/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    grid = parse(data)
    return sum(
        val + 1
        for pos, val in grid.items()
        if all(val < n_val for n_val in neighbors_vals(pos, grid))
    )


def part2(data: str):
    """Part 2 solution"""
    grid = {pos for pos, val in parse(data).items() if val < 9}
    sizes = []
    while grid:
        todo = {grid.pop()}
        size = 0
        while todo:
            size += 1
            pos = todo.pop()
            grid.discard(pos)
            for n_pos in neighbors(pos):
                if n_pos in grid:
                    todo.add(n_pos)
        sizes.append(size)
    return prod(sorted(sizes, reverse=True)[:3])


def parse(data: str):
    return {
        complex(row, col): int(letter)
        for row, line in enumerate(data.splitlines())
        for col, letter in enumerate(line)
    }


def neighbors_vals(pos: complex, grid: dict[complex, int]):
    for n_pos in neighbors(pos):
        try:
            yield grid[n_pos]
        except KeyError:
            continue


def neighbors(pos: complex):
    for d_pos in (1, 1j, -1j, -1):
        yield pos + d_pos


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
