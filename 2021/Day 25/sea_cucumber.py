"""Day 25: Sea Cucumber"""
with open("2021/Day 25/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    east, south, rows, cols = parse(data)
    steps = 0
    while True:
        new_east, new_south = step(east, south, rows, cols)
        steps += 1

        if (new_east == east) and (new_south == south):
            return steps
        east, south = new_east, new_south


def step(east: set[complex], south: set[complex], rows: int, cols: int):
    occupied = east | south
    east = {
        cuc
        if (n_cuc := complex((cuc.real + 1) % cols, cuc.imag)) in occupied
        else n_cuc
        for cuc in east
    }

    occupied = east | south
    south = {
        cuc
        if (n_cuc := complex(cuc.real, (cuc.imag + 1) % rows)) in occupied
        else n_cuc
        for cuc in south
    }

    return east, south


def parse(data: str):
    lines = data.splitlines()
    east = {
        complex(col, row)
        for row, line in enumerate(lines)
        for col, char in enumerate(line)
        if char == ">"
    }
    south = {
        complex(col, row)
        for row, line in enumerate(lines)
        for col, char in enumerate(line)
        if char == "v"
    }
    return east, south, len(lines), len(lines[0])


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
