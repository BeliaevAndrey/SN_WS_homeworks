import pytest
from time import time_ns as _tns

import block_03.task_03.cus_log
from block_03.task_03.task_03_02_ver2 import factorial_calc


@pytest.mark.parametrize("number, expected, semaphore", [(5, 120, 'SEMAPHORE (v2): time normal'),
                                                         (6, 720, 'SEMAPHORE (v2): time normal'),
                                                         (0, 1, 'SEMAPHORE (v2): time normal'),
                                                         ])
def test_factorial_calc_success(number, expected, semaphore, capsys):
    assert (expected == factorial_calc(number))
    deco_answer = capsys.readouterr().out
    assert (semaphore in deco_answer)


@pytest.mark.parametrize("number, semaphore", [(500, 'SEMAPHORE (v2): time normal; result calculated'),
                                               (600, 'SEMAPHORE (v2): time normal; result calculated'),
                                               (500, 'SEMAPHORE (v2): time normal; result cached'),
                                               (600, 'SEMAPHORE (v2): time normal; result cached'),
                                               (400_000, 'SEMAPHORE (v2): time normal; result calculated'),
                                               (600, 'SEMAPHORE (v2): time exceeded; result calculated'),
                                               ])
def test_factorial_calc_success_semaphores(number, semaphore, capsys):
    factorial_calc(number)
    deco_answer = capsys.readouterr().out
    assert (semaphore in deco_answer)


@pytest.mark.parametrize("number_lap1, number_lap2, expected_comparison", [(500, 500, True),
                                                                (700, 700, True),
                                                                (5000, 300, True,),
                                                                (5000, 900, False),
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
