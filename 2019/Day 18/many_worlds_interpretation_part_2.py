"""Day 18 Answers part 2"""
import heapq
from typing import (
    NamedTuple,
    Dict,
    Set,
    Tuple,
    FrozenSet,
    Iterator,
)
from collections import deque
from itertools import combinations
import networkx as nx


INPUT = "2019/Day 18/input"


class Vec(NamedTuple):
    """2D Vec"""

    line: int
    col: int

    def __add__(self, other):
        return Vec(self.line + other.line, self.col + other.col)


def parse(data: str) -> Tuple[Dict[Vec, str], Dict[str, Vec]]:
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
    center = objects["@"]
    del objects["@"]
    del field[center]
    for p in neighbors(center):
        del field[p]
    for i, dp in enumerate((Vec(1, 1), Vec(-1, 1), Vec(1, -1), Vec(-1, -1),)):
        objects[str(i)] = center + dp

    return field, objects


def neighbors(p: Vec) -> Iterator[Vec]:
    """yield points near p"""
    for dp in [
        Vec(0, 1),
        Vec(0, -1),
        Vec(1, 0),
        Vec(-1, 0),
    ]:
        yield p + dp


def field_graph(field, objects) -> nx.Graph:
    """make graph form field"""
    graph = nx.Graph()
    visited: Set[Vec] = set()
    queue = deque([objects[o] for o in objects if o.isdigit()])
    while queue:
        src = queue.popleft()
        if src in visited:
            continue
        visited.add(src)
        for dst in neighbors(src):
            if dst in field:
                graph.add_edge(src, dst)
                queue.append(dst)
    return graph


def key_to_key_graph(fg, field, objects) -> nx.Graph:
    """return graph with distances between nodes, required open doors and collected keys"""
    pois = [obj for obj in objects if obj.islower() or obj.isdigit()]
    graph = nx.Graph()
    for obj1, obj2 in combinations(pois, 2):
        p1 = objects[obj1]
        p2 = objects[obj2]
        try:
            path = nx.shortest_path(fg, p1, p2)
            doors = frozenset(field[p] for p in path if field[p].isupper())
            keys = frozenset(field[p].upper() for p in path if field[p].islower())
            if len(keys) <= 2:
                closed_doors = doors - keys
                graph.add_edge(
                    p1, p2, length=len(path) - 1, doors=closed_doors, keys=keys
                )
        except nx.NetworkXNoPath:
            pass
    return graph


Keys = FrozenSet[str]
Drones = Tuple[Vec, ...]
Node = Tuple[int, Drones, Keys]


def dijkstra(k2k: nx.Graph, start: Drones, all_doors) -> int:
    """return shortest path between all keys or rises ValueError"""
    visited: Tuple[Set[Tuple[Vec, Keys]], ...] = (set(), set(), set(), set())
    node: Node = (0, start, frozenset(""))
    queue = [node]
    while queue:
        dist, drons, open_doors = heapq.heappop(queue)
        if open_doors == all_doors:
            return dist

        for i in range(4):
            pos = drons[i]
            if (pos, open_doors) in visited[i]:
                continue
            visited[i].add((pos, open_doors))

            if pos not in k2k:
                continue
            available_keys = []
            for n, a in k2k[pos].items():
                if open_doors >= a["doors"]:
                    available_keys.append(n)
            for key in available_keys:
                new_dist = dist + k2k.edges[(pos, key)]["length"]
                keys = k2k.edges[(pos, key)]["keys"] | open_doors
                new_drones = drons[:i] + (key,) + drons[i + 1 :]
                heapq.heappush(queue, (new_dist, new_drones, keys))

    raise ValueError


def shortest_path_length(data) -> int:
    """return shortest path between all keys"""
    field, objects = parse(data)
    fg = field_graph(field, objects)
    k2k = key_to_key_graph(fg, field, objects)
    drons = tuple(objects[o] for o in objects if o.isdigit())
    all_doors = set(k.upper() for k in objects if k.islower())
    return dijkstra(k2k, drons, all_doors)


def part2():
    """Part 2 answer"""
    with open(INPUT) as data:
        data = data.read()
    return shortest_path_length(data)


if __name__ == "__main__":
    ANSWER = part2()
    print(f"Part 2: {ANSWER}")
