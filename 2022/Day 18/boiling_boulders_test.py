"""Day 18: tests"""
from boiling_boulders import DATA, part1, part2

EXAMPLE = """
2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1("1,1,1\n2,1,1") == 10
    assert part1(EXAMPLE) == 64
    assert part1(DATA) == 4282


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 58
    assert part2(DATA) == 2452
