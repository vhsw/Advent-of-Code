"Day 10 answers"
import re
from math import prod
from typing import Dict, List, Set, Tuple

INPUT = "2016/Day 10/input.txt"


def parts_1_2(data: List[str]):
    "Part 1 answer"
    bots: Dict[str, Set[int]] = {}
    rules: Dict[str, Tuple[str, str]] = {}
    for line in data:
        if m := re.match(r"value (\d+) goes to (\w+ \d+)", line):
            value, bot = m.groups()
            bots.setdefault(bot, set()).add(int(value))
        elif m := re.match(
            r"(\w+ \d+) gives low to (\w+ \d+) and high to (\w+ \d+)", line
        ):
            bot, low_target, high_target = m.groups()
            rules[bot] = (low_target, high_target)
    while any(1 for val in bots.values() if len(val) == 2):
        for bot in rules:
            if bot not in bots or len(bots[bot]) < 2:
                continue
            if bots[bot] == {61, 17}:
                print(f"Part 1: {bot }")
            low_target, high_target = rules[bot]
            bots.setdefault(low_target, set()).add(min(bots[bot]))
            bots.setdefault(high_target, set()).add(max(bots[bot]))
            bots[bot].clear()
    part_2 = prod(val for out in range(3) for val in bots[f"output {out}"])
    print(f"Part 2: {part_2}")


def part2(data):
    "Part 2 answer"


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.read().strip().split("\n")

    DATA1 = """value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2""".split(
        "\n"
    )

    parts_1_2(DATA)
