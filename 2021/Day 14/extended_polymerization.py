"""Day 14: Extended Polymerization"""
from typing import Counter

with open("2021/Day 14/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    template, rules_str = data.split("\n\n")
    rules = parse(rules_str)
    letter_counts = polymerize(template, rules, 10)
    most_common = letter_counts.most_common()
    return most_common[0][1] - most_common[-1][1]


def part2(data: str):
    """Part 2 solution"""
    template, rules_str = data.split("\n\n")
    rules = parse(rules_str)
    letter_counts = polymerize(template, rules, 40)
    most_common = letter_counts.most_common()
    return most_common[0][1] - most_common[-1][1]


def parse(rules_str: str):
    rules: dict[str, str] = {}
    for line in rules_str.splitlines():
        pair, element = line.split(" -> ")
        rules[pair] = element
    return rules


def polymerize(template: str, rules: dict[str, str], steps: int):
    pair_counts = Counter(zip(template, template[1:]))
    letter_counts = Counter(template)
    for _ in range(steps):
        new_pair_counts: Counter[tuple[str, str]] = Counter()
        for pair, num in pair_counts.items():
            # pylint: disable=invalid-name
            a, c = pair
            b = rules[a + c]
            new_pair_counts[(a, b)] += num
            new_pair_counts[(b, c)] += num
            letter_counts[b] += num
            # pylint: enable=invalid-name
        pair_counts = new_pair_counts
    return letter_counts


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
