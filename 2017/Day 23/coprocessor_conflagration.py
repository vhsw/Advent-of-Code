"""Day 23: Coprocessor Conflagration"""
from string import ascii_lowercase

with open("2017/Day 23/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    reg = {l: 0 for l in ascii_lowercase[:8]}

    def value(arg: str):
        if arg.isalpha():
            return reg[arg]
        return int(arg)

    feed = data.splitlines()
    ip = 0
    mults = 0
    while ip < len(feed):
        op, X, Y = feed[ip].split()
        match op:
            case "set":
                reg[X] = value(Y)
            case "sub":
                reg[X] -= value(Y)
            case "mul":
                reg[X] *= value(Y)
                mults += 1
            case "jnz":
                if value(X) != 0:
                    ip += value(Y) - 1
            case unknown:
                raise ValueError(unknown)
        ip += 1
    return mults


def part2(data: str):
    """Part 2 solution"""
    reg = {l: 0 for l in ascii_lowercase[:8]}

    def value(arg: str):
        if arg.isalpha():
            return reg[arg]
        return int(arg)

    reg["a"] = 1
    feed = data.splitlines()
    ip = 0
    while ip < len(feed):
        op, X, Y = feed[ip].split()
        if feed[ip] == "set d 2":
            if is_prime(reg["b"]):
                ip = 30
            else:
                ip = 25
            continue
        match op:
            case "set":
                reg[X] = value(Y)
            case "sub":
                reg[X] -= value(Y)
            case "mul":
                reg[X] *= value(Y)
            case "jnz":
                if value(X) != 0:
                    ip += value(Y) - 1
            case unknown:
                raise ValueError(unknown)
        ip += 1
    return reg["h"]


def is_prime(n: int):
    return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
