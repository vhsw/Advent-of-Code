"""Day 4: Scratchcards"""
from typing import NamedTuple

with open("2023/Day 04/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    cards = map(Card.from_str, data.splitlines())
    return sum(card.worth for card in cards)


def part2(data: str):
    """Part 2 solution"""
    cards = list(map(Card.from_str, data.splitlines()))
    copies = {card.id: 1 for card in cards}
    for card in cards:
        for num in range(card.matching_numbers):
            copies[card.id + num + 1] += copies[card.id]
    return sum(copies.values())


class Card(NamedTuple):
    id: int
    numbers_you_have: set[int]
    winning_numbers: set[int]

    @classmethod
    def from_str(cls, line: str):
        id_, nums = line.split(": ")
        have, win = nums.split("| ")
        return cls(
            int(id_.removeprefix("Card ")),
            set(map(int, have.split())),
            set(map(int, win.split())),
        )

    @property
    def matching_numbers(self):
        return len(self.winning_numbers & self.numbers_you_have)

    @property
    def worth(self):
        if not self.matching_numbers:
            return 0
        return 2 ** (self.matching_numbers - 1)


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
