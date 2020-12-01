"Day 04 answers"
from hashlib import md5

INPUT = "2015/Day 04/input.txt"


def part1(data):
    "Part 1 answer"
    num = 0
    while not md5(f"{data}{num}".encode("utf-8")).hexdigest().startswith("00000"):
        num += 1
    return num


def part2(data):
    "Part 2 answer"
    num = 0
    while not md5(f"{data}{num}".encode("utf-8")).hexdigest().startswith("000000"):
        num += 1
    return num


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.read().strip()
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
