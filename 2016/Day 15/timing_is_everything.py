"""Day 15: Timing is Everything"""
import re
from itertools import count

with open("2016/Day 15/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    disks = parse(data)
    for time in count():
        for dt, disk in enumerate(disks, start=1):
            n_pos, pos = disk
            if (pos + time + dt) % n_pos:
                break
        else:
            return time


def part2(data: str):
    """Part 2 solution"""
    data += "\nDisc #7 has 11 positions; at time=0, it is at position 0."
    return part1(data)


def parse(data: str):
    regex = r"Disc #\d has (\d+) positions; at time=0, it is at position (\d+)"
    disks = []
    for line in data.splitlines():
        n_pos, pos = re.match(regex, line).groups()
        disks.append((int(n_pos), int(pos)))
    return disks


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
