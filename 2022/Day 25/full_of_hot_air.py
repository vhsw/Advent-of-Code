"""Day 25: Full of Hot Air"""
with open("2022/Day 25/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    nums = parse(data)
    return make_snafu(sum(nums))


def part2(data: str):
    """Part 2 solution"""
    return


def parse(data: str):
    return [parse_snafu(line) for line in data.splitlines()]


def parse_snafu(data: str):
    nums = {
        "2": 2,
        "1": 1,
        "0": 0,
        "-": -1,
        "=": -2,
    }
    result = 0
    for char in data:
        num = nums[char]
        result *= 5
        result += num
    return result


def make_snafu(n: int):
    if n == 0:
        return "0"

    nums = {
        2: "2",
        1: "1",
        0: "0",
        -1: "-",
        -2: "=",
    }
    result = []
    while n:
        d, m = divmod(n, 5)
        if m >= 3:
            result.append(nums[m - 5])
            d += 1
        else:
            result.append(nums[m])

        n = d
    return "".join(result)[::-1]


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
