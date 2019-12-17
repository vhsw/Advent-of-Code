"""Day 17 Answers"""
from typing import NamedTuple, List
from itertools import dropwhile

from intcode_v17 import Intcode


INPUT = "2019/Day 17/input"


class Vec(NamedTuple):
    """2D Point"""

    x: int
    y: int

    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)

    def rot_left(self):
        return Vec(-self.y, self.x)

    def rot_right(self):
        return Vec(self.y, -self.x)


def get_field(code: List[int]) -> List[str]:
    ic = Intcode(code)
    output = ic.evaluate()
    scafold = "".join(chr(i) for i in output)
    return scafold.strip().splitlines()


def raw_instructions(lines: List[str]) -> List[str]:
    field = set()
    for line, row in enumerate(lines):
        for col, char in enumerate(row):
            if char == "^":
                pos = Vec(line, col)
            if char in "^#":
                field.add(Vec(line, col))
    direct = Vec(-1, 0)
    instructions: List[str] = []
    while True:
        forward = pos + direct
        left = pos + direct.rot_left()
        right = pos + direct.rot_right()

        if forward in field:
            if instructions and instructions[-1].isdigit():
                num = int(instructions[-1])
                num += 1
                instructions[-1] = str(num)
            else:
                instructions.append("1")
            pos = forward
        elif left in field:
            instructions.append("L")
            direct = direct.rot_left()

        elif right in field:
            instructions.append("R")
            direct = direct.rot_right()
        else:
            return instructions


def join(lst):
    return ",".join(lst)


def count(hey, needle):
    shey = join(hey)
    sneedle = join(needle)
    return shey.count(sneedle)


def replace(hey, needle, repl):
    shey = join(hey)
    sneedle = join(needle)
    shey = shey.replace(sneedle, repl)

    return shey.split(",")


def simplify(commands: List[str], repl):
    window: List[str] = []
    for c in dropwhile("ABC".__contains__, commands):
        new_window = window + [c]
        new_occur = count(commands, new_window)
        if c not in "ABC" and len(join(new_window)) <= 20 and new_occur >= 3:
            window = new_window
        else:
            break
    if not window:
        window = [c for c in commands if c not in "ABC"]
    return ",".join(window), replace(commands, window, repl)


def part1():
    """Part 1 answer"""
    with open(INPUT) as data:
        data = data.read().strip().split(",")
    code = [int(d) for d in data]
    sf = get_field(code)
    intersections = set()
    for line, (up, mid, dn) in enumerate(zip(sf, sf[1:], sf[2:]), start=1):
        for col in range(1, len(mid) - 1):
            if up[col] == "#" and dn[col] == "#":
                if mid[col - 1 : col + 2] == "###":
                    intersections.add(line * col)
    return sum(intersections)


def part2():
    """Part 2 answer"""
    with open(INPUT) as data:
        data = data.read().strip().split(",")
    code = [int(d) for d in data]
    text_field = get_field(code)
    instructions = raw_instructions(text_field)
    A, instructions = simplify(instructions, "A")
    B, instructions = simplify(instructions, "B")
    C, instructions = simplify(instructions, "C")
    main_routine = ",".join(instructions) + "\n"
    movement_functions = "\n".join([A, B, C]) + "\n"
    input_data = main_routine + movement_functions + "n\n"
    assert code[0] == 1
    code[0] = 2
    ic = Intcode(code)
    result = ic.evaluate([ord(c) for c in input_data])
    return result[-1]


if __name__ == "__main__":
    ANSWER1 = part1()
    print(f"Part 1: {ANSWER1}")
    ANSWER2 = part2()
    print(f"Part 2: {ANSWER2}")
