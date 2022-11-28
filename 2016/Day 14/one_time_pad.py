"""Day 14: One-Time Pad"""
from collections import deque
from hashlib import md5
from itertools import count

with open("2016/Day 14/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def hashsum(data: str, idx: int):
    return md5(f"{data}{idx}".encode("utf-8")).hexdigest()


def stretched_hashsum(data: str, idx: int):
    digest = hashsum(data, idx)
    for _ in range(2016):
        digest = md5(digest.encode("utf-8")).hexdigest()
    return digest


def part1(data: str, key_func=hashsum):
    """Part 1 solution"""
    history = deque([key_func(data, i) for i in range(1000)])
    num_found = 0
    for idx in count():
        digest = history.popleft()
        history.append(key_func(data, idx + 1000))
        if triple := three_in_row(digest):
            if any(has_five_in_row(d, triple) for d in history):
                num_found += 1
                if num_found >= 64:
                    return idx


def part2(data: str):
    """Part 2 solution"""
    return part1(data, key_func=stretched_hashsum)


def three_in_row(digest: str):
    prev = ""
    counter = 0
    for char in digest:
        if char != prev:
            counter = 1
            prev = char
            continue
        counter += 1
        if counter >= 3:
            return char


def has_five_in_row(digest: str, match: str):
    counter = 0
    for char in digest:
        if char != match:
            counter = 0
            continue
        counter += 1
        if counter >= 5:
            return True
    return False


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
