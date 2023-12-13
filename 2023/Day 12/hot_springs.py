"""Day 12: Hot Springs"""
from functools import cache

with open("2023/Day 12/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str, folds=1):
    """Part 1 solution"""
    return sum(
        count_arrangements(pattern, groups) for pattern, groups in parse(data, folds)
    )


def part2(data: str):
    """Part 2 solution"""
    return part1(data, folds=5)


def parse(data: str, folds: int):
    return [parse_line(line, folds) for line in data.splitlines()]


def parse_line(line: str, folds: int):
    pattern, groups = line.split()
    pattern = "?".join(pattern for _ in range(folds))
    groups = ",".join(groups for _ in range(folds))
    return pattern, tuple(map(int, groups.split(",")))


# https://www.reddit.com/r/adventofcode/comments/18hbbxe/2023_day_12python_stepbystep_tutorial_with_bonus/
@cache
def count_arrangements(pattern: str, groups: tuple[int, ...]):
    if not groups:
        if "#" in pattern:
            return 0
        return 1

    if not pattern:
        return 0

    def sharp():
        group = groups[0]
        subpattern = pattern[:group]
        damaged = subpattern.count("#")
        unknown = subpattern.count("?")
        if (damaged + unknown) < group:
            return 0

        rest_groups = groups[1:]
        if not rest_groups:
            return count_arrangements(pattern[group:], rest_groups)

        if len(pattern) > group and pattern[group] == "#":
            return 0

        return count_arrangements(pattern[group + 1 :], rest_groups)

    def dot():
        return count_arrangements(pattern[1:], groups)

    match pattern[0]:
        case "#":
            return sharp()
        case ".":
            return dot()
        case "?":
            return sharp() + dot()


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
