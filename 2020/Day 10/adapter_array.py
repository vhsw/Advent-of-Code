"Day 10 answers"

import networkx as nx

INPUT = "2020/Day 10/input.txt"


def part1(data, joltage=0):
    "Part 1 answer"
    d3 = 0
    d1 = 0
    for adapter in sorted(data):
        if joltage + 1 <= adapter <= joltage + 3:
            if adapter - joltage == 3:
                d3 += 1
            if adapter - joltage == 1:
                d1 += 1
            joltage = adapter
    return d1 * d3


def part2(data):
    "Part 2 answer"
    g = {}
    for adapter in data:
        g[adapter] = [d for d in data if adapter < d < adapter + 4]

    G = nx.DiGraph(g)
    s = 1
    fixed_points = (
        [0] + [k for k in g if len(g[k]) == 1 and g[k][0] - k == 3] + [max(data)]
    )
    for src, dst in zip(fixed_points, fixed_points[1:]):
        pathes = sum(1 for _ in nx.all_simple_paths(G, src, dst))
        s *= pathes
    return s


if __name__ == "__main__":
    with open(INPUT) as fp:
        RAW = list(map(int, fp.readlines()))

    DATA = set([0] + RAW + [max(RAW) + 3])
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
