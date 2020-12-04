"Day 04 answers"
import re

INPUT = "2020/Day 04/input.txt"


def part1(data):
    "Part 1 answer"
    items = data.split("\n\n")
    fields = "ecl: pid: eyr: hcl: byr: iyr: hgt:".split(": ")

    return sum(all(f in i for f in fields) for i in items)


def part2(data):
    "Part 2 answer"
    items = data.split("\n\n")
    s = 0
    for i in items:
        i = " " + i.replace("\n", " ") + " "
        if m := re.search(r"\sbyr:(\d{4})\s", i):
            if not 1920 <= int(m.group(1)) <= 2002:
                continue
        else:
            continue
        if m := re.search(r"\siyr:(\d{4})\s", i):
            if not 2010 <= int(m.group(1)) <= 2020:
                continue
        else:
            continue
        if m := re.search(r"\seyr:(\d{4})\s", i):
            if not 2020 <= int(m.group(1)) <= 2030:
                continue
        else:
            continue
        if m := re.search(r"\shgt:(\d{2,3})(cm|in)\s", i):
            v, u = m.groups()
            if u == "cm":
                if not (150 <= int(v) <= 193):
                    continue
            if u == "in":
                if not (59 <= int(v) <= 76 and u == "in"):
                    continue
        else:
            continue
        if not re.search(r"\shcl:#[0-9a-f]{6}\s", i):
            continue
        if not re.search(r"\secl:(amb|blu|brn|gry|grn|hzl|oth)\s", i):
            continue
        if not re.search(r"\spid:\d{9}\s", i):
            continue
        s += 1

    return s


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.read()
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
