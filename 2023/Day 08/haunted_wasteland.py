"""Day 8: Haunted Wasteland"""
import re
from itertools import cycle
from math import lcm
from typing import Callable

with open("2023/Day 08/input.txt", encoding="utf-8") as fp:
    DATA = fp.read().strip()


def part1(data: str):
    """Part 1 solution"""
    instructions, nodes = parse(data)

    def is_dst(node: str):
        return node == "ZZZ"

    return count_steps(instructions, nodes, "AAA", is_dst)


def part2(data: str):
    """Part 2 solution"""
    instructions, nodes = parse(data)
    starts = [node for node in nodes if node.endswith("A")]

    def is_dst(node: str):
        return node.endswith("Z")

    return lcm(*(count_steps(instructions, nodes, src, is_dst) for src in starts))


def parse(data: str):
    instructions, nodes = data.split("\n\n")
    return instructions, parse_network(nodes)


def parse_network(nodes: str):
    return dict(map(parse_node, nodes.splitlines()))


def parse_node(node: str):
    match = re.match(r"(\w*) = \((\w+), (\w+)\)", node)
    if match is None:
        raise ValueError(node)
    return match[1], (match[2], match[3])


def count_steps(
    instructions: str,
    nodes: dict[str, tuple[str, str]],
    src: str,
    is_dst: Callable[[str], bool],
):
    steps = 0
    moves = {"L": 0, "R": 1}
    for instruction in cycle(instructions):
        if is_dst(src):
            return steps
        move = moves[instruction]
        src = nodes[src][move]
        steps += 1
    return steps


if __name__ == "__main__":
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
