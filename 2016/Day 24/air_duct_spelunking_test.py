"""Day 24: tests"""
from air_duct_spelunking import DATA, part1, part2

EXAMPLE = """
###########
#0.1.....2#
#.#######.#
#4.......3#
###########
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 14
    assert part1(DATA) == 464


def test_part2():
    """Part 2 test"""
    assert part2(DATA) == 0
