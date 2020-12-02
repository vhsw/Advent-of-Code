"Day 08 answers"

INPUT = "2015/Day 08/input.txt"


def part1(data):
    "Part 1 answer"
    chars = 0
    mem = 0
    for line in data:
        line = line.strip()
        chars += len(line)
        mem += len(bytes(line, "utf-8").decode("unicode_escape").replace("\n", "")) - 2

    return chars - mem


def part2(data):
    "Part 2 answer"
    chars = 0
    esc = 0
    for line in data:
        line = line.strip()
        escaped = '"' + line.replace("\\", "\\\\").replace('"', r"\"") + '"'
        esc += len(escaped)
        chars += len(line)

    return esc - chars


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.readlines()
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
