"""Day 6: tests"""
from lanternfish import DATA, evolve, parse, part1, part2

EXAMPLE = "3,4,3,1,2"


def test_parse():
    assert parse(EXAMPLE) == [0, 1, 1, 2, 1, 0, 0, 0, 0]


def test_part1():
    """Part 1 test"""
    state = parse(EXAMPLE)
    assert evolve(state, days=18) == 26
    assert evolve(state, days=80) == 5934
    assert part1(DATA) == 362666


def test_part2():
    """Part 2 test"""
    state = parse(EXAMPLE)
    assert evolve(state, days=256) == 26984457539
    assert part2(DATA) == 1640526601595
