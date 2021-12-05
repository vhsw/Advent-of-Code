"""Day 6: Memory Reallocation"""
from itertools import count

with open("2017/Day 06/input.txt", encoding="utf-8") as fp:
    DATA = [int(block) for block in fp.read().strip().split()]


def part1(data: list[int]):
    """Part 1 solution"""
    seen = {tuple(data)}
    while True:
        data = redistribute(data)
        t_data = tuple(data)
        if t_data in seen:
            return len(seen)
        seen.add(tuple(t_data))


def redistribute(blocks: list[int]):
    blocks = blocks.copy()
    max_val = max(blocks)
    max_idx = blocks.index(max_val)
    blocks[max_idx] = 0
    val, rem = divmod(max_val, len(blocks))
    blocks = [b + val for b in blocks]
    while rem:
        max_idx += 1
        blocks[max_idx % len(blocks)] += 1
        rem -= 1
    return blocks


def part2(data: list[int]):
    """Part 2 solution"""
    seen = {tuple(data)}
    while True:
        data = redistribute(data)
        t_data = tuple(data)
        if t_data in seen:
            loop_mark = t_data
            break
        seen.add(tuple(t_data))
    for loop_size in count(1):
        data = redistribute(data)
        if tuple(data) == loop_mark:
            return loop_size


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
