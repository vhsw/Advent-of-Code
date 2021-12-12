"""Day 17: Spinlock"""
from collections import deque

with open("2017/Day 17/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    steps = int(data)
    buf = deque((0,))
    for val in range(2017):
        buf.rotate(-steps)
        buf.append(val + 1)
    return buf[0]


def part2(data: str):
    """Part 2 solution"""
    steps = int(data)

    pos = 0
    after_zero = None
    for val in range(50000000):
        pos += steps
        pos %= val + 1
        if pos == 0:
            after_zero = val + 1
        pos += 1

    return after_zero


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
