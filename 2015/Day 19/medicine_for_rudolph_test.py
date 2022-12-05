"""Day 19: tests"""
from medicine_for_rudolph import DATA, part1, part2

EXAMPLE = """
H => HO
H => OH
O => HH

HOH
""".strip()

EXAMPLE_2 = """
e => H
e => O
H => HO
H => OH
O => HH

HOH
""".strip()

EXAMPLE_3 = """
e => H
e => O
H => HO
H => OH
O => HH

HOHOHO
""".strip()

EXAMPLE_4 = """
Al => ThRnFAr
Ca => SiTh
F => SiAl
Th => ThCa
e => HF

HSiThCaRnFAr
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 4
    assert part1(DATA) == 518


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE_2) == 3
    assert part2(EXAMPLE_3) == 6
    assert part2(EXAMPLE_4) == 4
    assert part2(DATA) == 200
