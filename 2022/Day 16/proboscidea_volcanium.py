"""Day 16: Proboscidea Volcanium"""
import re
from functools import cache

import networkx as nx

with open("2022/Day 16/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    rooms = parse(data)
    flow = {k: v["flow"] for k, v in rooms.items()}
    neighbours = {k: v["dsts"] for k, v in rooms.items()}

    @cache
    def dfs(src, open_valves, time):
        if time <= 1:
            return 0
        gas = max(dfs(dst, open_valves, time - 1) for dst in neighbours[src])
        if src not in open_valves and flow[src] > 0:
            src_gas = flow[src] * (time - 1)
            gas = max(gas, dfs(src, open_valves | {src}, time - 1) + src_gas)
        return gas

    return dfs("AA", frozenset(), 30)


def part2(data: str):
    """Part 2 solution"""
    rooms = parse(data)
    flow = {k: v["flow"] for k, v in rooms.items()}
    valves = {k: v for k, v in flow.items() if v > 0}
    G = build_graph(rooms)

    @cache
    def get_path_length(src, dst):
        return nx.shortest_path_length(G, src, dst)

    @cache
    def dfs(state, open_valves):
        time, src = state[0]
        gas = 0
        for dst in valves:
            if dst in open_valves:
                continue
            new_time = time - get_path_length(src, dst) - 1
            if new_time <= 0:
                continue
            new_state = sort((new_time, dst), state[1])
            new_gas = valves[dst] * new_time
            gas = max(gas, dfs(new_state, open_valves | {dst}) + new_gas)
        return gas

    return dfs(((26, "AA"), (26, "AA")), frozenset())


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


def sort(a, b):
    return tuple(sorted((a, b), reverse=True))


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
