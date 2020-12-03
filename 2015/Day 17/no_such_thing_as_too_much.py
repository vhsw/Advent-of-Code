"Day 17 answers"
from functools import cache

INPUT = "2015/Day 17/input.txt"


@cache
def part1(data, vol=150, n=float("inf")):
    "Part 1 answer"
    if len(data) == 0:
        return vol == 0
    s = 0
    head = data[0]
    tail = data[1:]
    dif = vol - head
    if dif >= 0:
        s += part1(tuple(v for v in tail if v <= dif), dif)
    s += part1(tail, vol)
    return s


@cache
def part2(data, vol=150, n=0):
    "Part 2 answer"

    if len(data) == 0:
        if vol == 0:
            return n == 4  # coz the min num of containers is 4
        return 0
    s = 0
    head = data[0]
    tail = data[1:]
    dif = vol - head
    if dif >= 0:
        fitred = tuple(v for v in tail if v <= dif)
        s += part2(fitred, dif, n + 1)
    s += part2(tail, vol, n)
    return s


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = tuple(map(int, fp.readlines()))
    # DATA = (20, 15, 10, 5, 5)
    print(f"Part 1: { part1(DATA) }")
    print(part1.cache_info())

    print(f"Part 2: { part2(DATA) }")
