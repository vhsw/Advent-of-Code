"""Day 3: tests"""
from binary_diagnostic import DATA, co2_bit_criteria, oxygen_bit_criteria, part1, part2

EXAMPLE = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 198
    assert part1(DATA) == 1458194


def test_part2():
    """Part 2 test"""
    assert oxygen_bit_criteria(EXAMPLE) == 23
    assert co2_bit_criteria(EXAMPLE) == 10
    assert part2(EXAMPLE) == 230
    assert part2(DATA) == 2829354
