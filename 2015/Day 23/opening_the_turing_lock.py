"Day 23 answers"
from typing import List


INPUT = "2015/Day 23/input.txt"


def run(code: List[str], a=0, b=0):
    reg = {
        "a": a,
        "b": b,
    }
    ip = 0
    while ip < len(code):
        opcode, arg = code[ip].split(maxsplit=1)
        if opcode == "hlf":
            reg[arg] = reg[arg] // 2
            ip += 1
        elif opcode == "tpl":
            reg[arg] = reg[arg] * 3
            ip += 1
        elif opcode == "inc":
            reg[arg] += 1
            ip += 1
        elif opcode == "jmp":
            ip += int(arg)
        elif opcode == "jie":
            r, offset = arg.split(", ")
            if reg[r] % 2 == 0:
                ip += int(offset)
            else:
                ip += 1
        elif opcode == "jio":
            r, offset = arg.split(", ")
            if reg[r] == 1:
                ip += int(offset)
            else:
                ip += 1
    return reg


def part1(data):
    "Part 1 answer"
    return run(data)["b"]


def part2(data):
    "Part 2 answer"
    return run(data, a=1)["b"]


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = [l.strip() for l in fp.readlines()]
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
