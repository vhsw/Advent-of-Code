"""Day 2: tests"""
from dive import DATA, part1, part2


def test_part1():
    """Part 1 test"""
    example = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
""".strip().splitlines()
    assert part1(example) == 150
    assert part1(DATA) == 2120749


def test_part2():
    """Part 2 test"""
    example = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
""".strip().splitlines()
    assert part2(example) == 900
    assert part2(DATA) == 2138382217
