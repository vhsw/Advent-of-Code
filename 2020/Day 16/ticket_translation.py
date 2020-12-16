"Day 16 answers"
import re
from typing import Dict, List

INPUT = "2020/Day 16/input.txt"


def part1(features, ticket, tickets):
    "Part 1 answer"
    s = 0
    for t in tickets:
        for f in t:
            if not any(f in v for v in features.values()):
                s += f
                break
    return s


def part2(features, ticket, tickets):
    "Part 2 answer"
    tickets = [
        t for t in tickets if all(any(f in v for v in features.values()) for f in t)
    ]
    names: Dict[List[str]] = {}
    for i, vals in enumerate(zip(*tickets)):
        for feature in features:
            if features[feature].issuperset(set(vals)):
                print(i, feature)
                names.setdefault(i, []).append(feature)
    print(names)
    while not all(len(v) == 1 for v in names.values()):
        for feature in names:
            if len(names[feature]) == 1:
                name = names[feature][0]
                for dup in set(names) - {feature}:
                    try:
                        names[dup].remove(name)
                    except ValueError:
                        pass
    print(names)
    mul = 1
    for k, v in names.items():
        if v[0].startswith("departure"):
            mul *= ticket[k]
    return mul


def parse(raw):
    raw_features, raw = raw.split("\n\n", 1)
    features = {}
    for f in raw_features.split("\n"):
        name, low1, high1, low2, high2 = re.match(
            r"([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)", f
        ).groups()
        low1, high1, low2, high2 = map(int, (low1, high1, low2, high2))
        features[name] = set(range(low1, high1 + 1)) | set(range(low2, high2 + 1))
    raw_ticket, raw_tickets = raw.split("\n\n", 1)
    ticket = list(map(int, raw_ticket.split("\n")[1].split(",")))
    tickets = [
        list(map(int, line.split(","))) for line in raw_tickets.strip().split("\n")[1:]
    ]

    return features, ticket, tickets


if __name__ == "__main__":
    with open(INPUT) as fp:
        RAW = fp.read()
    RAW1 = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
11,3,47
40,4,50
55,2,20
38,6,12"""

    print(f"Part 1: { part1(*parse(RAW)) }")
    print(f"Part 2: { part2(*parse(RAW)) }")
