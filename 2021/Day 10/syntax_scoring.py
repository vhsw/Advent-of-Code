"""Day 10: Syntax Scoring"""
with open("2021/Day 10/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""

    score = 0
    for line in data.splitlines():
        try:
            autocomplete(line)
        except ValueError as ex:
            score += score_illigal(ex.args[0])
    return score


def part2(data: str):
    """Part 2 solution"""
    scores = []
    for line in data.splitlines():
        try:
            completion = autocomplete(line)
            scores.append(score_completion(completion))
        except ValueError:
            pass
    return sorted(scores)[len(scores) // 2]


def autocomplete(line):
    openings = {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">",
    }
    expected = []
    for char in line:
        if char in openings:
            expected.append(openings[char])
        elif char == expected[-1]:
            expected.pop()
        else:
            raise ValueError(char)
    return reversed(expected)


def score_illigal(char):
    return {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137,
    }[char]


def score_completion(line):
    scores = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }
    score = 0
    for char in line:
        score *= 5
        score += scores[char]
    return score


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
