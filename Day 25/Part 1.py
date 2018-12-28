#!/usr/bin/env python
import networkx as nx


class Star:
    def __init__(self, pos: tuple):
        self.pos = pos

    @classmethod
    def from_strint(cls, line: str):
        line = line.strip()
        coords = tuple(map(int, line.split(',')))
        return cls(coords)

    def __repr__(self):
        return f'Star{self.pos}'

    def __eq__(self, other):
        return self.pos == other.pos

    def __hash__(self):
        return hash(self.pos)

    def distance(self, other):
        return sum(abs(s - o) for (s, o) in zip(self.pos, other.pos))


def madness(path):
    with open(path) as f:
        raw_data = f.read().splitlines()
    stars = [Star.from_strint(line) for line in raw_data]
    graph = nx.Graph()
    for star in stars:
        for other in stars:
            if star.distance(other) <= 3:
                graph.add_edge(star, other)

    # import matplotlib.pyplot as plt
    # nx.draw(graph, with_labels=True, pos=nx.spring_layout(graph, weight='weight'))
    # plt.show()

    return nx.number_connected_components(graph)


assert madness('Day 25/example.0.txt') == 2
assert madness('Day 25/example.1.txt') == 4
assert madness('Day 25/example.2.txt') == 3
assert madness('Day 25/example.3.txt') == 8
print(madness('Day 25/input.txt'))
