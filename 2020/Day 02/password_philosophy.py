"Day 02 answers"
import re

INPUT = "2020/Day 02/input.txt"


def check(line):
    low, high, char, password = re.match(r"(\d+)-(\d+) (\w): (\w+)", line).groups()
    low = int(low)
    high = int(high)
    return low <= password.count(char) <= high


def check2(line):
    p1, p2, char, password = re.match(r"(\d+)-(\d+) (\w): (\w+)", line).groups()
    p1 = int(p1) - 1
    p2 = int(p2) - 1
    c1 = password[p1]
    c2 = password[p2]
    return c1 != c2 and (c1 == char or c2 == char)


def part1(data):
    "Part 1 answer"
    return sum(map(check, data))


def part2(data):
    "Part 2 answer"
    return sum(map(check2, data))


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.readlines()
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
