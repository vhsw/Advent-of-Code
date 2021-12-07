"""Day 2: Dive!"""
with open("2021/Day 02/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    horizontal = 0
    depth = 0
    for line in data.splitlines():
        direction, displacement = line.split()
        displacement = int(displacement)
        match direction:
            case "forward":
                horizontal += displacement
            case "up":
                depth -= displacement
            case "down":
                depth += displacement
    return horizontal * depth


def part2(data: str):
    """Part 2 solution"""
    horizontal = 0
    depth = 0
    aim = 0
    for line in data.splitlines():
        direction, displacement = line.split()
        displacement = int(displacement)
        match direction:
            case "forward":
                horizontal += displacement
                depth += aim * displacement
            case "up":
                aim -= displacement
            case "down":
                aim += displacement
    return horizontal * depth


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
