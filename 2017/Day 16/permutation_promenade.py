"""Day 16: Permutation Promenade"""
from string import ascii_lowercase

with open("2017/Day 16/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str, size=16):
    """Part 1 solution"""
    programs = list(ascii_lowercase[:size])
    execute(data.split(","), programs)
    return "".join(programs)


def part2(data: str, size=16):
    """Part 2 solution"""
    programs = list(ascii_lowercase[:size])
    cmds = data.split(",")
    seen = [programs.copy()]
    while True:
        execute(cmds, programs)
        if programs in seen:
            break
        seen.append(programs.copy())

    return "".join(seen[1000000000 % len(seen)])


def execute(cmds, programs):
    for cmd in cmds:
        match cmd[0]:
            case "s":
                dist = -int(cmd[1:])
                programs[:] = programs[dist:] + programs[:dist]
            case "x":
                pos_a, pos_b = map(int, cmd[1:].split("/"))
                programs[pos_a], programs[pos_b] = programs[pos_b], programs[pos_a]
            case "p":
                pos_a, pos_b = map(programs.index, cmd[1:].split("/"))
                programs[pos_a], programs[pos_b] = programs[pos_b], programs[pos_a]


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
