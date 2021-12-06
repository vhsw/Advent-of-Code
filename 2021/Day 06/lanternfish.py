"""Day 6: Lanternfish"""

with open("2021/Day 06/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    return evolve(parse(data), 80)


def part2(data: str):
    """Part 2 solution"""
    return evolve(parse(data), 256)


def parse(data: str):
    state = [0] * 9
    for day in map(int, data.split(",")):
        state[day] += 1
    return state


def evolve(state, days):
    for _ in range(days):
        head, *tail = state
        state = tail + [head]
        state[6] += head
    return sum(state)


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
