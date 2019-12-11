"""Day 11 Answers"""
from intcode_v11 import Intcode, InputError

INPUT = "2019/Day 11/input"


def draw_pannels(code, init_color=0):
    ic = Intcode(code)
    pannels = {}
    pos = (0, 0)
    pannels[pos] = init_color
    direction = 0
    try:
        ic.evaluate()
    except InputError:
        pass
    while ic.running:
        color = pannels.get(pos, 0)
        ic.provide_input(color)
        try:
            ic.evaluate()
        except InputError:
            new_color, turn = ic.output_data[-2:]
        pannels[pos] = new_color
        if turn == 0:
            direction += 1
        else:
            direction -= 1
        direction %= 4
        dx, dy = ((1, 0), (0, 1), (-1, 0), (0, -1))[direction]
        x, y = pos
        pos = x + dx, y + dy
    return pannels


def part1():
    """Part 1 answer"""
    with open(INPUT) as data:
        data = data.read().strip().split(",")
    code = [int(d) for d in data]
    pannels = draw_pannels(code, 0)
    return len(pannels)


def part2():
    """Part 2 answer"""
    with open(INPUT) as data:
        data = data.read().strip().split(",")
    code = [int(d) for d in data]
    pannels = draw_pannels(code, 1)
    minx = min(p[0] for p in pannels)
    maxx = max(p[0] for p in pannels)
    miny = min(p[1] for p in pannels)
    maxy = max(p[1] for p in pannels)
    lines = []
    for row in range(maxx, minx - 1, -1):
        line = [" #"[pannels.get((row, col), 0)] for col in range(maxy, miny - 1, -1)]
        lines.append("".join(line))

    return "\n".join(lines)


if __name__ == "__main__":
    ANSWER1 = part1()
    print(f"Part 1: {ANSWER1}")
    ANSWER2 = part2()
    print(f"Part 2:\n{ANSWER2}")
