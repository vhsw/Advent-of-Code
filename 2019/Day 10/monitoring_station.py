"""Day 10 Answers"""

from math import gcd, atan2, sqrt, pi
from typing import NamedTuple, Dict, List


Point = NamedTuple("Point", [("x", int), ("y", int)])
Vector = NamedTuple("Vector", [("x", int), ("y", int)])

INPUT = "2019/Day 10/input"


def direction(src: Point, dst: Point) -> Vector:
    """direction from src to dst"""
    x = dst.x - src.x
    y = dst.y - src.y
    g = gcd(x, y)
    if x != 0:
        x //= g
    if y != 0:
        y //= g
    return Vector(x, y)


def distance(src: Point, dst: Point):
    """distance from src to dst"""
    x = src.x - dst.x
    y = src.y - dst.y

    return sqrt(x ** 2 + y ** 2)


def vaporization_order(src, field: List[Point]) -> List[Point]:
    """Fortunately, in addition to an asteroid scanner, the new monitoring station also comes equipped with a giant rotating laser perfect for vaporizing asteroids. The laser starts by pointing up and always rotates clockwise, vaporizing any asteroid it hits.
    If multiple asteroids are exactly in line with the station, the laser only has enough power to vaporize one of them before continuing its rotation. In other words, the same asteroids that can be detected can be vaporized, but if vaporizing one asteroid makes another one detectable, the newly-detected asteroid won't be vaporized until the laser has returned to the same position by rotating a full 360 degrees."""
    angles: Dict[float, List[Point]] = {}
    for dst in field:
        if dst == src:
            continue
        x, y = direction(src, dst)
        angle = atan2(-x, y)
        if angle == pi:
            angle = -pi
        angles.setdefault(angle, []).append(dst)
        angles[angle].sort(key=lambda dst: distance(src, dst), reverse=True)

    order = []
    while any(angles.values()):
        for angle in sorted(angles):
            if not angles[angle]:
                continue
            pos = angles[angle].pop()
            order.append(pos)

    return order


def count_at_pos(src, field):
    """number of distinct directions"""
    directions = set(direction(src, dst) for dst in field)
    return len(directions) - 1


def max_asteroids(field):
    """The best location is the asteroid that can detect the largest number of other asteroids."""
    return max(field, key=lambda pos: count_at_pos(pos, field))


def parse_field(text):
    """coordinates of asteroinds"""
    text = text.splitlines()
    field = [
        Point(w, h)
        for h, row in enumerate(text)
        for w, col in enumerate(row)
        if col == "#"
    ]
    return field


def part1():
    """Part 1 answer"""
    with open(INPUT) as data:
        text = data.read()
    field = parse_field(text)
    pos = max_asteroids(field)
    return count_at_pos(pos, field)


def part2():
    """Part 2 answer"""
    with open(INPUT) as data:
        text = data.read()
    field = parse_field(text)
    pos = max_asteroids(field)
    order = vaporization_order(pos, field)
    x, y = order[199]
    return 100 * x + y


if __name__ == "__main__":
    ANSWER1 = part1()
    print(f"Part 1: {ANSWER1}")
    ANSWER2 = part2()
    print(f"Part 2: {ANSWER2}")
