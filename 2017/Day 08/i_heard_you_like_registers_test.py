"""Day 8: tests"""
from i_heard_you_like_registers import DATA, part1, part2

EXAMPLE = """
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 1
    assert part1(DATA) == 5946


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 10
    assert part2(DATA) == 6026
