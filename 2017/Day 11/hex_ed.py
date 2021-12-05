"""Day 11: Hex Ed"""

with open("2017/Day 11/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    pos = 0j
    for mov in data.split(","):
        match mov:
            case "n":
                pos -= 1
            case "s":
                pos += 1
            case "nw":
                pos -= 1j
            case "se":
                pos += 1j
            case "ne":
                pos -= 1-1j
            case "sw":
                pos += 1-1j

    return distance(pos)


def part2(data: str):
    """Part 2 solution"""
    max_dist = 0
    pos = 0j
    for mov in data.split(","):
        match mov:
            case "n":
                pos -= 1
            case "s":
                pos += 1
            case "nw":
                pos -= 1j
            case "se":
                pos += 1j
            case "ne":
                pos -= 1-1j
            case "sw":
                pos += 1-1j
        max_dist = max(max_dist, distance(pos))

    return max_dist

def distance(pos: complex):
    r = pos.real
    q = pos.imag
    s = -pos.imag-pos.real
    return int(max(map(abs, [r,q,s])))


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
