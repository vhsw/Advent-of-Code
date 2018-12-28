#!/usr/bin/env python


class Tree:
    def __init__(self, data):
        head, child_data = data[:2], data[2:]
        n_child, n_meta = map(int, head)
        self.child, child_end = self.add_childs(child_data, n_child)
        self.meta = tuple(map(int, child_data[child_end:child_end+n_meta]))
        self.end = child_end + n_meta+2

    @staticmethod
    def add_childs(data, n):
        res = []
        pos = 0
        for _ in range(n):
            tree = Tree(data[pos:])
            res.append(tree)
            pos += tree.end
        return res, pos

    def checksum(self):
        res = sum(self.meta)
        for c in self.child:
            res += c.checksum()
        return res

    def __repr__(self):
        return f'Tree child: {self.child}, meta: {self.meta}'


def puzzle(path):
    with open(path) as f:
        data = tuple(f.read().split())
    root = Tree(data)
    return root.checksum()


assert puzzle('Day 08/example.txt') == 138
print(puzzle('Day 08/input.txt'))
