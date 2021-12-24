"""Day 23: tests"""
from amphipod import DATA, part1, part2

EXAMPLE = """
#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 12521
    assert part1(DATA) == 10321


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 44169
    assert part2(DATA) == 46451
