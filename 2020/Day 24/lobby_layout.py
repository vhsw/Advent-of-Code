"Day 24 answers"
from time import sleep
from typing import Dict, List, Set, Tuple

INPUT = "2020/Day 24/input.txt"


def parse(line):
    idx = 0
    directions = []
    while idx < len(line):
        a = line[idx]
        b = ""
        if idx < len(line) - 1:
            b = line[idx + 1]
        if a + b in ["se", "sw", "nw", "ne"]:
            directions.append(a + b)
            idx += 2
        else:
            directions.append(a)
            idx += 1
    return directions


#   _____         _____         _____
#  /     \       /     \       /     \
# /       \_____/  1,-1 \_____/       \
# \       /     \  nw   /     \       /
#  \_____/  0,-1 \_____/  1, 0 \_____/
#  /     \   w   /     \  ne   /     \
# /       \_____/  0,0  \_____/       \
# \       /     \   #   /     \       /
#  \_____/ -1, 0 \_____/  0, 1 \_____/
#  /     \  se   /     \   e   /     \
# /       \_____/ -1, 1 \_____/       \
# \       /     \  se   /     \       /
#  \_____/       \_____/       \_____/
#        \       /     \       /
#         \_____/       \_____/

MOVES: Dict[str, Tuple[int, int]] = {
    "nw": (1, -1),
    "ne": (1, 0),
    "w": (0, -1),
    "e": (0, 1),
    "sw": (-1, 0),
    "se": (-1, 1),
}


def move(directions: List[str]):
    x, y = 0, 0
    for direction in directions:
        dx, dy = MOVES[direction]
        x += dx
        y += dy
    return x, y


def tile_floor(data: List[str]):
    tiles: Set[Tuple[int, int]] = set()
    for line in data:
        directions = parse(line)
        tile = move(directions)
        if tile in tiles:
            tiles.remove(tile)
        else:
            tiles.add(tile)
    return tiles


def part1(data: List[str]):
    "Part 1 answer"
    tiles = tile_floor(data)
    return len(tiles)


def neighbors(x, y):
    for dx, dy in MOVES.values():
        yield x + dx, y + dy


def display(tiles):
    size = max(max(abs(t[0]), abs(t[1])) for t in tiles)
    if size % 2 == 0:
        size += 1
    lines = []
    for y in range(-size, size + 1):
        line = " " if y % 2 == 0 else ""
        line += ". " * ((size - y) // 2)
        for x in range(-size, size + 1):
            x = -x
            if x == y == 0:
                line += "x "
                continue
            line += "# " if (x, y) in tiles else ". "

        line += ". " * ((size + y) // 2)
        lines.append(line)
    print("\n".join(lines) + "\n")
    sleep(0.1)


def part2(data: List[str], make_show=False):
    "Part 2 answer"
    tiles = tile_floor(data)
    for _ in range(100):
        tmp = set()
        size = max(max(abs(t[0]), abs(t[1])) for t in tiles) + 1
        for x in range(-size, size + 1):
            for y in range(-size, size + 1):
                tile = x, y
                s = sum(neighbor in tiles for neighbor in neighbors(*tile))
                if s == 2 or tile in tiles and s == 1:
                    tmp.add(tile)
        tiles = tmp
        size += 1
        if make_show:
            display(tiles)
    return len(tiles)


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.read().strip().split("\n")
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA, make_show=False) }")
