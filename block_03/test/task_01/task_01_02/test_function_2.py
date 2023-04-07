import pytest

from block_03.task_01.task_01_2 import function_other, ADV2


@pytest.mark.parametrize("limit, expected", [(10, (2, 3, 5, 7)),
                                             (20, (2, 3, 5, 7, 11, 13, 17, 19))
                                             ])
def test_function_other_success(limit, expected, capsys):
    assert (expected == function_other(limit))
    decorator_result = capsys.readouterr().out.rstrip('\n')
    assert (decorator_result == ADV2)
