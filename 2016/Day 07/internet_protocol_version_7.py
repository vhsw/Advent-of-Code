"Day 07 answers"
import re

INPUT = "2016/Day 07/input.txt"


def part1(data):
    "Part 1 answer"
    s = 0
    for line in data:
        hypernets = re.findall(r"\[(\w+)\]", line)
        for hypernet in hypernets:
            if m := re.search(r"(\w)(\w)\2\1", hypernet):
                a, b = m.groups()
                if a != b:
                    break
        else:
            for word in re.split(r"\[\w+\]", line):
                if m := re.search(r"(\w)(\w)\2\1", word):
                    a, b = m.groups()
                    if a != b:
                        s += 1
                        break
    return s


def part2(data):
    "Part 2 answer"
    s = 0
    for line in data:
        As = []
        Bs = []
        hypernets = re.findall(r"\[(\w+)\]", line)
        for hypernet in hypernets:
            for i in range(len(hypernet) - 2):
                b, a, c = hypernet[i : i + 3]
                if a != b and b == c:
                    As.append(a)
                    Bs.append(b)
        s += any(
            f"{a}{b}{a}" in word
            for word in re.split(r"\[\w+\]", line)
            for a, b in zip(As, Bs)
        )

    return s


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.read().strip().split()
    DATA1 = """aba[bab]xyz
xyx[xyx]xyx
aaa[kek]eke
zazbz[bzb]cdb""".split()
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
