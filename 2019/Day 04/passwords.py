"""Day 4 Answers"""


def valid(password):
    """a few key facts about the password:
    It is a six-digit number.
    The value is within the range given in your puzzle input.
    Two adjacent digits are the same (like 22 in 122345).
    Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679)."""
    if not any(password.count(str(d)) >= 2 for d in range(10)):
        return False
    if sorted(password) != list(password):
        return False
    return True


def valid2(password):
    """one more important detail: the two adjacent matching digits are not part of a larger group of matching digits"""
    if not any(password.count(str(d)) == 2 for d in range(10)):
        return False
    if sorted(password) != list(password):
        return False
    return True


INPUT = "2019/Day 04/input"


def part1():
    """Part 1 answer"""
    with open(INPUT) as data:
        low, high = map(int, data.read().split("-"))
    return sum(valid(str(digs)) for digs in range(low, high))


def part2():
    """Part 2 answer"""
    with open(INPUT) as data:
        low, high = map(int, data.read().split("-"))
    return sum(valid2(str(digs)) for digs in range(low, high))


if __name__ == "__main__":
    ANSWER1 = part1()
    print(f"Part 1: {ANSWER1}")
    ANSWER2 = part2()
    print(f"Part 2: {ANSWER2}")
