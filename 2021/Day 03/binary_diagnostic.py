"""Day 3: Binary Diagnostic"""
from statistics import mode, multimode

with open("2021/Day 03/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    report = data.splitlines()
    bin_str = "".join(mode(col) for col in zip(*report))
    gamma = int(bin_str, base=2)
    mask = (1 << len(report[0])) - 1
    epsilon = ~gamma & mask
    return gamma * epsilon


def part2(data: str):
    """Part 2 solution"""
    oxygen_rating = oxygen_bit_criteria(data)
    co2_rating = co2_bit_criteria(data)

    return oxygen_rating * co2_rating


def oxygen_bit_criteria(data: str):
    report = data.splitlines()
    for pos in range(len(report[0])):
        col = [line[pos] for line in report]
        target = max(multimode(col))
        report = [line for line in report if line[pos] == target]
        if len(report) <= 1:
            return int(report[0], 2)
    raise ValueError(data)


def co2_bit_criteria(data: str):
    report = data.splitlines()
    for pos in range(len(report[0])):
        col = [line[pos] for line in report]
        target = {"0": "1", "1": "0"}[max(multimode(col))]
        report = [line for line in report if line[pos] == target]
        if len(report) <= 1:
            return int(report[0], 2)
    raise ValueError(data)


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
