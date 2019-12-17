"""Day 16 Answers"""
from itertools import cycle

INPUT = "2019/Day 16/input"


def calc(data):
    out = []
    base = (0, 1, 0, -1)
    for i in range(1, len(data) + 1):
        pattern = []
        for d in base:
            pattern.extend([d] * i)
        pattern = cycle(pattern)
        next(pattern)
        res = sum(n * p for n, p in zip(data, pattern) if p)
        out.append(abs(res) % 10)
    return out


def calc2(data, offset):
    for _ in range(100):
        partial_sum = sum(data[offset:])
        for i in range(offset, len(data)):
            t = partial_sum
            partial_sum -= data[i]
            data[i] = abs(t) % 10

    return data[offset : offset + 8]


def part1():
    """Part 1 answer"""
    with open(INPUT) as data:
        data = data.read().strip()
    code = [int(d) for d in data]
    for _ in range(100):
        code = calc(code)
    return int("".join(str(d) for d in code[:8]))


def part2():
    """Part 2 answer"""
    with open(INPUT) as data:
        data = data.read().strip()
    data = data * 10000
    code = [int(d) for d in data]
    offset = int(data[:7])
    assert offset > len(data) / 2
    code = calc2(code, offset)
    return int("".join(str(d) for d in code))


if __name__ == "__main__":
    ANSWER1 = part1()
    print(f"Part 1: {ANSWER1}")
    ANSWER2 = part2()
    print(f"Part 2: {ANSWER2}")
