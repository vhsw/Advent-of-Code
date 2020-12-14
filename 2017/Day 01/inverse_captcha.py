"Day 01 answers"
INPUT = "2017/Day 01/input.txt"


def part1(data):
    "Part 1 answer"
    data = data.strip()
    data = [int(i) for i in data] + [int(data[0])]
    return sum(c for c, n in zip(data, data[1:]) if c == n)


def part2(data):
    "Part 2 answer"
    data = data.strip()
    data = [int(i) for i in data]
    s = 0
    l = len(data)
    for i, c in enumerate(data):
        offset = (i + l // 2) % l
        print(i, offset, c, data[offset])
        if c == data[offset]:
            s += c
    return s


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.read()
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
