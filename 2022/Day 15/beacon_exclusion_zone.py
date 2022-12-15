"""Day 15: Beacon Exclusion Zone"""
import re

with open("2022/Day 15/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str, y=2000000):
    """Part 1 solution"""
    sensors, beacons = parse(data)
    uniq_beacons = set(beacons)
    radii = [manhattan_distance(s, b) for s, b in zip(sensors, beacons)]
    intervals = intervals_on_line(sensors, radii, y)
    return sum(
        end - start + 1 - count_beacons(uniq_beacons, start, end, y)
        for start, end in intervals
    )


def part2(data: str, size=4000000):
    """Part 2 solution"""
    sensors, beacons = parse(data)
    radii = [manhattan_distance(s, b) for s, b in zip(sensors, beacons)]
    for y in range(size):
        intervals = intervals_on_line(sensors, radii, y)
        for i1, i2 in zip(intervals, intervals[1:]):
            if i2[0] - i1[1] == 2:
                return 4000000 * (i1[1] + 1) + y


def parse(data: str) -> tuple[list[complex], list[complex]]:
    regex = r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
    sensors = []
    beacons = []
    for line in data.splitlines():
        match = re.match(regex, line)
        if not match:
            raise ValueError(line)
        s_x, s_y, b_x, b_y = match.groups()
        sensors.append(complex(int(s_x), int(s_y)))
        beacons.append(complex(int(b_x), int(b_y)))
    return sensors, beacons


def manhattan_distance(x: complex, y: complex):
    diff = x - y
    return abs(diff.real) + abs(diff.imag)


def intervals_on_line(sensors, radii, line):
    intervals = []
    for s, r in zip(sensors, radii):
        dist_to_line = manhattan_distance(s, complex(s.real, line))
        diff = r - dist_to_line
        if diff < 0:
            continue
        intervals.append((int(s.real - diff), int(s.real + diff)))

    return merge(intervals)


def merge(intervals: list[tuple[int, int]]):
    intervals = sorted(intervals)
    stack = [intervals[0]]
    for rule in intervals[1:]:
        last_rule = stack[-1]
        if last_rule[0] <= rule[0] <= last_rule[1]:
            stack[-1] = (last_rule[0], max(last_rule[1], rule[1]))
        else:
            stack.append(rule)
    return stack


def count_beacons(beacons, start, end, line):
    return sum(b.imag == line and start <= b.real <= end for b in beacons)


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
