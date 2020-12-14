"Day 02 answers"
INPUT = "2016/Day 02/input.txt"


def part1(data):
    "Part 1 answer"
    pos_x = 0
    pos_y = 0
    code = ""
    for line in data.split():
        for char in line:
            if char == "D":
                pos_x = min(pos_x + 1, 1)
            if char == "U":
                pos_x = max(pos_x - 1, -1)
            if char == "R":
                pos_y = min(pos_y + 1, 1)
            if char == "L":
                pos_y = max(pos_y - 1, -1)
        code += str(3 * (pos_x + 1) + pos_y + 2)
    return code


def part2(data):
    "Part 2 answer"
    key_map = [
        "    1    ",
        "  2 3 4  ",
        "5 6 7 8 9",
        "  A B C  ",
        "    D    ",
    ]
    pos_x = 2
    pos_y = 0
    code = ""
    for line in data.split():
        for char in line:
            old_x, old_y = pos_x, pos_y
            keys = key_map.copy()
            if char == "D":
                pos_x = pos_x + 1
            if char == "U":
                pos_x = pos_x - 1
            if char == "R":
                pos_y = pos_y + 2
            if char == "L":
                pos_y = pos_y - 2
            try:
                if pos_x < 0 or pos_y < 0 or keys[pos_x][pos_y] == " ":
                    raise ValueError
            except (IndexError, ValueError):
                pos_x, pos_y = old_x, old_y

        code += key_map[pos_x][pos_y]

    return code


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.read()

    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
