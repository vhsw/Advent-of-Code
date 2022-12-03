"""Day 21: Chronal Conversion"""
from typing import TypeAlias

Instruction: TypeAlias = tuple[str, int, int, int]

with open("2018/Day 21/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    ip_reg, code = parse(data)
    return run(ip_reg, [0, 0, 0, 0, 0, 0], code, return_first=True)


def part2(data: str):
    """Part 2 solution"""
    ip_reg, code = parse(data)
    return run(ip_reg, [0, 0, 0, 0, 0, 0], code, return_first=False)


def parse(data: str):
    lines = data.splitlines()
    ip_reg = int(lines[0].split()[-1])
    code: list[Instruction] = []
    for line in lines[1:]:
        instr, A, B, C = line.split()
        a, b, c = map(int, (A, B, C))
        code.append((instr, a, b, c))
    return ip_reg, code


def run(ip_reg, regs: list[int], code: list[Instruction], return_first):
    ip = 0
    last = 0
    seen = set()

    while 0 <= ip < len(code):
        regs[ip_reg] = ip
        line = code[ip]
        instr, a, b, c = line
        match instr:
            case "addr":
                regs[c] = regs[a] + regs[b]
            case "addi":
                regs[c] = regs[a] + b
            case "mulr":
                regs[c] = regs[a] * regs[b]
            case "muli":
                regs[c] = regs[a] * b
            case "banr":
                regs[c] = regs[a] & regs[b]
            case "bani":
                regs[c] = regs[a] & b
            case "borr":
                regs[c] = regs[a] | regs[b]
            case "bori":
                regs[c] = regs[a] | b
            case "setr":
                regs[c] = regs[a]
            case "seti":
                regs[c] = a
            case "gtir":
                regs[c] = int(a > regs[b])
            case "gtri":
                regs[c] = int(regs[a] > b)
            case "gtrr":
                regs[c] = int(regs[a] > regs[b])
            case "eqir":
                regs[c] = int(a == regs[b])
            case "eqri":
                regs[c] = int(regs[a] == b)
            case "eqrr":
                if b == 0:
                    val = regs[a]
                    if return_first:
                        return val
                    if val in seen:
                        return last
                    seen.add(val)
                    last = val
                regs[c] = int(regs[a] == regs[b])
        ip = regs[ip_reg]
        ip += 1
        # print(regs)


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
