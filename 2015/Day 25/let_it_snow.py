"Day 25 answers"
import re

INPUT = "2015/Day 25/input.txt"


def f():
    s = 20151125
    m = 252533
    d = 33554393
    while True:
        yield s
        s = (s * m) % d


def part1(data):
    "Part 1 answer"
    regex = r".*row (\d+), column (\d+)"
    row, col = map(int, re.match(regex, data).groups())
    r = 1
    c = 1
    g = iter(f())
    while True:
        r += 1
        c = 1
        while c < r:
            if (r - c) == row and c == col:
                return next(g)
            c += 1
            next(g)


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.read()
    print(f"Part 1: { part1(DATA) }")
