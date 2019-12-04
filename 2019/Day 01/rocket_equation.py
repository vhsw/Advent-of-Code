"""Day 1 Answers"""


def just_fuel(mass):
    """Return mass of fuel for given module mass"""
    return mass // 3 - 2


def total_fuel(mass):
    """Return mass of fuel for given module ajusted for fuel mass"""
    added_mass = just_fuel(mass)
    if added_mass > 0:
        return added_mass + total_fuel(added_mass)
    return 0


INPUT = "2019/Day 01/input"


def part1():
    """Part 1 answer"""
    with open(INPUT) as data:
        return sum(just_fuel(int(mass)) for mass in data)


def part2():
    """Part 2 answer"""
    with open(INPUT) as data:
        return sum(total_fuel(int(mass)) for mass in data)


if __name__ == "__main__":
    ANSWER1 = part1()
    print(f"Part 1: {ANSWER1}")
    ANSWER2 = part2()
    print(f"Part 2: {ANSWER2}")
