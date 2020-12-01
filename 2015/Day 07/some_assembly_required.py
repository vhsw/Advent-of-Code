"Day 07 answers"
import re

import numpy as np

INPUT = "2015/Day 07/input.txt"

BINOPS = "AND|OR|LSHIFT|RSHIFT".split("|")


def parse(line):
    load = r"^(\w+) -> (\w+)"
    unop = r"^(NOT) (\w+) -> (\w+)"
    binop = r"^(\w+) ?(AND|OR|LSHIFT|RSHIFT) (\w+) -> (\w+)"
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
        in1, out = m.groups()
        if in1.isnumeric():
            in1 = int(in1)
        return "LOAD", in1, out


def do(op, ins):
    ins = np.array(ins, dtype="uint16")
    # print(op, ins)
    if op == "LOAD":
        return ins[0]
    if op == "NOT":
        return ~ins[0]
    if op == "AND":
        return ins[0] & ins[1]
    if op == "OR":
        return ins[0] | ins[1]
    if op == "LSHIFT":
        return ins[0] << ins[1]
    if op == "RSHIFT":
        return ins[0] >> ins[1]


def part1(data):
    "Part 1 answer"
    lst = []
    wires = {}
    for line in data:
        op, *ins, out = parse(line)
        lst.append([op, ins, out])
        wires[out] = None
        for i in ins:
            if isinstance(i, str):
                wires[i] = None
            else:
                wires[i] = i
    todo = lst
    while todo:
        for op, ins, out in todo:
            if not all(wires[i] is not None for i in ins):
                continue
            res = do(op, [wires[i] for i in ins])
            if res is not None:
                if out == "a":
                    return res
                wires[out] = res
        todo = [[op, ins, out] for op, ins, out in lst if wires[out] is None]


def part2(data):
    "Part 2 answer"
    lst = []
    wires = {}
    for line in data:
        op, *ins, out = parse(line)
        lst.append([op, ins, out])
        wires[out] = None
        for i in ins:
            if isinstance(i, str):
                wires[i] = None
            else:
                wires[i] = i
    wires["b"] = 956
    todo = [[op, ins, out] for op, ins, out in lst if wires[out] is None]
    while todo:
        for op, ins, out in todo:
            if not all(wires[i] is not None for i in ins):
                continue
            res = do(op, [wires[i] for i in ins])
            if res is not None:
                if out == "a":
                    return res
                wires[out] = res
        todo = [[op, ins, out] for op, ins, out in lst if wires[out] is None]


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.readlines()
    #     DATA = """123 -> x
    # 456 -> y
    # h -> a
    # x AND y -> d
    # x OR y -> e
    # x LSHIFT 2 -> f
    # y RSHIFT 2 -> g
    # NOT x -> h
    # NOT y -> i""".splitlines()
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
