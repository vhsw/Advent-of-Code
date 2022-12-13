"""Day 13: tests"""
from distress_signal import DATA, part1, part2

EXAMPLE = """
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 13
    assert part1(DATA) == 5350


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 140
    assert part2(DATA) == 19570
