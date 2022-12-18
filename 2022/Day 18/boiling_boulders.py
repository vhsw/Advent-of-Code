"""Day 18: Boiling Boulders"""

with open("2022/Day 18/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    cubes = parse(data)
    return sum(6 - sum(n in cubes for n in neighbors(cube)) for cube in cubes)


def part2(data: str):
    """Part 2 solution"""
    cubes = parse(data)
    lo = min(min(cube) for cube in cubes) - 1
    hi = max(max(cube) for cube in cubes) + 1
    water = set()
    todo = [(lo, lo, lo)]
    while todo:
        item = todo.pop()
        if item in water or item in cubes or any(i < lo or i > hi for i in item):
            continue
        water.add(item)
        todo.extend(neighbors(item))

    return sum(sum(n in water for n in neighbors(cube)) for cube in cubes)


def parse(data: str):
    return {tuple(map(int, line.split(","))) for line in data.splitlines()}


def neighbors(pos: tuple[int, int, int]):
    for i in range(3):
        for v in (-1, 1):
            d_pos = (v * (i == j) for j in range(3))
            yield tuple(a + b for a, b in zip(pos, d_pos))


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
