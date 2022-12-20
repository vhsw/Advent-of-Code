"""Day 20: Grove Positioning System"""

with open("2022/Day 20/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    order = parse(data)
    to_mix = list(enumerate(order))
    mix(to_mix, order)
    return calc_result([n for _, n in to_mix])


def part2(data: str):
    """Part 2 solution"""
    nums = parse(data)
    decryption_key = 811589153
    order = [n * decryption_key for n in nums]
    to_mix = list(enumerate(order))
    for _ in range(10):
        mix(to_mix, order)
    return calc_result([n for _, n in to_mix])


def parse(data: str):
    return list(map(int, data.splitlines()))


def mix(to_mix: list[tuple[int, int]], order: list[int]):
    for idx, n in enumerate(order):
        pos = to_mix.index((idx, n))
        new_pos = pos + n
        new_pos %= len(to_mix) - 1
        val = to_mix.pop(pos)
        to_mix.insert(new_pos, val)


def calc_result(nums: list[int]):
    zero_idx = nums.index(0)

    return (
        nums[(zero_idx + 1000) % len(nums)]
        + nums[(zero_idx + 2000) % len(nums)]
        + nums[(zero_idx + 3000) % len(nums)]
    )


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
