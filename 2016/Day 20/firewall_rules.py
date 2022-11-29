"""Day 20: Firewall Rules"""
with open("2016/Day 20/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str, max_num=4294967295):
    """Part 1 solution"""
    rules = parse(data)
    vals = []
    for rule in rules:
        val = rule[1] + 1
        for a, b in rules:
            if a <= val <= b:
                break
        else:
            vals.append(val)
    return min(vals)


def part2(data: str, max_num=4294967295):
    """Part 2 solution"""
    rules = parse(data)
    allowed = max_num + 1
    for lo, hi in merge(rules):
        allowed -= hi - lo + 1
    return allowed


def merge(rules: list[tuple[int, int]]):
    rules = sorted(rules)
    stack = [rules[0]]
    for rule in rules[1:]:
        last_rule = stack[-1]
        if last_rule[0] <= rule[0] <= last_rule[1]:
            stack[-1] = (last_rule[0], max(last_rule[1], rule[1]))
        else:
            stack.append(rule)
    return stack


def parse(data: str):
    res = []
    for line in data.splitlines():
        a, b = line.split("-")
        res.append((int(a), int(b)))
    return res


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
