"Day 14 answers"
import re

INPUT = "2020/Day 14/input.txt"


def part1(data):
    "Part 1 answer"
    mask_and = 0
    mask_or = 0
    mem = {}
    for line in data.strip().splitlines():
        if m := re.match(r"mask = ([01X]{36})", line):
            mask = m.group(1)
            mask_and = int(mask.replace("X", "1"), 2)
            mask_or = int(mask.replace("X", "0"), 2)
        elif m := re.match(r"mem\[(\d+)\] = (\d+)", line):
            addr, value = m.groups()
            mem[int(addr)] = int(value) & mask_and | mask_or
        else:
            raise ValueError
    return sum(mem.values())


def part2(data):
    "Part 2 answer"
    mem = {}
    mask = "0" * 36
    for line in data.strip().splitlines():
        if m := re.match(r"mask = ([01X]{36})", line):
            mask = m.group(1)
        elif m := re.match(r"mem\[(\d+)\] = (\d+)", line):
            addr, value = m.groups()
            addr = bin(int(addr))[2:].rjust(36, "0")
            addr_mask = "".join(m if m in "X1" else a for a, m in zip(addr, mask))
            value = int(value)
            Xs = mask.count("X")
            for i in range(2 ** Xs):
                addr = addr_mask
                for d in bin(i)[2:].rjust(Xs, "0"):
                    addr = addr.replace("X", d, 1)
                addr = int(addr)
                mem[addr] = int(value)
        else:
            raise ValueError
    return sum(mem.values())


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.read()
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
