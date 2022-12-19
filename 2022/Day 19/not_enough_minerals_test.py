"""Day 19: tests"""
from not_enough_minerals import DATA, part1, part2

EXAMPLE = """Blueprint 1:
  Each ore robot costs 4 ore.
  Each clay robot costs 2 ore.
  Each obsidian robot costs 3 ore and 14 clay.
  Each geode robot costs 2 ore and 7 obsidian.

Blueprint 2:
  Each ore robot costs 2 ore.
  Each clay robot costs 3 ore.
  Each obsidian robot costs 3 ore and 8 clay.
  Each geode robot costs 3 ore and 12 obsidian.
""".strip()

EXAMPLE = EXAMPLE.replace("\n  ", " ").replace("\n\n", "\n").strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 33
    assert part1(DATA) == 1589


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 56 * 62
    assert part2(DATA) == 29348
