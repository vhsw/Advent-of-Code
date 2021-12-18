"""Day 18: Snailfish"""
from copy import deepcopy
from dataclasses import dataclass
from functools import reduce
from itertools import combinations
from math import ceil, floor
from operator import add
from typing import Optional, Union


@dataclass
class Node:
    left: Optional[Union["Node", int]] = None
    right: Optional[Union["Node", int]] = None
    ancestor: Optional["Node"] = None

    def __str__(self) -> str:
        return f"[{self.left},{self.right}]"

    def __add__(self, other):
        if not isinstance(other, Node):
            return NotImplemented
        node = Node(deepcopy(self), deepcopy(other))
        node.left.ancestor = node
        node.right.ancestor = node
        changed = True
        while changed:
            changed = False
            while explode(node):
                changed = True
            changed |= split(node)

        return node


with open("2021/Day 18/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    numbers = parse(data)
    return magnitude(reduce(add, numbers))


def part2(data: str):
    """Part 2 solution"""
    numbers = parse(data)
    return max(
        max(magnitude(a + b), magnitude(b + a)) for a, b in combinations(numbers, 2)
    )


def magnitude(node: Node):
    if isinstance(node, int):
        return node
    return 3 * magnitude(node.left) + 2 * magnitude(node.right)


def explode(root: Node):
    todo = [(0, root)]
    while todo:
        level, num = todo.pop()
        if isinstance(num, int):
            continue
        if level == 3:
            if isinstance(num.left, Node):
                explode_num(num.left)
                num.left = 0
                return True
            if isinstance(num.right, Node):
                explode_num(num.right)
                num.right = 0
                return True
        if level < 3:
            todo.append((level + 1, num.right))
            todo.append((level + 1, num.left))
    return False


def explode_num(num: Node):
    add_right(num, num.right)
    add_left(num, num.left)


def add_right(num: Node, value):
    prev = num
    num = num.ancestor

    while num is not None and num.right is prev:
        prev = num
        num = num.ancestor
    if num is None:
        return
    if isinstance(num.right, int):
        num.right += value
        return
    num = num.right
    while isinstance(num.left, Node):
        num = num.left
    num.left += value


def add_left(num: Node, value):
    prev = num
    num = num.ancestor
    while num is not None and num.left is prev:
        prev = num
        num = num.ancestor
    if num is None:
        return
    if isinstance(num.left, int):
        num.left += value
        return
    num = num.left
    while isinstance(num.right, Node):
        num = num.right
    num.right += value


def split(root: Node):
    todo = [(root, root.ancestor)]
    while todo:
        node, anc = todo.pop()
        if isinstance(node, int):
            if node >= 10:
                new_node = split_num(node)
                if anc.left == node:
                    new_node.ancestor = anc
                    anc.left = new_node
                else:
                    new_node.ancestor = anc
                    anc.right = new_node
                return True
            continue

        todo.append((node.right, node))
        todo.append((node.left, node))
    return False


def split_num(num: int):
    return Node(floor(num / 2), ceil(num / 2))


def parse(data: str):
    return list(map(parse_line, data.splitlines()))


def parse_line(line: str):
    stack: list[tuple[Node, str]] = []
    num = None
    side = "left"
    level = -1
    for char in line:
        match char:
            case "[":
                stack.append((num, side))
                side = "left"
                level += 1
                num = Node(ancestor=num)
            case "]":
                prev = num
                num, side = stack.pop()
                level -= 1
                if level == -1:
                    num = prev
                else:
                    setattr(num, side, prev)

            case ",":
                side = "right"
            case dig:
                val = int(dig)
                if getattr(num, side) is not None:
                    val += getattr(num, side) * 10
                setattr(num, side, val)
    return num


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
