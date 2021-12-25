"""Day 25: tests"""
from sea_cucumber import DATA, part1

EXAMPLE = """
v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 58
    assert part1(DATA) == 435
