"""Day 14 Answers"""
from dataclasses import dataclass, field
import networkx as nx
from math import ceil
from typing import Dict, List, Tuple
from collections import deque, namedtuple

# Ingr = namedtuple("Ingr", ["name", "b"])

data = """157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT"""


def asd(s: str) -> Tuple[str, int]:
    n, name = s.split()
    return name, int(n)


def parse(data):
    graph: Dict[str, Tuple[int, Tuple[str, int]]] = {}

    for line in data.splitlines():
        inputs_str, output_str = line.split(" => ")
        inputs: List[Tuple[str, int]] = []
        for i in inputs_str.split(", "):
            if i is None:
                continue
            inputs.append(asd(i))
        name, n = asd(output_str)
        graph[name] = n, inputs
    return graph


def make(ingr, amount, graph):
    leftovers = {k: 0 for k in graph}
    maden = {k: 0 for k in graph}
    queue = deque([(ingr, amount)])
    total_ore = 0
    while queue:
        i, a = queue.popleft()
        if i == "ORE":
            total_ore += a
            continue
        yild, ingrs = graph[i]
        a -= leftovers[i]
        to_make = ceil(a / yild)
        made = to_make * yild
        maden[i] += made
        leftovers[i] = made - a
        queue.extend(ingrs * to_make)
    print(leftovers)
    print(maden)
    return total_ore


def make2(ingr, amount, graph):
    leftovers = {k: 0 for k in graph}
    queue = deque([(ingr, amount)])
    total_ore = 0
    while queue:
        i, a = queue.popleft()
        if i == "ORE":
            total_ore += a
            continue
        yild, ingrs = graph[i]
        a -= leftovers[i]
        to_make = ceil(a / yild)
        made = to_make * yild
        leftovers[i] = made - a
        queue.extend(ingrs * to_make)
    return total_ore, leftovers


def from_leftovers(leftovers, graph):
    queue = deque([("FUEL", 1)])

    while queue:
        i, a = queue.popleft()
        if i == "ORE":
            leftovers[i] -= a
            assert leftovers[i] >= 0
            continue
        yild, ingrs = graph[i]
        a -= leftovers[i]
        to_make = ceil(a / yild)
        made = to_make * yild
        leftovers[i] = made - a
        queue.extend(ingrs * to_make)
    return leftovers


INPUT = "2019/Day 14/input"


def part1():
    """Part 1 answer"""
    with open(INPUT) as data:
        G = parse(data.read())
    return make("FUEL", 1, G)


def part2():
    """Part 2 answer"""
    with open(INPUT) as data:
        G = parse(data.read())
    opf, lefovers = make2("FUEL", 1, G)
    cycles, fuel_left = divmod(1000000000000, opf)
    lefovers = {k: v * cycles for (k, v) in lefovers.items()}
    lefovers["ORE"] = fuel_left
    print(lefovers, cycles)
    while True:
        try:
            print()
            for k in sorted(lefovers):
                print(k, lefovers[k])
            lefovers = from_leftovers(lefovers, G)
            cycles += 1
        except AssertionError:
            break
    return cycles


if __name__ == "__main__":
    ANSWER1 = part1()
    print(f"Part 1: {ANSWER1}")
    ANSWER2 = part2()
    print(f"Part 2: {ANSWER2}")
