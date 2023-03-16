import pytest

from block_01.Medium.task02 import summation_first
from block_01.Medium.task02 import summation_second


# testing summation_first
@pytest.mark.parametrize("args, expected", [((1, 2, 3, 4, 5), 15),
                                            ((1.5, 2.5, 3.5, 4.5, 5.5), 17.5),
                                            ])
def test_summation_first_success(args: tuple, expected: [int, float]):
    assert expected == summation_first(*args)


# testing summation_second
@pytest.mark.parametrize("arg, expected_exception", [(1, TypeError)])
def test_summation_second_fail_01(arg: int, expected_exception):
    with pytest.raises(expected_exception):
        assert summation_second(arg)


@pytest.mark.parametrize("args, expected_exception", [((1, 2, 3, 4, 'b=4'), TypeError)])
def test_summation_second_fail_01(args: tuple, expected_exception):
    with pytest.raises(expected_exception):
        assert summation_second(*args)


@pytest.mark.parametrize("args, expected", [((1, 2, 3, 4, 5, 6, 7, 8, 9, 0), 45),
                                            ])
def test_summation_second_success(args: tuple, expected: [int, float]):
    assert expected == summation_second(*args)


@pytest.mark.parametrize("args, expected", [({'a': 1, 'c': 3, 'b': 2, 'd': 5}, 11),
                                            ])
def test_summation_second_success(args: dict, expected: [int, float]):
    assert expected == summation_second(**args)
