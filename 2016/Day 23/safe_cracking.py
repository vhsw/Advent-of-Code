"""Day 23: Safe Cracking"""
with open("2016/Day 23/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str, reg_a=7):
    """Part 1 solution"""
    code = parse(data)
    return run({"a": reg_a, "b": 0, "c": 1, "d": 0}, code)["a"]


def part2(data: str):
    """Part 2 solution"""
    patch = [
        "cpy c a",
        "mul d a",
        "nop",
        "nop",
        "nop",
    ]
    code = data.splitlines()
    code = code[:5] + patch + code[10:]
    return part1("\n".join(code), reg_a=12)


def parse(data: str):
    return [line.split() for line in data.splitlines()]


def run(regs: dict[str, int], code: list[tuple[str, ...]]):
    ip = 0
    max_ip = len(code)
    while 0 <= ip < max_ip:
        match code[ip]:
            case "cpy", x, y:
                if y not in regs:
                    ip += 1
                    continue
                regs[y] = get(regs, x)
            case "inc", x:
                if x not in regs:
                    ip += 1
                    continue
                regs[x] += 1
            case "dec", x:
                if x not in regs:
                    ip += 1
                    continue
                regs[x] -= 1
            case "jnz", x, y:
                ip += (get(regs, y) - 1) * (get(regs, x) != 0)
            case "tgl", x:
                pos = ip + get(regs, x)
                if pos < 0 or pos >= len(code):
                    ip += 1
                    continue
                instr = code[pos]
                if len(instr) == 2:
                    if instr[0] == "inc":
                        code[pos] = ("dec", instr[1])
                    else:
                        code[pos] = ("inc", instr[1])
                else:
                    if instr[0] == "jnz":
                        code[pos] = ("cpy", *instr[1:])
                    else:
                        code[pos] = ("jnz", *instr[1:])
            case "mul", x, y:
                regs[y] *= get(regs, x)
            case ("nop",):
                pass
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
    # print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
