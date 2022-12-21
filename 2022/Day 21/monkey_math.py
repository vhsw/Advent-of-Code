"""Day 21: Monkey Math"""
from operator import add, floordiv, mul, sub

with open("2022/Day 21/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    values, ops = parse(data)
    return run(values, ops)


def part2(data: str):
    """Part 2 solution"""
    values, ops = parse(data)
    ops["root"][-1] = sub
    start_num = 1
    while True:
        result = run(values, ops, start_num)
        if result == 0:
            return start_num
        delta = (run(values, ops, start_num + 1) - run(values, ops, start_num - 1)) / 2
        start_num = int(start_num - result / delta)


def parse(data: str):
    values = {}
    ops = {}
    operators = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": floordiv,
    }
    for line in data.splitlines():
        monkey, value = line.split(": ")
        if value.isdigit():
            values[monkey] = int(value)
            continue
        left, op, right = value.split()
        ops[monkey] = [left, right, operators[op]]
    return values, ops


def run(values: dict, ops: dict, humn=None):
    values = values.copy()
    if humn is not None:
        values["humn"] = humn
    ops = ops.copy()
    while "root" not in values:
        for monkey, (left, right, op) in ops.items():
            if left in values and right in values:
                values[monkey] = op(values[left], values[right])
                del ops[monkey]
                break
    return values["root"]


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
