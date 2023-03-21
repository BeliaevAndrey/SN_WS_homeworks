import pytest

from block_02.Easy.task01 import (
    counter,
    summation
)


def test_counter_success(capsys):
    fun = counter(summation)
    expected = []
    for i in range(5):
        expected.append(f'count={str(i + 1)}')
        print(out := fun(*range(1, i+1)))
        expected.append(str(out))
    actual = capsys.readouterr().out.strip().split('\n')
    assert (expected == actual)
