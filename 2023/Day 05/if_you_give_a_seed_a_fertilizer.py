"""Day 5: If You Give A Seed A Fertilizer"""
from typing import NamedTuple

with open("2023/Day 05/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    almanac = Almanac.from_str(data)
    return almanac.get_lowest_location_number()


def part2(data: str):
    """Part 2 solution"""
    almanac = Almanac.from_str(data, seeds_as_ranges=True)
    return almanac.get_lowest_location_number()


class Range(NamedTuple):
    start: int
    length: int

    @property
    def end(self):
        return self.start + self.length

    def __and__(self, other: object):
        if not isinstance(other, self.__class__):
            return NotImplemented
        start = max(self.start, other.start)
        end = min(self.end, other.end)
        length = end - start
        if length <= 0:
            return None
        return Range(start, length)


class Shift(NamedTuple):
    source: Range
    destination: Range

    @classmethod
    def from_str(cls, line: str):
        dst, src, length = map(int, line.split())
        return cls(Range(src, length), Range(dst, length))

    def translate(self, range_: Range):
        offset = self.destination.start - self.source.start
        return Range(range_.start + offset, range_.length)


class Map(NamedTuple):
    source_category: str
    destination_category: str
    shifts: list[Shift]

    @classmethod
    def from_str(cls, data: str):
        head, *ranges = data.splitlines()
        src, dst = head.removesuffix(" map:").split("-to-")
        return cls(
            src,
            dst,
            sorted(Shift.from_str(line) for line in ranges),
        )

    def translate(self, ranges: list[Range]):
        new_ranges: list[Range] = []
        for src in ranges:
            overlaps: list[Range] = []
            for shift in self.shifts:
                if overlap := src & shift.source:
                    overlaps.append(overlap)
                    new_ranges.append(shift.translate(overlap))
            start = src.start
            for overlap in overlaps:
                new_ranges.append(Range(start, overlap.start - start))
                start = overlap.end
            new_ranges.append(Range(start, src.end - start))

        return sorted(dst for dst in new_ranges if dst.length)


class Almanac(NamedTuple):
    seed_ranges: list[Range]
    maps: dict[str, Map]

    @classmethod
    def from_str(cls, data: str, seeds_as_ranges=False):
        raw_seeds, *raw_maps = data.split("\n\n")
        seeds = list(map(int, raw_seeds.removeprefix("seeds: ").split()))
        ranges = sorted(
            cls._seeds_as_ranges(seeds)
            if seeds_as_ranges
            else cls._seeds_as_seeds(seeds)
        )
        maps = {map.source_category: map for map in map(Map.from_str, raw_maps)}
        return cls(ranges, maps)

    def get_lowest_location_number(self):
        return min(self.translate(self.seed_ranges)).start

    @staticmethod
    def _seeds_as_seeds(seeds: list[int]):
        return [Range(start, 1) for start in seeds]

    @staticmethod
    def _seeds_as_ranges(seeds: list[int]):
        return [Range(seeds[idx], seeds[idx + 1]) for idx in range(0, len(seeds), 2)]

    def translate(self, ranges: list[Range], src="seed", dst="location"):
        if src == dst:
            return ranges
        return self.translate(
            self.maps[src].translate(ranges),
            self.maps[src].destination_category,
        )


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
