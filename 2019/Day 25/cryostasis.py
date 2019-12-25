"""Day 25 Answers"""
from itertools import combinations
from intcode_v25 import Intcode

INPUT = "2019/Day 25/input"


def parse_springscript(path):
    springcode = []
    with open(path) as fp:
        data = fp.read().splitlines()
        for line in data:
            if not line or line.startswith("#"):
                continue
            springcode.extend(ord(i) for i in line)
            springcode.append(ord("\n"))
    return springcode


def part1():
    """Part 1 answer"""
    with open(INPUT) as data:
        data = data.read().strip().split(",")
    code = [int(d) for d in data]
    ic = Intcode(code)
    with open("2019/Day 25/instructions.txt") as fp:
        instr = list(fp.read())
    out = ic.evaluate(instr)

    # items = [
    #     "hologram",
    #     "shell",
    #     "whirled peas",
    #     "fuel cell",
    #     "fixed point",
    #     "polygon",
    #     "antenna",
    #     "candy cane",
    # ]
    # for l in [4]:  # range(1, len(items) + 1):
    #     for p in combinations(items, r=l):
    #         instr = []
    #         for i in items:
    #             instr.extend(f"drop {i}\n")
    #         for i in p:
    #             instr.extend(f"take {i}\n")
    #         instr.extend("inv\n")
    #         instr.extend("west\n")
    #         instr.extend("west\n")
    #         out = ic.evaluate(instr[:])

    return out


if __name__ == "__main__":
    ANSWER1 = part1()
    print(f"Part 1: {ANSWER1}")
