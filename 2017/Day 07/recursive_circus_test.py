"""Day 7: tests"""
from recursive_circus import DATA, get_balance, part1, part2

EXAMPLE = """
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == "tknk"
    assert part1(DATA) == "ahnofa"


def test_part2():
    """Part 2 test"""
    assert get_balance((1, 1, 0, 1)) == (0, 1)
    assert part2(EXAMPLE) == 60
    assert part2(DATA) == 802
