"""Day 25: Snowverload"""

from math import prod
import networkx as nx

with open("2023/Day 25/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    G = nx.Graph()
    for line in data.splitlines():
        src, dsts = line.split(": ")
        for dst in dsts.split():
            G.add_edge(src, dst)
    return prod(map(len, nx.k_edge_components(G, k=4)))


if __name__ == "__main__":
    print(f"Part 1: {part1(DATA)}")
