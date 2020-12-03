"Day 18 answers"
INPUT = "2015/Day 18/input.txt"


def to_dict(s: str):
    d = {}
    for i, line in enumerate(s.splitlines()):
        for j, char in enumerate(line):
            d[(i, j)] = char == "#"
    return d


def neighbors(i, j):
    return [
        (di, dj)
        for di in range(i - 1, i + 2)
        for dj in range(j - 1, j + 2, 1 + (i == di))
    ]


def disp(grid, size=100):
    for i in range(size):
        for j in range(size):
            print(".#"[grid[(i, j)]], end="")
        print()
    print()


def part1(data):
    "Part 1 answer"
    grid = to_dict(data)
    # disp(grid)

    for _ in range(100):
        tmp = {}
        for t in grid:
            s = sum(grid.get(n, False) for n in neighbors(*t))
            if grid[t]:
                tmp[t] = s in (2, 3)
            else:
                tmp[t] = s == 3
        grid = tmp
        # disp(grid)
    return sum(grid.values())


def pin_corners(grid):
    grid[(0, 0)] = True
    grid[(0, 99)] = True
    grid[(99, 0)] = True
    grid[(99, 99)] = True


def part2(data):
    "Part 2 answer"
    grid = to_dict(data)
    pin_corners(grid)
    # disp(grid)

    for _ in range(100):
        tmp = {}
        for t in grid:
            s = sum(grid.get(n, False) for n in neighbors(*t))
            if grid[t]:
                tmp[t] = s in (2, 3)
            else:
                tmp[t] = s == 3
        grid = tmp
        pin_corners(grid)
        # disp(grid)
    return sum(grid.values())


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.read()
    DATA2 = """.#.#.#
...##.
#....#
..#...
#.#..#
####.."""
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
