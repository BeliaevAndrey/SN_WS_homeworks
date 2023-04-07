import pytest

from block_03.task_02.task_02_1 import residues_lister


@pytest.mark.parametrize("number, divisors, expected", [(10, [3, 4, 5], [1, 2, 0]),
                                                        (3, [2], [1]),
                                                        ])
def test_residues_lister_success(number: int, divisors: list[int], expected: list):
    assert (expected == residues_lister(number, divisors))


@pytest.mark.parametrize("number, divisors, expected", [(10, [*range(10)], ZeroDivisionError),
                                                        (3, [1, 2, 0, 4], ZeroDivisionError),
                                                        ])
def test_residues_lister_fail(number: int, divisors: list[int], expected):
    with pytest.raises(expected):
        assert (expected == residues_lister(number, divisors))
