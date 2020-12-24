"Day 23 answers"
from collections import deque


INPUT = "2020/Day 23/input.txt"

"""The crab picks up the three cups that are immediately clockwise of the current cup. They are removed from the circle; cup spacing is adjusted as necessary to maintain the circle.
The crab selects a destination cup: the cup with a label equal to the current cup's label minus one. If this would select one of the cups that was just picked up, the crab will keep subtracting one until it finds a cup that wasn't just picked up. If at any point in this process the value goes below the lowest value on any cup's label, it wraps around to the highest value on any cup's label instead.
The crab places the cups it just picked up so that they are immediately clockwise of the destination cup. They keep the same order as when they were picked up.
The crab selects a new current cup: the cup which is immediately clockwise of the current cup."""


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
    circle = deque(data)
    for i in range(10000000):
        # print(f"{i:02d}", circle)
        current = circle[0]
        circle.rotate(-1)
        # print(circle)
        picked = [circle.popleft() for _ in range(3)]
        # print("pick up:", picked)
        dst = current - 1
        while dst not in circle:
            dst -= 1
            if dst < 0:
                dst = 9
        # print("destination:", dst)
        idx = circle.index(dst) + 1
        while picked:
            circle.insert(idx, picked.pop())
    while circle[0] != 1:
        circle.rotate(-1)
    return "".join(map(str, circle))[1:]


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.read().strip()
    # DATA = "389125467"
    print(f"Part 1: { part1(list(map(int, DATA))) }")
    print(f"Part 2: { part2(list(map(int, DATA))) }")
