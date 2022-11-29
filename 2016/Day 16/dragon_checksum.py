"""Day 16: Dragon Checksum"""
with open("2016/Day 16/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str, size=272):
    """Part 1 solution"""
    data = fill(data, size)
    return checksum(data)


def part2(data: str):
    """Part 2 solution"""
    return part1(data, size=35651584)


def expand(data: str):
    orz = ord("0")
    oro = ord("1")
    part_b = data[::-1].translate({oro: orz, orz: oro})
    return f"{data}0{part_b}"


def fill(data: str, size: int):
    while len(data) < size:
        data = expand(data)
    return data[:size]


def collapse(data: str):
    return "".join(
        "1" if data[idx] == data[idx + 1] else "0" for idx in range(0, len(data), 2)
    )


def checksum(data: str):
    while len(data) % 2 == 0:
        data = collapse(data)
    return data


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
