import pytest

from block_01.Hard.task03 import summation


@pytest.mark.parametrize("a, b, c, d, e, expected", [(1, 2, 3, 4, 5, 10)])
def test_summation_success_01(a, b, c, d, e, expected: int):
    assert expected == summation(a, b, c, d, e)


@pytest.mark.parametrize("tpl, expected",
                         [((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), range(30, 35))
                          ])
def test_summation_success_02(tpl, expected):
    assert summation(*tpl) in expected


@pytest.mark.parametrize("tpl, dct, expected",
                         [((1, 2, 3, 4, 5, 6, 7, 8, ),  {'f': 9, 'g': 10, 'h': 11}, range(39, 43))
                          ])
def test_summation_success_03(tpl, dct, expected):
    assert summation(*tpl, **dct) in expected
