import pytest

from block_02.Medium.task02_01 import factorial_linear, factorial_rec


@pytest.mark.parametrize("number, expected", [(5, 120),
                                              (6, 720),
                                              (3, 6),
                                              ])
def test_factorial_linear_success(number, expected):
    assert (expected == factorial_linear(number))


def test_factorial_linear_fail_01():
    with pytest.raises(TypeError):
        factorial_rec()


def test_factorial_linear_fail_02():
    with pytest.raises(TypeError):
        factorial_rec('a')


@pytest.mark.parametrize("number, expected", [(5, 120),
                                              (6, 720),
                                              (4, 24),
                                              ])
def test_factorial_rec_success(number, expected):
    assert (expected == factorial_linear(number))


def test_factorial_rec_fail_01():
    with pytest.raises(TypeError):
        factorial_rec()


def test_factorial_rec_fail_02():
    with pytest.raises(TypeError):
        factorial_rec('a')
