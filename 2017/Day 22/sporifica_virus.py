"""Day 22: Sporifica Virus"""

from enum import Enum, auto


class States(Enum):
    CLEAN = auto()
    WEAKENED = auto()
    INFECTED = auto()
    FLAGGED = auto()


with open("2017/Day 22/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str, steps=10000):
    """Part 1 solution"""
    grid = parse(data)
    node = 0j
    direction = -1j
    infected = 0
    for _ in range(steps):
        if node in grid:
            direction *= 1j
            grid.pop(node)
        else:
            grid[node] = States.INFECTED
            direction *= -1j
            infected += 1
        node += direction
    return infected


def part2(data: str, steps=10000000):
    """Part 2 solution"""
    grid = parse(data)
    node = 0j
    direction = -1j
    infected = 0
    for _ in range(steps):
        state = grid.get(node, States.CLEAN)
        match state:
            case States.CLEAN:
                grid[node] = States.WEAKENED
                direction *= -1j
            case States.WEAKENED:
                grid[node] = States.INFECTED
                infected += 1
            case States.INFECTED:
                grid[node] = States.FLAGGED
                direction *= 1j
            case States.FLAGGED:
                grid.pop(node, None)
                direction *= -1
        node += direction
    return infected


def parse(data: str):
    lines = data.splitlines()
    return {
        complex(col, row): States.INFECTED
        for row, line in enumerate(lines, start=-(len(lines) // 2))
        for col, char in enumerate(line, start=-(len(lines[0]) // 2))
        if char == "#"
    }


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
