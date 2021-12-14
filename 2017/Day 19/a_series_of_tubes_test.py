"""Day 19: tests"""
from a_series_of_tubes import DATA, part1, part2

EXAMPLE = """
     |
     |  +--+
     A  |  C
 F---|----E|--+
     |  |  |  D
     +B-+  +--+
""".strip(
    "\n"
)


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == "ABCDEF"
    assert part1(DATA) == "RYLONKEWB"


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 38
    assert part2(DATA) == 16016
