"""Day 14: tests"""
from extended_polymerization import DATA, part1, part2

EXAMPLE = """
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 1588
    assert part1(DATA) == 3143


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 2188189693529
    assert part2(DATA) == 4110215602456
