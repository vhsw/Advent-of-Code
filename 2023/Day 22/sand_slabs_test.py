"""Day 22: tests"""
import pytest
from sand_slabs import DATA, part1, part2

EXAMPLE = """
1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
""".strip()


@pytest.mark.slow
def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 5
    assert part1(DATA) == 391


@pytest.mark.slow
def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 7
    assert part2(DATA) == 69601
