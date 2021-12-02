"""Day 3: Spiral Memory"""
from itertools import count

with open("2017/Day 03/input.txt", encoding="utf-8") as fp:
    DATA = int(fp.read().strip())


def part1(data: int):
    """Part 1 solution"""
    if data == 1:
        return 0

    circle = 1
    min_num = 2

    while True:
        max_num = min_num + 8 * circle - 1
        if min_num <= data <= max_num:
            break
        circle += 1
        min_num = max_num + 1
    offset = data - min_num
    dist = min(map(lambda corner: abs(corner - offset), centers(circle)))
    return circle + dist


def centers(size):
    first = size - 1
    for i in range(4):
        yield first + i * (2 * size)


def part2(data: int):
    """Part 2 solution"""
    grid = {complex(0, 0): 1}
    pos = complex(0, 1)

    def update():
        val = sum(grid.get(pos + d_pos, 0) for d_pos in offsets())
        if val > data:
            raise StopIteration(val)
        grid[pos] = val

    try:
        for circle in count(1):
            for _ in range(f(circle)):
                update()
                pos -= 1
            for _ in range(f(circle + 1) - 1):
                update()
                pos -= 1j
            for _ in range(f(circle + 1) - 1):
                update()
                pos += 1
            for _ in range(f(circle + 1)):
                update()
                pos += 1j
    except StopIteration as ex:
        return ex.value


def f(n):
    return 2 * n - 1


def offsets():
    for r in range(-1, 2):
        for c in range(-1, 2):
            if r == c == 0:
                continue
            yield complex(r, c)


if __name__ == "__main__":

    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
