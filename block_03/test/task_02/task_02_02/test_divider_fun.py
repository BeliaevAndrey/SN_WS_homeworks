import pytest

from block_03.task_02.task_02_02 import divider_fun_t02_02


@pytest.mark.parametrize("number, divisor, expected, deco_expected",
                         [(10, 5, 2.0, 'restarts=9'),
                          (2, 5, 0.4, 'restarts=9'),
                          (3, 2, 1.5, 'restarts=9'),
                          ])
def test_divider_fun_success(number, divisor, expected, deco_expected, capsys):
    assert (expected == divider_fun_t02_02(number, divisor))
    decorator_results = capsys.readouterr().out.rstrip()
    assert (decorator_results == deco_expected)


@pytest.mark.parametrize("number, divisor, expected, deco_expected",
                         [(10, 0, ZeroDivisionError, 'restarts=0'),
                          (2, 0, ZeroDivisionError, 'restarts=0'),
                          (3, 0, ZeroDivisionError, 'restarts=0'),
                          ])
def test_divider_fun_fail(number, divisor, expected, deco_expected, capsys):
    with pytest.raises(expected):
        divider_fun_t02_02(number, divisor)
    decorator_results = capsys.readouterr().out.rstrip()
    assert (decorator_results == deco_expected)
