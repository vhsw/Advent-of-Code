"""Day 15: tests"""
from dueling_generators import DATA, part1, part2

EXAMPLE = """
Generator A starts with 65
Generator B starts with 8921
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 588
    assert part1(DATA) == 569


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 309
    assert part2(DATA) == 298
