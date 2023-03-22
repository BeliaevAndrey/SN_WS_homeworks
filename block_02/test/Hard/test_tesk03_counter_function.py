import pytest

from block_02.Hard.task03 import outer_function, counter


@pytest.mark.parametrize("args_tuple, expected", [((1, 2, 3, 4,), 10),
                                                  ((1, 2, 3, 4, 5), 15),
                                                  ((1, 2, 3, 4, 15), 25),
                                                  ])
def test_outer_function_success(args_tuple, expected, capsys):
    fun = counter(outer_function)
    expected = []
    for i in range(5):
        expected.append(f'Function "outer_function" calls: {i + 1}')
        fun(*args_tuple)
    result = capsys.readouterr().out.strip().split('\n')
    assert (expected == result)
