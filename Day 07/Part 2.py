#!/usr/bin/env python3
import string


class Tree:
    def __init__(self):
        self.nodes = {}
        self.done = []
        self.in_progress = {}

    def __bool__(self):
        return len(self.nodes) != 0

    def add(self, s, m):
        if m not in self.nodes.keys():
            self.nodes[m] = []
        if s in self.nodes:
            self.nodes[s].append(m)
        else:
            self.nodes[s] = [m]

    def get(self, workers, time):
        res = []
        for name, before in self.nodes.items():
            if name not in [nt for nt, t in self.in_progress.items() if t > time]:
                if len(before) == 0:
                    res.append(name)
        res.sort()
        return res[:workers]

    def check(self, time):
        done = []
        for step, t in self.in_progress.items():
            if time >= t:
                done.append(step)
        for step in done:
            del self.in_progress[step]
            for before in self.nodes.values():
                if step in before:
                    before.remove(step)
            del self.nodes[step]
            self.done.append(step)

    def do(self, step, duration, time):
        work_time = duration + string.ascii_uppercase.index(step) + 1
        self.in_progress[step] = time+work_time
        return work_time


def task(path, n_workers, duration):
    with open(path) as f:
        raw = list(f.read().splitlines())
    data = [(line[5], line[36]) for line in raw]
    tree = Tree()
    for m, s in data:
        tree.add(s, m)
    workers = [0] * n_workers
    time = 0
    while tree:
        free_workers = [i for i, w in enumerate(workers) if w <= time]
        tree.check(time)
        steps = tree.get(len(free_workers), time)
        for i, step in enumerate(steps):
            workers[free_workers[i]] += tree.do(step, duration, time)
        time += 1
    return time -1


assert task('Day 07/example.txt', 2, 0) == 15
print(task('Day 07/input.txt', 5, 60))
