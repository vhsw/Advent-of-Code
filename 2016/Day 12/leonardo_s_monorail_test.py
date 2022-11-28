"""Day 12: tests"""
from leonardo_s_monorail import DATA, part1, part2

EXAMPLE = """
cpy 41 a
inc a
inc a
dec a
jnz a 2
dec a
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 42
    assert part1(DATA) == 318007


def test_part2():
    """Part 2 test"""
    assert part2(DATA) == 9227661
