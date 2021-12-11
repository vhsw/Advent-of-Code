"""Day 15: Dueling Generators"""
with open("2017/Day 15/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()

MOD = 2147483647
FACTOR_A = 16807
FACTOR_B = 48271


def part1(data: str):
    """Part 1 solution"""
    gen_a, gen_b = parse(data)
    total = 0
    for _ in range(40_000_000):
        gen_a = (gen_a * FACTOR_A) % MOD
        gen_b = (gen_b * FACTOR_B) % MOD
        if gen_a & 0xFFFF == gen_b & 0xFFFF:
            total += 1
    return total


def part2(data: str):
    """Part 2 solution"""
    gen_a, gen_b = parse(data)
    total = 0
    for _ in range(5_000_000):
        gen_a = (gen_a * FACTOR_A) % MOD
        while gen_a % 4:
            gen_a = (gen_a * FACTOR_A) % MOD
        gen_b = (gen_b * FACTOR_B) % MOD
        while gen_b % 8:
            gen_b = (gen_b * FACTOR_B) % MOD
        if gen_a & 0xFFFF == gen_b & 0xFFFF:
            total += 1
    return total


def parse(data: str):
    line_a, line_b = data.splitlines()
    return int(line_a.split()[-1]), int(line_b.split()[-1])


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
