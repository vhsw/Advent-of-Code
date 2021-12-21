"""Day 21: Dirac Dice"""
from collections import Counter
from functools import cache
from itertools import product

with open("2021/Day 21/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    pos = list(parse(data))
    scores = [0, 0]
    player = 0
    dice = 0
    roll = 0
    while scores[0] < 1000 and scores[1] < 1000:
        value = 0
        for _ in range(3):
            value += dice + 1
            dice += 1
            dice %= 100
            roll += 1
        pos[player] += value
        pos[player] %= 10
        scores[player] += pos[player] + 1
        player += 1
        player %= 2

    return min(scores) * roll


def part2(data: str):
    """Part 2 solution"""

    outcomes = Counter(map(sum, product((1, 2, 3), repeat=3)))

    @cache
    def wins(pos_1, pos_2, score_1=0, score_2=0):
        if score_2 >= 21:
            return 0, 1
        total_1 = 0
        total_2 = 0
        for outcome, universes in outcomes.items():
            pos = (pos_1 + outcome) % 10
            wins_2, wins_1 = wins(pos_2, pos, score_2, score_1 + pos + 1)
            total_1 += wins_1 * universes
            total_2 += wins_2 * universes
        return total_1, total_2

    return max(wins(*parse(data)))


def parse(data: str):
    return [int(line.split()[-1]) - 1 for line in data.splitlines()]


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
