"""Day 8: tests"""
from treetop_tree_house import DATA, part1, part2

EXAMPLE = """
30373
25512
65332
33549
35390
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 21
    assert part1(DATA) == 1859


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 8
    assert part2(DATA) == 332640
