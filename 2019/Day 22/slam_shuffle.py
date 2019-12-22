"""Day 22 Answers"""
from collections import deque

INPUT = "2019/Day 22/input"


def shuffle(commands, deck_size=10007):
    deck = deque(range(deck_size))
    for command in commands:
        if command == "deal into new stack":
            deck.reverse()
        elif command.startswith("cut"):
            n = int(command[4:])
            deck.rotate(-n)
        elif command.startswith("deal with increment"):
            n = int(command[20:])
            lst = [-1] * deck_size
            i = 0
            while deck:
                lst[i] = deck.popleft()
                i = (i + n) % deck_size
            deck = deque(lst)

    return deck


def weird_math_shuffle(commands, MOD=119315717514047):
    offset = 0
    increment = 1
    for command in commands:
        if command == "deal into new stack":
            increment = -increment
            increment %= MOD
            offset += increment
            offset %= MOD
        elif command.startswith("cut"):
            n = int(command[4:])
            offset += increment * n
            offset %= MOD
        elif command.startswith("deal with increment"):
            n = int(command[20:])
            increment *= pow(n, MOD - 2, MOD)
            increment %= MOD
    return offset, increment


def part1():
    """Part 1 answer"""
    with open(INPUT) as fp:
        data = fp.read()
    commands = data.splitlines()
    deck = shuffle(commands)
    return deck.index(2019)


def part2():
    """Part 2 answer"""
    with open(INPUT) as fp:
        data = fp.read()
    commands = data.splitlines()
    offset_dif, incr_mul = weird_math_shuffle(commands)
    MOD = 119315717514047
    iterations = 101741582076661
    increment = pow(incr_mul, iterations, MOD)

    def inv(n):
        return pow(n, MOD - 2, MOD)

    offset = offset_dif * (1 - increment) * inv((1 - incr_mul) % MOD)
    offset %= MOD
    return (offset + 2020 * increment) % MOD


if __name__ == "__main__":
    ANSWER1 = part1()
    print(f"Part 1: {ANSWER1}")
    ANSWER2 = part2()
    print(f"Part 2: {ANSWER2}")
