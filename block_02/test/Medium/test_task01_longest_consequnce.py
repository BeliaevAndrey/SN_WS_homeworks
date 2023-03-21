import pytest

from block_02.Medium.task02_01 import longest_consequence


@pytest.mark.parametrize("line_in, expected", [("zzzzzzzaaaaaabbb", ('z', 7)),
                                               ("zzzzbbbzzzaaaaaa", ('a', 6)),
                                               ("asdfgh", ('a', 1)),
                                               ])
def test_longest_consequence_success(line_in, expected):
    assert (expected == longest_consequence(line_in))


def test_longest_consequence_fail_01():
    with pytest.raises(TypeError):
        longest_consequence()


def test_longest_consequence_fail_02():
    with pytest.raises(TypeError):
        longest_consequence("testing string", 1)
