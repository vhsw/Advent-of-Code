"Day 20 answers"
# from functools import cache
from math import ceil, floor, sqrt

INPUT = "2015/Day 20/input.txt"

# @cache
def f(n):
    s = 0
    for i in range(1, floor(sqrt(n)) + 1):
        d, m = divmod(n, i)
        if m == 0:
            # print("x", n, i, d)
            s += i + d * (d != i)
    return s


def part1(data):
    "Part 1 answer"
    i = data // 100
    while f(i) * 10 < data:
        i += 1
    return i


def f2(n):
    s = 0
    for i in range(1, floor(sqrt(n)) + 1):
        d, m = divmod(n, i)
        if m == 0:
            # print("x", n, i, d)
            s += i * (d != i) * (i * 50 >= n) + d * (d * 50 >= n)
    return s


def part2(data):
    "Part 2 answer"
    i = data // 100
    lim = data / 11
    while (n := f2(i)) < lim:
        i += 1
    return i


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = int(fp.read())

    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
