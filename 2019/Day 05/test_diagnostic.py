"""Day 5 Tests"""

import pytest

from diagnostic import Intcode


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
