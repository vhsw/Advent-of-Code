"Day 09 answers"
import re
from itertools import permutations

import networkx as nx

INPUT = "2015/Day 09/input.txt"


def part1(data):
    "Part 1 answer"
    G = nx.Graph()
    for line in data:
        match = re.match(r"(\w+) to (\w+) = (\d+)", line)
        src, dst, dist = match.groups()
        G.add_edge(src, dst, weight=int(dist))
    dists = []
    for p in permutations(G.nodes):
        dists.append(sum(G[src][dst]["weight"] for src, dst in zip(p, p[1:])))
    return min(dists)


def part2(data):
    "Part 2 answer"
    G = nx.Graph()
    for line in data:
        match = re.match(r"(\w+) to (\w+) = (\d+)", line)
        src, dst, dist = match.groups()
        G.add_edge(src, dst, weight=int(dist))
    dists = []
    for p in permutations(G.nodes):
        dists.append(sum(G[src][dst]["weight"] for src, dst in zip(p, p[1:])))
    return max(dists)


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.readlines()
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
