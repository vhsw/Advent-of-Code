"Day 03 answers"
INPUT = "2020/Day 03/input.txt"


def part1(data):
    "Part 1 answer"
    pos = 0
    s = 0
    for line in data:
        s += line[pos] == "#"
        pos = (pos + 3) % len(line)
    return s


def part2(data):
    "Part 2 answer"
    answer = 1
    for x, y in (
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ):
        pos = 0
        s = 0
        for line in data[::y]:
            s += line[pos] == "#"
            pos = (pos + x) % len(line)
        answer *= s
    return answer


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.read().strip().split("\n")
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
