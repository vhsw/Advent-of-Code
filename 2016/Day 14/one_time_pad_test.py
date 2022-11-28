"""Day 14: tests"""
from one_time_pad import (
    DATA,
    part1,
    part2,
    hashsum,
    three_in_row,
    has_five_in_row,
    stretched_hashsum,
)

EXAMPLE = "abc"


def test_hashsum():
    assert hashsum(EXAMPLE, 18) == "0034e0923cc38887a57bd7b1d4f953df"


def test_stretched_hashsum():
    assert stretched_hashsum(EXAMPLE, 0) == "a107ff634856bb300138cac6568c0f24"


def test_three_in_row():
    assert three_in_row("333abc") == "3"
    assert three_in_row("333444") == "3"
    assert three_in_row("abc333") == "3"
    assert three_in_row("cc38887a5") == "8"
    assert three_in_row("33abc") is None


def test_has_five_in_row():
    assert has_five_in_row("88888", "7") is False
    assert has_five_in_row("88888", "8")
    assert has_five_in_row("555558888855555", "8")


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 22728
    assert part1(DATA) == 25427


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 22551
    assert part2(DATA) == 22045
