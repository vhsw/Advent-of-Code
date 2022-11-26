"""Day 24: Arithmetic Logic Unit"""
from functools import cache

with open("2021/Day 24/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    sep = "inp w\n"
    parts = data.split(sep)[1:]
    todo = [(0, 0, ())]
    while todo:
        part, z, path = todo.pop()
        # 456976 := 26**4
        if part >= 10 and z > 456976:
            continue
        if part > 13:
            if z != 0:
                continue
            return "".join(map(str, path))
        for num in range(1, 10):
            result = run(parts[part], num, z)
            if result < 10_000_000:
                todo.append((part + 1, result, path + (num,)))


def part2(data: str):
    """Part 2 solution"""
    sep = "inp w\n"
    parts = data.split(sep)[1:]
    todo = [(0, 0, ())]
    while todo:
        part, z, path = todo.pop()
        if part >= 10 and z > 456976:
            continue
        if part > 13:
            if z != 0:
                continue
            return "".join(map(str, path))
        for num in range(9, 0, -1):
            result = run(parts[part], num, z)
            if result < 10_000_000:
                todo.append((part + 1, result, path + (num,)))


@cache
def run(code: str, data: int, z: int = 0):
    reg = {"w": data, "x": 0, "y": 0, "z": z}

    def value(arg):
        try:
            return reg[arg]
        except KeyError:
            return int(arg)

    for line in code.splitlines():
        opcode, a, b = line.split()
        match opcode:
            case "add":
                reg[a] += value(b)
            case "mul":
                reg[a] *= value(b)
            case "div":
                reg[a] //= value(b)
            case "mod":
                reg[a] %= value(b)
            case "eql":
                reg[a] = 1 * value(a) == value(b)
    return reg["z"]


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
