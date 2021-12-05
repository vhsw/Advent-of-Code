"""Day 10: tests"""
from knot_hash import DATA, condense, part1, part2, to_hex_str


def test_part1():
    """Part 1 test"""
    assert part1("3,4,1,5", size=5) == 12
    assert part1(DATA) == 11413


def test_condense():
    condensed = condense([65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22] * 16)
    assert list(condensed) == [64] * 16


def test_to_hex_str():
    assert to_hex_str([64, 7, 255]) == "4007ff"


def test_part2():
    """Part 2 test"""
    assert part2("") == "a2582a3a0e66e6e86e3812dcb672a272"
    assert part2("AoC 2017") == "33efeb34ea91902bb2f59c9920caa6cd"
    assert part2("1,2,3") == "3efbe78a8d82f29979031a4aa0b16a9d"
    assert part2("1,2,4") == "63960835bcdc130f0b66d7ff4f6a5a8e"
    assert part2(DATA) == "7adfd64c2a03a4968cf708d1b7fd418d"
