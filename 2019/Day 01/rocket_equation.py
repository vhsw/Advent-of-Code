def just_fuel(mass):
    return mass // 3 - 2


def total_fuel(mass):
    added_mass = just_fuel(mass)
    # print(added_mass)
    if added_mass > 0:
        return added_mass + total_fuel(added_mass)
    return 0


if __name__ == "__main__":
    with open("input", "r") as f:
        print(f"Part 1: {sum(just_fuel(int(mass)) for mass in f)}")
    with open("input", "r") as f:
        print(f"Part 1: {sum(total_fuel(int(mass)) for mass in f)}")
