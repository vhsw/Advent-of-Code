"""Day 16: tests"""
from dragon_checksum import DATA, expand, part1, part2

EXAMPLE = "10000"


def test_expand():
    assert expand("1") == "100"
    assert expand("0") == "001"
    assert expand("11111") == "11111000000"
    assert expand("111100001010") == "1111000010100101011110000"


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE, size=20) == "01100"
    assert part1(DATA) == "11111000111110000"


def test_part2():
    """Part 2 test"""
    assert part2(DATA) == "10111100110110100"
