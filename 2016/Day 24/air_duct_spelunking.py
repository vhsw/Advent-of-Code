"""Day 24: Air Duct Spelunking"""

from itertools import permutations, product

import networkx as nx

with open("2016/Day 24/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    G, poi = parse(data)
    head = [k for k, v in poi.items() if v == 0][0]
    tail = [k for k in poi if k != head]
    path_lens = []
    cache = {}
    for p in permutations(tail):
        path = (head,) + p
        path_len = 0
        for src, dst in zip(path, path[1:]):
            pair = (src, dst)
            if pair not in cache:
                cache[pair] = nx.shortest_path_length(G, src, dst)
            path_len += cache[pair]
        path_lens.append(path_len)
    return min(path_lens)


def part2(data: str):
    """Part 2 solution"""
    G, poi = parse(data)
    head = [k for k, v in poi.items() if v == 0][0]
    tail = [k for k in poi if k != head]
    path_lens = []
    cache = {}
    for p in permutations(tail):
        path = (head,) + p + (head,)
        path_len = 0
        for src, dst in zip(path, path[1:]):
            pair = (src, dst)
            if pair not in cache:
                cache[pair] = nx.shortest_path_length(G, src, dst)
            path_len += cache[pair]
        path_lens.append(path_len)
    return min(path_lens)


def parse(data: str):
    G = nx.Graph()
    poi = {}
    lines = data.splitlines()
    for row, col in product(range(1, len(lines) - 1), range(1, len(lines[0]) - 1)):
        if lines[row][col] == "#":
            continue
        src = complex(row, col)
        char = lines[row][col]
        if char.isdigit():
            poi[src] = int(char)

        for d_pos in (1, -1, 1j, -1j):
            dst = src + d_pos
            if lines[int(dst.real)][int(dst.imag)] == "#":
                continue
            G.add_edge(src, dst)
    return G, poi


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
