import pytest

from block_02.Medium.task02_01 import symbol_counter


@pytest.mark.parametrize('symbol, consequence, expected', [('b', 'abracadabra', 2),
                                                           ('a', 'banana', 3),
                                                           ])
def test_symbol_counter_success(symbol: str,
                                consequence: str,
                                expected: int):
    assert (expected == symbol_counter(symbol, consequence))


@pytest.mark.parametrize('symbol, consequence, expected', [('abracadabra', 'b', 2),
                                                           (3, 'abracadabra', 2),
                                                           ])
def test_symbol_counter_fail(symbol: str,
                             consequence: str,
                             expected: int):
    with pytest.raises(TypeError):
        symbol_counter(symbol, consequence)
