"""Day 23: Coprocessor Conflagration"""
from string import ascii_lowercase

with open("2017/Day 23/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    mults = 0
    reg = {l: 0 for l in ascii_lowercase[:8]}
    feed = data.splitlines()
    ip = 0

    def value(arg: str):
        if arg.isalpha():
            return reg[arg]
        return int(arg)

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

    feed = data.splitlines()
    start = get_int(feed[0])
    start *= get_int(feed[4])
    start -= get_int(feed[5])
    stop = start - get_int(feed[7])
    step = -get_int(feed[30])
    return sum(not is_prime(num) for num in range(start, stop + 1, step))


def get_int(line: str):
    return int(line.split()[2])


def is_prime(n):
    return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
