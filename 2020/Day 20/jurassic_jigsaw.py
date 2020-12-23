"Day 20 answers"
import re
from typing import Dict, List

INPUT = "2020/Day 20/input.txt"


def rotations(tile):
    T, L, R, B = tile
    yield T, L, R, B
    yield L[::-1], B, T, R[::-1]
    yield B[::-1], R[::-1], L[::-1], T[::-1]
    yield R, T[::-1], B[::-1], L


def flips(tile):
    A, B, C, D = tile
    yield A, B, C, D
    yield D, B[::-1], C[::-1], A


def jiggle(tile):
    for f in flips(tile):
        yield from rotations(f)


def without_key(d, key):
    return {k: v for k, v in d.items() if k != key}


def fit(tile, top, left):
    for idx, (a, b, c, d) in enumerate(jiggle(tile)):
        if (top is None or top == a) and (left is None or left == b):
            return idx, (a, b, c, d)


def assemble(tiles, grid, nums, x=0, y=0, size=4):
    if x == size:
        return nums
    top = None
    left = None
    if y > 0:
        left = grid[x, y - 1][2]
    if x > 0:
        top = grid[x - 1, y][3]
    for idx in tiles:
        if fitted := fit(tiles[idx], top, left):
            pos, sides = fitted
            if res := assemble(
                without_key(tiles, idx),
                grid | {(x, y): sides},
                nums | {(x, y): (idx, pos)},
                x + (y + 1 == size),
                (y + 1) % size,
                size,
            ):
                return res


def prepare(data: str):
    tiles = {}
    for tile in data.split("\n\n"):
        lines = tile.split("\n")
        if m := re.match(r"Tile (\d+):", lines[0]):
            idx = int(m.group(1))
        else:
            raise ValueError(lines[0])
        tiles[idx] = (
            lines[1],
            "".join(line[0] for line in lines[1:]),
            "".join(line[-1] for line in lines[1:]),
            lines[-1],
        )
    return tiles


def part1(data):
    "Part 1 answer"
    tiles = prepare(data)
    size = int(len(tiles.keys()) ** 0.5)
    grid = assemble(tiles, {}, {}, 0, 0, size=size)
    return (
        grid[0, 0][0]
        * grid[0, size - 1][0]
        * grid[size - 1, 0][0]
        * grid[size - 1, size - 1][0]
    )


def flip(data: List[str]):
    return data[::-1]


def rotate(data: list, angle: int):
    if angle == 0:
        return data
    if angle == 1:
        return ["".join(line[::-1]) for line in zip(*data)]
    if angle == 2:
        return ["".join(line[::-1]) for line in data][::-1]
    if angle == 3:
        return ["".join(line) for line in zip(*data)][::-1]


def position(data, index):
    flipped, angle = divmod(index, 4)
    if flipped:
        data = flip(data)
    return rotate(data, angle)


def search(grid, monster):
    n = 0
    for x in range(len(grid) - 2):
        for y in range(len(grid[0]) - 19):
            rect = set()
            for dx in range(3):
                for dy in range(20):
                    if grid[x + dx][y + dy] == "#":
                        rect.add((dx, dy))
            if monster.issubset(rect):
                n += 1
    return n


def part2(data: str):
    "Part 2 answer"
    tiles = prepare(data)
    filled: Dict[int, List[str]] = {}
    for tile in data.split("\n\n"):
        lines = tile.split("\n")
        if m := re.match(r"Tile (\d+):", lines[0]):
            idx = int(m.group(1))
        else:
            raise ValueError(lines[0])
        filled[idx] = lines[1:]

    size = int(len(tiles.keys()) ** 0.5)
    placed_puzzles = assemble(tiles, {}, {}, 0, 0, size=size)
    grid = [[" "] * size * 8 for _ in range(size * 8)]
    for x in range(size):
        for y in range(size):
            idx, pos = placed_puzzles[x, y]
            for dx, line in enumerate(position(filled[idx], pos)[1:-1]):
                for dy, char in enumerate(line[1:-1]):
                    grid[x * 8 + dx][y * 8 + dy] = char

    picture = [
        "                  # ",
        "#    ##    ##    ###",
        " #  #  #  #  #  #   ",
    ]
    monster = {(x, y) for x in range(3) for y in range(20) if picture[x][y] == "#"}
    for i in range(8):
        n = search(position(grid, i), monster)
        if n > 0:
            return sum(line.count("#") for line in grid) - n * len(monster)


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.read().strip()

    print(f"Part 1: { part1(DATA) == 18482479935793 }")
    print(f"Part 2: { part2(DATA) == 2118}")
