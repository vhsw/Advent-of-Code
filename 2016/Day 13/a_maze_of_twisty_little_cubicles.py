"""Day 13: A Maze of Twisty Little Cubicles"""
from collections import deque


with open("2016/Day 13/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str, target=31 + 39j):
    """Part 1 solution"""
    num = int(data)
    todo = deque([(0, 1 + 1j)])
    seen = set()
    while todo:
        steps, pos = todo.popleft()
        seen.add(pos)
        if pos == target:
            return steps
        for next_pos in maze_gen(pos, num):
            if next_pos in seen:
                continue
            todo.append((steps + 1, next_pos))


def part2(data: str):
    """Part 2 solution"""
    num = int(data)
    todo = deque([(0, 1 + 1j)])
    seen = set()
    while todo:
        steps, pos = todo.popleft()
        seen.add(pos)
        if steps >= 50:
            continue
        for next_pos in maze_gen(pos, num):
            if next_pos in seen:
                continue
            todo.append((steps + 1, next_pos))
    return len(seen)


def maze_gen(src: complex, num: int):
    for d_pos in (1, 1j, -1, -1j):
        dst = src + d_pos
        x = int(dst.real)
        y = int(dst.imag)
        if x < 0 or y < 0:
            continue
        if is_open_space(x, y, num):
            yield dst


def is_open_space(x: int, y: int, num: int):
    val = x**2 + 3 * x + 2 * x * y + y + y**2 + num
    result = True
    while val:
        val, mod = divmod(val, 2)
        if mod:
            result = not result
    return result


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
