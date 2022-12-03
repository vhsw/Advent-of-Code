"""Day 3: tests"""
from rucksack_reorganization import DATA, part1, part2

EXAMPLE = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 157
    assert part1(DATA) == 7428


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 70
    assert part2(DATA) == 2650
