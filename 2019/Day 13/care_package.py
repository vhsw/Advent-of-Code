"""Day 13 Answers"""
import curses


from intcode_v13 import Intcode

INPUT = "2019/Day 13/input"


def grouper(n, iterable):
    "grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip(*args)


def part1():
    """Part 1 answer"""
    with open(INPUT) as data:
        data = data.read().strip().split(",")
    code = [int(d) for d in data]
    ic = Intcode(code)
    ic.evaluate()
    display = {(x, y): tile for x, y, tile in grouper(3, ic.output_data)}
    return list(display.values()).count(2)


def part2(stdscr):
    """Part 2 answer"""
    with open(INPUT) as data:
        data = data.read().strip().split(",")
    code = [int(d) for d in data]
    code[0] = 2
    ic = Intcode(code, stdscr)
    ic.evaluate()
    return ic.score


if __name__ == "__main__":
    ANSWER1 = part1()
    # print(f"Part 1: {ANSWER1}")
    try:
        STDSCR = curses.initscr()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)
        STDSCR.leaveok(True)
        ANSWER2 = part2(STDSCR)
        # print(f"Part 2: {ANSWER2}")

    except KeyboardInterrupt:
        pass
    curses.endwin()
    # print(f"Part 2: {ANSWER2}")
