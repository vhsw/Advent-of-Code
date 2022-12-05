"""Day 5: tests"""
from supply_stacks import DATA, part1, part2

EXAMPLE = """
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
""".strip(
    "\n"
)


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == "CMZ"
    assert part1(DATA) == "ZWHVFWQWW"


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == "MCD"
    assert part2(DATA) == "HZFZCCWWV"
