import pytest
from puzzle import func


@pytest.mark.parametrize(
    "param1, result", [["", ""],],
)
def test_func(param1, result):
    assert func(param1) == result
