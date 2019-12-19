"""Day 18 Answers"""

from typing import NamedTuple, Dict, Set, Tuple, List

import networkx as nx


class Vec(NamedTuple):
    """2D Vec"""

    line: int
    col: int

    def __add__(self, other):
        return Vec(self.line + other.line, self.col + other.col)


def parse(data: str):
    """Parse map"""
    field: Dict[Vec, str] = {}
    objects: Dict[str, Vec] = {}
    for line, row in enumerate(data.splitlines()):
        for col, char in enumerate(row):
            if char != "#":
                p = Vec(line, col)
                field[p] = char
                if char != ".":
                    objects[char] = p
    return field, objects


def near(p):
    return [p + dp for dp in [Vec(0, 1), Vec(0, -1), Vec(1, 0), Vec(-1, 0),]]


def get_available_keys(pos: Vec, field, open_doors=""):
    """distance to currenly available keys"""
    open_tiles = open_doors + ".@"
    open_tiles = open_tiles.upper()
    points = set()
    keys: Set[Vec] = set()
    for p in field:
        if field[p] in open_tiles:
            points.add(p)
        if field[p].islower():
            keys.add(p)
            points.add(p)
    graph = nx.Graph()
    for p in points:
        for near_p in near(p):
            if near_p in points:
                graph.add_edge(p, near_p)

    key_list = []
    for k in keys:
        try:
            path = nx.shortest_path(graph, pos, k)
            key_list.append((k, path))
        except nx.NetworkXNoPath:
            pass
    return key_list


def key_graph(pos: Vec, field: Dict[Vec, str], objects):
    graph = nx.DiGraph()
    visited: Set[Tuple[Vec, str]] = set()
    all_keys = set(o for o in objects if o.islower())
    print(all_keys)
    ends = []

    def f(pos: Vec, keys=""):
        if set(keys) == all_keys:
            ends.append(pos)
            return
        if (pos, keys) in visited:
            return
        visited.add((pos, keys))
        collected = field[pos]
        if collected == "@":
            collected = ""
        for t, p in get_available_keys(pos, field, keys + collected):
            if field[t] in keys:
                continue
            graph.add_edge(pos, t, weight=len(p))
            new_doors = keys if collected in keys else keys + collected
            f(t, new_doors)

    f(pos)
    print(ends)
    pathes_lens = []
    for end in ends:
        l = nx.shortest_path_length(graph, pos, end, weight="weight")
        pathes_lens.append(l)
        print(l, "allah")
    return min(pathes_lens)


INPUT = "2019/Day 18/input"


def part1():
    """Part 1 answer"""
    with open(INPUT) as data:
        data = data.read()
        data = """########################
    #...............b.C.D.f#
    #.######################
    #.....@.a.B.c.d.A.e.F.g#
    ########################"""
    field, objects = parse(data)
    entrance = objects["@"]
    return key_graph(entrance, field, objects)


def part2():
    """Part 2 answer"""
    with open(INPUT) as data:
        pass
    return 0


if __name__ == "__main__":
    ANSWER1 = part1()
    print(f"Part 1: {ANSWER1}")
    ANSWER2 = part2()
    print(f"Part 2: {ANSWER2}")
