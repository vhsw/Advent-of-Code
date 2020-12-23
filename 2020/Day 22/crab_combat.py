"Day 22 answers"
from collections import deque

INPUT = "2020/Day 22/input.txt"


def part1(data):
    "Part 1 answer"
    player = [deque(), deque()]
    for i, p in enumerate(data.split("\n\n")):
        for card in p.split("\n")[1:]:
            player[i].append(int(card))
    # print(players)
    while len(player[0]) > 0 and len(player[1]) > 0:
        card0 = player[0].popleft()
        card1 = player[1].popleft()
        if card0 > card1:
            player[0].extend((card0, card1))
        else:
            player[1].extend((card1, card0))
        # print(players)
    if len(player[0]) > 0:
        winner = player[0]
    else:
        winner = player[1]
    return sum(mul * val for mul, val in enumerate(list(winner)[::-1], start=1))


def part2(data):
    "Part 2 answer"


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.read().strip()
    DATA1 = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10""".strip()
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
