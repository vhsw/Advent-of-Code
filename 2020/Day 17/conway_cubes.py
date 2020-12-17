"Day 17 answers"
INPUT = "2020/Day 17/input.txt"


def range3d(x, y, z):
    for dx in range(-x, x + 1):
        for dy in range(-y, y + 1):
            for dz in range(-z, z + 1):
                yield dx, dy, dz


def range4d(x, y, z, w):
    for dx in range(-x, x + 1):
        for dy in range(-y, y + 1):
            for dz in range(-z, z + 1):
                for dw in range(-w, w + 1):
                    yield dx, dy, dz, dw


def neighbors3d(x, y, z):
    for dx, dy, dz in range3d(1, 1, 1):
        if dx == dy == dz == 0:
            continue
        yield x + dx, y + dy, z + dz


def neighbors4d(x, y, z, w):
    for dx, dy, dz, dw in range4d(1, 1, 1, 1):
        if dx == dy == dz == dw == 0:
            continue
        yield x + dx, y + dy, z + dz, w + dw


def disp3d(grid, size_x, size_y, size_z):
    for z in range(-size_z, size_z + 1):
        print(f"{z=}")
        for x in range(-size_x, size_x + 1):
            for y in range(-size_y, size_y + 1):
                print("#" if (x, y, z) in grid else ".", end="")
            print()


def part1(data):
    "Part 1 answer"
    active = set()
    size_x = len(data)
    size_y = len(data[0])
    size_z = 1
    for x, line in enumerate(data, start=-size_x // 2):
        for y, char in enumerate(line, start=-size_y // 2):
            if char == "#":
                active.add((x, y, 0))

    for i in range(6):
        tmp = set()
        for cube in range3d(size_x + i, size_y + i, size_z + i):
            s = len(set(neighbors3d(*cube)) & active)
            if s == 3 or (cube in active and s == 2):
                tmp.add(cube)
        size_x += 1
        size_y += 1
        size_z += 1
        active = tmp
    return len(active)


def part2(data):
    "Part 2 answer"
    active = set()
    size_x = len(data)
    size_y = len(data[0])
    size_z = 1
    size_w = 1
    for x, line in enumerate(data, start=-size_x // 2):
        for y, char in enumerate(line, start=-size_y // 2):
            if char == "#":
                active.add((x, y, 0, 0))

    for i in range(6):
        tmp = set()
        for cube in range4d(size_x + i, size_y + i, size_z + i, size_w + i):
            s = len(set(neighbors4d(*cube)) & active)
            if s == 3 or (cube in active and s == 2):
                tmp.add(cube)
        size_x += 1
        size_y += 1
        size_z += 1
        size_w += 1
        active = tmp
    return len(active)


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.read().strip().split()
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
