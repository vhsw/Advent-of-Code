"""Day 22: Grid Computing"""
import re
from typing import TypedDict

import networkx as nx


class Node(TypedDict):
    used: int
    avail: int


with open("2016/Day 22/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    nodes = parse(data)
    pairs = 0
    for k_a, v_a in nodes.items():
        for k_b, v_b in nodes.items():
            if k_a == k_b:
                continue
            if v_a["used"] == 0:
                continue
            if v_a["used"] >= v_b["avail"]:
                continue
            pairs += 1
    return pairs


def part2(data: str):
    """Part 2 solution"""
    nodes = parse(data)
    target = complex(max(n.real for n in nodes if n.imag == 0), 0)
    path = get_path(nodes, target, 0)
    carret = [k for k, v in nodes.items() if v["used"] == 0][0]
    carret_path = get_path(nodes, carret, path[1], skip=target)
    path_len = len(carret_path) - 1
    path_len += 1
    for dst, skip, src in zip(path, path[1:], path[2:]):
        carret_path = get_path(nodes, src, dst, skip)
        path_len += len(carret_path) - 1
        path_len += 1

    return path_len


def get_path(
    nodes: dict[complex, Node],
    src: complex,
    dst: complex,
    skip=None,
):
    G = nx.Graph()
    for node in nodes:
        if node == skip:
            continue
        for d_pos in (-1, -1j, 1j, 1):
            pos = node + d_pos
            if (
                pos == skip
                or pos not in nodes
                or nodes[pos]["used"] > nodes[node]["avail"] + nodes[node]["used"]
                or nodes[node]["used"] > nodes[pos]["avail"] + nodes[pos]["used"]
            ):
                continue
            G.add_edge(node, pos)
    return nx.astar_path(G, src, dst, heuristic=lambda u, v: abs(u - v))


def parse(data: str):
    # root@ebhq-gridcenter# df -h
    # Filesystem              Size  Used  Avail  Use%
    # /dev/grid/node-x0-y0     86T   73T    13T   84%
    nodes: dict[complex, Node] = {}

    for line in data.splitlines()[2:]:
        node, _, used, avail, _ = line.split()
        x, y = re.match(r"/dev/grid/node-x(\d+)-y(\d+)", node).groups()  # type: ignore
        nodes[complex(int(x), int(y))] = {
            "used": int(used.removesuffix("T")),
            "avail": int(avail.removesuffix("T")),
        }
    return nodes


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
