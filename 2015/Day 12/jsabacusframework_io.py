"Day 12 answers"
import json
import re

INPUT = "2015/Day 12/input.txt"


def part1(data):
    "Part 1 answer"
    return sum(int(m) for m in re.findall(r"-?\d+", data))


def trav(d, acc=0):
    if isinstance(d, int):
        return d + acc
    if isinstance(d, list):
        return sum(trav(i) for i in d)
    if isinstance(d, dict):
        if "red" in d.values():
            return 0
        return sum(trav(i) for i in d.values())
    return 0


def part2(data):
    "Part 2 answer"
    d = json.loads(data)
    return trav(d)


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.read()
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
