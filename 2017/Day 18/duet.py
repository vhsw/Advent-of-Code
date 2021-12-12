"""Day 18: Duet"""
from collections import deque
from string import ascii_lowercase

with open("2017/Day 18/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    reg = {l: 0 for l in ascii_lowercase}
    played = None
    feed = data.splitlines()
    ip = 0

    def value(arg: str):
        if arg.isalpha():
            return reg[arg]
        return int(arg)

    while ip < len(feed):
        op, arg, *rest = feed[ip].split()
        match op:
            case "snd":
                played = value(arg)
            case "set":
                reg[arg] = value(rest[0])
            case "add":
                reg[arg] += value(rest[0])
            case "mul":
                reg[arg] *= value(rest[0])
            case "mod":
                reg[arg] %= value(rest[0])
            case "rcv" if arg != "0":
                return played
            case "jgz" if reg[arg] > 0:
                ip += value(rest[0]) - 1
        ip += 1
    return played


def part2(data: str):
    """Part 2 solution"""
    feed = data.splitlines()
    q_0: deque[int] = deque()
    q_1: deque[int] = deque()
    count = 0

    def evaluate(program_id: int, rx: deque[int], tx: deque[int], feed: list[str]):
        nonlocal count
        reg = {l: 0 for l in ascii_lowercase}
        reg["p"] = program_id

        def value(arg: str):
            if arg.isalpha():
                return reg[arg]
            return int(arg)

        ip = 0
        while ip < len(feed):
            op, arg, *rest = feed[ip].split()
            match op:
                case "snd":
                    if program_id == 1:
                        count += 1
                    tx.append(value(arg))
                case "set":
                    reg[arg] = value(rest[0])
                case "add":
                    reg[arg] += value(rest[0])
                case "mul":
                    reg[arg] *= value(rest[0])
                case "mod":
                    reg[arg] %= value(rest[0])
                case "rcv" if arg != "0":
                    if not rx:
                        yield "WAIT"
                    val = rx.popleft()
                    reg[arg] = val
                case "jgz" if value(arg) > 0:
                    ip += value(rest[0]) - 1
            ip += 1

    gen_0 = evaluate(0, q_0, q_1, feed)
    gen_1 = evaluate(1, q_1, q_0, feed)
    while True:
        try:
            next(gen_0)
            next(gen_1)
        except IndexError:
            return count


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
