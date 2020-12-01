"Day 07 answers"
import networkx as nx
import re

INPUT = "2015/Day 07/input.txt"

BINOPS = "AND|OR|LSHIFT|RSHIFT".split("|")


def parse(line):
    load = r"(\w+) -> (\w+)"
    unop = r"(NOT) (\w+) -> (\w+)"
    binop = r"(\w+) ?(AND|OR|LSHIFT|RSHIFT) (\w+) -> (\w+)"
    if m := re.match(binop, line):
        in1, op, in2, out = m.groups()
        if in1.isnumeric():
            in1 = int(in1)
        if in2.isnumeric():
            in2 = int(in2)
        return op, in1, in2, out
    if m := re.match(unop, line):
        op, in1, out = m.groups()
        if in1.isnumeric():
            in1 = int(in1)
        return op, in1, out
    if m := re.match(load, line):
        op, in1, out = m.groups()
        if in1.isnumeric():
            in1 = int(in1)
        return "LOAD", in1, out


def part1(data):
    "Part 1 answer"

    G = nx.DiGraph()
    for line in data:
        op, *ins, out = parse(line)
        for i in ins:
            G.add_edge(i, out, op=op)
    nx.draw(G, with_labels=True)


def part2(data):
    "Part 2 answer"


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.readlines()
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
