"""Day 21: tests"""
from monkey_math import DATA, part1, part2

EXAMPLE = """
root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 152
    assert part1(DATA) == 379578518396784


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 301
    assert part2(DATA) == 3353687996514
