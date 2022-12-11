"""Day 11: tests"""
from monkey_in_the_middle import DATA, part1, part2

EXAMPLE = """
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 10605
    assert part1(DATA) == 120384


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 2713310158
    assert part2(DATA) == 32059801242
