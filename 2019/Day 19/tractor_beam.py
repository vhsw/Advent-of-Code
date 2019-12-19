"""Day 19 Answers"""
from intcode_v19 import Intcode

INPUT = "2019/Day 19/input"


def part1():
    """Part 1 answer"""
    with open(INPUT) as data:
        data = data.read().strip().split(",")
    code = [int(d) for d in data]

    total = 0
    for line in range(50):
        for col in range(50):
            ic = Intcode(code)
            res = ic.evaluate([line, col])
            total += res
    return total


def part2():
    """Part 2 answer"""
    with open(INPUT) as data:
        data = data.read().strip().split(",")
    code = [int(d) for d in data]

    def check(line, col):
        ic = Intcode(code)
        return ic.evaluate([line, col]) == 1

    def check_sqare(line, col, size=99):
        return check(line, col) and check(line + size, col - size)

    size = 99
    line = 0
    col = size
    while True:
        if check_sqare(line, col, size):
            print(line, col)
            return line * 10000 + (col - size)
        col += 1
        while check(line, col) == 0:
            line += 1


if __name__ == "__main__":
    ANSWER1 = part1()
    print(f"Part 1: {ANSWER1}")
    ANSWER2 = part2()
    print(f"Part 2: {ANSWER2}")
