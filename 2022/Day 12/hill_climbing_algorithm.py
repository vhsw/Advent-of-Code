"""Day 12: Hill Climbing Algorithm"""

from contextlib import suppress

import networkx as nx

with open("2022/Day 12/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    grid, start, end = parse(data)
    G = build_graph(grid)
    return nx.shortest_path_length(G, start, end)


def part2(data: str):
    """Part 2 solution"""
    grid, _, end = parse(data)
    G = build_graph(grid)
    path_lengths = []
    for pos, char in grid.items():
        if char != "a":
            continue
        with suppress(nx.NetworkXNoPath):
            length = nx.shortest_path_length(G, pos, end)
            path_lengths.append(length)
    return min(path_lengths)


def parse(data: str):
    grid = {}
    start = 0j
    end = 0j
    for row, line in enumerate(data.splitlines()):
        for col, char in enumerate(line):
            pos = complex(row, col)
            if char == "S":
                start = pos
                char = "a"
            if char == "E":
                end = pos
                char = "z"
            grid[pos] = char
    return grid, start, end


def build_graph(grid: dict[complex, str]):
    G = nx.DiGraph()
    for src, src_elevation in grid.items():
        for d_pos in (1, -1, -1j, 1j):
            dst = src + d_pos
            dst_elevation = grid.get(dst)
            if not dst_elevation:
                continue
            if ord(dst_elevation) - ord(src_elevation) > 1:
                continue
            G.add_edge(src, dst)
    return G


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
