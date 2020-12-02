"Day 10 answers"
INPUT = "2015/Day 10/input.txt"


def part1(data):
    "Part 1 answer"
    for _ in range(40):
        n = 0
        prev = data[0]
        buf = ""
        for c in data:
            if c == prev:
                n += 1
                continue
            buf += f"{n}{prev}"
            n = 1
            prev = c
        buf += f"{n}{c}"
        data = buf
    return len(buf)


def part2(data):
    "Part 2 answer"
    for _ in range(50):
        n = 0
        prev = data[0]
        buf = ""
        for c in data:
            if c == prev:
                n += 1
                continue
            buf += f"{n}{prev}"
            n = 1
            prev = c
        buf += f"{n}{c}"
        data = buf
    return len(buf)


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.read().strip()
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
