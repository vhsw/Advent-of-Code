"""Day 21 Answers"""
from intcode_v21 import Intcode

INPUT = "2019/Day 21/input"


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
    springcode = parse_springscript("2019/Day 21/part1.springscript")
    return ic.evaluate_auto(springcode)


def part2():
    """Part 2 answer"""
    with open(INPUT) as data:
        data = data.read().strip().split(",")
    code = [int(d) for d in data]
    ic = Intcode(code)
    springcode = springcode = parse_springscript("2019/Day 21/part2.springscript")
    return ic.evaluate_auto(springcode)


if __name__ == "__main__":
    ANSWER1 = part1()
    print(f"Part 1: {ANSWER1}")
    ANSWER2 = part2()
    print(f"Part 2: {ANSWER2}")
