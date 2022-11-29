"""Day 18: tests"""
from like_a_rogue import DATA, part1, part2


def test_part1():
    """Part 1 test"""
    assert part1("..^^.", size=3) == 6
    assert part1(".^^.^.^^^^", size=10) == 38
    assert part1(DATA) == 2016


def test_part2():
    """Part 2 test"""
    assert part2(DATA) == 19998750
