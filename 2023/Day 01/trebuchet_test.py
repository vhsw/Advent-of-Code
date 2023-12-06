"""Day 1: tests"""
from trebuchet import DATA, part1, part2

EXAMPLE = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
""".strip()
EXAMPLE_2 = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 142
    assert part1(DATA) == 55090


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE_2) == 281
    assert part2(DATA) == 54845
