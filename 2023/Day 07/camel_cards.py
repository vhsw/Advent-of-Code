"""Day 7: Camel Cards"""
from collections import Counter
from enum import IntEnum, auto
from functools import total_ordering
from typing import NamedTuple

with open("2023/Day 07/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    games = parse(data)
    return total_winnings(games)


def part2(data: str):
    """Part 2 solution"""
    games = parse(data, wildcards=True)
    return total_winnings(games)


class HandType(IntEnum):
    HIGH_CARD = auto()
    ONE_PAIR = auto()
    TWO_PAIR = auto()
    THREE_OF_A_KIND = auto()
    FULL_HOUSE = auto()
    FOUR_OF_A_KIND = auto()
    FIVE_OF_A_KIND = auto()


@total_ordering
class Game(NamedTuple):
    hand: str
    bid: int
    wildcards: bool

    @classmethod
    def from_str(cls, line: str, wildcards=False):
        cards, bid = line.split()
        return cls(cards, int(bid), wildcards)

    @property
    def type(self):
        return max(self._type(hand) for hand in self._possible_hands())

    def _possible_hands(self):
        if self.wildcards:
            for card in "23456789TQKA":
                yield self.hand.replace("J", card)
        else:
            yield self.hand

    @staticmethod
    def _type(hand: str):
        counts = [v for (_, v) in Counter(hand).most_common()]
        match counts:
            case [5]:
                return HandType.FIVE_OF_A_KIND
            case [4, 1]:
                return HandType.FOUR_OF_A_KIND
            case [3, 2]:
                return HandType.FULL_HOUSE
            case [3, 1, 1]:
                return HandType.THREE_OF_A_KIND
            case [2, 2, 1]:
                return HandType.TWO_PAIR
            case [2, 1, 1, 1]:
                return HandType.ONE_PAIR
            case [1, 1, 1, 1, 1]:
                return HandType.HIGH_CARD

    @property
    def strength(self):
        return tuple(self._strength_order.index(card) for card in self.hand)

    @property
    def _strength_order(self):
        if self.wildcards:  # pylint: disable=no-else-return
            return "J23456789TQKA"
        else:
            return "23456789TJQKA"

    def __eq__(self, other: object):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.hand == other.hand

    def __lt__(self, other: object):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return (self.type, self.strength) < (other.type, other.strength)


def parse(data: str, wildcards=False):
    return [Game.from_str(line, wildcards) for line in data.splitlines()]


def total_winnings(games: list[Game]):
    return sum(game.bid * rank for rank, game in enumerate(sorted(games), start=1))


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
