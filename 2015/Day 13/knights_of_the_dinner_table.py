"Day 13 answers"
import re
from itertools import permutations

INPUT = "2015/Day 13/input.txt"


def part1(data):
    "Part 1 answer"
    d = {}
    for line in data:
        p1, sign, points, p2 = re.match(
            r"(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)", line
        ).groups()
        points = int(points)
        if sign == "lose":
            points *= -1
        d.setdefault(p1, {})[p2] = points
    vals = []
    for p in permutations(d, len(d)):
        # print(p)
        s = sum(d[p2][p1] + d[p1][p2] for p1, p2 in zip(p, p[1:]))
        s += d[p[0]][p[-1]] + d[p[-1]][p[0]]
        vals.append(s)
    return max(vals)


def part2(data):
    "Part 2 answer"
    d = {}
    for line in data:
        p1, sign, points, p2 = re.match(
            r"(\w+) would (\w+) (\d+) happiness units by sitting next to (\w+)", line
        ).groups()
        points = int(points)
        if sign == "lose":
            points *= -1
        d.setdefault(p1, {})[p2] = points
    d["me"] = {}
    for p1 in d:
        d[p1]["me"] = 0
        if p1 != "me":
            d["me"][p1] = 0
    vals = []
    for p in permutations(d, len(d)):
        # print(p)
        s = sum(d[p2][p1] + d[p1][p2] for p1, p2 in zip(p, p[1:]))
        s += d[p[0]][p[-1]] + d[p[-1]][p[0]]
        vals.append(s)
    return max(vals)


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.readlines()
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
