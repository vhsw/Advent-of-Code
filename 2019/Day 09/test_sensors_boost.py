"""Day 9 Tests"""
from intcode import Intcode

import pytest
from sensors_boost import part1, part2


def test_quine():
    code = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
    ic = Intcode(code)
    assert ic.output_data == code


def test_16bit():
    code = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]
    ic = Intcode(code)
    assert len(ic.output_data) == 1
    assert len(str(ic.output_data[0])) == 16


def test_large():
    code = [104, 1125899906842624, 99]
    ic = Intcode(code)
    assert len(ic.output_data) == 1
    assert ic.output_data[0] == 1125899906842624


def test_parts():
    assert part1() == 3340912345
    assert part2() == 51754
