"""Day 13: tests"""
from packet_scanners import DATA, part1, part2, scanner_posititon


def test_get_scanner_position():
    assert scanner_posititon(3, 0) == 0
    assert scanner_posititon(3, 1) == 1
    assert scanner_posititon(3, 2) == 2
    assert scanner_posititon(3, 3) == 1
    assert scanner_posititon(3, 4) == 0

    assert scanner_posititon(2, 0) == 0
    assert scanner_posititon(2, 1) == 1
    assert scanner_posititon(2, 2) == 0
    assert scanner_posititon(2, 3) == 1

    assert scanner_posititon(4, 3) == 3
    assert scanner_posititon(4, 4) == 2
    assert scanner_posititon(4, 5) == 1
    assert scanner_posititon(4, 6) == 0


EXAMPLE = """
0: 3
1: 2
4: 4
6: 4
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 24
    assert part1(DATA) == 1840


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 10
    assert part2(DATA) == 3850260
