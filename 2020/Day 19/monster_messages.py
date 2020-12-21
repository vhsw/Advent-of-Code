"Day 19 answers"
import re

INPUT = "2020/Day 19/input.txt"


def build(idx, rules, depth=0):
    if depth > 15:  # works in my case, increase if your answer fails
        return ""
    rule = rules[idx]
    if isinstance(rule, str):
        return rule
    return (
        "("
        + "|".join(
            "".join(build(item, rules, depth + 1) for item in group) for group in rule
        )
        + ")"
    )


def part1(data: str):
    "Part 1 answer"
    rules_data, data = data.split("\n\n")
    rules = {}
    for line in rules_data.split("\n"):
        if m := re.match(r"(\d+): (.*)", line):
            num, rule = m.groups()
        else:
            raise Exception(line)
        if rule in {'"a"', '"b"'}:
            rules[int(num)] = rule.strip('"')
        else:
            rules[int(num)] = [
                list(map(int, group.split())) for group in rule.strip().split("|")
            ]
    regex = build(0, rules)
    regex = "^" + regex.replace(" ", "") + "$"
    s = 0
    for line in data.split("\n"):
        if re.match(regex, line):
            s += 1
    return s


def part2(data):
    "Part 2 answer"
    rules_data, data = data.split("\n\n")
    rules = {}
    for line in rules_data.split("\n"):
        if m := re.match(r"(\d+): (.*)", line):
            num, rule = m.groups()
        else:
            raise Exception(line)
        if rule in {'"a"', '"b"'}:
            rules[int(num)] = rule.strip('"')
        else:
            rules[int(num)] = [
                list(map(int, group.split())) for group in rule.strip().split("|")
            ]
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]

    regex = build(0, rules)
    regex = "^" + regex.replace(" ", "") + "$"
    s = 0
    for line in data.split("\n"):
        if re.match(regex, line):
            s += 1
    return s


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.read().strip()

    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
