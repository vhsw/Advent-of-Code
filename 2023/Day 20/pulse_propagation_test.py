"""Day 20: tests"""
from pulse_propagation import DATA, part1, part2

EXAMPLE = """
broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
""".strip()

MORE_INTERESTING_EXAMPLE = """
broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 32000000
    assert part1(MORE_INTERESTING_EXAMPLE) == 11687500
    assert part1(DATA) == 739960225


def test_part2():
    """Part 2 test"""
    assert part2(DATA) == 231897990075517
