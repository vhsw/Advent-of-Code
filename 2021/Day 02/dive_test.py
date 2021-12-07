"""Day 2: tests"""
from dive import DATA, part1, part2

EXAMPLE = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 150
    assert part1(DATA) == 2120749


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 900
    assert part2(DATA) == 2138382217
