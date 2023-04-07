import pytest

from block_03.task_01.task_01_1 import function_2, ADV


@pytest.mark.parametrize("hi_lim, lo_lim,  expected", [(20, 10, (11, 13, 17, 19)),
                                                       (102, 99, (101,)),
                                                       (101, 99, tuple()),
                                                       ])
def test_function_1_success(hi_lim, lo_lim, expected, capsys):
    assert (expected == function_2(hi_lim, lo_lim))
    decorator_result = capsys.readouterr().out.strip().split('\n')
    assert (decorator_result == [ADV])
