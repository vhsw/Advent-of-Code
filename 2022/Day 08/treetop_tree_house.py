"""Day 8: Treetop Tree House"""
from itertools import product

with open("2022/Day 08/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    trees = parse(data)
    visible = 0
    for i, j in product(range(len(trees)), range(len(trees[0]))):
        row = trees[i]
        col = [r[j] for r in trees]
        if is_visible_from_outside(j, row) or is_visible_from_outside(i, col):
            visible += 1
    return visible


def part2(data: str):
    """Part 2 solution"""
    trees = parse(data)
    max_score = 0
    for i, j in product(range(len(trees)), range(len(trees[0]))):
        score = get_scenic_score(i, j, trees)
        max_score = max(max_score, score)

    return max_score


def is_visible_from_outside(pos, line):
    tree = line[pos]
    return all(tree > t for t in line[:pos]) or all(tree > t for t in line[pos + 1 :])


def get_scenic_score(i, j, trees):
    tree = trees[i][j]
    up = [t[j] for t in trees[:i][::-1]]
    left = trees[i][:j][::-1]
    right = trees[i][j + 1 :]
    down = [t[j] for t in trees[i + 1 :]]

    up_score = count_visible_from_inside(tree, up)
    left_score = count_visible_from_inside(tree, left)
    right_score = count_visible_from_inside(tree, right)
    down_score = count_visible_from_inside(tree, down)
    return up_score * left_score * right_score * down_score


def count_visible_from_inside(target, row):
    visible = 0
    for tree in row:
        visible += 1
        if target <= tree:
            break
    return visible


def rotate(trees):
    return list(zip(*trees[::-1]))


def parse(data: str):
    trees = []
    for line in data.splitlines():
        trees.append(list(map(int, line)))
    return trees


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
