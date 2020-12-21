"""Day 18 answers

This algorithm is python implementation of Theodore Norvell's article
http://www.engr.mun.ca/~theo/Misc/exp_parsing.htm
"""
import operator
import re
from typing import List, Union


class Leaf:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.value}"


class Node(Leaf):
    def __init__(self, value, left=None, right=None):
        super().__init__(value)
        self.left: Node = left
        self.right: Node = right

    def __repr__(self):
        return f"({self.left}{self.value}{self.right})"


def consume(tokens):
    """reads one token. When "next=end", consume is still allowed, but has no effect."""
    try:
        return tokens.pop(0)
    except IndexError:
        return


priority = {
    "+": 1,
    "*": 1,
}
operations = {
    "+": operator.add,
    "*": operator.mul,
}


def expect(expected: str, tokens: List[str]):
    if tokens[0] == expected:
        return tokens.pop(0)
    raise SyntaxError(f"unexpected token {tokens[0]}, expect {expected}")


def eparser(tokens: List[str]):
    operands: List[Union[Leaf, Node]] = []
    E([], operands, tokens)
    assert len(tokens) == 0
    return operands[-1]


def E(operators: List[str], operands: List[Union[Leaf, Node]], tokens: List[str]):
    P(operands, tokens)
    while tokens and tokens[0] in "+*":
        pushOperator(tokens[0], operators, operands)
        consume(tokens)
        P(operands, tokens)
    while operators:
        popOperator(operators, operands)


def P(operands: List[Union[Leaf, Node]], tokens: List[str]):
    token = tokens[0]
    if token.isdigit():
        operands.append(Leaf(int(token)))
        consume(tokens)
        return
    if token == "(":
        consume(tokens)
        E([], operands, tokens)
        expect(")", tokens)
        return
    raise Exception


def popOperator(operators: List[str], operands: List[Union[Leaf, Node]]):
    op = operators.pop()
    if op in "+*":
        t1 = operands.pop()
        t0 = operands.pop()
        operands.append(Node(op, t0, t1))


def pushOperator(op, operators: List[str], operands: List[Union[Leaf, Node]]):
    while operators and priority[operators[-1]] >= priority[op]:
        popOperator(operators, operands)
    operators.append(op)


def compute(node: Node):
    try:
        left_result = compute(node.left)
        right_result = compute(node.right)
        operation = operations[node.value]
        return operation(left_result, right_result)
    except AttributeError:
        return node.value


INPUT = "2020/Day 18/input.txt"


def part1(data):
    "Part 1 answer"
    s = 0
    for line in data:
        line = line.replace(" ", "")
        tokens = re.findall(r"([\(\)+*]|\d+)", line)
        ast = eparser(tokens)
        res = compute(ast)
        s += res
    return s


def part2(data):
    "Part 2 answer"
    s = 0
    priority["+"] = 2
    for line in data:
        line = line.replace(" ", "")
        tokens = re.findall(r"([\(\)+*]|\d+)", line)
        ast = eparser(tokens)
        res = compute(ast)
        s += res
    return s


if __name__ == "__main__":
    with open(INPUT) as fp:
        DATA = fp.read().strip().split("\n")
    print(f"Part 1: { part1(DATA) }")
    print(f"Part 2: { part2(DATA) }")
