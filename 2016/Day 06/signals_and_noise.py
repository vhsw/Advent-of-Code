"Day 06 answers"
from collections import Counter

INPUT = "2016/Day 06/input.txt"


def part1(data):
    "Part 1 answer"
    return "".join([Counter(letter).most_common(1)[0][0] for letter in zip(*data)])


def part2(data):
    "Part 2 answer"
    return "".join([Counter(letter).most_common()[-1][0] for letter in zip(*data)])


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.read().strip().split()
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
