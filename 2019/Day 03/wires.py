"""Day 3 Answers"""


def parse_command(command):
    """Return direction and distance for command"""
    return command[0], int(command[1:])


def move(pos, direction):
    """move position for given direction"""
    if direction == "R":
        return pos[0], pos[1] + 1
    if direction == "L":
        return pos[0], pos[1] - 1
    if direction == "U":
        return pos[0] + 1, pos[1]
    if direction == "D":
        return pos[0] - 1, pos[1]
    raise ValueError


def points(wire):
    pos = (0, 0)
    result = {}
    length = 0
    for command in wire:
        direction, dist = parse_command(command)
        for _ in range(dist):
            pos = move(pos, direction)
            length += 1
            result[pos] = length

    return result


def distance(wire1, wire2):
    wire1 = wire1.split(",")
    wire2 = wire2.split(",")
    points1 = set(points(wire1))
    points2 = set(points(wire2))
    home = (0, 0)
    intersection = (points1 & points2) - set((home,))
    return min(map(lambda pos: abs(pos[0]) + abs(pos[1]), intersection))


def steps(wire1, wire2):
    wire1 = wire1.split(",")
    wire2 = wire2.split(",")
    points1 = points(wire1)
    points2 = points(wire2)
    home = (0, 0)
    intersection = set(points1) & set(points2)
    distances = []
    for p in intersection:
        if p == home:
            continue
        distances.append(points1[p] + points2[p])

    return min(distances)


INPUT = "2019/Day 03/input"


def part1():
    with open(INPUT) as data:
        WIRE1, WIRE2 = data.readlines()
    return distance(WIRE1, WIRE2)


def part2():
    with open(INPUT) as data:
        WIRE1, WIRE2 = data.readlines()
    return steps(WIRE1, WIRE2)


if __name__ == "__main__":
    ANSWER1 = part1()
    print(f"Part 1: {ANSWER1}")
    ANSWER2 = part2()
    print(f"Part 2: {ANSWER2}")
