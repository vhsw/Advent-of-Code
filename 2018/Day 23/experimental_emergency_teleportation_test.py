"""Day 23: tests"""
from experimental_emergency_teleportation import DATA, part1, part2

EXAMPLE = """
pos=<0,0,0>, r=4
pos=<1,0,0>, r=1
pos=<4,0,0>, r=3
pos=<0,2,0>, r=1
pos=<0,5,0>, r=3
pos=<0,0,3>, r=1
pos=<1,1,1>, r=1
pos=<1,1,2>, r=1
pos=<1,3,1>, r=1
""".strip()

EXAMPLE_2 = """
pos=<10,12,12>, r=2
pos=<12,14,12>, r=2
pos=<16,12,12>, r=4
pos=<14,14,14>, r=6
pos=<50,50,50>, r=200
pos=<10,10,10>, r=5
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 7
    assert part1(DATA) == 408


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE_2) == 36
    assert part2(DATA) == 0
