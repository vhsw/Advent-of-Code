"""Day 23 Answers"""
from intcode_v23 import Intcode
from collections import Counter

INPUT = "2019/Day 23/input"


def part1():
    """Part 1 answer"""
    with open(INPUT) as data:
        data = data.read().strip().split(",")
    code = [int(d) for d in data]
    network = [Intcode(code, i) for i in range(50)]
    while True:
        for ic in network:
            while ic.output:
                dst, *package = ic.output.pop()
                if dst == 255:
                    return package[1]
                network[dst].input_data.extend(package)
        for ic in network:
            ic.evalute()


def part2():
    """Part 2 answer"""
    with open(INPUT) as data:
        data = data.read().strip().split(",")
    code = [int(d) for d in data]
    network = [Intcode(code, i) for i in range(50)]
    nat = None
    nat_pkgs = Counter()
    idle = False
    while True:
        idle = True
        for ic in network:
            while ic.output:
                idle = False
                dst, *package = ic.output.pop()
                if dst == 255:
                    nat = tuple(package)
                else:
                    network[dst].input_data.extend(package)
        for ic in network:
            ic.evalute()

        if all(len(ic.input_data) == 0 and len(ic.output) == 0 for ic in network):
            if nat and idle:
                network[0].input_data.extend(nat)
                nat_pkgs.update((nat,))
                if nat_pkgs[nat] > 2:
                    return nat[1]


if __name__ == "__main__":
    ANSWER1 = part1()
    print(f"Part 1: {ANSWER1}")
    ANSWER2 = part2()
    print(f"Part 2: {ANSWER2}")
