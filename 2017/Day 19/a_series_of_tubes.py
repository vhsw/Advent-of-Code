"""Day 19: A Series of Tubes"""
with open("2017/Day 19/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip("\n")


def part1(data: str):
    """Part 1 solution"""
    grid = parse(data)
    origin = data.splitlines()[0].index("|")
    pos = complex(origin, 0)
    heading = 1j
    letters = []
    while pos in grid:
        match grid[pos]:
            case "+":
                for new_heading in (heading * 1j, -heading * 1j):
                    if pos + new_heading in grid:
                        heading = new_heading
                        break
                else:
                    return 0
            case "|" | "-":
                pass
            case letter:
                letters.append(letter)
        pos += heading

    return "".join(letters)


def part2(data: str):
    """Part 2 solution"""
    grid = parse(data)
    origin = data.splitlines()[0].index("|")
    pos = complex(origin, 0)
    heading = 1j
    steps = 0
    while pos in grid:
        if grid[pos] == "+":
            for new_heading in (heading * 1j, -heading * 1j):
                if pos + new_heading in grid:
                    heading = new_heading
                    break
        pos += heading
        steps += 1

    return steps


def parse(data: str):
    return {
        complex(col, row): char
        for row, line in enumerate(data.splitlines())
        for col, char in enumerate(line)
        if char != " "
    }


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
