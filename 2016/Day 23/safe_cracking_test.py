"""Day 23: tests"""
from safe_cracking import DATA, part1, part2

EXAMPLE = """
cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE, reg_a=0) == 3
    assert part1(DATA) == 14160


def test_part2():
    """Part 2 test"""
    assert part2(DATA) == 479010720
