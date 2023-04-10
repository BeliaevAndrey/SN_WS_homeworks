import pytest
from time import time_ns as _tns

from block_03.task_03.task_03_01 import factorial_calc


@pytest.mark.parametrize("number, expected", [(5, 120),
                                              (6, 720),
                                              (0, 1),
                                              ])
def test_factorial_calc_success(number, expected):
    assert (expected == factorial_calc(number))


@pytest.mark.parametrize("number_lap1, number_lap2, expected_comparison", [(500, 500, True),
                                                                (700, 700, True),
                                                                (500, 300, False),
                                                                (500, 100, False),
                                                                ])
def test_factorial_calc_success_timed(number_lap1, number_lap2, expected_comparison):
    start = _tns()
    factorial_calc(number_lap1)
    end1 = _tns() - start

    start = _tns()
    factorial_calc(number_lap2)
    end2 = _tns() - start
    print(end1, end2)
    assert (expected_comparison == (end1 > end2))
