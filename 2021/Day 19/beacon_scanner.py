"""Day 19: Beacon Scanner"""
from collections import Counter
from itertools import combinations

with open("2021/Day 19/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    scanners = parse(data)
    _, beacons = find_posinions(scanners)
    return len(beacons)


def part2(data: str):
    """Part 2 solution"""
    scanners = parse(data)
    scanner_pos, _ = find_posinions(scanners)
    return max(
        first.manhattan(second)
        for first, second in combinations(scanner_pos.values(), 2)
    )


class Vec(tuple):
    @classmethod
    def from_str(cls, string: str):
        return cls(map(int, string.split(",")))

    def __add__(self, other: object):
        if not isinstance(other, Vec):
            return NotImplemented
        return Vec(map(sum, zip(self, other)))

    def __sub__(self, other: object):
        if not isinstance(other, Vec):
            return NotImplemented
        return Vec(map(lambda p: p[0] - p[1], zip(self, other)))

    def dist(self, other):
        return sum(map(lambda p: (p[0] - p[1]) ** 2, zip(self, other)))

    def manhattan(self, other):
        return sum(map(lambda p: abs(p[0] - p[1]), zip(self, other)))


def find_posinions(scanners: dict[int, tuple[Vec, ...]]):
    distances = get_distances(scanners)
    rotations = {0: ((0, 1, 2), (1, 1, 1))}
    scanner_pos = {0: Vec((0, 0, 0))}
    beacon_pos = set(scanners[0])
    todo = list(scanners)
    while todo:
        unknown = todo.pop()
        if unknown in scanner_pos:
            continue
        for known in scanner_pos:  # pylint: disable=consider-using-dict-items
            pairs = [
                (s1, s2)
                for s1, c1 in distances[known].items()
                for s2, c2 in distances[unknown].items()
                if cmp(c1, c2) >= 11
            ]
            if len(pairs) < 12:
                continue
            a_known = rotate(pairs[0][0], *rotations[known])
            b_known = rotate(pairs[1][0], *rotations[known])
            a_unknown = pairs[0][1]
            b_unknown = pairs[1][1]
            rotations[unknown] = get_position(a_known - b_known, a_unknown - b_unknown)
            scanner_pos[unknown] = (
                scanner_pos[known] + a_known - rotate(a_unknown, *rotations[unknown])
            )

            beacon_pos.update(
                rotate(vec, *rotations[unknown]) + scanner_pos[unknown]
                for vec in scanners[unknown]
            )
            break
        else:
            todo.insert(0, unknown)

    return scanner_pos, beacon_pos


def cmp(first: Counter[int], second: Counter[int]):
    return sum(min(first[key], second[key]) for key in first & second)


def get_distances(scanners: dict[int, tuple[Vec, ...]]):
    return {
        scanner_id: {
            beacon: Counter(
                beacon.dist(other_beacon)
                for idx_1, other_beacon in enumerate(beacons)
                if idx_1 != idx_2
            )
            for idx_2, beacon in enumerate(beacons)
        }
        for scanner_id, beacons in scanners.items()
    }


def get_position(first: Vec, second: Vec):
    abs_second = tuple(map(abs, second))
    indices = tuple(map(abs_second.index, tuple(map(abs, first))))
    signs = tuple(
        1 if f == s else -1
        for f, s in zip(first, tuple(second[idx] for idx in indices))
    )
    return indices, signs


def rotate(vec: Vec, indices, signs):
    return Vec(vec[idx] * sign for idx, sign in zip(indices, signs))


def parse(data: str):
    return dict(parse_block(b) for b in data.split("\n\n"))


def parse_block(block: str):
    lines = block.splitlines()
    num = lines[0].split()[2]
    beacons = map(Vec.from_str, lines[1:])
    return int(num), tuple(beacons)


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
