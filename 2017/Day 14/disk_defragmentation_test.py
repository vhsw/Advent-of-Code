"""Day 14: tests"""
from disk_defragmentation import DATA, part1, part2

EXAMPLE = "flqrgnkx"


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 8108
    assert part1(DATA) == 8140


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 1242
    assert part2(DATA) == 1182
