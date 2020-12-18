"Day 12 answers"
from math import cos, radians, sin

INPUT = "2020/Day 12/input.txt"


#       N(0)
#
# W(270)     E(90)
#
#      S(180)


def part1(data):
    "Part 1 answer"
    east = 0
    north = 0
    heading = 90
    for line in data:
        cmd = line[0]
        val = int(line[1:])
        if cmd == "F":
            cmd = {
                0: "N",
                90: "E",
                180: "S",
                270: "W",
            }[heading]
        if cmd == "N":
            north += val
        elif cmd == "S":
            north -= val
        elif cmd == "E":
            east += val
        elif cmd == "W":
            east -= val
        elif cmd == "R":
            heading += val
            heading %= 360
        elif cmd == "L":
            heading -= val
            heading %= 360
    return abs(east) + abs(north)


def part2(data):
    "Part 2 answer"
    east = 0
    north = 0
    wp_east = 10
    wp_north = 1
    for line in data:
        cmd = line[0]
        val = int(line[1:])
        if cmd == "F":
            east += val * wp_east
            north += val * wp_north
        elif cmd == "N":
            wp_north += val
        elif cmd == "S":
            wp_north -= val
        elif cmd == "E":
            wp_east += val
        elif cmd == "W":
            wp_east -= val
        elif cmd == "R":
            val = -val
            te = round(wp_east * cos(radians(val)) - wp_north * sin(radians(val)))
            wp_north = round(wp_east * sin(radians(val)) + wp_north * cos(radians(val)))
            wp_east = te
        elif cmd == "L":
            te = round(wp_east * cos(radians(val)) - wp_north * sin(radians(val)))
            wp_north = round(wp_east * sin(radians(val)) + wp_north * cos(radians(val)))
            wp_east = te
    return abs(east) + abs(north)


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.readlines()
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
