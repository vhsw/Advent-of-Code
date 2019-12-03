#!/usr/bin/env python3


class Tree:
    def __init__(self):
        self.nodes = {}
        self.done = []

    def __bool__(self):
        return len(self.nodes) != 0

    def add(self, s, m):
        if m not in self.nodes.keys():
            self.nodes[m] = []
        if s in self.nodes:
            self.nodes[s].append(m)
        else:
            self.nodes[s] = [m]

    def get(self):
        res = []
        for name, before in self.nodes.items():
            if len(before) == 0:
                res.append(name)
        return min(res)

    def do(self, step):
        for before in self.nodes.values():
            if step in before:
                before.remove(step)
        del self.nodes[step]
        self.done.append(step)


def task(path):
    with open(path) as f:
        raw = list(f.read().splitlines())
    data = [(line[5], line[36]) for line in raw]
    tree = Tree()
    for m, s in data:
        tree.add(s, m)
    while tree:
        step = tree.get()
        tree.do(step)
    return ''.join(tree.done)


assert task('Day 07/example.txt') == 'CABDFE'
print(task('Day 07/input.txt'))
