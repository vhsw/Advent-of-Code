"Day 23 answers"
from collections import deque


INPUT = "2020/Day 23/input.txt"


def part1(data):
    "Part 1 answer"
    circle = deque(data)
    for _ in range(100):
        current = circle[0]
        circle.rotate(-1)
        picked = [circle.popleft() for _ in range(3)]
        dst = current - 1
        while dst not in circle:
            dst -= 1
            if dst < 0:
                dst = 9
        idx = circle.index(dst) + 1
        while picked:
            circle.insert(idx, picked.pop())
    while circle[0] != 1:
        circle.rotate(-1)
    return "".join(map(str, circle))[1:]


def part2(data):
    "Part 2 answer"
    size = 1_000_000
    data = data + list(range(10, size + 1))
    circle = [0] * (size + 1)
    for cur, nxt in zip(data, data[1:] + [data[0]]):
        circle[cur] = nxt
    current = data[0]
    for _ in range(10_000_000):
        old_current = current
        picked = []
        for _ in range(3):
            current = circle[current]
            picked.append(current)
        current = circle[current]
        dst = old_current - 1
        if dst == 0:
            dst = size
        while dst in picked:
            dst -= 1
            if dst == 0:
                dst = size
        after_picked = circle[picked[-1]]
        circle[old_current] = after_picked
        after_dst = circle[dst]
        circle[dst] = picked[0]
        circle[picked[-1]] = after_dst

    after_one = circle[1]
    return after_one * circle[after_one]


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.read().strip()
    print(f"Part 1: { part1(list(map(int, DATA))) }")
    print(f"Part 2: { part2(list(map(int, DATA))) }")
