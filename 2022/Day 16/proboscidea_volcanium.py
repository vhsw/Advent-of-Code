"""Day 16: Proboscidea Volcanium"""
import re
from functools import cache
from itertools import permutations

import networkx as nx

with open("2022/Day 16/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    rooms = parse(data)
    print(rooms)
    G = build_graph(rooms)
    print(G)
    valve_flow = {k: v["flow"] for k, v in rooms.items() if v["flow"] > 0}
    print(valve_flow)
    max_gas = 0
    for i, p in enumerate(permutations(valve_flow)):
        if i % 100_000 == 0:
            print(i, p)
        gas = f(G, p, valve_flow)
        max_gas = max(max_gas, gas)
    return max_gas


def part2(data: str):
    """Part 2 solution"""
    return


def parse(data: str):
    rooms = {}
    regex = r"Valve (\w\w) has flow rate=(\d+); tunnels? leads? to valves? (.*)"
    for line in data.splitlines():
        match = re.match(regex, line)
        if not match:
            raise ValueError(line)
        src, flow, dsts = match.groups()
        rooms[src] = {
            "flow": int(flow),
            "dsts": dsts.split(", "),
        }
    return rooms


def build_graph(valves):
    G = nx.DiGraph()
    for src, props in valves.items():
        dsts = props["dsts"]
        for dst in dsts:
            G.add_edge(src, dst)
    return G


def f(G, nodes, valve_flow):
    time = 30
    gas = 0
    for src, dst in zip(("AA",) + nodes, nodes):
        lenght = get_path_length(G, src, dst)
        # print(src, dst, lenght)
        time -= lenght + 1
        if time < 0:
            return 0
        gas += time * valve_flow[dst]
    return gas


@cache
def get_path_length(G, src, dst):
    return nx.shortest_path_length(G, src, dst)


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
