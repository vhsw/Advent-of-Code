"""Day 4 Answers"""


def valid(password):
    if not any(password.count(str(d)) >= 2 for d in range(10)):
        return False
    if sorted(password) != list(password):
        return False
    return True


def valid2(password):
    if not any(password.count(str(d)) == 2 for d in range(10)):
        return False
    if sorted(password) != list(password):
        return False
    return True


INPUT = "2019/Day 04/input"


def part1():
    with open(INPUT) as data:
        low, high = map(int, data.read().split("-"))
    return sum(valid(str(digs)) for digs in range(low, high))


def part2():
    with open(INPUT) as data:
        low, high = map(int, data.read().split("-"))
    return sum(valid2(str(digs)) for digs in range(low, high))


if __name__ == "__main__":
    ANSWER1 = part1()
    print(f"Part 1: {ANSWER1}")
    ANSWER2 = part2()
    print(f"Part 2: {ANSWER2}")
