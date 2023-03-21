import pytest

from block_02.Easy.task01 import summation


@pytest.mark.parametrize("tuple_in, expected", [((1, 2, 3, 4,), 10),
                                                ((1, 2, 3, 4, 5,), 15),
                                                ((), 0),
                                                ])
def test_summation_success(tuple_in, expected):
    assert (expected == summation(*tuple_in))


def test_summation_fail_01():
    with pytest.raises(TypeError):
        summation('a', 'b', 'c')
