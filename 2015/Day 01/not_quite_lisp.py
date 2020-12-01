"Day 01 answers"
INPUT = "2015/Day 01/input.txt"


def part1():
    "Part 1 answer"
    with open(INPUT) as data:
        text = data.read()
        return text.count("(") - text.count(")")


def part2():
    "Part 2 answer"
    floor = 0
    with open(INPUT) as data:
        for pos, char in enumerate(*data, start=1):
            floor += {"(": 1, ")": -1}[char]
            if floor < 0:
                return pos
    raise ValueError


if __name__ == "__main__":
    print(f"Part 1: { part1() }")
    print(f"Part 2: { part2() }")
