"Day 13 answers"
INPUT = "2020/Day 13/input.txt"


def part1(data):
    "Part 1 answer"
    ts, buses = data
    ts = int(ts)
    buses = [int(i) for i in buses.split(",") if i != "x"]
    offset = 0
    while True:
        for b in buses:
            if (ts + offset) % b == 0:
                return b * offset
        offset += 1


def part2(data):
    "Part 2 answer"
    buses = {int(v): i for i, v in enumerate(data.split(",")) if v != "x"}
    step = 1
    offset = 0
    for b in buses:
        for i in range(offset, b * step, step):
            if i % b == (b - buses[b]) % b:
                offset = i
                step *= b
    return offset


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.read().split()
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA[1]) }")
