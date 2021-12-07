"""Day 7: tests"""
from the_treachery_of_whales import DATA, cost, part1, part2

EXAMPLE = "16,1,2,0,4,2,7,1,2,14"


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 37
    assert part1(DATA) == 355592


def test_cost():
    assert cost(16, 5) == 66
    assert cost(1, 5) == 10


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 168
    assert part2(DATA) == 101618069
