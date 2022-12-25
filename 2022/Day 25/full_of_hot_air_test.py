"""Day 25: tests"""
import pytest
from full_of_hot_air import DATA, make_snafu, parse_snafu, part1, part2

EXAMPLE = """
1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122
""".strip()

test_data = """
        1              1
        2              2
        3             1=
        4             1-
        5             10
        6             11
        7             12
        8             2=
        9             2-
       10             20
       15            1=0
       20            1-0
     2022         1=11-2
    12345        1-0---0
314159265  1121-1110-1=0
""".strip().splitlines()


@pytest.mark.parametrize("line", test_data)
def test_parse_snafu(line: str):
    line = line.strip()
    decimal, snafu = line.split()
    assert parse_snafu(snafu) == int(decimal)


@pytest.mark.parametrize("line", test_data)
def test_make_snafu(line: str):
    line = line.strip()
    decimal, snafu = line.split()
    assert make_snafu(int(decimal)) == snafu


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == "2=-1=0"
    assert part1(DATA) == "2=2-1-010==-0-1-=--2"


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 0
    assert part2(DATA) == 0
