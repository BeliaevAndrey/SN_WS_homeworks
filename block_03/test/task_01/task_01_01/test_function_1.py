import pytest

from block_03.task_01.task_01_1 import function_1, ADV


@pytest.mark.parametrize("limit, expected", [(10, (2, 3, 5, 7)),
                                             (20, (2, 3, 5, 7, 11, 13, 17, 19))
                                             ])
def test_function_1_success(limit, expected, capsys):
    assert (expected == function_1(limit))
    decorator_result = capsys.readouterr().out.strip().split('\n')
    assert (decorator_result == [ADV])
