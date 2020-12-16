"Day 05 answers"
from hashlib import md5

INPUT = "2016/Day 05/input.txt"


def part1(prefix):
    "Part 1 answer"
    i = 0
    password = ""
    for _ in range(8):
        while not (
            digset := md5((prefix + str(i)).encode("utf-8")).hexdigest()
        ).startswith("0" * 5):
            i += 1
        i += 1
        password += digset[5]
    return password


def part2(prefix):
    "Part 2 answer"
    i = 0
    password = ["#"] * 8
    while "#" in password:
        while not (
            digset := md5((prefix + str(i)).encode("utf-8")).hexdigest()
        ).startswith("0" * 5):
            i += 1
        i += 1
        idx = int(digset[5], 16)
        if idx < 8 and password[idx] == "#":
            password[idx] = digset[6]
    return "".join(password)


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.read().strip()
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
