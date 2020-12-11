"Day 11 answers"
INPUT = "2020/Day 11/input.txt"


def to_dict(s: str):
    d = {}
    for i, line in enumerate(s.splitlines()):
        for j, char in enumerate(line):
            if char == "L":
                d[(i, j)] = False
            elif char == "#":
                d[(i, j)] = True
    return d


def neighbors(i, j):
    return [
        (di, dj)
        for di in range(i - 1, i + 2)
        for dj in range(j - 1, j + 2, 1 + (i == di))
    ]


def disp(grid):
    mx = max(i[0] for i in grid)
    my = max(i[1] for i in grid)
    for i in range(mx + 1):
        for j in range(my + 1):
            if (i, j) in grid:
                print("L#"[grid[(i, j)]], end="")
            else:
                print(".", end="")
        print()
    print()


def part1(data):
    "Part 1 answer"
    grid = to_dict(data)
    while True:
        tmp = {}
        for t in grid:
            s = sum(grid.get(n, False) for n in neighbors(*t))
            tmp[t] = grid[t]
            if grid[t] and s >= 4:
                tmp[t] = False
            elif not grid[t] and s == 0:
                tmp[t] = True
        if tmp == grid:
            return sum(grid.values())
        grid = tmp


def part2(data):
    "Part 2 answer"
    grid = to_dict(data)
    mx = max(k[0] for k in grid)
    my = max(k[1] for k in grid)
    while True:
        tmp = {}
        for t in grid:
            s = 0
            for dx, dy in (
                (-1, 0),
                (1, 0),
                (0, -1),
                (0, 1),
                (-1, -1),
                (1, -1),
                (1, 1),
                (-1, 1),
            ):
                tx, ty = t
                tx += dx
                ty += dy
                while 0 <= tx <= mx and 0 <= ty <= my and (tx, ty) not in grid:
                    tx += dx
                    ty += dy
                s += grid.get((tx, ty), False)

            tmp[t] = grid[t]
            if grid[t] and s >= 5:
                tmp[t] = False
            elif not grid[t] and s == 0:
                tmp[t] = True
        if tmp == grid:
            return sum(grid.values())
        grid = tmp


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.read().strip()

    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
