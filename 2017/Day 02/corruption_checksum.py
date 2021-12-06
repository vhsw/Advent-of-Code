"""Day 2: Corruption Checksum"""
from itertools import combinations

with open("2017/Day 02/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    return sum(max(row) - min(row) for row in parse(data))


def part2(data: str):
    """Part 2 solution"""
    total = 0
    for line in parse(data):
        for denom, num in combinations(sorted(line), 2):
            if num % denom == 0:
                total += num // denom
                break
    return total


def parse(data: str):
    return [list(map(int, line.split())) for line in data.splitlines()]


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
