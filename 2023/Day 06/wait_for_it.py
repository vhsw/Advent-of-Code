"""Day 6: Wait For It"""
from math import prod
from typing import NamedTuple

with open("2023/Day 06/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    races = parse(data)
    return prod(race.number_of_ways_you_can_beat_the_record() for race in races)


def part2(data: str):
    """Part 2 solution"""
    race = parse_ignore_spaces(data)
    return race.number_of_ways_you_can_beat_the_record()


class Race(NamedTuple):
    time: int
    record_distance: int

    def number_of_ways_you_can_beat_the_record(self):
        number_of_ways = 0
        for hold_time in range(self.time):
            speed = hold_time
            distance = speed * (self.time - hold_time)
            if distance > self.record_distance:
                number_of_ways += 1

        return number_of_ways


def parse(data: str):
    lines = data.splitlines()
    _, *times = lines[0].split()
    _, *distances = lines[1].split()
    return [Race(int(time), int(dist)) for time, dist in zip(times, distances)]


def parse_ignore_spaces(data: str):
    lines = data.splitlines()
    _, *times = lines[0].split()
    _, *distances = lines[1].split()
    return Race(int("".join(times)), int("".join(distances)))


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
