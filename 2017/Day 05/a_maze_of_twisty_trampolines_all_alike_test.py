"""Day 5: tests"""
from a_maze_of_twisty_trampolines_all_alike import DATA, part1, part2


def test_part1():
    """Part 1 test"""

    assert part1([0, 3, 0, 1, -3]) == 5
    assert part1(DATA) == 396086


def test_part2():
    """Part 2 test"""
    assert part2([0, 3, 0, 1, -3]) == 10
    assert part2(DATA) == 28675390
