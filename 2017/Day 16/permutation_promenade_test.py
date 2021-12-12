"""Day 16: tests"""
from permutation_promenade import DATA, part1, part2

EXAMPLE = "s1,x3/4,pe/b"


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE, size=5) == "baedc"
    assert part1(DATA) == "giadhmkpcnbfjelo"


def test_part2():
    """Part 2 test"""
    assert part2(DATA) == "njfgilbkcoemhpad"
