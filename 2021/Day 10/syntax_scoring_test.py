"""Day 10: tests"""
from syntax_scoring import DATA, part1, part2

EXAMPLE = """
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
""".strip()


def test_part1():
    """Part 1 test"""
    assert part1(EXAMPLE) == 26397
    assert part1(DATA) == 413733


def test_part2():
    """Part 2 test"""
    assert part2(EXAMPLE) == 288957
    assert part2(DATA) == 3354640192
