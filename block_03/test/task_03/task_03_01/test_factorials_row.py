import pytest
from time import time_ns as _tns

from block_03.task_03.task_03_01 import factorials_row


@pytest.mark.parametrize("number, expected", [
    (5, {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120}),
    (6, {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720}),
    (0, {0: 1}),
])
def test_factorial_calc_success(number: int, expected: dict):
    assert (expected == factorials_row(number))


@pytest.mark.parametrize("number_lap1, number_lap2, expected_comparison", [
    (500, 500, True),
    (700, 700, True),
    (500, 300, False),
    (500, 100, False),
])
def test_factorial_calc_success_timed(number_lap1, number_lap2, expected_comparison):
    start = _tns()
    factorials_row(number_lap1)
    end1 = _tns() - start

    start = _tns()
    factorials_row(number_lap2)
    end2 = _tns() - start
    print(end1, end2)
    assert (expected_comparison == (end1 > end2))
