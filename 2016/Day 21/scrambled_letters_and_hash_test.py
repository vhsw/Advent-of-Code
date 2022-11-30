"""Day 21: tests"""
import pytest
from scrambled_letters_and_hash import DATA, part1, part2

EXAMPLE = """
swap position 4 with position 0
swap letter d with letter b
reverse positions 0 through 4
rotate left 1 step
move position 1 to position 4
move position 3 to position 0
rotate based on position of letter b
rotate based on position of letter d
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE, start="abcde") == "decab"
    assert part1(DATA) == "agcebfdh"


@pytest.mark.parametrize(
    "start",
    [
        "b_______",
        "_b______",
        "__b_____",
        "___b____",
        "____b___",
        "_____b__",
        "______b_",
        "_______b",
    ],
)
def test_rotate(start):
    end = part1("rotate based on position of letter b", start)
    assert part2("rotate based on position of letter b", end) == start


def test_part2_short():
    assert part2(EXAMPLE, end="decab") == "abcde"


def test_part2_long():
    assert part2(DATA, end="agcebfdh") == "abcdefgh"


def test_part2():
    """Part 2 test"""
    assert part2(DATA) == "afhdbegc"
