"""Day 21: tests"""
from chronal_conversion import DATA, part1, part2

EXAMPLE = """
#ip 0
seti 5 0 1
seti 6 0 2
addi 0 1 0
addr 1 2 3
setr 1 0 0
seti 8 0 4
seti 9 0 5
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(DATA) == 9079325


def test_part2():
    """Part 2 test"""
    # runs 13 minutes
    # assert part2(DATA) == 3715167
