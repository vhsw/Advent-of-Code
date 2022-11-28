"""Day 12: Leonardo's Monorail"""
with open("2016/Day 12/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    code = parse(data)
    regs = run({"a": 0, "b": 0, "c": 0, "d": 0}, code)
    return regs["a"]


def part2(data: str):
    """Part 2 solution"""
    code = parse(data)
    regs = run({"a": 0, "b": 0, "c": 1, "d": 0}, code)
    return regs["a"]


def parse(data: str):
    return [line.split() for line in data.splitlines()]


def run(regs: dict[str, int], code: list[tuple[str, ...]]):
    ip = 0
    max_ip = len(code)
    while ip < max_ip:
        match code[ip]:
            case ("cpy", x, y):
                regs[y] = regs[x] if x in regs else int(x)
            case ("inc", x):
                regs[x] += 1
            case ("dec", x):
                regs[x] -= 1
            case ("jnz", x, y):
                ip += (int(y) - 1) * ((regs[x] if x in regs else int(x)) != 0)
        ip += 1
    return regs


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
