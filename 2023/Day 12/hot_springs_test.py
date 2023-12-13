"""Day 12: tests"""
import pytest
from hot_springs import DATA, count_arrangements, parse_line, part1, part2

EXAMPLE = """
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
""".strip()


@pytest.mark.parametrize(
    "line,count",
    [
        ["???.### 1,1,3", 1],
        [".??..??...?##. 1,1,3", 4],
        ["?#?#?#?#?#?#?#? 1,3,1,6", 1],
        ["????.#...#... 4,1,1", 1],
        ["????.######..#####. 1,6,5", 4],
        ["?###???????? 3,2,1", 10],
    ],
)
def test_count_arrangements(line, count):
    assert count_arrangements(*parse_line(line, 1)) == count


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 21
    assert part1(DATA) == 6488


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 525152
    assert part2(DATA) == 815364548481
