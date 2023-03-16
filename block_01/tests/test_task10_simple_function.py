import pytest


from block_01.Easy.task01 import simple_function


@pytest.mark.parametrize("test_line, test_mult, expected",
                         [("test", 3, "testTESTtest"), ])
def test_simple_function_success(test_line: str,
                                 test_mult: int,
                                 expected: str):
    assert expected == simple_function(test_line, test_mult)


def test_simple_function_success_through_var():
    import re
    random_var = simple_function
    pattern = re.compile("<function simple_function at 0x\\w+>")
    assert pattern.match(random_var.__repr__())


@pytest.mark.parametrize("test_line, test_mult, expected",
                         [("test", 3, "testTESTtest"), ])
def test_simple_function_success_through_var_02(test_line: str,
                                                test_mult: int,
                                                expected: str):
    random_var = simple_function
    assert expected == random_var(test_line, test_mult)
