import pytest

from block_03.task_02.task_02_1 import divider_fun


@pytest.mark.parametrize("number, divisor, expected", [(10, 5, 2.0),
                                                       (2, 5, 0.4),
                                                       (3, 2, 1.5),
                                                       ])
def test_divider_fun_success(number, divisor, expected):
    assert (expected == divider_fun(number, divisor))


@pytest.mark.parametrize("number, divisor, expected", [(10, 0, ZeroDivisionError),
                                                       (2, 0, ZeroDivisionError),
                                                       (3, 0, ZeroDivisionError),
                                                       ])
def test_divider_fun_fail(number, divisor, expected):
    with pytest.raises(expected):
        divider_fun(number, divisor)
