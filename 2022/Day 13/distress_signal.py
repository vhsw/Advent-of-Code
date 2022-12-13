"""Day 13: Distress Signal"""
import json
from itertools import zip_longest

with open("2022/Day 13/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    pairs = parse(data)
    return sum(
        idx
        for idx, (left, right) in enumerate(pairs, start=1)
        if is_smaller(left, right)
    )


def part2(data: str):
    """Part 2 solution"""
    pairs = parse(data)
    packets = []
    for pair in pairs:
        packets.extend(pair)
    packets.extend(([[2]], [[6]]))
    bubble_sort(packets)
    a = packets.index([[2]]) + 1
    b = packets.index([[6]]) + 1

    return a * b


def parse(data: str):
    pairs = []
    for pair in data.split("\n\n"):
        left, right = pair.splitlines()
        pairs.append((parse_value(left), parse_value(right)))
    return pairs


def parse_value(string: str):
    return json.loads(string)


def is_smaller(left, right):
    return compare(left, right) is not False


def compare(left, right):
    if right is None:
        return False
    if left is None:
        return True

    if isinstance(left, int) and isinstance(right, int):
        return None if left == right else left < right

    if isinstance(left, list) and isinstance(right, list):
        for l, r in zip_longest(left, right):
            val = compare(l, r)
            if val is None:
                continue
            return val
        return None

    if isinstance(left, int):
        left = [left]
    if isinstance(right, int):
        right = [right]
    return compare(left, right)


def bubble_sort(arr):
    length = len(arr)
    for i in range(length - 1):
        for j in range(length - i - 1):
            if not is_smaller(arr[j], arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
