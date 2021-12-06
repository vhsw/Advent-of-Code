"""Day 13: Packet Scanners"""
from math import ceil

with open("2017/Day 13/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    return sum(
        depth * size
        for depth, size in parse(data).items()
        if scanner_posititon(size, depth) == 0
    )


def parse(data: str):
    res: dict[int, int] = {}
    for line in data.splitlines():
        depth, size = line.split(": ")
        res[int(depth)] = int(size)
    return res


def scanner_posititon(size, step):
    step = step % (2 * (size - 1))
    if step < size:
        return step
    return size - ceil(step / 2)


def part2(data):
    """Part 2 solution"""
    cache = tuple(parse(data).items())
    delay = 0
    while True:
        for depth, size in cache:
            if scanner_posititon(size, depth + delay) == 0:
                delay += 1
                break
        else:
            return delay


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
