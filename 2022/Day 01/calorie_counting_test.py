"""Day 1: tests"""
from calorie_counting import DATA, part1, part2

EXAMPLE = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 24000
    assert part1(DATA) == 70613


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 45000
    assert part2(DATA) == 205805
