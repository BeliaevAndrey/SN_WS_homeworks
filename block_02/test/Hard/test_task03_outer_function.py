import pytest

from block_02.Hard.task03 import outer_function


@pytest.mark.parametrize("args_tuple, expected", [((1, 2, 3, 4,), 10), ])
def test_outer_function_success(args_tuple, expected):
    assert (expected == outer_function()(args_tuple))


@pytest.mark.parametrize("args_tuple, expected", [((1, 2, 3, 4,), 10), ])
def test_outer_function_fail_01(args_tuple, expected):
    with pytest.raises(TypeError):
        outer_function()(*args_tuple)


@pytest.mark.parametrize("args_tuple, expected", [((1, 2, 3, 4,), 10), ])
def test_outer_function_fail_02(args_tuple, expected):
    with pytest.raises(TypeError):
        outer_function(args_tuple)
