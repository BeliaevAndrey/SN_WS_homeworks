import pytest

from block_03.task_02.task_02_02 import residues_lister_t02_02


@pytest.mark.parametrize("number, divisors, expected, deco_expected",
                         [(10, [3, 4, 5], [1, 2, 0], 'restarts=4'),
                          (3, [2], [1], 'restarts=4'),
                          ])
def test_residues_lister_success(number: int, divisors: list[int], expected: list, deco_expected: str, capsys):
    assert (expected == residues_lister_t02_02(number, divisors))
    assert (deco_expected == capsys.readouterr().out.rstrip())


@pytest.mark.parametrize("number, divisors, expected, deco_expected",
                         [(10, [*range(10)], ZeroDivisionError, 'restarts=0'),
                          (3, [1, 2, 0, 4], ZeroDivisionError, 'restarts=0'),
                          ])
def test_residues_lister_fail(number: int, divisors: list[int], expected, deco_expected, capsys):
    with pytest.raises(expected):
        assert (expected == residues_lister_t02_02(number, divisors))
    assert (deco_expected == capsys.readouterr().out.rstrip())
