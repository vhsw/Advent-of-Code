"""Day 11: tests"""
from hex_ed import DATA, part1, part2


def test_part1():
    """Part 1 test"""

    assert part1("n,nw,sw,s,se,ne") == 0
    assert part1("ne,ne,ne") == 3
    assert part1("ne,ne,sw,sw") == 0
    assert part1("ne,ne,s,s") == 2
    assert part1("se,sw,se,sw,sw") == 3
    assert part1(DATA) == 812


def test_part2():
    assert part2(DATA) == 1603
