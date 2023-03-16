import pytest

from block_01.Hard.task03 import summation


@pytest.mark.parametrize("a, b, c, d, e, expected", [(1, 2, 3, 4, 5, 10)])
def test_summation_success_01(a, b, c, d, e, expected: int):
    assert expected == summation(a, b, c, d, e)
