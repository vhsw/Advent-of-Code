"Day 06 answers"
INPUT = "2020/Day 06/input.txt"


def part1(data):
    "Part 1 answer"
    return sum(len(set(group.replace("\n", ""))) for group in data)


def part2(data):
    "Part 2 answer"
    s = 0
    for group in data:
        s += len(set.intersection(*map(set, group.strip().split("\n"))))
    return s


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.read().split("\n\n")
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
