"Day 07 answers"
import re

INPUT = "2020/Day 07/input.txt"


def parse(data):
    m = {}
    for line in data:
        src, dst = line.split(" bags contain ")
        for n, color in re.findall(r"(\d+) (\w+ \w+)", dst):
            m.setdefault(src, []).append((int(n), color))
    return m


def part1(data):
    "Part 1 answer"
    rules = parse(data)
    bag_map = {c: [i[1] for i in rules[c]] for c in rules}
    to_do = {c for c in bag_map if "shiny gold" in bag_map[c]}
    seen = set()
    while to_do:
        new_c = to_do.pop()
        seen.add(new_c)
        to_do |= {c for c in bag_map if new_c in bag_map[c]}
    return len(seen)


def f(c, rules):
    if c not in rules:
        return 1
    s = 0
    for n, new_c in rules[c]:
        s += n * f(new_c, rules)
    return s + 1


def part2(data):
    "Part 2 answer"
    rules = parse(data)

    return f("shiny gold", rules) - 1


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.readlines()
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
