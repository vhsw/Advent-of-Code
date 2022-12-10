"""Day 10: Cathode-Ray Tube"""


with open("2022/Day 10/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    reg_x = 1
    sample_it = get_sample_cycle()
    sample_cycle = next(sample_it)
    feed = parse(data)
    total = 0
    cycle = 0
    ip = 0
    skip = 0
    reg_x_buf = 0
    while True:
        cycle += 1
        if cycle == sample_cycle:
            total += cycle * reg_x
            sample_cycle = next(sample_it)
        if skip:
            skip -= 1
            reg_x += reg_x_buf
            continue
        if ip >= len(feed):
            break
        instr, val = feed[ip]
        ip += 1
        if instr == "addx":
            reg_x_buf = val
            skip = 1

    return total


def part2(data: str):
    """Part 2 solution"""
    reg_x = 1
    feed = parse(data)
    cycle = 0
    ip = 0
    skip = 0
    reg_x_buf = 0
    screen = []
    while True:
        if cycle % 40 == 0:
            screen.append("")
        if reg_x - 1 <= cycle % 40 <= reg_x + 1:
            screen[-1] = screen[-1] + "#"
        else:
            screen[-1] = screen[-1] + "."

        cycle += 1
        if skip:
            skip -= 1
            reg_x += reg_x_buf
            continue
        if ip >= len(feed):
            break
        instr, val = feed[ip]
        ip += 1
        if instr == "addx":
            reg_x_buf = val
            skip = 1
    return "\n".join(screen[:-1])


def parse(data: str):
    result = []
    for line in data.splitlines():
        if line == "noop":
            result.append((line, 0))
            continue
        instr, val = line.split()
        result.append((instr, int(val)))
    return result


def get_sample_cycle():
    cycle = 20
    while True:
        yield cycle
        cycle += 40


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
