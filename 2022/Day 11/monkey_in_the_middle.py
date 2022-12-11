"""Day 11: Monkey in the Middle"""
from collections import deque
from dataclasses import dataclass
from math import lcm
from operator import add, mul
from typing import Callable


@dataclass
class Monkey:
    id: int
    items: deque[int]
    inspect: Callable[[int], int]
    test_val: int
    test: Callable[[int], int]

    @classmethod
    def from_text(cls, text: str):
        lines = text.splitlines()
        id_ = int(lines[0].split()[1].removesuffix(":"))
        items = deque(map(int, lines[1].removeprefix("  Starting items: ").split(", ")))
        arg1, op, arg2 = lines[2].removeprefix("  Operation: new = ").split()
        ops = {"+": add, "*": mul}

        def operation(old):
            return ops[op](
                old if arg1 == "old" else int(arg1),
                old if arg2 == "old" else int(arg2),
            )

        test_val = int(lines[3].removeprefix("  Test: divisible by "))
        true_monkey_id = int(lines[4].removeprefix("    If true: throw to monkey "))
        false_monkey_id = int(lines[5].removeprefix("    If false: throw to monkey"))

        def test(item: int):
            return true_monkey_id if item % test_val == 0 else false_monkey_id

        return cls(id_, items, operation, test_val, test)


with open("2022/Day 11/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    monkeys = parse(data)
    return solve(monkeys, 20, lambda n: n // 3)


def part2(data: str):
    """Part 2 solution"""
    monkeys = parse(data)
    worry_lcm = lcm(*(monkey.test_val for monkey in monkeys))
    return solve(monkeys, 10_000, lambda n: n % worry_lcm)


def parse(data: str):
    return [Monkey.from_text(monkey) for monkey in data.split("\n\n")]


def solve(monkeys: list[Monkey], rounds: int, decay: Callable[[int], int]):
    activity = [0 for _ in monkeys]
    for _ in range(rounds):
        for monkey in monkeys:
            while monkey.items:
                activity[monkey.id] += 1
                item = monkey.items.popleft()
                worry_level = monkey.inspect(item)
                worry_level = decay(worry_level)
                target_monkey = monkey.test(worry_level)
                monkeys[target_monkey].items.append(worry_level)
    activity.sort(reverse=True)
    return activity[0] * activity[1]


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
