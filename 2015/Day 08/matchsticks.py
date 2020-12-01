"Day 08 answers"
from typing import Tuple


INPUT = "2015/Day 08/input.txt"


def part1(data: Tuple[str, ...]):
    "Part 1 answer"
    chars = 0
    mem = 0
    for line in data:
        print(repr(line))
        print(repr(bytes(line, "utf-8").decode("unicode_escape")))
        chars += len([i for i in line if i not in {" ", "\n"}])
        mem += len(bytes(line, "utf-8").decode("unicode_escape").replace("\n", "")) - 2

    return chars - mem


def part2(data):
    "Part 2 answer"
    chars = 0
    mem = 0
    for line in data:
        print(repr(line))
        print(repr(bytes(line, "utf-8").decode("unicode_escape")))
        chars += len([i for i in line if i not in {" ", "\n"}])
        mem += len(bytes(line, "utf-8").decode("unicode_escape").replace("\n", "")) - 2

    return chars - mem


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.readlines()
        DATA = r"""
""
"abc"
"aaa\"aaa"
"\x27"
""".strip().splitlines()
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
