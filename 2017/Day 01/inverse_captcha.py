"""Day 1: Inverse Captcha"""
with open("2017/Day 01/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    digits = list(map(int, data))
    digits += [digits[0]]
    return sum(c for c, n in zip(digits, digits[1:]) if c == n)


def part2(data: str):
    """Part 2 solution"""
    digits = list(map(int, data))
    length = len(digits)
    total = 0
    for idx, digit in enumerate(digits):
        offset = (idx + length // 2) % length
        if digit == digits[offset]:
            total += digit
    return total


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
