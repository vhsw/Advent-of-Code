"Day 02 answers"
from math import prod

INPUT = "2015/Day 02/input.txt"


def part1(data):
    "Part 1 answer"
    paper = 0
    for l, w, h in data:
        sides = [l * w, w * h, h * l]
        paper += 2 * sum(sides) + min(sides)
    return paper


def part2(data):
    "Part 2 answer"
    ribbon = 0
    for d in data:
        min_sides = sum(d) - max(d)
        ribbon += 2 * min_sides + prod(d)
    return ribbon


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = [[*map(int, i.split("x"))] for i in fp]
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
