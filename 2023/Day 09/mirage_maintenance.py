"""Day 9: Mirage Maintenance"""

with open("2023/Day 09/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    return sum(map(find_next, parse(data)))


def part2(data: str):
    """Part 2 solution"""
    return sum(map(find_prev, parse(data)))


def parse(data: str):
    for line in data.splitlines():
        yield list(map(int, line.split()))


def find_next(row: list[int]):
    end = 0
    while True:
        end += row[-1]
        d_row = deriv(row)
        if not any(d_row):
            break
        row = d_row

    return end


def find_prev(row: list[int]):
    starts = []
    while True:
        starts.append(row[0])
        d_row = deriv(row)
        if not any(d_row):
            starts.append(0)
            break
        row = d_row
    k = 0
    for n0 in starts[::-1]:
        k = n0 - k
    return k


def deriv(row: list[int]):
    return [b - a for a, b in zip(row, row[1:])]


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
