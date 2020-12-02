"Day 14 answers"
from os import device_encoding
import re

INPUT = "2015/Day 14/input.txt"


def part1(data):
    "Part 1 answer"
    deers = {}
    for line in data:
        name, speed, active, rest = re.match(
            r"(\w+) can fly (\d+) km\/s for (\d+) seconds, but then must rest for (\d+)",
            line,
        ).groups()
        deers[name] = [int(speed), int(active), int(rest)]

    dists = {name: 0 for name in deers}
    for s in range(2503):
        for name in deers:
            speed, active, rest = deers[name]
            if s % (active + rest) < active:
                dists[name] += speed
    return max(dists.values())


def part2(data):
    "Part 2 answer"
    deers = {}
    for line in data:
        name, speed, active, rest = re.match(
            r"(\w+) can fly (\d+) km\/s for (\d+) seconds, but then must rest for (\d+)",
            line,
        ).groups()
        deers[name] = [int(speed), int(active), int(rest)]

    dists = {name: 0 for name in deers}
    points = {name: 0 for name in deers}
    for s in range(2503):
        for name in deers:
            speed, active, rest = deers[name]
            if s % (active + rest) < active:
                dists[name] += speed
        m = max(dists.values())
        for name in deers:
            points[name] += dists[name] == m

    return max(points.values())


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.readlines()
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
