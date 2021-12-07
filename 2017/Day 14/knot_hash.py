"""Knot Hash Module"""
from collections import deque
from functools import reduce
from operator import xor
from typing import Sequence


def knot_hash(data: str):
    """Knot Hash"""
    lengths = list(map(int, data.encode("ascii"))) + [17, 31, 73, 47, 23]
    numbers = deque(range(256))
    pos = 0
    skip_size = 0
    for _ in range(64):
        for length in lengths:
            buf = [numbers.popleft() for _ in range(length)]
            numbers.extendleft(buf)
            offset = length + skip_size
            numbers.rotate(-offset)
            pos += offset
            skip_size += 1
    numbers.rotate(pos)
    return to_hex_str(condense(numbers))


def condense(sparse_hash: Sequence[int]):
    sparse_hash = list(sparse_hash)
    assert len(sparse_hash) == 256
    size = 16
    for idx in range(0, 256, size):
        yield reduce(xor, sparse_hash[idx : idx + size])


def to_hex_str(dense_hash: Sequence[int]):
    return bytes(dense_hash).hex()
