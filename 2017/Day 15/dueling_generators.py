"""Day 15: Dueling Generators"""

from ctypes import CDLL

lib = CDLL("2017/Day 15/libdueling_generators.so")

with open("2017/Day 15/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    gen_a, gen_b = parse(data)
    return lib.part1(gen_a, gen_b)


def part2(data: str):
    """Part 2 solution"""
    gen_a, gen_b = parse(data)
    return lib.part2(gen_a, gen_b)


def parse(data: str):
    line_a, line_b = data.splitlines()
    return int(line_a.split()[-1]), int(line_b.split()[-1])


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
