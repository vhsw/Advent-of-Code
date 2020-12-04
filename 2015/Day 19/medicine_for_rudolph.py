"Day 19 answers"
from typing import List
from collections import deque

INPUT = "2015/Day 19/input.txt"


def part1(data: List[str]):
    "Part 1 answer"
    repls = data[:-2]
    target = data[-1]
    s = set()
    for repl in repls:
        repl = repl.strip()
        src, dst = repl.split(" => ")
        pos = 0
        while (pos := target.find(src, pos)) >= 0:
            new = target[:pos] + target[pos:].replace(src, dst, 1)
            s.add(new)
            pos += len(src)
    return len(s)


def part2_slow(data):
    "Part 2 answer"
    target = data[-1].strip()
    repls = {}
    for repl in data[:-2]:
        repl = repl.strip()
        src, dst = repl.split(" => ")
        repls.setdefault(dst, []).append(src)
    todo = deque([(target, 0)])
    seen = {}
    print(f"{repls=}")
    while todo:
        s, n = todo.pop()
        # print(f"{s=}")
        if len(todo) % 1000 == 0:
            print(f"{n=}, {len(todo)=}")
        for src in repls:
            pos = 0
            while (pos := s.find(src, pos)) >= 0:
                news = [s[:pos] + s[pos:].replace(src, dst, 1) for dst in repls[src]]
                for new in sorted(news):
                    print(f"{src=}, {n=}, {new=}")
                    if new not in seen:
                        seen[new] = n + 1
                        if "e" not in new:
                            todo.append((new, n + 1))
                    else:
                        seen[new] = min(seen[new], n + 1)
                    if new == "e":
                        print(f"{'#'*10} {(n+1)=} {'#'*10}")
                pos += len(src)
    return seen["e"]


def part2(data):
    "Part 2 answer"
    target = data[-1].strip()
    repls = {}
    for repl in data[:-2]:
        repl = repl.strip()
        src, dst = repl.split(" => ")
        repls.setdefault(dst, []).append(src)
    todo = deque([(target, 0)])
    seen = {}
    print(f"{repls=}")
    while todo:
        s, n = todo.pop()
        if len(todo) % 1000 == 0:
            print(f"{n=}, {len(todo)=}")
        for src in repls:
            pos = 0
            while (pos := s.find(src, pos)) >= 0:
                news = [s[:pos] + s[pos:].replace(src, dst, 1) for dst in repls[src]]
                for new in sorted(news):
                    if new not in seen:
                        seen[new] = n + 1
                        if "e" not in new:
                            todo.append((new, n + 1))
                    else:
                        seen[new] = min(seen[new], n + 1)
                    if new == "e":
                        print(f"{'#'*10} {(n+1)=} {'#'*10}")
                pos += len(src)
    return seen["e"]


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.readlines()
    DATA2 = """e => H
e => O
H => HO
H => OH
O => HH

HOHOHO
""".splitlines()
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
