"""Day 5 Tests"""

import pytest
from hypothesis import given, example
import hypothesis.strategies as st

from diagnostic import Intcode, part1, part2


@pytest.mark.parametrize(
    "code, result",
    [
        [
            [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50],
            [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50],
        ],
        [[1, 0, 0, 0, 99], [2, 0, 0, 0, 99]],
        [[2, 3, 0, 3, 99], [2, 3, 0, 6, 99]],
        [[2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]],
        [[1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99]],
    ],
)
def test_day2_evaluate(code, result):
    ic = Intcode(code)
    assert ic.mem == result
    assert ic.output_data == []


@pytest.mark.parametrize(
    "code, result",
    [
        [[1002, 4, 3, 4, 33], [1002, 4, 3, 4, 99]],
        [[1101, 100, -1, 4, 0], [1101, 100, -1, 4, 99]],
    ],
)
def test_evaluate(code, result):
    ic = Intcode(code)
    assert ic.mem == result
    assert ic.output_data == []


@given(inp=st.integers())
@example(inp=8)
def test_equals_position(inp):
    ic = Intcode([3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], input_data=[inp])
    assert len(ic.output_data) == 1
    if inp == 8:
        assert ic.output_data[0] == 1
    else:
        assert ic.output_data[0] == 0


@given(inp=st.integers())
@example(inp=8)
def test_equals_immediate(inp):
    ic = Intcode([3, 3, 1108, -1, 8, 3, 4, 3, 99], input_data=[inp])
    assert len(ic.output_data) == 1
    if inp == 8:
        assert ic.output_data[0] == 1
    else:
        assert ic.output_data[0] == 0


@given(inp=st.integers())
@example(inp=7)
@example(inp=8)
@example(inp=9)
def test_less_than_position(inp):
    ic = Intcode([3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], input_data=[inp])
    assert len(ic.output_data) == 1
    if inp < 8:
        assert ic.output_data[0] == 1
    else:
        assert ic.output_data[0] == 0


@given(inp=st.integers())
@example(inp=7)
@example(inp=8)
@example(inp=9)
def test_less_than_immediate(inp):
    ic = Intcode([3, 3, 1107, -1, 8, 3, 4, 3, 99], input_data=[inp])
    assert len(ic.output_data) == 1
    if inp < 8:
        assert ic.output_data[0] == 1
    else:
        assert ic.output_data[0] == 0


@given(inp=st.integers())
@example(inp=7)
@example(inp=1)
@example(inp=0)
def test_jump_immediate(inp):
    ic = Intcode([3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], input_data=[inp])
    assert len(ic.output_data) == 1
    if inp == 0:
        assert ic.output_data[0] == 0
    else:
        assert ic.output_data[0] == 1


@given(inp=st.integers())
@example(inp=7)
@example(inp=1)
@example(inp=0)
def test_jump_position(inp):
    ic = Intcode(
        [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], input_data=[inp]
    )
    assert len(ic.output_data) == 1
    if inp == 0:
        assert ic.output_data[0] == 0
    else:
        assert ic.output_data[0] == 1


def test_parts():
    assert part1() == 9006673
    assert part2() == 3629692
