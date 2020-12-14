"Day 01 answers"
INPUT = "2016/Day 01/input.txt"


def part1(data):
    "Part 1 answer"
    east = 0
    north = 0
    d_east = 0
    d_north = 1
    for instr in data:
        turn = instr[0]
        distance = int(instr[1:])
        if turn == "R":
            d_east, d_north = -d_north, d_east
        elif turn == "L":
            d_east, d_north = d_north, -d_east
        east += distance * d_east
        north += distance * d_north
    return abs(east) + abs(north)


def part2(data):
    "Part 2 answer"
    east = 0
    north = 0
    d_east = 0
    d_north = 1
    seen = set(((east, north),))
    for instr in data:
        turn = instr[0]
        distance = int(instr[1:])
        if turn == "R":
            d_east, d_north = -d_north, d_east
        elif turn == "L":
            d_east, d_north = d_north, -d_east
        for _ in range(1, distance + 1):
            east += d_east
            north += d_north
            if (east, north) in seen:
                return abs(east) + abs(north)
            seen.add((east, north))


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.read().split(", ")
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
