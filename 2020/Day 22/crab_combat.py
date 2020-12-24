"Day 22 answers"
from functools import cache
from collections import deque

INPUT = "2020/Day 22/input.txt"


def deal(data):
    players = [deque(), deque()]
    for player, deck in enumerate(data.split("\n\n")):
        for card in deck.split("\n")[1:]:
            players[player].append(int(card))
    return players


def score(winner):
    return sum(mul * val for mul, val in enumerate(list(winner)[::-1], start=1))


def part1(data):
    "Part 1 answer"
    player = deal(data)
    while len(player[0]) > 0 and len(player[1]) > 0:
        card0 = player[0].popleft()
        card1 = player[1].popleft()
        if card0 > card1:
            player[0].extend((card0, card1))
        else:
            player[1].extend((card1, card0))
    if len(player[0]) > 0:
        winner = player[0]
    else:
        winner = player[1]
    return score(winner)


@cache
def play(player, game=1):
    player = [deque(player[0]), deque(player[1])]
    prev = [set(), set()]
    winner = None
    while len(player[0]) > 0 and len(player[1]) > 0:
        if tuple(player[0]) in prev[0] or tuple(player[1]) in prev[1]:
            winner = 0
            break
        prev[0].add(tuple(player[0]))
        prev[1].add(tuple(player[1]))
        card0 = player[0].popleft()
        card1 = player[1].popleft()

        if len(player[0]) >= card0 and len(player[1]) >= card1:
            winner = play((tuple(player[0])[:card0], tuple(player[1])[:card1]), 2)
        else:
            if card0 > card1:
                winner = 0
            else:
                winner = 1
        if winner == 0:
            player[0].extend((card0, card1))
        else:
            player[1].extend((card1, card0))
    else:
        if len(player[0]) > 0:
            winner = 0
        else:
            winner = 1
    if game > 1:
        return winner
    return player[winner]


def part2(data):
    "Part 2 answer"
    player = deal(data)
    win = play((tuple(player[0]), tuple(player[1])))
    return score(win)


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.read().strip()
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
