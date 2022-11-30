"""Day 25: Clock Signal"""
with open("2016/Day 25/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    code = parse(data)
    for i in range(1000):
        val = run({"a": i, "b": 0, "c": 1, "d": 0}, code)
        if all(a != b for a, b in zip(val, val[1:])):
            return i


def parse(data: str):
    return [line.split() for line in data.splitlines()]


def run(regs: dict[str, int], code: list[tuple[str, ...]]):
    ip = 0
    max_ip = len(code)
    buf = []
    while 0 <= ip < max_ip:
        match code[ip]:
            case "cpy", x, y:
                regs[y] = get(regs, x)
            case "inc", x:
                regs[x] += 1
            case "dec", x:
                regs[x] -= 1
            case "jnz", x, y:
                ip += (get(regs, y) - 1) * (get(regs, x) != 0)
            case "out", x:
                buf.append(get(regs, x))
                if len(buf) > 25:
                    return buf
            case _:
                raise ValueError(code[ip])
        ip += 1
    return regs


def get(regs: dict[str, int], x):
    try:
        return regs[x]
    except KeyError:
        return int(x)


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
