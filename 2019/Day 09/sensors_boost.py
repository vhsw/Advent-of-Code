"""Day 9 Answers"""
from intcode import Intcode

INPUT = "2019/Day 09/input"


def part1():
    """Part 1 answer"""
    with open(INPUT) as data:
        data = data.read().strip().split(",")
    code = [int(d) for d in data]
    ic = Intcode(code, input_data=[1])
    return ic.output_data[0]


def part2():
    """Part 2 answer"""
    with open(INPUT) as data:
        data = data.read().strip().split(",")
    code = [int(d) for d in data]
    ic = Intcode(code, input_data=[2])
    return ic.output_data[0]


if __name__ == "__main__":
    ANSWER1 = part1()
    print(f"Part 1: {ANSWER1}")
    ANSWER2 = part2()
    print(f"Part 2: {ANSWER2}")
