"""Day 8: I Heard You Like Registers"""
import re
from collections import defaultdict
from operator import eq, ge, gt, le, lt, ne
from typing import DefaultDict

with open("2017/Day 08/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()

CONDITION = {
    ">": gt,
    "<": lt,
    ">=": ge,
    "<=": le,
    "==": eq,
    "!=": ne,
}

SIGN = {
    "inc": 1,
    "dec": -1,
}
INSTRUCTION = re.compile(r"(\w+) (inc|dec) (-?\d+) if (\w+) (\S+) (-?\d+)")


def part1(data: str):
    """Part 1 solution"""
    registers: DefaultDict[str, int] = defaultdict(int)
    for line in data.splitlines():
        match = INSTRUCTION.match(line)
        if not match:
            raise ValueError(line)
        reg, op, val, chk_reg, chk_op, chk_val = match.groups()
        if CONDITION[chk_op](registers[chk_reg], int(chk_val)):
            registers[reg] += int(val) * SIGN[op]
    return max(registers.values())


def part2(data):
    """Part 2 solution"""
    registers: DefaultDict[str, int] = defaultdict(int)
    max_val = 0
    for line in data.splitlines():
        match = INSTRUCTION.match(line)
        if not match:
            raise ValueError(line)
        reg, op, val, chk_reg, chk_op, chk_val = match.groups()
        if CONDITION[chk_op](registers[chk_reg], int(chk_val)):
            registers[reg] += int(val) * SIGN[op]
        max_val = max(max_val, max(registers.values()))
    return max_val


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
