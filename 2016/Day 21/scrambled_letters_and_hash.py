"""Day 21: Scrambled Letters and Hash"""
from collections import deque
from typing import Callable

with open("2016/Day 21/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str, start: str = "abcdefgh"):
    """Part 1 solution"""
    buf = start
    for line in data.splitlines():
        match line.split():
            case "swap", "position", X, "with", "position", Y:
                buf = swap_position(buf, X, Y)
            case "swap", "letter", X, "with", "letter", Y:
                buf = swap_letter(buf, X, Y)
            case "rotate", direction, X, _:
                buf = rotate(buf, direction, X)
            case "rotate", "based", "on", "position", "of", "letter", X:
                buf = rotate_based_on_position(buf, X)
            case "reverse", "positions", X, "through", Y:
                buf = reverse_positions(buf, X, Y)
            case "move", "position", X, "to", "position", Y:
                buf = move_position(buf, X, Y)
            case _:
                raise ValueError(line)
    return buf


def part2(data: str, end: str = "fbgdceah"):
    """Part 2 solution"""
    buf = end
    for line in data.splitlines()[::-1]:
        match line.split():
            case "swap", "position", X, "with", "position", Y:
                buf = swap_position(buf, X, Y)
            case "swap", "letter", X, "with", "letter", Y:
                buf = swap_letter(buf, X, Y)
            case "rotate", direction, X, _:
                direction = {"left": "right", "right": "left"}[direction]
                buf = rotate(buf, direction, X)
            case "rotate", "based", "on", "position", "of", "letter", X:
                buf = unrotate_based_on_position(buf, X)
            case "reverse", "positions", X, "through", Y:
                buf = reverse_positions(buf, X, Y)
            case "move", "position", X, "to", "position", Y:
                buf = move_position(buf, Y, X)
            case _:
                raise ValueError(line)
    return buf


def debug(func: Callable):
    def wrap(*args):
        res = func(*args)
        print(f"{func.__name__}{args} = {res}")
        return res

    return wrap


@debug
def swap_position(buf: str, X: str, Y: str):
    x = int(X)
    y = int(Y)
    buf_x = buf[x]
    buf_y = buf[y]
    buf = buf[:x] + buf_y + buf[x + 1 :]
    return buf[:y] + buf_x + buf[y + 1 :]


@debug
def swap_letter(buf: str, X: str, Y: str):
    table = str.maketrans({X: Y, Y: X})
    return buf.translate(table)


@debug
def rotate(buf: str, direction: str, X: str | int):
    mul = 1 if direction == "left" else -1
    n = int(X) * mul
    return _rotate(buf, n)


@debug
def _rotate(buf: str, n: int):
    d = deque(buf)
    d.rotate(-n)
    return "".join(d)


@debug
def rotate_based_on_position(buf: str, X: str):
    pos = buf.index(X)
    rot = pos + 1
    if pos >= 4:
        rot += 1
    return _rotate(buf, -rot)


@debug
def unrotate_based_on_position(buf: str, X: str):
    pos = buf.index(X)
    if pos == 0:
        rot = 1
    elif pos % 2:
        rot = pos // 2 + 1
    else:
        rot = pos // 2 + 5
    return _rotate(buf, rot)


@debug
def reverse_positions(buf: str, X: str, Y: str):
    x = int(X)
    y = int(Y)
    return buf[:x] + buf[x : y + 1][::-1] + buf[y + 1 :]


@debug
def move_position(buf: str, X: str, Y: str):
    x = int(X)
    y = int(Y)
    buf_x = buf[x]
    buf = buf[:x] + buf[x + 1 :]
    return buf[:y] + buf_x + buf[y:]


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
