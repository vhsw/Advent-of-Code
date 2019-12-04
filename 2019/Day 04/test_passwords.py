"""Day 4 Tests"""
import pytest
from passwords import valid, valid2, part1, part2


@pytest.mark.parametrize(
    "pswd, result", [["111111", True], ["223450", False], ["123789", False],]
)
def test_valid(pswd, result):
    assert valid(pswd) is result


@pytest.mark.parametrize(
    "pswd, result", [["112233", True], ["123444", False], ["111122", True],]
)
def test_valid2(pswd, result):
    assert valid2(pswd) is result


def test_parts():
    assert part1() == 1675
    assert part2() == 1142
