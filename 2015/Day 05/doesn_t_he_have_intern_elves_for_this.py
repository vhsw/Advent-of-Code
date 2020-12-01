"Day 05 answers"
import re

INPUT = "2015/Day 05/input.txt"


def nice(line):
    return bool(
        len(re.sub(r"[^aeiou]", "", line)) >= 3
        and re.findall(r".*(\w)\1", line)
        and all(forbidden not in line for forbidden in ("ab", "cd", "pq", "xy"))
    )


def nice2(line):
    return bool(
        re.findall(r"(\w{2})(?:.*)\1", line) and re.findall(r"(\w{1})\w\1", line)
    )


def part1(data):
    "Part 1 answer"
    total = 0
    for line in data:
        total += nice(line)
    return total


def part2(data):
    "Part 2 answer"
    total = 0
    for line in data:
        total += nice2(line)
    return total


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.readlines()
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
