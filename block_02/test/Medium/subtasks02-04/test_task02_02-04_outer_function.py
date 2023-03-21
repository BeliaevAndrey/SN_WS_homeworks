import re
import pytest

from block_02.Medium.task02_02_04 import outer_function


def test_outer_function_bare_output_success(capsys):
    expected = re.compile('<function outer_function.<locals>.summation at 0x\\w+>')
    print(outer_function())
    actual = capsys.readouterr().out.strip()
    assert (expected.match(actual))


@pytest.mark.parametrize("args_tuple", [(1, 2, 3, 4, 5, )])
def test_outer_function_args_output_success(capsys, args_tuple):
    expected = str(sum(args_tuple))
    print(outer_function()(*args_tuple))
    actual = capsys.readouterr().out.strip()
    assert (expected == actual)


def test_outer_function_bare_through_var_output_success(capsys):
    expected = re.compile('<function outer_function.<locals>.summation at 0x\\w+>')
    result = outer_function()
    print(result)
    actual = capsys.readouterr().out.strip()
    assert (expected.match(actual))


@pytest.mark.parametrize("args_tuple", [(1, 2, 3, 4, )])
def test_outer_function_args_through_var_output_success(capsys, args_tuple):
    result = outer_function()
    expected = str(sum(args_tuple))
    print(result(*args_tuple))
    actual = capsys.readouterr().out.strip()
    assert (expected == actual)
