"""Day 7: The Treachery of Whales"""
from statistics import median

with open("2021/Day 07/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    positions = list(map(int, data.split(",")))
    mid = int(median(positions))
    return sum(abs(pos - mid) for pos in positions)


def part2(data: str):
    """Part 2 solution"""
    positions = list(map(int, data.split(",")))
    return min(
        sum(cost(pos, mid) for pos in positions)
        for mid in range(min(positions), max(positions) + 1)
    )


def cost(src: int, dst: int):
    num = abs(src - dst)
    return num * (num + 1) // 2


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
