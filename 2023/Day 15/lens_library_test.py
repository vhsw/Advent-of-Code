"""Day 15: tests"""
from lens_library import DATA, part1, part2

EXAMPLE = """
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 1320
    assert part1(DATA) == 518107


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 145
    assert part2(DATA) == 303404
