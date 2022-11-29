"""Day 17: Two Steps Forward"""
from collections import deque
from hashlib import md5
from itertools import product

with open("2016/Day 17/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    grid = make_grid()
    todo = deque([(0j, "")])
    seen = set()
    while todo:
        src, path = todo.popleft()
        if src == 3 + 3j:
            return path
        seen.add(src)
        allowed_moves = (
            (src + MOVES[m], m)
            for m in get_allowed_moves(data, path)
            if MOVES[m] in grid[src]
        )
        for dst, p_path in allowed_moves:
            todo.append((dst, path + p_path))


def part2(data: str):
    """Part 2 solution"""
    grid = make_grid()
    todo = deque([(0j, "")])
    seen = set()
    pathes_len = []
    while todo:
        src, path = todo.pop()
        if src == 3 + 3j:
            pathes_len.append(len(path))
            continue
        seen.add(src)
        allowed_moves = (
            (src + MOVES[m], m)
            for m in get_allowed_moves(data, path)
            if MOVES[m] in grid[src]
        )
        for dst, p_path in allowed_moves:
            todo.append((dst, path + p_path))
    return max(pathes_len)


MOVES = {
    "D": 1,
    "U": -1,
    "L": -1j,
    "R": 1j,
}


def make_grid():
    grid: dict[complex, set[complex]] = {}
    for row, col in product(range(4), range(4)):
        key = complex(row, col)
        moves = set()
        if row > 0:
            moves.add(MOVES["U"])
        if row < 3:
            moves.add(MOVES["D"])
        if col > 0:
            moves.add(MOVES["L"])
        if col < 3:
            moves.add(MOVES["R"])
        grid[key] = moves
    return grid


def get_allowed_moves(passcode: str, path: str):
    return {
        v
        for k, v in zip(md5((passcode + path).encode("utf-8")).hexdigest(), "UDLR")
        if k in "bcdef"
    }


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
