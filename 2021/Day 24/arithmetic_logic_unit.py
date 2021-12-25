"""Day 24: Arithmetic Logic Unit"""

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


def run(code: str, data: int, z: int = 0):
    reg = {"w": data, "x": 0, "y": 0, "z": z}

    def value(arg):
        if arg in reg:
            return reg[arg]
        return int(arg)

    for line in code.splitlines():
        opcode, a, b = line.split()
        match opcode:
            case "add":
                val = value(b)
                reg[a] += value(b)
            case "mul":
                reg[a] *= value(b)
            case "div":
                val = value(b)
                assert val != 0
                reg[a] //= val
            case "mod":
                val = value(b)
                assert val > 0
                assert reg[a] >= 0
                reg[a] %= value(b)
            case "eql":
                reg[a] = 1 if value(a) == value(b) else 0
    return reg["z"]


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
