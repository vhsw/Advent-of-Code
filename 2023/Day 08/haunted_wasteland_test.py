"""Day 8: tests"""
from haunted_wasteland import DATA, part1, part2

EXAMPLE_2 = """
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
""".strip()

EXAMPLE_6 = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
""".strip()

GHOST_EXAMPLE = """
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE_2) == 2
    assert part1(EXAMPLE_6) == 6
    assert part1(DATA) == 19783


def test_part2():
    """Part 2 test"""
    assert part2(GHOST_EXAMPLE) == 6
    assert part2(DATA) == 9177460370549
